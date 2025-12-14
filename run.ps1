# YOLO BISINDO Predictor - PowerShell Launcher
# Jalankan dengan: powershell -ExecutionPolicy Bypass -File run.ps1

Write-Host "======================================" -ForegroundColor Cyan
Write-Host "  YOLO BISINDO Predictor Launcher" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Check Python installation
Write-Host "🐍 Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ $pythonVersion found" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Please install Python first." -ForegroundColor Red
    Exit 1
}

Write-Host ""
Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
python -m pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to install dependencies" -ForegroundColor Red
    Exit 1
}

Write-Host ""
Write-Host "🚀 Launching Streamlit application..." -ForegroundColor Yellow
Write-Host "💻 App will open at http://localhost:8501" -ForegroundColor Cyan
Write-Host ""

streamlit run yolo_bisindo.py
