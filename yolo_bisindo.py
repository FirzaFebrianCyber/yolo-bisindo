import streamlit as st
import numpy as np
from PIL import Image
import tempfile
import os

try:
    import cv2
    from ultralytics import YOLO
except ImportError:
    st.error("Dependencies not installed")
    st.stop()

st.set_page_config(page_title="YOLO BISINDO", page_icon="🤖", layout="wide")

st.markdown("""
    <style>
    .title-box {
        background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title-box'><h1>🤖 YOLO BISINDO Predictor</h1><p>Deteksi Objek Dengan AI</p></div>", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    try:
        # Use best.pt - model for BISINDO abjad detection (26 classes A-Z)
        import os
        if os.path.exists("best.pt"):
            model = YOLO("best.pt")
            st.success("✓ Model BISINDO 26 Abjad loaded")
            return model
        else:
            st.error("❌ best.pt tidak ditemukan!")
            return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

with st.sidebar:
    st.header("⚙️ Settings")
    confidence = st.slider("Confidence Threshold", 0.0, 1.0, 0.5, 0.05)
    st.info("Model: best.pt\n26 Kelas BISINDO Abjad (A-Z)")

model = load_model()

if model is None:
    st.error("Model failed to load")
    st.stop()

tab1, tab2, tab3, tab4 = st.tabs(["📸 Upload", "🎥 Webcam", "📱 Phone", "ℹ️ Info"])

# ===== TAB 1: UPLOAD =====
with tab1:
    st.header("📸 Upload Gambar")
    
    uploaded = st.file_uploader("Pilih gambar", type=["jpg", "jpeg", "png", "bmp"])
    
    if uploaded:
        col1, col2 = st.columns(2)
        
        with col1:
            img = Image.open(uploaded)
            # Convert RGBA to RGB if needed
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            st.image(img, caption="Gambar Original", width=300)
            img_array = np.array(img)
        
        with col2:
            st.subheader("📊 Hasil Deteksi")
            
            with st.spinner("🔄 Memproses..."):
                try:
                    # Run prediction (classification)
                    results = model.predict(source=img_array, conf=confidence, verbose=False)
                    
                    if results is not None and len(results) > 0:
                        result = results[0]
                        
                        # For classification model - get top predictions
                        if hasattr(result, 'probs') and result.probs is not None:
                            probs = result.probs
                            top_idx = int(probs.top1) if hasattr(probs, 'top1') else np.argmax(probs.data.cpu().numpy())
                            top_conf = float(probs.top1conf) if hasattr(probs, 'top1conf') else float(np.max(probs.data.cpu().numpy()))
                            class_name = result.names[top_idx]
                            
                            st.success(f"✓ Abjad Terdeteksi!")
                            st.write("")
                            st.markdown(f"### 🔤 **{class_name}**")
                            st.write(f"Confidence: `{top_conf*100:.2f}%`")
                            st.divider()
                            
                            # Show top 3 predictions
                            st.write("**Top 3 Predictions:**")
                            sorted_probs = np.argsort(probs.data.cpu().numpy())[::-1][:3]
                            
                            for rank, idx in enumerate(sorted_probs, 1):
                                conf = float(probs.data.cpu().numpy()[idx])
                                cls_name = result.names[idx]
                                st.write(f"{rank}. **{cls_name}**: `{conf*100:.2f}%`")
                        else:
                            st.warning("⚠️ Tidak ada prediksi")
                    else:
                        st.warning("⚠️ Prediksi gagal")
                
                except Exception as e:
                    st.error(f"❌ Error prediksi: {str(e)}")

# ===== TAB 2: WEBCAM =====
with tab2:
    st.header("🎥 Webcam Real-time")
    
    st.subheader("📹 Capture Foto Langsung")
    st.info("💡 Klik tombol CAPTURE untuk foto langsung dari webcam Anda")
    
    # Create HTML5 camera input
    camera_html = """
    <div style="text-align: center; padding: 20px;">
        <video id="webcam" autoplay playsinline style="width: 100%; max-width: 500px; border-radius: 10px;"></video>
        <br><br>
        <button onclick="captureImage()" style="padding: 10px 20px; font-size: 16px; background-color: #4ECDC4; color: white; border: none; border-radius: 5px; cursor: pointer;">📸 CAPTURE</button>
        <canvas id="canvas" style="display: none;"></canvas>
    </div>
    
    <script>
    const video = document.getElementById('webcam');
    const canvas = document.getElementById('canvas');
    
    navigator.mediaDevices.getUserMedia({video: true})
        .then(stream => {
            video.srcObject = stream;
        })
        .catch(err => {
            console.error('Error accessing webcam:', err);
            document.getElementById('webcam').innerHTML = 'Webcam tidak dapat diakses';
        });
    
    function captureImage() {
        const context = canvas.getContext('2d');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        context.drawImage(video, 0, 0);
        
        canvas.toBlob(blob => {
            const url = URL.createObjectURL(blob);
            window.parent.postMessage({type: 'camera_capture', data: url}, '*');
        });
    }
    </script>
    """
    
    st.html(camera_html)

# ===== TAB 3: PHONE =====
with tab3:
    st.header("📱 Kamera Handphone")
    
    st.subheader("📹 Capture Foto Langsung")
    st.info("💡 Gunakan kamera handphone Anda untuk capture foto abjad")
    
    # Create HTML5 camera input for phone
    camera_html_phone = """
    <div style="text-align: center; padding: 20px;">
        <video id="webcam_phone" autoplay playsinline style="width: 100%; max-width: 500px; border-radius: 10px;"></video>
        <br><br>
        <button onclick="captureImagePhone()" style="padding: 10px 20px; font-size: 16px; background-color: #FF6B6B; color: white; border: none; border-radius: 5px; cursor: pointer;">📸 CAPTURE</button>
        <canvas id="canvas_phone" style="display: none;"></canvas>
    </div>
    
    <script>
    const video_phone = document.getElementById('webcam_phone');
    const canvas_phone = document.getElementById('canvas_phone');
    
    navigator.mediaDevices.getUserMedia({video: true})
        .then(stream => {
            video_phone.srcObject = stream;
        })
        .catch(err => {
            console.error('Error accessing camera:', err);
            document.getElementById('webcam_phone').innerHTML = 'Kamera tidak dapat diakses';
        });
    
    function captureImagePhone() {
        const context = canvas_phone.getContext('2d');
        canvas_phone.width = video_phone.videoWidth;
        canvas_phone.height = video_phone.videoHeight;
        context.drawImage(video_phone, 0, 0);
        
        canvas_phone.toBlob(blob => {
            const url = URL.createObjectURL(blob);
            window.parent.postMessage({type: 'camera_capture_phone', data: url}, '*');
        });
    }
    </script>
    """
    
    st.html(camera_html_phone)

# ===== TAB 4: INFO =====
with tab4:
    st.header("ℹ️ Informasi")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📸 Fitur
        - **Upload Gambar**: Prediksi gambar dari komputer
        - **Webcam**: Deteksi real-time dari kamera
        - **Handphone**: Upload foto/video dari handphone
        - **Adjustable**: Sesuaikan confidence threshold
        """)
    
    with col2:
        st.markdown("""
        ### 🤖 Model
        - **Type**: YOLOv8 Classification
        - **File**: best.pt
        - **Classes**: 26 Abjad (A-Z)
        - **Framework**: PyTorch
        - **Task**: BISINDO Sign Language Detection
        """)
    
    st.divider()
    
    st.markdown("""
    ### 💡 Tips Penggunaan
    1. **Pencahayaan**: Pastikan pencahayaan cukup
    2. **Confidence**: Tinggi = lebih ketat, Rendah = lebih sensitif
    3. **Jarak**: Optimal 30-100cm dari objek
    4. **Format**: JPG, PNG untuk gambar; MP4, MOV untuk video
    """)

st.markdown("---")
st.markdown("<center>Made with ❤️ | YOLO BISINDO v1.0</center>", unsafe_allow_html=True)
