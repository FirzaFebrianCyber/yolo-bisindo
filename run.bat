@echo off
echo ========================================
echo   YOLO BISINDO Predictor Launcher
echo ========================================
echo.
echo Instalasi dependencies...
pip install -r requirements.txt
echo.
echo Meluncurkan aplikasi Streamlit...
streamlit run yolo_bisindo.py
pause
