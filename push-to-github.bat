@echo off
setlocal enabledelayedexpansion
cd /d "%~dp0"

echo =================================================================
echo  AccessMap - Push Files to GitHub Repository
echo  Target: https://github.com/smahammadarshad08-debu/conclaveindia.git
echo =================================================================

set "GIT_EXE=git"

:: 1. Check if git is already available in PATH
where git >nul 2>nul
if %errorlevel% equ 0 (
    set "GIT_EXE=git"
    goto :git_ready
)

:: 2. Check standard Git installation directories
if exist "C:\Program Files\Git\cmd\git.exe" (
    set "GIT_EXE=C:\Program Files\Git\cmd\git.exe"
    goto :git_ready
)
if exist "C:\Program Files\Git\bin\git.exe" (
    set "GIT_EXE=C:\Program Files\Git\bin\git.exe"
    goto :git_ready
)
if exist "%LOCALAPPDATA%\Programs\Git\cmd\git.exe" (
    set "GIT_EXE=%LOCALAPPDATA%\Programs\Git\cmd\git.exe"
    goto :git_ready
)
if exist "C:\Program Files (x86)\Git\cmd\git.exe" (
    set "GIT_EXE=C:\Program Files (x86)\Git\cmd\git.exe"
    goto :git_ready
)

:: 3. Git is not found - attempt automatic install via winget
echo.
echo [!] Git is not yet installed on this PC.
echo [*] Attempting automatic install via Windows Package Manager (winget)...
echo.
winget install --id Git.Git -e --source winget

:: Re-check after install
if exist "C:\Program Files\Git\cmd\git.exe" (
    set "GIT_EXE=C:\Program Files\Git\cmd\git.exe"
    goto :git_ready
)
if exist "%LOCALAPPDATA%\Programs\Git\cmd\git.exe" (
    set "GIT_EXE=%LOCALAPPDATA%\Programs\Git\cmd\git.exe"
    goto :git_ready
)
where git >nul 2>nul
if %errorlevel% equ 0 (
    set "GIT_EXE=git"
    goto :git_ready
)

echo.
echo [!] Automatic installation requires admin approval or was cancelled.
echo [*] Opening official Git for Windows download page...
start https://git-scm.com/download/win
echo.
echo Please run the installer, then re-run this script: push-to-github.bat
pause
exit /b 1

:git_ready
echo.
echo [*] Using Git: !GIT_EXE!
echo [*] Initializing Git repository...
"!GIT_EXE!" init

echo [*] Configuring remote repository...
"!GIT_EXE!" remote remove origin 2>nul
"!GIT_EXE!" remote add origin https://github.com/smahammadarshad08-debu/conclaveindia.git
"!GIT_EXE!" branch -M main

echo [*] Staging all files...
"!GIT_EXE!" add .

echo [*] Checking Git identity...
"!GIT_EXE!" config user.email >nul 2>nul
if !errorlevel! neq 0 (
    echo [*] Setting Git author identity...
    "!GIT_EXE!" config user.name "smahammadarshad08-debu"
    "!GIT_EXE!" config user.email "smahammadarshad08-debu@users.noreply.github.com"
)

echo [*] Committing files...
"!GIT_EXE!" commit -m "feat: complete AccessMap platform aligned with MoHUA Harmonised Guidelines 2021"

echo.
echo [*] Pushing files to GitHub...
echo (If prompted, sign in via your browser or Personal Access Token)
echo.
"!GIT_EXE!" push -u origin main

if !errorlevel! neq 0 (
    echo.
    echo [*] Remote repository has existing files (e.g., initial README/License).
    echo [*] Syncing and updating repository...
    "!GIT_EXE!" pull origin main --rebase --allow-unrelated-histories 2>nul
    "!GIT_EXE!" push -u origin main 2>nul
    if !errorlevel! neq 0 (
        echo [*] Pushing project files to remote main branch (--force)...
        "!GIT_EXE!" push -u origin main --force
    )
)

if !errorlevel! equ 0 (
    echo.
    echo =================================================================
    echo  SUCCESS: All files pushed to conclaveindia repository!
    echo  https://github.com/smahammadarshad08-debu/conclaveindia
    echo =================================================================
) else (
    echo.
    echo [!] Push failed or requires authentication.
    echo Please verify your GitHub login or token permissions and try again.
)

pause
exit /b 0
