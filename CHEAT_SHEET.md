# 📋 CHEAT SHEET - Quick Reference

## 🚀 START APP

```
Method 1 (Easiest):
  Double-click → run.bat

Method 2 (PowerShell):
  powershell -ExecutionPolicy Bypass -File run.ps1

Method 3 (Command Line):
  streamlit run yolo_bisindo.py
```

**Result:** Browser opens at `http://localhost:8501`

---

## 📸 USAGE MODES

### Mode 1: Upload Image
```
1. Click "📸 Upload Gambar" tab
2. Choose image file (JPG/PNG/BMP)
3. Wait for prediction
4. See results with bounding boxes
```

### Mode 2: Webcam Real-time
```
1. Click "🎥 Webcam Real-time" tab
2. Click "🎬 Mulai Webcam"
3. Allow browser access to webcam
4. Live streaming starts
5. Click "🛑 Stop Webcam" to stop
```

### Mode 3: Phone Camera
```
1. Take photo/video with phone camera
2. Click "📱 Kamera Handphone" tab
3. Upload file
4. App processes automatically
5. See analysis results
```

---

## ⚙️ SETTINGS SIDEBAR

```
Model Selection:
  □ Classification (yolov8n-cls.pt)
  □ Detection (best.pt) ← Recommended
  □ TFLite Float32
  □ TFLite Float16

Confidence Threshold: [0.0 ─────── 1.0]
  Lower = More detections (more false positives)
  Higher = Fewer detections (more accurate)
  Default: 0.5 (50%)
```

---

## 🧪 TESTING & DIAGNOSTICS

```powershell
# Run full system test
python test_system.py

# Or double-click
test.bat

# Output: ✅ All tests passed!
```

**Tests:**
- Python imports ✓
- Model files exist ✓
- Model loading works ✓
- Config file valid ✓
- Utilities functional ✓
- GPU available ✓

---

## 🐛 QUICK FIXES

| Problem | Solution |
|---------|----------|
| Python not found | Install Python 3.8+ from python.org |
| Port 8501 in use | Run: `streamlit run yolo_bisindo.py --server.port 8502` |
| Webcam not working | Browser → Settings → Allow camera access |
| Model not loading | Check model files exist in folder |
| App is slow | Increase confidence threshold to 0.7 |
| Out of memory | Use TFLite Float16 model |
| GPU not detected | NVIDIA GPU + CUDA needed for GPU mode |

---

## 📁 IMPORTANT FILES

```
yolo_bisindo.py    ← Main app (DO NOT RENAME)
utils.py           ← Helper functions
config.json        ← Configuration
requirements.txt   ← Dependencies
run.bat            ← Launcher
```

---

## 🔧 CONFIGURATION (config.json)

```json
{
  "default_confidence": 0.5,        // 0.0 to 1.0
  "webcam_resolution": [640, 480],  // [width, height]
  "max_file_size_mb": 200
}
```

Change settings:
1. Open config.json in text editor
2. Edit values
3. Save
4. Restart app

---

## 💻 COMMAND REFERENCE

```powershell
# Install dependencies manually
pip install -r requirements.txt

# Run app
streamlit run yolo_bisindo.py

# Run with custom port
streamlit run yolo_bisindo.py --server.port 8502

# Create virtual environment
python -m venv env
.\env\Scripts\Activate.ps1

# Install specific package
pip install ultralytics

# Check package version
pip show streamlit

# Update pip
python -m pip install --upgrade pip

# List installed packages
pip list

# Run test suite
python test_system.py
```

---

## 🎨 CUSTOMIZE COLORS

Edit `yolo_bisindo.py`, find CSS section:

```python
:root {
    --primary-color: #FF6B6B;      ← Main color (pink)
    --secondary-color: #4ECDC4;    ← Secondary color (teal)
    --success-color: #45B7D1;      ← Success color (blue)
}
```

Hex colors:
- Red: #FF6B6B
- Green: #00FF00
- Blue: #0066FF
- Yellow: #FFFF00
- Purple: #9933FF
- Orange: #FF8800

