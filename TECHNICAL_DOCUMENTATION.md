# 📚 Dokumentasi Teknis - YOLO BISINDO Predictor

## 📖 Table of Contents
1. [Architecture](#architecture)
2. [Dependencies](#dependencies)
3. [Code Structure](#code-structure)
4. [API Reference](#api-reference)
5. [Configuration](#configuration)
6. [Performance Optimization](#performance-optimization)

## Architecture

### System Overview
```
┌─────────────────────────────────────────────────────────┐
│           YOLO BISINDO Predictor App                    │
├─────────────────────────────────────────────────────────┤
│                  Streamlit Frontend                      │
│  ┌─────────────┬──────────────┬──────────────┐          │
│  │Upload Image │ Webcam Video │Phone Camera  │          │
│  └──────┬──────┴──────┬───────┴──────┬───────┘          │
├─────────┼─────────────┼──────────────┼─────────────────┤
│         Backend Processing Layer                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Image Preprocessing (OpenCV)                     │  │
│  │ Model Inference (PyTorch/ONNX)                   │  │
│  │ Results Post-processing                          │  │
│  └──────────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────────┤
│           Model Layer                                   │
│  ┌──────────────┬──────────────┬──────────────────┐    │
│  │YOLOv8n-cls   │ YOLOv8 Custom│ TFLite Models    │    │
│  │Classification│ Detection    │ (FP32/FP16)      │    │
│  └──────────────┴──────────────┴──────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

## Dependencies

### Core Libraries
| Library | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.28.1 | Web UI Framework |
| opencv-python | 4.8.1.78 | Image/Video Processing |
| torch | 2.1.1 | PyTorch Deep Learning |
| ultralytics | 8.0.202 | YOLO Implementation |
| pillow | 10.0.1 | Image Handling |
| numpy | 1.24.3 | Numerical Computing |
| torchvision | 0.16.1 | Computer Vision Utilities |

### Installation Priority
```
1. numpy (base dependency)
2. torch (core deep learning)
3. torchvision (model utilities)
4. pillow (image support)
5. opencv-python (video/image processing)
6. ultralytics (YOLO models)
7. streamlit (web interface)
```

## Code Structure

### Main Application File: `yolo_bisindo.py`

#### 1. Initialization
```python
# Page Configuration
st.set_page_config(
    page_title="YOLO BISINDO Predictor",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS Styling
st.markdown("""<style>...""")
```

#### 2. Model Loading
```python
@st.cache_resource
def load_model(model_path):
    """Load dan cache model untuk performa optimal"""
    model = YOLO(model_path)
    return model
```

**Key Features:**
- `@st.cache_resource` decorator untuk caching
- Lazy loading saat dibutuhkan
- Error handling untuk model tidak ditemukan

#### 3. Main Tabs

##### Tab 1: Upload Gambar
```
┌─────────────────────────────────┐
│     Upload Gambar Tab           │
├─────────────────────────────────┤
│ File Uploader                   │
│  ↓                              │
│ Image Preprocessing             │
│  ↓                              │
│ Model Inference                 │
│  ↓                              │
│ Results Display                 │
│  - Original Image               │
│  - Annotated Image              │
│  - Predictions Table            │
└─────────────────────────────────┘
```

**Functions:**
- `predict_image()` - Jalankan prediksi
- `draw_predictions()` - Visualisasi hasil

##### Tab 2: Webcam Real-time
```
┌─────────────────────────────────┐
│     Webcam Tab                  │
├─────────────────────────────────┤
│ Control Buttons (Start/Stop)    │
│  ↓                              │
│ Webcam Loop                     │
│  ├─ Capture Frame               │
│  ├─ Preprocess                  │
│  ├─ Inference                   │
│  └─ Display Result              │
│  ↓                              │
│ FPS Counter & Stats             │
└─────────────────────────────────┘
```

**Key Components:**
- `cv2.VideoCapture(0)` untuk akses webcam
- Real-time loop untuk continuous processing
- FPS calculation untuk monitoring

##### Tab 3: Phone Camera
```
┌─────────────────────────────────┐
│     Phone Camera Tab            │
├─────────────────────────────────┤
│ Upload Image/Video              │
│  ↓                              │
│ File Type Detection             │
│  ├─ If Image                    │
│  │  └─ Single Inference         │
│  └─ If Video                    │
│     └─ Frame by Frame Process   │
│  ↓                              │
│ Results Display                 │
└─────────────────────────────────┘
```

## API Reference

### Core Functions

#### `load_model(model_path: str) -> YOLO`
Load model YOLO dengan caching.

**Parameters:**
- `model_path`: Path ke file model (.pt atau .tflite)

**Returns:**
- YOLO model object

**Exceptions:**
- Menampilkan error jika model tidak ditemukan

#### `predict_image(image: np.ndarray, model: YOLO, conf_threshold: float) -> List`
Jalankan prediksi pada gambar.

**Parameters:**
- `image`: Input image (numpy array BGR)
- `model`: YOLO model
- `conf_threshold`: Minimum confidence (0-1)

**Returns:**
- List of detection results

#### `draw_predictions(image: np.ndarray, results: List) -> np.ndarray`
Menggambar bounding box pada gambar.

**Parameters:**
- `image`: Input image
- `results`: Results dari prediksi

**Returns:**
- Annotated image dengan bounding boxes

### Streamlit Specific

#### `@st.cache_resource`
Decorator untuk cache resource berat (models).

#### `st.tabs()`
Membuat tab interface.

#### `st.file_uploader()`
Widget untuk upload file.

#### `st.columns()`
Layout columns untuk responsive design.

## Configuration

### File: `config.json`

```json
{
  "models": {
    "classification": {
      "path": "yolov8n-cls.pt",
      "type": "classification"
    },
    "detection": {
      "path": "best.pt",
      "type": "detection"
    }
  },
  "settings": {
    "default_confidence": 0.5,
    "webcam_resolution": [640, 480],
    "supported_formats": ["jpg", "png", "mp4"]
  }
}
```

### Environment Variables
```
# Optional
YOLO_CACHE_DIR=./models
TORCH_HOME=./torch_cache
```

## Performance Optimization

### 1. Model Caching
```python
@st.cache_resource
def load_model(path):
    return YOLO(path)
```
- Load model sekali saja
- Reuse untuk multiple predictions

### 2. Image Resizing
```python
image = cv2.resize(frame, (640, 480))
```
- Reduce memory usage
- Accelerate inference
- Maintain aspect ratio

### 3. GPU Acceleration
```python
# Automatic GPU detection
model = YOLO("best.pt")  # Uses GPU if available
```

### 4. Batch Processing
```python
conf = confidence_threshold
results = model.predict(image, conf=conf)
```
- Set confidence threshold tinggi untuk skip low-confidence detections
- Reduce processing time

### 5. Frame Skipping (Optional Enhancement)
```python
frame_count = 0
skip_frames = 2

if frame_count % skip_frames == 0:
    results = model.predict(frame)

frame_count += 1
```

## Monitoring & Logging

### FPS Tracking
```python
import time
frame_time = time.time()
fps = 1 / (current_time - frame_time)
```

### Result Logging
```python
# Save prediction results
results_json = results[0].to_json()
```

## Error Handling

### Model Loading Errors
```python
try:
    model = YOLO(model_path)
except Exception as e:
    st.error(f"Error loading model: {e}")
```

### Webcam Errors
```python
if not cap.isOpened():
    st.error("Webcam tidak dapat diakses")
```

### File Upload Errors
```python
if uploaded_file is None:
    st.warning("Pilih file terlebih dahulu")
```

## Development Notes

### Adding New Model
1. Save model file ke folder
2. Update `config.json` dengan path baru
3. Add option di radio button
4. Test loading dan inference

### Customizing UI
Ubah CSS di section:
```python
st.markdown("""
    <style>
    :root {
        --primary-color: #YOUR_COLOR;
    }
    </style>
""", unsafe_allow_html=True)
```

### Debugging Tips
1. Use `st.write()` untuk output
2. Check console untuk error messages
3. Use `@st.cache_resource` dengan `show_spinner=True`
4. Test models locally sebelum deploy

## Resources

- [YOLO Documentation](https://docs.ultralytics.com/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [OpenCV Tutorials](https://docs.opencv.org/)
- [PyTorch Documentation](https://pytorch.org/docs/)

---

**Last Updated:** December 2024
**Version:** 1.0
