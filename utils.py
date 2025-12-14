"""
Utilities untuk YOLO BISINDO Predictor
Helper functions dan utilities
"""

import cv2
import numpy as np
from PIL import Image
import json
import os
from datetime import datetime

class ImageUtils:
    """Utilities untuk image processing"""
    
    @staticmethod
    def resize_image(image, max_width=1920, max_height=1080):
        """Resize gambar dengan mempertahankan aspect ratio"""
        height, width = image.shape[:2]
        
        if width > max_width or height > max_height:
            scale = min(max_width/width, max_height/height)
            new_width = int(width * scale)
            new_height = int(height * scale)
            return cv2.resize(image, (new_width, new_height))
        
        return image
    
    @staticmethod
    def enhance_image(image, brightness=0, contrast=1.0):
        """Enhance gambar dengan brightness dan contrast"""
        image = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
        return image
    
    @staticmethod
    def convert_to_rgb(image):
        """Convert BGR ke RGB"""
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    @staticmethod
    def draw_text(image, text, position, font_scale=0.8, color=(255, 255, 255)):
        """Draw text pada image"""
        cv2.putText(image, text, position, cv2.FONT_HERSHEY_SIMPLEX, 
                   font_scale, color, 2, cv2.LINE_AA)
        return image
    
    @staticmethod
    def draw_box(image, x1, y1, x2, y2, color=(0, 255, 0), thickness=2):
        """Draw bounding box pada image"""
        cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
        return image


class VideoUtils:
    """Utilities untuk video processing"""
    
    @staticmethod
    def get_video_properties(video_path):
        """Get properties dari video file"""
        cap = cv2.VideoCapture(video_path)
        
        properties = {
            'fps': int(cap.get(cv2.CAP_PROP_FPS)),
            'frame_count': int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),
            'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        }
        
        cap.release()
        return properties
    
    @staticmethod
    def get_video_duration(video_path):
        """Get durasi video dalam detik"""
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        duration = frame_count / fps
        cap.release()
        return duration


class ConfigManager:
    """Manage config file"""
    
    @staticmethod
    def load_config(config_path="config.json"):
        """Load config dari file"""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return None
    
    @staticmethod
    def save_config(config, config_path="config.json"):
        """Save config ke file"""
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
    
    @staticmethod
    def get_model_path(model_type="detection", config=None):
        """Get path untuk model berdasarkan type"""
        if config is None:
            config = ConfigManager.load_config()
        
        if config and "models" in config:
            models = config["models"]
            if model_type == "detection":
                return models.get("detection", {}).get("path", "best.pt")
            elif model_type == "classification":
                return models.get("classification", {}).get("path", "yolov8n-cls.pt")
        
        return None


class FPSCounter:
    """Counter untuk FPS calculation"""
    
    def __init__(self):
        self.prev_frame_time = 0
        self.current_time = 0
        self.fps = 0
    
    def update(self):
        """Update FPS counter"""
        self.current_time = datetime.now()
        
        if self.prev_frame_time != 0:
            time_diff = (self.current_time - self.prev_frame_time).total_seconds()
            self.fps = 1 / time_diff if time_diff > 0 else 0
        
        self.prev_frame_time = self.current_time
        return self.fps
    
    def get_fps(self):
        """Get current FPS"""
        return self.fps


class ResultLogger:
    """Log hasil prediksi"""
    
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
    
    def log_prediction(self, filename, predictions):
        """Log hasil prediksi"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(self.log_dir, f"predictions_{timestamp}.json")
        
        log_data = {
            "timestamp": timestamp,
            "filename": filename,
            "predictions": predictions
        }
        
        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        return log_file


class ColorPalette:
    """Color palette untuk visualization"""
    
    # BGR format untuk OpenCV
    COLORS = {
        'red': (0, 0, 255),
        'green': (0, 255, 0),
        'blue': (255, 0, 0),
        'yellow': (0, 255, 255),
        'cyan': (255, 255, 0),
        'magenta': (255, 0, 255),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'orange': (0, 165, 255),
        'purple': (128, 0, 128),
    }
    
    @staticmethod
    def get_color(name):
        """Get color dari nama"""
        return ColorPalette.COLORS.get(name.lower(), (0, 255, 0))
    
    @staticmethod
    def get_random_color():
        """Get random color"""
        return tuple(np.random.randint(0, 256, 3).tolist())


class ValidationUtils:
    """Utilities untuk validation"""
    
    SUPPORTED_IMAGE_FORMATS = ['jpg', 'jpeg', 'png', 'bmp', 'gif']
    SUPPORTED_VIDEO_FORMATS = ['mp4', 'mov', 'avi', 'mkv']
    MAX_FILE_SIZE_MB = 200
    
    @staticmethod
    def is_valid_image_file(filepath):
        """Check apakah file adalah valid image"""
        if not os.path.exists(filepath):
            return False
        
        ext = filepath.split('.')[-1].lower()
        return ext in ValidationUtils.SUPPORTED_IMAGE_FORMATS
    
    @staticmethod
    def is_valid_video_file(filepath):
        """Check apakah file adalah valid video"""
        if not os.path.exists(filepath):
            return False
        
        ext = filepath.split('.')[-1].lower()
        return ext in ValidationUtils.SUPPORTED_VIDEO_FORMATS
    
    @staticmethod
    def is_valid_file_size(filepath):
        """Check ukuran file"""
        file_size_mb = os.path.getsize(filepath) / (1024 * 1024)
        return file_size_mb <= ValidationUtils.MAX_FILE_SIZE_MB
    
    @staticmethod
    def validate_file(filepath):
        """Validate file secara menyeluruh"""
        if not os.path.exists(filepath):
            return False, "File tidak ditemukan"
        
        if not ValidationUtils.is_valid_file_size(filepath):
            return False, f"Ukuran file melebihi {ValidationUtils.MAX_FILE_SIZE_MB}MB"
        
        if (ValidationUtils.is_valid_image_file(filepath) or 
            ValidationUtils.is_valid_video_file(filepath)):
            return True, "File valid"
        
        return False, "Format file tidak didukung"


# Export utilities
__all__ = [
    'ImageUtils',
    'VideoUtils',
    'ConfigManager',
    'FPSCounter',
    'ResultLogger',
    'ColorPalette',
    'ValidationUtils'
]
