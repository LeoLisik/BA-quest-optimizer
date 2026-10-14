@echo off
cd /d "%~dp0"

REM ---- Check Python (needed even if venv exists, in case system is broken) ----
where python >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Python not found in PATH.
    echo Please install Python 3.8+ from https://www.python.org/downloads/
    echo During installation, make sure to check "Add Python to PATH".
    echo.
    pause
    exit /b 1
)

REM ---- Ensure venv exists ----
if not exist ".venv\Scripts\activate.bat" (
    echo Virtual environment not found. Running install.bat...
    echo.
    call install.bat silent
    if errorlevel 1 (
        echo [ERROR] Installation failed. See messages above.
        pause
        exit /b 1
    )
)

REM ---- Activate venv ----
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment.
    pause
    exit /b 1
)

REM ---- Run ----
echo.
echo Starting BA Quest Optimizer...
python main.py

pause