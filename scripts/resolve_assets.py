#!/usr/bin/env python3
"""Resolve Bayer-ppt assets from env overrides, assets root, KB root, or repo.

Stdlib only. Search order (first hit wins) per asset:
  a. BAYER_ASSET_<ID>  (e.g. BAYER_ASSET_ICON_LIBRARY_POTX)
  b. BAYER_ASSETS_ROOT/<rel> or BAYER_ASSETS_ROOT/<filename>
  c. BAYER_KB_ROOT/ recursive basename / alias match
  d. ${REPO_ROOT}/<rel>
  e. BAYER_ASSET_PATH entries (os.pathsep-separated extra roots)

CLI:
  --check         Exit 0 if required brand-kit present; warn on missing optional
  --json          Full resolution map
  --get ID        Print absolute path or exit 1
  --write-env     Write ${REPO_ROOT}/.bayer-ppt.env
  --prepare-master  Copy resolved potx → exports/bayer-radiology-master.pptx
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


CONTENT_TYPES_TEMPLATE = (
    'ContentType="application/vnd.openxmlformats-officedocument'
    '.presentationml.template.main+xml"'
)
CONTENT_TYPES_PRESENTATION = (
    'ContentType="application/vnd.openxmlformats-officedocument'
    '.presentationml.presentation.main+xml"'
)


def env_id_key(asset_id: str) -> str:
    """icon-library-potx → BAYER_ASSET_ICON_LIBRARY_POTX"""
    return "BAYER_ASSET_" + asset_id.upper().replace("-", "_")


def find_repo_root(start: Optional[Path] = None) -> Path:
    env_root = os.environ.get("BAYER_PPT_ROOT")
    if env_root:
        p = Path(env_root).expanduser().resolve()
        if (p / "brand-kit").is_dir():
            return p

    assets_root = os.environ.get("BAYER_ASSETS_ROOT")
    if assets_root:
        p = Path(assets_root).expanduser().resolve()
        # Parent may be repo if assets live under brand-assets/source
        for cand in (p, p.parent, p.parent.parent):
            if (cand / "brand-kit").is_dir():
                return cand

    here = (start or Path(__file__).resolve()).parent
    cur = here if here.is_dir() else here.parent
    for _ in range(12):
        if (cur / "brand-kit").is_dir():
            return cur
        if cur.parent == cur:
            break
        cur = cur.parent

    # Fallback: script is scripts/resolve_assets.py → parent.parent
    return Path(__file__).resolve().parent.parent


def load_manifest(repo_root: Path) -> Dict[str, Any]:
    path = repo_root / "brand-kit" / "assets.manifest.json"
    if not path.is_file():
        raise FileNotFoundError(f"Manifest not found: {path}")
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def _is_hit(path: Path, kind: str) -> bool:
    if kind == "dir":
        return path.is_dir()
    return path.is_file()


def _kb_index(kb_root: Path) -> Dict[str, Path]:
    """Basename → first absolute path under KB (files and dirs)."""
    index: Dict[str, Path] = {}
    if not kb_root.is_dir():
        return index
    try:
        for root, dirs, files in os.walk(kb_root):
            # Skip heavy / hidden trees
            dirs[:] = [d for d in dirs if not d.startswith(".") and d not in
                       ("node_modules", ".git", "__pycache__", ".venv", "venv")]
            rpath = Path(root)
            for name in files:
                if name not in index:
                    index[name] = rpath / name
            for name in dirs:
                if name not in index:
                    index[name] = rpath / name
    except OSError:
        pass
    return index


def resolve_one(
    asset: Dict[str, Any],
    repo_root: Path,
    assets_root: Optional[Path],
    kb_root: Optional[Path],
    kb_index: Dict[str, Path],
    extra_roots: List[Path],
    aliases: Dict[str, str],
) -> Dict[str, Any]:
    aid = asset["id"]
    kind = asset.get("kind", "file")
    rel = asset.get("rel", "")
    filenames: List[str] = list(asset.get("filenames") or [])
    if rel:
        filenames = list(dict.fromkeys(filenames + [Path(rel).name]))

    # Reverse aliases pointing to this id
    for alias_name, target_id in aliases.items():
        if target_id == aid and alias_name not in filenames:
            filenames.append(alias_name)

    sources_tried: List[str] = []
    resolved: Optional[Path] = None
    via: Optional[str] = None

    # a. Explicit env override
    env_key = env_id_key(aid)
    env_val = os.environ.get(env_key)
    if env_val:
        cand = Path(env_val).expanduser().resolve()
        sources_tried.append(f"env:{env_key}")
        if _is_hit(cand, kind):
            resolved, via = cand, f"env:{env_key}"

    # b. BAYER_ASSETS_ROOT
    if resolved is None and assets_root is not None:
        candidates = []
        if rel:
            # If assets_root is brand-assets/source, rel may include that prefix
            candidates.append(assets_root / rel)
            candidates.append(assets_root / Path(rel).name)
            # Strip brand-assets/source/ prefix if assets_root already points there
            parts = Path(rel).parts
            if len(parts) >= 3 and parts[0] == "brand-assets" and parts[1] == "source":
                candidates.append(assets_root / Path(*parts[2:]))
        for fn in filenames:
            candidates.append(assets_root / fn)
        for cand in candidates:
            sources_tried.append(f"assets_root:{cand}")
            if _is_hit(cand, kind):
                resolved, via = cand.resolve(), "BAYER_ASSETS_ROOT"
                break

    # c. BAYER_KB_ROOT recursive basename / alias
    if resolved is None and kb_root is not None:
        for fn in filenames:
            sources_tried.append(f"kb:{fn}")
            hit = kb_index.get(fn)
            if hit is not None and _is_hit(hit, kind):
                resolved, via = hit.resolve(), "BAYER_KB_ROOT"
                break

    # d. REPO_ROOT/<rel>
    if resolved is None and rel:
        cand = (repo_root / rel).resolve()
        sources_tried.append(f"repo:{cand}")
        if _is_hit(cand, kind):
            resolved, via = cand, "REPO_ROOT"

    # e. Extra roots from BAYER_ASSET_PATH
    if resolved is None:
        for root in extra_roots:
            for fn in filenames:
                cand = root / fn
                sources_tried.append(f"path:{cand}")
                if _is_hit(cand, kind):
                    resolved, via = cand.resolve(), "BAYER_ASSET_PATH"
                    break
            if resolved is not None:
                break
            if rel:
                cand = root / rel
                sources_tried.append(f"path:{cand}")
                if _is_hit(cand, kind):
                    resolved, via = cand.resolve(), "BAYER_ASSET_PATH"

    return {
        "id": aid,
        "kind": kind,
        "rel": rel,
        "optional": bool(asset.get("optional", True)),
        "required_for": asset.get("required_for", []),
        "description": asset.get("description", ""),
        "resolved": str(resolved) if resolved else None,
        "via": via,
        "missing": resolved is None,
        "sources_tried": sources_tried[:12],
    }


def resolve_all(repo_root: Path) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    manifest = load_manifest(repo_root)
    assets_root_env = os.environ.get("BAYER_ASSETS_ROOT")
    assets_root = (
        Path(assets_root_env).expanduser().resolve() if assets_root_env else None
    )
    kb_root_env = os.environ.get("BAYER_KB_ROOT")
    kb_root = Path(kb_root_env).expanduser().resolve() if kb_root_env else None
    kb_index = _kb_index(kb_root) if kb_root else {}

    extra: List[Path] = []
    path_env = os.environ.get("BAYER_ASSET_PATH", "")
    if path_env:
        for part in path_env.split(os.pathsep):
            part = part.strip()
            if part:
                extra.append(Path(part).expanduser().resolve())

    aliases = manifest.get("aliases") or {}
    results = [
        resolve_one(a, repo_root, assets_root, kb_root, kb_index, extra, aliases)
        for a in manifest.get("assets", [])
    ]
    meta = {
        "version": manifest.get("version"),
        "repo_root": str(repo_root),
        "BAYER_PPT_ROOT": os.environ.get("BAYER_PPT_ROOT"),
        "BAYER_ASSETS_ROOT": assets_root_env,
        "BAYER_KB_ROOT": kb_root_env,
        "BAYER_ASSET_PATH": path_env or None,
    }
    return meta, results


def write_env_file(repo_root: Path, meta: Dict[str, Any], results: List[Dict[str, Any]]) -> Path:
    out = repo_root / ".bayer-ppt.env"
    lines = [
        "# Generated by scripts/resolve_assets.py — do not commit",
        f"BAYER_PPT_ROOT={repo_root}",
    ]
    if meta.get("BAYER_ASSETS_ROOT"):
        lines.append(f"BAYER_ASSETS_ROOT={meta['BAYER_ASSETS_ROOT']}")
    if meta.get("BAYER_KB_ROOT"):
        lines.append(f"BAYER_KB_ROOT={meta['BAYER_KB_ROOT']}")
    if meta.get("BAYER_ASSET_PATH"):
        lines.append(f"BAYER_ASSET_PATH={meta['BAYER_ASSET_PATH']}")

    for r in results:
        if r["resolved"]:
            lines.append(f"{env_id_key(r['id'])}={r['resolved']}")

    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def patch_potx_to_pptx(src: Path, dest: Path) -> None:
    """Copy potx/pptx and patch content-type template → presentation if needed."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)

    try:
        with zipfile.ZipFile(dest, "r") as zin:
            names = zin.namelist()
            if "[Content_Types].xml" not in names:
                return
            ct = zin.read("[Content_Types].xml").decode("utf-8")
            if CONTENT_TYPES_TEMPLATE not in ct:
                return
            patched = ct.replace(CONTENT_TYPES_TEMPLATE, CONTENT_TYPES_PRESENTATION)
            # Rebuild zip with patched content types
            tmp = dest.with_suffix(dest.suffix + ".tmp")
            with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED) as zout:
                for item in zin.infolist():
                    data = zin.read(item.filename)
                    if item.filename == "[Content_Types].xml":
                        data = patched.encode("utf-8")
                    zout.writestr(item, data)
        tmp.replace(dest)
    except zipfile.BadZipFile:
        # Leave the copy as-is; caller still has a file
        pass


