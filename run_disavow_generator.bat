@echo off
echo Disavow List Generator for BlueCap Advisors
echo =========================================
echo.

REM Check if Python is installed
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH. Please install Python and try again.
    pause
    exit /b 1
)

REM Check if pandas is installed
python -c "import pandas" > nul 2>&1
if %errorlevel% neq 0 (
    echo Installing pandas module...
    pip install pandas
)

REM Run the disavow list generator
echo Running disavow list generator...
python create_disavow_list.py "C:\Users\gunja\OneDrive\Desktop\bluecapeconomicadvisors.com-backlinks-2025-04-18.xls"

echo.
echo Process complete!
pause
