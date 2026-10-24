$ErrorActionPreference = 'Continue'
$targetScript = Join-Path $PSScriptRoot "accessmap-site\Start-AccessMap.ps1"
if (Test-Path $targetScript) {
    & $targetScript
} else {
    $indexPath = Join-Path $PSScriptRoot "accessmap-site\index.html"
    Start-Process $indexPath
}
