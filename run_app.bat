@echo off
title AI CropCare - Streamlit Application
cd /d "%~dp0"
echo ====================================================
echo Starting AI CropCare - Plant Disease Detection App
echo ====================================================
echo.
.\venv\Scripts\streamlit.exe run main.py
pause
