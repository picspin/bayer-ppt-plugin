#Requires -Version 5.1
<#
.SYNOPSIS
  Windows wrapper for Bayer-ppt install.sh (prefers Git Bash / WSL).

.DESCRIPTION
  Invokes scripts/install.sh with the same flags when bash is available.
  If bash is missing, prints WSL / Git-Bash setup steps and mirrors env vars.

.EXAMPLE
  .\scripts\install.ps1 -SkipPptMaster -SkipAntvRuntime
  .\scripts\install.ps1 -AssetsDir "D:\BayerAssets" -KbDir "D:\KB"
#>
[CmdletBinding()]
param(
  [string]$Prefix = "",
  [switch]$SkipPptMaster,
  [switch]$SkipAntvRuntime,
  [string]$AssetsDir = "",
  [string]$KbDir = ""
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
$InstallSh = Join-Path $PSScriptRoot "install.sh"

function Find-Bash {
  $candidates = @(
    "bash",
    "$env:ProgramFiles\Git\bin\bash.exe",
    "${env:ProgramFiles(x86)}\Git\bin\bash.exe",
    "$env:LOCALAPPDATA\Programs\Git\bin\bash.exe"
  )
  foreach ($c in $candidates) {
    try {
      $cmd = Get-Command $c -ErrorAction SilentlyContinue
      if ($cmd) { return $cmd.Source }
      if (Test-Path $c) { return $c }
    } catch {}
  }
  return $null
}

$bashArgs = @()
if ($Prefix) { $bashArgs += @("--prefix", $Prefix) }
if ($SkipPptMaster) { $bashArgs += "--skip-ppt-master" }
if ($SkipAntvRuntime) { $bashArgs += "--skip-antv-runtime" }
if ($AssetsDir) { $bashArgs += @("--assets-dir", $AssetsDir) }
if ($KbDir) { $bashArgs += @("--kb-dir", $KbDir) }

$bash = Find-Bash
if ($bash) {
  Write-Host "==> Invoking bash install.sh via $bash"
  & $bash $InstallSh @bashArgs
  exit $LASTEXITCODE
}

# WSL fallback
$wsl = Get-Command wsl -ErrorAction SilentlyContinue
if ($wsl) {
  Write-Host "==> bash not on PATH; trying WSL"
  $unixPath = (wsl wslpath -a $InstallSh 2>$null)
  if (-not $unixPath) { $unixPath = $InstallSh -replace '\\', '/' }
  $argLine = ($bashArgs | ForEach-Object {
    if ($_ -match '\s') { "'$_'" } else { $_ }
  }) -join ' '
  wsl bash $unixPath $bashArgs
  exit $LASTEXITCODE
}

Write-Host @"
bash / WSL not found. Options:
  1. Install Git for Windows and re-run:  .\scripts\install.ps1 ...
  2. Enable WSL, then:  wsl bash scripts/install.sh ...
  3. Manual env setup (no full install):

     `$env:BAYER_PPT_ROOT = '$RepoRoot'
     `$env:BAYER_ASSETS_ROOT = '<local proprietary folder>'   # optional
     `$env:BAYER_KB_ROOT = '<KB / SharePoint mount>'          # optional
     python scripts\resolve_assets.py --check --write-env

  Create a venv and:  pip install python-pptx lxml Pillow
  Peer ppt-master:    npx --yes skills add hugohe3/ppt-master
  AntV CDN fallback:  https://infographic.antv.vision/
"@
exit 1
