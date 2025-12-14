# 🚀 Quick Start Guide

## 5 Langkah Mudah untuk Menjalankan Aplikasi

### Step 1: Buka Folder Project
```
📁 Buka folder: C:\Users\DESKTOP\Documents\PCD Peoject
```

### Step 2: Pilih Salah Satu Cara Menjalankan

#### ✅ Cara 1: Double-Click File (PALING MUDAH)
```
1. Cari file: run.bat (atau run.ps1 untuk PowerShell)
2. Double-click file tersebut
3. Tunggu hingga aplikasi terbuka di browser
4. Selesai! 🎉
```

#### ✅ Cara 2: Command Prompt / Terminal
```powershell
# Buka Command Prompt atau PowerShell di folder project
# Kemudian ketik:

python launcher.py
```

#### ✅ Cara 3: Manual Install & Run
```powershell
# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
streamlit run yolo_bisindo.py
```

---

## Pertama Kali Menjalankan

⏱️ **Waktu Tunggu:** 2-5 menit (first-time setup)
- Download models
- Install dependencies
- Kompilasi PyTorch

📱 **Browser Otomatis Terbuka** di:
```
http://localhost:8501
```

Jika tidak terbuka otomatis, buka browser dan ketik URL di atas.

---

## 📖 Cara Menggunakan

### 🖼️ Mode 1: Upload Gambar
```
1. Klik Tab "📸 Upload Gambar"
2. Klik "Pilih gambar untuk diprediksi"
3. Select gambar dari komputer
4. Tunggu hasil prediksi
5. Lihat hasil dengan bounding box
```

**Format yang Didukung:** JPG, PNG, BMP  
**Ukuran Max:** 200MB

### 🎥 Mode 2: Webcam Real-time
```
1. Klik Tab "🎥 Webcam Real-time"
2. Pastikan webcam terhubung
3. Klik tombol "🎬 Mulai Webcam"
4. Browser akan minta izin akses webcam
5. Klik "Allow" / "Izinkan"
6. Streaming live akan dimulai
7. Klik "🛑 Stop Webcam" untuk berhenti
```

**Requirements:**
- Webcam/USB Camera terhubung
- Browser dengan WebRTC support

### 📱 Mode 3: Kamera Handphone
```
1. Ambil foto/video dengan kamera handphone
2. Klik Tab "📱 Kamera Handphone"
3. Klik upload untuk gambar/video
4. Pilih file dari handphone
5. Aplikasi otomatis analisis
6. Lihat hasil analisis
```

**Format Gambar:** JPG, PNG  
**Format Video:** MP4, MOV

---

## ⚙️ Settings

### Di Sidebar Kiri:

**1. Pilih Model:**
```
□ Classification (yolov8n-cls.pt)  ← Untuk klasifikasi gambar
□ Detection (best.pt)               ← Untuk deteksi objek (RECOMMENDED)
□ TFLite Float32                    ← Untuk mobile optimization
□ TFLite Float16                    ← Untuk mobile (paling ringan)
```

**2. Confidence Threshold (0-100%):**
```
Lebih tinggi = Lebih ketat (lebih sedikit detection)
Lebih rendah = Lebih santai (lebih banyak detection)

Rekomendasi: 50% (default)
```

---

## 🆘 Troubleshooting

### ❌ "Python not found"
**Solusi:**
1. Install Python dari https://www.python.org/downloads/
2. Pastikan "Add Python to PATH" dicentang saat install
3. Restart computer
4. Coba jalankan ulang

### ❌ "Webcam tidak berfungsi"
**Solusi:**
1. Periksa webcam terhubung
2. Beri izin akses di browser
3. Coba browser lain (Chrome/Firefox)
4. Restart browser

### ❌ "Model tidak bisa load"
**Solusi:**
1. Pastikan file model ada di folder (best.pt, yolov8n-cls.pt, dll)
2. Tunggu internet stabil saat first-time load
3. Delete folder cache dan coba ulang
4. Reinstall: `pip install --upgrade ultralytics`

### ❌ "Aplikasi lambat"
**Solusi:**
1. Naikkan Confidence Threshold ke 70%
2. Gunakan model yang lebih ringan
3. Gunakan GPU jika tersedia
4. Close aplikasi lain untuk free up RAM

### ❌ "Error saat install dependencies"
**Solusi:**
```powershell
# Update pip terlebih dahulu
python -m pip install --upgrade pip

# Coba install ulang
pip install -r requirements.txt --force-reinstall
```

---

## 📊 Hasil Output

### Untuk Deteksi (Detection):
```
✓ Gambar original + Gambar dengan bounding box
✓ Nama objek yang terdeteksi
✓ Confidence score (probabilitas keakuratan)
✓ Koordinat lokasi objek
```

### Untuk Klasifikasi (Classification):
```
✓ Top 5 prediksi kemungkinan kelas
✓ Confidence score untuk masing-masing
✓ Progress bar visualization
```

---

## 💡 Tips & Tricks

### Untuk Hasil Terbaik:
1. **Pencahayaan:** Pastikan area terang dan tidak terlalu gelap
2. **Fokus:** Arahkan kamera langsung ke objek yang dideteksi
3. **Background:** Gunakan background yang kontras
4. **Jarak:** Jarak optimal 30-100cm dari kamera

### GPU Acceleration (Opsional):
Jika punya GPU NVIDIA:
```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Custom Model:
Untuk menambahkan model sendiri:
1. Letakkan file `.pt` di folder
2. Update `config.json`
3. Add option di sidebar
4. Restart aplikasi

---

## 📁 File Structure

```
PCD Project/
├── yolo_bisindo.py           ⭐ Main App
├── utils.py                  🛠️ Helper Functions
├── requirements.txt          📦 Dependencies
├── config.json               ⚙️ Configuration
├── run.bat                   🖱️ Windows Runner
├── run.ps1                   💻 PowerShell Runner
├── launcher.py               🚀 Python Launcher
├── README.md                 📖 Full Documentation
├── QUICK_START.md            ⚡ This File
├── TECHNICAL_DOCUMENTATION.md 🔧 Technical Details
├── best.pt                   🎯 Detection Model
├── yolov8n-cls.pt           🏷️ Classification Model
├── best_float32.tflite      📱 TFLite Model
└── best_float16.tflite      📱 TFLite Model (Compact)
```

---

## 🎓 Belajar Lebih Lanjut

### Dokumentasi Lengkap:
- `README.md` - Full documentation
- `TECHNICAL_DOCUMENTATION.md` - Technical details

### Resources:
- [YOLO Docs](https://docs.ultralytics.com/)
- [Streamlit Tutorial](https://docs.streamlit.io/library/get-started)
- [OpenCV Guide](https://docs.opencv.org/)

---

## 🎉 Selesai!

Anda sudah siap menggunakan YOLO BISINDO Predictor!

**Pertanyaan atau Masalah?**
1. Cek file dokumentasi
2. Cek Troubleshooting section
3. Verify file model ada di folder

---

**Version:** 1.0  
**Last Updated:** December 2024