---

## 🎯 MODEL SELECTION

| Model | Size | Speed | Accuracy | Use Case |
|-------|------|-------|----------|----------|
| yolov8n-cls.pt | 50MB | ⚡⚡⚡ | Medium | Classification |
| best.pt | 500MB | ⚡⚡ | High | Detection |
| best_float32.tflite | 200MB | ⚡ | High | Mobile |
| best_float16.tflite | 150MB | ⚡⚡ | Medium | Lightweight |

---

## 🔌 FILE UPLOAD LIMITS

```
Image formats: JPG, JPEG, PNG, BMP
Max size: 200MB
Max dimensions: Auto-resized to 1920x1080

Video formats: MP4, MOV, AVI, MKV
Max size: 200MB
Processing: Frame by frame
```

---

## 📊 OUTPUT FORMATS

**Detection Results:**
```
Object: [Class Name]
Confidence: [0-100%]
Location: x1,y1,x2,y2 (pixel coordinates)
```

**Classification Results:**
```
Top 1: [Class] - [Confidence]%
Top 2: [Class] - [Confidence]%
Top 3: [Class] - [Confidence]%
...
```

---

## ✅ FIRST-TIME SETUP CHECKLIST

- [ ] Python 3.8+ installed
- [ ] All files in same folder
- [ ] Model files present (.pt, .tflite)
- [ ] Ran test.bat - all passed ✓
- [ ] run.bat started app successfully
- [ ] Browser opened automatically
- [ ] Can upload image
- [ ] Can use webcam
- [ ] Can upload phone photo

---

## 🎓 FILE READING ORDER

1. **START_HERE.txt** ← You should read this first
2. **QUICK_START.md** ← 5-minute guide
3. **README.md** ← Full documentation
4. **INSTALLATION_GUIDE.md** ← If having problems
5. **TECHNICAL_DOCUMENTATION.md** ← For code details

---

## 🆘 ERROR MESSAGES

```
"Python was not found"
  → Install Python from python.org

"ModuleNotFoundError: No module named 'streamlit'"
  → pip install -r requirements.txt

"Address already in use"
  → streamlit run yolo_bisindo.py --server.port 8502

"FileNotFoundError: [Errno 2] No such file or directory: 'best.pt'"
  → Check model files exist in folder

"CUDA out of memory"
  → Use smaller model or reduce batch size

"Camera access denied"
  → Allow browser access in system settings
```

---

## 🚀 PERFORMANCE TIPS

```
For Faster Processing:
  ✓ Increase confidence threshold (0.7+)
  ✓ Use lighter model (TFLite Float16)
  ✓ Reduce image size
  ✓ Enable GPU if available

For Better Accuracy:
  ✓ Lower confidence threshold (0.3-0.5)
  ✓ Use larger model (best.pt)
  ✓ Improve lighting
  ✓ Zoom in on object

For Better Webcam:
  ✓ Good lighting
  ✓ Clean camera lens
  ✓ Stable internet
  ✓ Close background apps
```

---

## 🎯 KEYBOARD SHORTCUTS

In Streamlit App:
```
Press 'R' → Rerun app
Press 'C' → Clear cache
Press 'T' → Toggle theme (light/dark)
```

---

## 📞 SUPPORT CHAIN

1. Check QUICK_START.md
2. Run test.bat → all pass?
3. Check Troubleshooting in README.md
4. Read INSTALLATION_GUIDE.md
5. Read TECHNICAL_DOCUMENTATION.md

---

## 🔗 USEFUL LINKS

- YOLO Docs: https://docs.ultralytics.com/
- Streamlit: https://docs.streamlit.io/
- PyTorch: https://pytorch.org/
- OpenCV: https://docs.opencv.org/

---

## 📝 NOTES

- First run takes 2-5 minutes (downloads models)
- After that: ~10 seconds to start
- Webcam needs browser permission
- GPU not required (CPU works fine)
- Maximum 200MB file upload

---

**Quick Help:** Double-click `run.bat` to start!

**Version:** 1.0 | December 2024