def prepare_master(repo_root: Path, results: List[Dict[str, Any]]) -> Path:
    by_id = {r["id"]: r for r in results}
    entry = by_id.get("icon-library-potx")
    if not entry or not entry.get("resolved"):
        raise FileNotFoundError(
            "icon-library-potx not resolved; set BAYER_ASSET_ICON_LIBRARY_POTX "
            "or place brand-assets/source/icon-language.potx / configure BAYER_KB_ROOT"
        )
    src = Path(entry["resolved"])
    dest = repo_root / "exports" / "bayer-radiology-master.pptx"
    patch_potx_to_pptx(src, dest)
    return dest


def cmd_check(meta: Dict[str, Any], results: List[Dict[str, Any]], write_env: bool, repo_root: Path) -> int:
    required_missing = [r for r in results if not r["optional"] and r["missing"]]
    optional_missing = [r for r in results if r["optional"] and r["missing"]]
    resolved = [r for r in results if not r["missing"]]

    report = {
        "ok": len(required_missing) == 0,
        "repo_root": meta["repo_root"],
        "resolved_count": len(resolved),
        "required_missing": [{"id": r["id"], "rel": r["rel"]} for r in required_missing],
        "optional_missing": [
            {"id": r["id"], "rel": r["rel"], "required_for": r["required_for"]}
            for r in optional_missing
        ],
        "resolved": [
            {"id": r["id"], "path": r["resolved"], "via": r["via"]} for r in resolved
        ],
    }

    if write_env:
        env_path = write_env_file(repo_root, meta, results)
        report["env_file"] = str(env_path)

    print(json.dumps(report, indent=2, ensure_ascii=False))

    if optional_missing:
        for r in optional_missing:
            print(
                f"warning: optional proprietary asset missing: {r['id']} "
                f"(rel={r['rel']}) — use brand-kit specs only for that capability",
                file=sys.stderr,
            )

    if required_missing:
        for r in required_missing:
            print(
                f"error: required brand-kit asset missing: {r['id']} (rel={r['rel']})",
                file=sys.stderr,
            )
        return 1
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Resolve Bayer-ppt assets")
    parser.add_argument("--check", action="store_true", help="Validate required assets")
    parser.add_argument("--json", action="store_true", help="Print full resolution map")
    parser.add_argument("--get", metavar="ID", help="Print path for one asset id")
    parser.add_argument("--write-env", action="store_true", help="Write .bayer-ppt.env")
    parser.add_argument(
        "--prepare-master",
        action="store_true",
        help="Copy resolved icon-library potx to exports/bayer-radiology-master.pptx",
    )
    args = parser.parse_args(argv)

    if not any([args.check, args.json, args.get, args.write_env, args.prepare_master]):
        parser.print_help()
        return 2

    try:
        repo_root = find_repo_root()
        meta, results = resolve_all(repo_root)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    by_id = {r["id"]: r for r in results}
    # Resolve aliases for --get
    aliases = load_manifest(repo_root).get("aliases") or {}

    if args.get:
        key = args.get
        if key in aliases:
            key = aliases[key]
        entry = by_id.get(key)
        if not entry or not entry.get("resolved"):
            print(f"error: asset not resolved: {args.get}", file=sys.stderr)
            return 1
        print(entry["resolved"])
        return 0

    if args.prepare_master:
        try:
            dest = prepare_master(repo_root, results)
            print(str(dest))
        except Exception as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1

    if args.json and not args.check:
        payload = {"meta": meta, "assets": results}
        if args.write_env:
            env_path = write_env_file(repo_root, meta, results)
            payload["env_file"] = str(env_path)
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0

    if args.write_env and not args.check and not args.json:
        env_path = write_env_file(repo_root, meta, results)
        print(str(env_path))
        return 0

    if args.check:
        return cmd_check(meta, results, args.write_env, repo_root)

    return 0


if __name__ == "__main__":
    sys.exit(main())
