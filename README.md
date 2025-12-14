# 🤖 YOLO BISINDO Predictor

Aplikasi modern dan user-friendly untuk deteksi dan klasifikasi gambar menggunakan YOLO dengan interface Streamlit yang menarik.

## ✨ Fitur Utama

### 📸 Upload Gambar
- Upload gambar dari komputer (JPG, PNG, BMP)
- Prediksi otomatis dengan hasil visual yang jelas
- Tampilkan confidence score untuk setiap deteksi
- Support multiple object detection

### 🎥 Webcam Real-time
- Streaming live dari webcam
- Deteksi real-time dengan FPS counter
- Adjustable confidence threshold
- Capture frame functionality

### 📱 Kamera Handphone
- Support foto dari kamera handphone
- Support video dari handphone
- Processing frame-by-frame untuk video
- Detail analisis untuk setiap deteksi

### 🎨 Interface Modern
- Design dengan gradient colors
- Responsive layout
- Dark theme yang nyaman dipandang
- Custom styling untuk widget

## 🚀 Instalasi & Menjalankan

### Metode 1: Double-click File Batch (Windows)
```
1. Double-click file "run.bat"
2. Tunggu dependencies terinstall
3. Aplikasi akan otomatis membuka di browser
```

### Metode 2: Command Line (Manual)
```powershell
# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
streamlit run yolo_bisindo.py
```

### Metode 3: Menggunakan Virtual Environment (Recommended)
```powershell
# Buat virtual environment
python -m venv env

# Aktivasi virtual environment
.\env\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
streamlit run yolo_bisindo.py
```

## 📋 Requirements

```
streamlit==1.28.1
opencv-python==8.0.1.78
pillow==10.0.1
torch==2.1.1
torchvision==0.16.1
ultralytics==8.0.202
numpy==1.24.3
```

## 📁 Struktur File

```
PCD Project/
├── yolo_bisindo.py           # Main application
├── requirements.txt          # Dependencies
├── run.bat                   # Windows batch runner
├── README.md                 # This file
├── best.pt                   # Detection model
├── yolov8n-cls.pt           # Classification model
├── best_float32.tflite      # TFLite 32-bit model
├── best_float16.tflite      # TFLite 16-bit model
└── results (1).csv          # Results data
```

## 🎯 Panduan Penggunaan

### Tab 1: Upload Gambar
1. Klik tombol "Upload Gambar"
2. Pilih file gambar dari komputer
3. Aplikasi otomatis memproses gambar
4. Lihat hasil deteksi dengan bounding box
5. Detail confidence score ditampilkan

### Tab 2: Webcam Real-time
1. Pastikan webcam sudah terhubung
2. Klik tombol "Mulai Webcam"
3. Streaming langsung akan dimulai
4. Hasil deteksi ditampilkan real-time
5. Klik "Stop Webcam" untuk menghentikan

### Tab 3: Kamera Handphone
1. Ambil foto/video dengan kamera handphone
2. Upload file ke aplikasi
3. Aplikasi memproses dan menampilkan hasil
4. Untuk video, processing dilakukan frame-by-frame

### Tab 4: Informasi
- Informasi tentang YOLO dan BISINDO
- Daftar model yang tersedia
- Tips dan trik penggunaan
- Panduan penggunaan lengkap

## ⚙️ Konfigurasi

### Pengaturan Sidebar
- **Pilih Model**: Pilih antara Classification atau Detection model
- **Confidence Threshold**: Sesuaikan sensitivitas deteksi (0.0 - 1.0)

### Optimal Settings
- **Untuk deteksi general**: Confidence = 0.5
- **Untuk deteksi yang lebih ketat**: Confidence = 0.7
- **Untuk deteksi yang lebih santai**: Confidence = 0.3

## 🖼️ Model Tersedia

| Model | Tipe | Kegunaan |
|-------|------|----------|
| yolov8n-cls.pt | Classification | Klasifikasi gambar |
| best.pt | Detection | Deteksi multi-objek |
| best_float32.tflite | TensorFlow Lite | Mobile optimization (32-bit) |
| best_float16.tflite | TensorFlow Lite | Mobile optimization (16-bit) |

## 🔧 Troubleshooting

### Webcam tidak berfungsi
- Pastikan webcam sudah terhubung
- Beri izin akses browser ke webcam
- Restart aplikasi

### Model tidak bisa diload
- Pastikan file model ada di folder yang sama
- Cek nama file model sesuai dengan code
- Pastikan CUDA/PyTorch terinstall dengan benar

### Aplikasi lambat
- Tingkatkan confidence threshold
- Gunakan model yang lebih ringan
- Kurangi ukuran gambar input

### Error: "ImportError"
- Install ulang dependencies: `pip install -r requirements.txt`
- Pastikan Python version >= 3.8

## 💡 Tips Optimasi

1. **Untuk Webcam Real-time**:
   - Gunakan resolusi 640x480
   - Set confidence threshold 0.5
   - Pastikan lighting cukup

2. **Untuk Video**:
   - File tidak lebih dari 1GB
   - Format: MP4 atau MOV
   - FPS: 24-30 untuk hasil terbaik

3. **Untuk Akurasi Terbaik**:
   - Fokus kamera pada objek utama
   - Pencahayaan yang baik
   - Jarak pandang optimal

## 📊 Output

### Untuk Image/Detection
- Gambar dengan bounding box
- Class name untuk setiap objek
- Confidence score (%)
- Koordinat bounding box

### Untuk Classification
- Top 5 predictions
- Confidence score untuk setiap class
- Progress bar untuk visualization

## 🎨 Customization

Anda bisa mengubah warna dengan memodifikasi CSS di bagian:
```python
:root {
    --primary-color: #FF6B6B;
    --secondary-color: #4ECDC4;
    --success-color: #45B7D1;
}
```

## 📝 Notes

- Pertama kali menjalankan mungkin membutuhkan waktu untuk download model
- GPU recommended untuk webcam real-time
- Webcam memerlukan izin akses browser

## 🤝 Support & Feedback

Jika ada masalah atau saran:
1. Cek bagian Troubleshooting
2. Verifikasi semua dependencies terinstall
3. Restart aplikasi

## 📄 License

YOLO BISINDO Predictor - Made with ❤️

---

**Version**: 1.0  
**Last Updated**: December 2024
