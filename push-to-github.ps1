$ErrorActionPreference = 'Continue'
Set-Location $PSScriptRoot

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host " AccessMap - Push Files to GitHub Repository" -ForegroundColor Green
Write-Host " Target: https://github.com/smahammadarshad08-debu/conclaveindia.git" -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan

# 1. Locate Git
$gitCmd = Get-Command git -ErrorAction SilentlyContinue
$gitExe = if ($gitCmd) { $gitCmd.Source } else { $null }

if (-not $gitExe) {
    $searchPaths = @(
        "C:\Program Files\Git\cmd\git.exe",
        "C:\Program Files\Git\bin\git.exe",
        "$env:LOCALAPPDATA\Programs\Git\cmd\git.exe",
        "C:\Program Files (x86)\Git\cmd\git.exe"
    )
    foreach ($p in $searchPaths) {
        if (Test-Path $p) {
            $gitExe = $p
            break
        }
    }
}

if (-not $gitExe) {
    Write-Host "`n[!] Git is not installed on this machine." -ForegroundColor Yellow
    Write-Host "[*] Attempting automatic install via winget..." -ForegroundColor Cyan
    winget install --id Git.Git -e --source winget
    Start-Sleep -Seconds 3

    $gitCmd = Get-Command git -ErrorAction SilentlyContinue
    $gitExe = if ($gitCmd) { $gitCmd.Source } else { $null }
    if (-not $gitExe -and (Test-Path "C:\Program Files\Git\cmd\git.exe")) {
        $gitExe = "C:\Program Files\Git\cmd\git.exe"
    }
}

if (-not $gitExe) {
    Write-Host "`n[!] Git installation required. Opening download page..." -ForegroundColor Red
    Start-Process "https://git-scm.com/download/win"
    Write-Host "Please complete Git installation, then re-run this script." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "`n[*] Using Git: $gitExe" -ForegroundColor Green
Write-Host "[*] Initializing repository..." -ForegroundColor Cyan
& $gitExe init

Write-Host "[*] Setting remote origin..." -ForegroundColor Cyan
& $gitExe remote remove origin 2>$null
& $gitExe remote add origin https://github.com/smahammadarshad08-debu/conclaveindia.git
& $gitExe branch -M main

Write-Host "[*] Adding files..." -ForegroundColor Cyan
& $gitExe add .

Write-Host "[*] Checking Git identity..." -ForegroundColor Cyan
$userEmail = & $gitExe config user.email 2>$null
if (-not $userEmail) {
    Write-Host "[*] Configuring Git author identity..." -ForegroundColor Yellow
    & $gitExe config user.name "smahammadarshad08-debu"
    & $gitExe config user.email "smahammadarshad08-debu@users.noreply.github.com"
}

Write-Host "[*] Committing changes..." -ForegroundColor Cyan
& $gitExe commit -m "feat: complete AccessMap platform aligned with MoHUA Harmonised Guidelines 2021"

Write-Host "`n[*] Pushing to GitHub (https://github.com/smahammadarshad08-debu/conclaveindia)..." -ForegroundColor Yellow
Write-Host "If prompted, please complete browser authentication." -ForegroundColor Gray
& $gitExe push -u origin main

if ($LASTEXITCODE -ne 0) {
    Write-Host "`n[*] Remote repository has initial files. Syncing and updating..." -ForegroundColor Cyan
    & $gitExe pull origin main --rebase --allow-unrelated-histories
    & $gitExe push -u origin main
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[*] Pushing with --force to complete initialization..." -ForegroundColor Yellow
        & $gitExe push -u origin main --force
    }
}

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n=================================================================" -ForegroundColor Green
    Write-Host " SUCCESS: Files pushed to https://github.com/smahammadarshad08-debu/conclaveindia" -ForegroundColor Green
    Write-Host "=================================================================" -ForegroundColor Green
} else {
    Write-Host "`n[!] Push completed with status code $LASTEXITCODE. If authentication was needed, please authorize and try again." -ForegroundColor Yellow
}

Read-Host "Press Enter to exit"
