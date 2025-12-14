@echo off
setlocal enabledelayedexpansion

echo ========================================
echo   YOLO BISINDO - Dependency Installer
echo ========================================
echo.

REM Upgrade pip
echo [1/6] Upgrading pip...
python -m pip install --upgrade pip setuptools wheel

REM Install packages one by one
echo [2/6] Installing numpy...
python -m pip install numpy

echo [3/6] Installing opencv-python...
python -m pip install opencv-python

echo [4/6] Installing pillow...
python -m pip install pillow

echo [5/6] Installing PyTorch...
python -m pip install torch torchvision torchaudio

echo [6/6] Installing Ultralytics and Streamlit...
python -m pip install ultralytics streamlit

echo.
echo ========================================
echo   ✅ Installation Complete!
echo ========================================
echo.
echo Starting application...
cd /d "%~dp0"
streamlit run yolo_bisindo.py

pause
