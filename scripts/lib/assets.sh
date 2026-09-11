# Optional bash helpers wrapping resolve_assets.py
# shellcheck shell=bash

_bayer_repo_root() {
  if [[ -n "${BAYER_PPT_ROOT:-}" ]]; then
    echo "$BAYER_PPT_ROOT"
    return
  fi
  local here
  here="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
  echo "$here"
}

bayer_resolve() {
  local root
  root="$(_bayer_repo_root)"
  python3 "${root}/scripts/resolve_assets.py" "$@"
}

bayer_asset_path() {
  bayer_resolve --get "$1"
}

bayer_check_assets() {
  bayer_resolve --check
}
