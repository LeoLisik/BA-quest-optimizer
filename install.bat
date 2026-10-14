@echo off
cd /d "%~dp0"

REM ---- Check Python ----
where python >nul 2>nul
if errorlevel 1 (
    echo [ERROR] Python not found in PATH.
    echo.
    echo Please install Python 3.8+ from https://www.python.org/downloads/
    echo During installation, make sure to check "Add Python to PATH".
    echo.
    if "%~1"=="" pause
    exit /b 1
)

REM ---- Check pip ----
python -m pip --version >nul 2>nul
if errorlevel 1 (
    echo [ERROR] pip is not available for the detected Python.
    echo Try reinstalling Python with pip enabled, or run:
    echo     python -m ensurepip --upgrade
    echo.
    if "%~1"=="" pause
    exit /b 1
)

REM ---- Create venv if missing ----
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment.
        if "%~1"=="" pause
        exit /b 1
    )
)

REM ---- Activate venv ----
if not exist ".venv\Scripts\activate.bat" (
    echo [ERROR] venv is broken: activate.bat not found.
    echo Try deleting the .venv folder and running install.bat again.
    if "%~1"=="" pause
    exit /b 1
)
call .venv\Scripts\activate.bat

REM ---- Install requirements ----
echo Installing requirements...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install requirements.
    if "%~1"=="" pause
    exit /b 1
)

echo.
echo Install successful
if "%~1"=="" pause