@echo off
title Kerala Talking Statue Kiosk (Standalone - No Python Required)
cd /d "%~dp0"

echo ================================================================
echo    Starting Kerala Talking Statue & Toy Kiosk (Standalone)
echo ================================================================

REM 1. Set Windows power state to ALWAYS AWAKE using native Win32 API via PowerShell
start /b powershell -NoProfile -Command ^
  "$sig = '[DllImport(\"kernel32.dll\")] public static extern uint SetThreadExecutionState(uint esFlags);'; " ^
  "$type = Add-Type -MemberDefinition $sig -Name 'WinPower' -Namespace 'Win32' -PassThru; " ^
  "Write-Host '[+] Keeping Windows awake 24/7...'; " ^
  "while($true) { [void]$type::SetThreadExecutionState(0x80000003); Start-Sleep -Seconds 60 }"

REM 2. Locate Microsoft Edge or Chrome
set "BROWSER_EXE=C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not exist "%BROWSER_EXE%" set "BROWSER_EXE=C:\Program Files\Microsoft\Edge\Application\msedge.exe"
if not exist "%BROWSER_EXE%" set "BROWSER_EXE=%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe"
if not exist "%BROWSER_EXE%" set "BROWSER_EXE=C:\Program Files\Google\Chrome\Application\chrome.exe"
if not exist "%BROWSER_EXE%" set "BROWSER_EXE=C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

set "TARGET_HTML=%~dp0index.html"
if not exist "%TARGET_HTML%" set "TARGET_HTML=%~dp0web\index.html"

echo [+] Launching Statue Kiosk Desktop Window...

if exist "%BROWSER_EXE%" (
    start "" "%BROWSER_EXE%" --app="file:///%TARGET_HTML%" --start-maximized --use-fake-ui-for-media-stream --autoplay-policy=no-user-gesture-required
) else (
    start "" "file:///%TARGET_HTML%"
)

echo.
echo ================================================================
echo  [OK] Statue Kiosk is now ACTIVE!
echo  - Microphone & Speaker are ready.
echo  - Windows PC will NOT sleep or turn off screen.
echo  - Close this window only when you want to stop the kiosk.
echo ================================================================
pause
