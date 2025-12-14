# 📋 Installation Guide

## 🎯 Tujuan
Instalasi lengkap YOLO BISINDO Predictor dengan semua dependencies.

## ✅ Prerequisites
- Windows 7 atau lebih baru
- Python 3.8 atau lebih baru
- Internet connection (untuk download dependencies)
- Minimal 2GB RAM tersedia

## 🚀 Instalasi Step-by-Step

### Opsi 1: Paling Mudah (Recommended) 🎯

```
┌─────────────────────────────────────────┐
│ 1. Buka folder: C:\Users\DESKTOP\Documents\PCD Peoject
│ 2. Double-click file: run.bat
│ 3. Tunggu hingga selesai
│ 4. Browser otomatis terbuka
│ 5. Aplikasi siap digunakan! ✨
└─────────────────────────────────────────┘
```

**Waktu:** 2-5 menit (first-time)  
**Difficulty:** ⭐ (Very Easy)

---

### Opsi 2: Menggunakan PowerShell

1. **Buka PowerShell sebagai Administrator**
   - Klik Win + X
   - Pilih "Windows PowerShell (Admin)"

2. **Navigate ke folder project**
   ```powershell
   cd "C:\Users\DESKTOP\Documents\PCD Peoject"
   ```

3. **Jalankan script**
   ```powershell
   powershell -ExecutionPolicy Bypass -File run.ps1
   ```

4. **Atau jalankan Python launcher**
   ```powershell
   python launcher.py
   ```

**Waktu:** 2-5 menit  
**Difficulty:** ⭐⭐ (Easy)

---

### Opsi 3: Manual Installation (Advanced)

#### Step 1: Install Python (jika belum)
```
Download dari: https://www.python.org/downloads/
✓ Centang "Add Python to PATH" saat install
```

#### Step 2: Verify Python Installation
```powershell
python --version
pip --version
```

Should output:
```
Python 3.x.x
pip 23.x.x from C:\...
```

#### Step 3: Create Virtual Environment (Optional tapi Recommended)
```powershell
# Create virtual environment
python -m venv env

# Activate virtual environment
.\env\Scripts\Activate.ps1

# Verify activation
# Prompt should show (env) at the beginning
```

#### Step 4: Upgrade pip
```powershell
python -m pip install --upgrade pip
```

#### Step 5: Install Dependencies
```powershell
pip install -r requirements.txt
```

**Installation Process:**
```
numpy ........................... ✓ (10 seconds)
pillow .......................... ✓ (30 seconds)
opencv-python ................... ✓ (1-2 minutes)
torch ........................... ✓ (3-5 minutes) *heaviest
torchvision ..................... ✓ (2-3 minutes)
ultralytics ..................... ✓ (1 minute)
streamlit ....................... ✓ (1 minute)
─────────────────────────────────────
Total Time: ~10-15 minutes
```

#### Step 6: Run Application
```powershell
streamlit run yolo_bisindo.py
```

**Waktu:** 10-15 menit (first-time)  
**Difficulty:** ⭐⭐⭐ (Advanced)

---

## 🔍 Verifikasi Instalasi

### Quick Check: Jalankan Test Suite
```powershell
# Windows Command Prompt / PowerShell
double-click test.bat

# Atau manual
python test_system.py
```

**Output yang diharapkan:**
```
✅ Imports PASSED
✅ Model Files PASSED
✅ Config PASSED
✅ Utilities PASSED
✅ GPU Support PASSED
✅ Model Loading PASSED

🎉 All tests passed! Your system is ready!
```

---

## 🐛 Troubleshooting Instalasi

### Problem 1: "Python not found"
**Penyebab:** Python belum diinstall atau tidak di PATH

**Solusi:**
```
1. Download Python: https://www.python.org/downloads/
2. Install dengan centang "Add Python to PATH"
3. Restart computer
4. Coba jalankan lagi
```

**Verify:**
```powershell
python --version  # Harus menampilkan versi Python
```

---

### Problem 2: "pip command not found"
**Penyebab:** pip tidak diinstall dengan Python

**Solusi:**
```powershell
# Try ini terlebih dahulu
python -m pip --version

# Jika masih error, reinstall Python dengan include pip option
# Atau upgrade pip
python -m pip install --upgrade pip
```

---

### Problem 3: "Error installing torch"
**Penyebab:** PyTorch download fail atau incompatible

