@echo off
setlocal
cd /d "%~dp0"

echo ==============================================
echo  AccessMap - Starting Local Application
echo ==============================================

where python >nul 2>nul
if %errorlevel% equ 0 (
    echo Starting local HTTP server on port 8000...
    start /b python -m http.server 8000 --bind 127.0.0.1
    timeout /t 1 /nobreak >nul
    start http://127.0.0.1:8000/
    echo AccessMap running at http://127.0.0.1:8000/
    goto :done
)

for /d %%D in ("%LOCALAPPDATA%\Programs\Python\Python*") do (
    if exist "%%D\python.exe" (
        echo Found Python at %%D
        echo Starting local HTTP server on port 8000...
        start /b "" "%%D\python.exe" -m http.server 8000 --bind 127.0.0.1
        timeout /t 1 /nobreak >nul
        start http://127.0.0.1:8000/
        echo AccessMap running at http://127.0.0.1:8000/
        goto :done
    )
)

echo Opening AccessMap directly in default browser...
start "" "index.html"

:done
exit /b 0
