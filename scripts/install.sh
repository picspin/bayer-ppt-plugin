#!/usr/bin/env bash
# Idempotent one-shot installer for Bayer-ppt + AntV runtime + ppt-master peer.
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: ./scripts/install.sh [--prefix DIR] [--skip-ppt-master] [--skip-antv-runtime]
                            [--assets-dir DIR] [--kb-dir DIR] [-h|--help]

  --prefix DIR           Virtualenv directory (default: $REPO_ROOT/.venv).
                         Vendor clones go to $REPO_ROOT/vendor (or $PREFIX/../vendor
                         when --prefix is customized under a parent layout).
  --skip-ppt-master      Do not install/clone hugohe3/ppt-master
  --skip-antv-runtime    Do not npm-install @antv/infographic under runtime/
  --assets-dir DIR       Local proprietary assets root → BAYER_ASSETS_ROOT
  --kb-dir DIR           Knowledge-base / synced drive root → BAYER_KB_ROOT
  -h, --help             Show this help

After install, agents should set:
  export BAYER_PPT_ROOT=<this-repo>
  export BAYER_ASSETS_ROOT=<optional local binary drop-in>
  export BAYER_KB_ROOT=<optional KB / SharePoint / Notion export mount>
  # or: source "$BAYER_PPT_ROOT/.bayer-ppt.env"
USAGE
}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

PREFIX="${REPO_ROOT}/.venv"
SKIP_PPT_MASTER=0
SKIP_ANTV=0
ASSETS_DIR=""
KB_DIR=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --prefix)
      PREFIX="${2:?--prefix requires DIR}"; shift 2 ;;
    --skip-ppt-master)
      SKIP_PPT_MASTER=1; shift ;;
    --skip-antv-runtime)
      SKIP_ANTV=1; shift ;;
    --assets-dir)
      ASSETS_DIR="${2:?--assets-dir requires DIR}"; shift 2 ;;
    --kb-dir)
      KB_DIR="${2:?--kb-dir requires DIR}"; shift 2 ;;
    -h|--help)
      usage; exit 0 ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2 ;;
  esac
done

echo "==> REPO_ROOT=${REPO_ROOT}"

# --- Python 3.10+ ---
PYTHON=""
for cand in python3.12 python3.11 python3.10 python3; do
  if command -v "$cand" >/dev/null 2>&1; then
    PYTHON="$cand"
    break
  fi
done
if [[ -z "$PYTHON" ]]; then
  echo "error: Python 3 not found" >&2
  exit 1
fi
PY_VER="$("$PYTHON" -c 'import sys; print("%d.%d" % sys.version_info[:2])')"
PY_OK="$("$PYTHON" -c 'import sys; print(1 if sys.version_info >= (3, 10) else 0)')"
if [[ "$PY_OK" != "1" ]]; then
  echo "error: need Python 3.10+, found ${PY_VER} (${PYTHON})" >&2
  exit 1
fi
echo "==> Python ${PY_VER} (${PYTHON})"

# --- venv layout ---
if [[ "$PREFIX" == "${REPO_ROOT}/.venv" ]]; then
  VENV_DIR="$PREFIX"
  VENDOR_ROOT="${REPO_ROOT}/vendor"
else
  VENV_DIR="${PREFIX}"
  # If PREFIX ends with .venv use sibling vendor; else PREFIX/vendor
  if [[ "$(basename "$PREFIX")" == ".venv" ]]; then
    VENDOR_ROOT="$(cd "$(dirname "$PREFIX")" && pwd)/vendor"
  else
    VENDOR_ROOT="${PREFIX}/vendor"
    VENV_DIR="${PREFIX}/.venv"
  fi
fi

mkdir -p "$(dirname "$VENV_DIR")"
if [[ ! -d "$VENV_DIR" ]]; then
  echo "==> Creating venv at ${VENV_DIR}"
  "$PYTHON" -m venv "$VENV_DIR"
else
  echo "==> Reusing venv at ${VENV_DIR}"
fi

# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"
pip install --upgrade pip setuptools wheel >/dev/null
echo "==> Installing minimal Python deps (python-pptx lxml Pillow)"
pip install "python-pptx" "lxml" "Pillow"

PPT_MASTER_ROOT=""

# --- ppt-master peer ---
if [[ "$SKIP_PPT_MASTER" -eq 0 ]]; then
  echo "==> Installing ppt-master peer"
  INSTALLED=0
  if command -v npx >/dev/null 2>&1; then
    if npx --yes skills add hugohe3/ppt-master; then
      INSTALLED=1
      echo "    npx skills add hugohe3/ppt-master succeeded"
    else
      echo "    npx skills add failed; falling back to git clone"
    fi
  else
    echo "    npx not found; falling back to git clone"
  fi

  if [[ "$INSTALLED" -eq 0 ]]; then
    mkdir -p "$VENDOR_ROOT"
    CLONE_DIR="${VENDOR_ROOT}/ppt-master"
    if [[ -d "${CLONE_DIR}/.git" ]]; then
      echo "    Reusing clone ${CLONE_DIR}"
      git -C "$CLONE_DIR" pull --ff-only 2>/dev/null || true
    else
      rm -rf "$CLONE_DIR"
      git clone --depth 1 https://github.com/hugohe3/ppt-master.git "$CLONE_DIR"
    fi
    PPT_MASTER_ROOT="$CLONE_DIR"
    if [[ -f "${CLONE_DIR}/requirements.txt" ]]; then
      echo "    pip install -r ppt-master/requirements.txt"
      pip install -r "${CLONE_DIR}/requirements.txt"
    fi
  else
    for search in \
      "${HOME}/.agents/skills/ppt-master" \
      "${HOME}/.claude/skills/ppt-master" \
      "${HOME}/.cursor/skills/ppt-master"; do
      if [[ -d "$search" ]]; then
        PPT_MASTER_ROOT="$search"
        break
      fi
    done
    if [[ -n "$PPT_MASTER_ROOT" ]]; then
      REQ_FILE="$(find "$PPT_MASTER_ROOT" -maxdepth 4 -name requirements.txt 2>/dev/null | head -1 || true)"
      if [[ -n "$REQ_FILE" ]]; then
        pip install -r "$REQ_FILE" || true
        PPT_MASTER_ROOT="$(cd "$(dirname "$REQ_FILE")" && pwd)"
      fi
    fi
  fi
  echo "    note: infographic-creator is already vendored in this repo (skills/infographic-creator)"