**Solusi 1 - Reinstall:**
```powershell
pip install --force-reinstall torch torchvision
```

**Solusi 2 - Dengan CUDA (jika punya GPU NVIDIA):**
```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**Solusi 3 - Manual Installation:**
```powershell
# Delete environment
rmdir env /s /q

# Create fresh environment
python -m venv env
.\env\Scripts\Activate.ps1

# Install dependencies one by one
pip install numpy
pip install pillow
pip install opencv-python
pip install torch
pip install torchvision
pip install ultralytics
pip install streamlit
```

---

### Problem 4: "Port 8501 already in use"
**Penyebab:** Port sudah digunakan aplikasi lain

**Solusi:**
```powershell
# Run dengan port berbeda
streamlit run yolo_bisindo.py --server.port 8502
```

---

### Problem 5: "Memory Error" atau "Out of Memory"
**Penyebab:** Insufficient RAM

**Solusi:**
```
1. Close aplikasi lain yang tidak perlu
2. Increase virtual memory
3. Use lighter model (TFLite Float16)
4. Reduce webcam resolution
```

---

## 📦 Dependencies Detail

| Package | Version | Size | Purpose | Time |
|---------|---------|------|---------|------|
| numpy | 1.24.3 | ~30MB | Math operations | 10s |
| pillow | 10.0.1 | ~50MB | Image handling | 30s |
| opencv-python | 4.8.1.78 | ~180MB | Video/Image processing | 1-2m |
| torch | 2.1.1 | ~2GB | Deep learning framework | 3-5m |
| torchvision | 0.16.1 | ~700MB | CV utilities | 2-3m |
| ultralytics | 8.0.202 | ~200MB | YOLO implementation | 1m |
| streamlit | 1.28.1 | ~300MB | Web UI framework | 1m |
| **TOTAL** | | **~4GB** | | **~10-15m** |

---

## 💾 Disk Space Requirements

```
Minimum:
├── Python environment: ~500MB
├── Dependencies: ~4GB
├── Models: ~500MB
└── Cache: ~1GB
──────────────────────
Total: ~6GB

Recommended:
~10GB available space
```

---

## 🔧 Advanced Configuration

### GPU Acceleration (Optional)

Jika punya GPU NVIDIA, optimalkan dengan CUDA:

```powershell
# Uninstall existing torch
pip uninstall torch torchvision

# Install dengan CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Verify CUDA
python -c "import torch; print(torch.cuda.is_available())"
```

**Output yang diharapkan:**
```
True
```

---

### CPU-Only Installation

Jika tidak punya GPU atau ingin CPU-only:

```powershell
# Already default, tapi bisa explicit
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

---

### Virtual Environment (Recommended)

**Mengapa Virtual Environment?**
- ✓ Isolated dependencies
- ✓ Tidak affect sistem Python
- ✓ Easy to remove
- ✓ Multiple projects possible

**Create & Activate:**
```powershell
# Create
python -m venv env

# Activate (Windows)
.\env\Scripts\Activate.ps1

# Deactivate (kapan saja)
deactivate
```

---

## ✅ Post-Installation Checklist

- [ ] Python installed dan 3.8+
- [ ] Dependencies terinstall (test.bat shows all ✓)
- [ ] Model files ada di folder (best.pt, etc)
- [ ] Run application berjalan
- [ ] Webcam berfungsi (jika ada)
- [ ] Upload gambar berfungsi
- [ ] Prediksi menampilkan hasil

---

## 🚀 Selanjutnya

Setelah instalasi sukses:

1. **Baca:** QUICK_START.md untuk panduan penggunaan
2. **Coba:** Semua 3 mode (Upload, Webcam, Phone Camera)
3. **Eksplor:** Settings dan model options
4. **Belajar:** TECHNICAL_DOCUMENTATION.md untuk detail teknis

---

## 📞 Perlu Bantuan?

1. **Installation failing?**
   - Jalankan `python test_system.py` untuk diagnostic
   - Check error messages di console

2. **Model tidak load?**
   - Verify file model ada di folder
   - Check internet connection (first-time download)

3. **Aplikasi lambat?**
   - Check GPU availability
   - Naikkan confidence threshold
   - Use lighter model

4. **Still stuck?**
   - Baca README.md untuk detail lebih lengkap
   - Cek TECHNICAL_DOCUMENTATION.md untuk troubleshooting

---

**Version:** 1.0  
**Last Updated:** December 2024

Good luck! 🎉
