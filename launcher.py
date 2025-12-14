"""
Launcher untuk YOLO BISINDO Predictor
Jalankan file ini untuk memulai aplikasi dengan instalasi dependencies otomatis
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install semua dependencies dari requirements.txt"""
    print("=" * 50)
    print("  YOLO BISINDO Predictor - Dependency Installer")
    print("=" * 50)
    print()
    
    try:
        print("📦 Menginstall dependencies...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )
        print("✅ Dependencies berhasil diinstall")
        return True
    except Exception as e:
        print(f"❌ Error saat menginstall: {e}")
        return False

def run_streamlit():
    """Jalankan aplikasi Streamlit"""
    print()
    print("🚀 Meluncurkan aplikasi Streamlit...")
    print("💻 Aplikasi akan terbuka di http://localhost:8501")
    print()
    
    try:
        subprocess.run(["streamlit", "run", "yolo_bisindo.py"])
    except Exception as e:
        print(f"❌ Error saat menjalankan Streamlit: {e}")

if __name__ == "__main__":
    # Install dependencies
    if install_dependencies():
        # Jalankan Streamlit
        run_streamlit()
    else:
        print("\n❌ Gagal menginstall dependencies. Silakan cek error message di atas.")
        sys.exit(1)
