$ErrorActionPreference = 'Continue'
$siteDirectory = $PSScriptRoot
$indexPath = Join-Path $siteDirectory "index.html"

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host " AccessMap - Starting Local Application Server " -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Cyan

# 1. Detect working Python binary (testing python.exe first, then py.exe, then AppData)
$pythonPath = $null

# Check 'python'
try {
    $cmd = Get-Command python -ErrorAction SilentlyContinue
    if ($cmd) {
        $test = & $cmd.Source -c "import sys; print(sys.executable)" 2>$null
        if ($test -and (Test-Path $test)) {
            $pythonPath = $test
        }
    }
} catch {}

# Check 'py'
if (-not $pythonPath) {
    try {
        $cmd = Get-Command py -ErrorAction SilentlyContinue
        if ($cmd) {
            $test = & $cmd.Source -c "import sys; print(sys.executable)" 2>$null
            if ($test -and (Test-Path $test)) {
                $pythonPath = $test
            }
        }
    } catch {}
}

# Check AppData python install paths
if (-not $pythonPath) {
    $appDataPy = Resolve-Path "$env:LOCALAPPDATA\Programs\Python\Python*\python.exe" -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($appDataPy) {
        $pythonPath = $appDataPy.Path
    }
}

# 2. Select an available port (prefer 8000, scan up to 8050)
$port = 8000
for ($p = 8000; $p -le 8050; $p++) {
    try {
        $tcp = [System.Net.Sockets.TcpClient]::new()
        $tcp.Connect('127.0.0.1', $p)
        $tcp.Close()
        # Port in use, continue to next
    } catch {
        # Port is available
        $port = $p
        break
    }
}

$siteUrl = "http://127.0.0.1:$port/"

if ($pythonPath) {
    Write-Host "Detected Python: $pythonPath" -ForegroundColor Gray
    Write-Host "Starting local HTTP server on port $port..." -ForegroundColor Yellow

    # Launch python HTTP server
    $pyArgs = @('-m', 'http.server', "$port", '--bind', '127.0.0.1')
    $proc = Start-Process -FilePath $pythonPath -ArgumentList $pyArgs -WorkingDirectory $siteDirectory -PassThru -WindowStyle Hidden
    Start-Sleep -Milliseconds 900

    if (-not $proc.HasExited) {
        Write-Host "Server running at: $siteUrl" -ForegroundColor Green
        try {
            Start-Process $siteUrl
        } catch {
            Start-Process $indexPath
        }
    } else {
        Write-Host "Local port server could not bind. Opening AccessMap in direct browser mode..." -ForegroundColor Yellow
        Start-Process $indexPath
    }
} else {
    Write-Host "Python not found. Opening AccessMap directly in default browser..." -ForegroundColor Yellow
    Start-Process $indexPath
}

Write-Host "AccessMap opened successfully!" -ForegroundColor Green
Start-Sleep -Seconds 2
