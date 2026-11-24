# AI CropCare Streamlit Launcher
Set-Location -Path $PSScriptRoot
Write-Host "Starting AI CropCare - Plant Disease Detection App..." -ForegroundColor Green
& ".\venv\Scripts\streamlit.exe" run main.py