else
  echo "==> Skipping ppt-master (--skip-ppt-master)"
fi

# --- AntV runtime ---
ANTV_RUNTIME="${REPO_ROOT}/runtime/antv-infographic"
if [[ "$SKIP_ANTV" -eq 0 ]]; then
  if command -v npm >/dev/null 2>&1; then
    echo "==> Installing AntV Infographic runtime at ${ANTV_RUNTIME}"
    mkdir -p "$ANTV_RUNTIME"
    if [[ ! -f "${ANTV_RUNTIME}/package.json" ]]; then
      (cd "$ANTV_RUNTIME" && npm init -y >/dev/null 2>&1)
    fi
    (cd "$ANTV_RUNTIME" && npm install @antv/infographic) || {
      echo "warning: npm install @antv/infographic failed — use CDN fallback:" >&2
      echo "  https://infographic.antv.vision/  or https://esm.sh/@antv/infographic" >&2
    }
  else
    echo "warning: npm not found — skip AntV runtime; use CDN:" >&2
    echo "  https://infographic.antv.vision/" >&2
  fi
else
  echo "==> Skipping AntV runtime (--skip-antv-runtime); CDN fallback documented in README"
fi

# --- Env + brand-assets/config.json ---
export BAYER_PPT_ROOT="$REPO_ROOT"
if [[ -n "$ASSETS_DIR" ]]; then
  ASSETS_DIR="$(cd "$ASSETS_DIR" && pwd)"
  export BAYER_ASSETS_ROOT="$ASSETS_DIR"
fi
if [[ -n "$KB_DIR" ]]; then
  KB_DIR="$(cd "$KB_DIR" && pwd)"
  export BAYER_KB_ROOT="$KB_DIR"
fi

mkdir -p "${REPO_ROOT}/brand-assets"
CONFIG_JSON="${REPO_ROOT}/brand-assets/config.json"
VENV_PYTHON="${VENV_DIR}/bin/python"

export _BAYER_CFG_PPT_MASTER_ROOT="$PPT_MASTER_ROOT"
export _BAYER_CFG_VENV_PYTHON="$VENV_PYTHON"
export _BAYER_CFG_REPO_ROOT="$REPO_ROOT"
export _BAYER_CFG_ANTV_RUNTIME="$ANTV_RUNTIME"
export _BAYER_CFG_CONFIG_JSON="$CONFIG_JSON"

"$VENV_PYTHON" - <<'PY'
import json, os
from pathlib import Path

cfg = {
    "assetsRoot": os.environ.get("BAYER_ASSETS_ROOT") or None,
    "kbRoot": os.environ.get("BAYER_KB_ROOT") or None,
    "pptMasterRoot": os.environ.get("_BAYER_CFG_PPT_MASTER_ROOT") or None,
    "venvPython": os.environ.get("_BAYER_CFG_VENV_PYTHON"),
    "repoRoot": os.environ.get("_BAYER_CFG_REPO_ROOT"),
    "antvRuntime": os.environ.get("_BAYER_CFG_ANTV_RUNTIME"),
}
path = Path(os.environ["_BAYER_CFG_CONFIG_JSON"])
path.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")
print(f"==> Wrote {path}")
PY

echo "==> Running resolve_assets.py --check --write-env"
set +e
"$VENV_PYTHON" "${REPO_ROOT}/scripts/resolve_assets.py" --check --write-env
CHECK_RC=$?
set -e
if [[ "$CHECK_RC" -ne 0 ]]; then
  echo "warning: resolve_assets --check reported issues (see JSON above)" >&2
fi

SKIP_NOTE=""
if [[ "$SKIP_ANTV" -eq 1 ]]; then
  SKIP_NOTE="(skipped)"
fi

cat <<NEXT

========================================================================
Bayer-ppt install complete
========================================================================
REPO_ROOT:     ${REPO_ROOT}
VENV:          ${VENV_DIR}
PPT_MASTER:    ${PPT_MASTER_ROOT:-"(npx-installed or skipped)"}
ANTV_RUNTIME:  ${ANTV_RUNTIME} ${SKIP_NOTE}
ENV FILE:      ${REPO_ROOT}/.bayer-ppt.env
CONFIG:        ${CONFIG_JSON}

Next steps for agents / shells:

  export BAYER_PPT_ROOT="${REPO_ROOT}"
  # optional local binaries:
  export BAYER_ASSETS_ROOT="${BAYER_ASSETS_ROOT:-${REPO_ROOT}/brand-assets/source}"
  # optional knowledge base / synced drive:
  # export BAYER_KB_ROOT=/path/to/kb
  source "${REPO_ROOT}/.bayer-ppt.env"

  # verify
  ${VENV_DIR}/bin/python ${REPO_ROOT}/scripts/resolve_assets.py --check

  # prepare radiology working master (if potx resolved)
  ${VENV_DIR}/bin/python ${REPO_ROOT}/scripts/resolve_assets.py --prepare-master

CDN fallback for AntV Infographic (if runtime skipped):
  https://infographic.antv.vision/
========================================================================
NEXT
