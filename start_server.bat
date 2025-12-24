@echo off
echo Starting Log Classification System...
echo.
echo Demo UI will be available at: http://localhost:8000
echo API Documentation at: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

cd /d "%~dp0"
call venv\Scripts\activate.bat
python main.py
