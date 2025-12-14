"""
Testing & Demo Script untuk YOLO BISINDO Predictor
Gunakan untuk test model loading dan basic functionality
"""

import os
import sys
from pathlib import Path

# Add project to path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

def test_imports():
    """Test semua imports"""
    print("=" * 50)
    print("🧪 Testing Imports...")
    print("=" * 50)
    
    try:
        import numpy as np
        print("✅ numpy imported successfully")
    except ImportError as e:
        print(f"❌ numpy import failed: {e}")
        return False
    
    try:
        import cv2
        print("✅ cv2 (OpenCV) imported successfully")
    except ImportError as e:
        print(f"❌ cv2 import failed: {e}")
        return False
    
    try:
        from PIL import Image
        print("✅ PIL imported successfully")
    except ImportError as e:
        print(f"❌ PIL import failed: {e}")
        return False
    
    try:
        import torch
        print(f"✅ torch imported successfully (version: {torch.__version__})")
    except ImportError as e:
        print(f"❌ torch import failed: {e}")
        return False
    
    try:
        from ultralytics import YOLO
        print("✅ ultralytics imported successfully")
    except ImportError as e:
        print(f"❌ ultralytics import failed: {e}")
        return False
    
    try:
        import streamlit
        print(f"✅ streamlit imported successfully (version: {streamlit.__version__})")
    except ImportError as e:
        print(f"❌ streamlit import failed: {e}")
        return False
    
    try:
        from utils import ImageUtils, ConfigManager, ValidationUtils
        print("✅ utils imported successfully")
    except ImportError as e:
        print(f"❌ utils import failed: {e}")
        return False
    
    return True


def test_model_files():
    """Test keberadaan model files"""
    print("\n" + "=" * 50)
    print("📁 Checking Model Files...")
    print("=" * 50)
    
    models = [
        "best.pt",
        "yolov8n-cls.pt",
        "best_float32.tflite",
        "best_float16.tflite"
    ]
    
    all_exist = True
    for model in models:
        model_path = project_dir / model
        if model_path.exists():
            file_size = model_path.stat().st_size / (1024 * 1024)
            print(f"✅ {model} found ({file_size:.2f} MB)")
        else:
            print(f"⚠️ {model} not found")
            all_exist = False
    
    return all_exist


def test_model_loading():
    """Test loading model YOLO"""
    print("\n" + "=" * 50)
    print("🎯 Testing Model Loading...")
    print("=" * 50)
    
    try:
        from ultralytics import YOLO
        
        model_path = project_dir / "best.pt"
        if model_path.exists():
            print(f"Loading model: {model_path}")
            model = YOLO(str(model_path))
            print("✅ Model loaded successfully!")
            
            # Get model info
            print(f"   Model type: {model.task}")
            print(f"   Model names: {model.names}")
            
            return True
        else:
            print(f"⚠️ Model file not found: {model_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return False


def test_config():
    """Test config loading"""
    print("\n" + "=" * 50)
    print("⚙️ Testing Configuration...")
    print("=" * 50)
    
    try:
        from utils import ConfigManager
        
        config_path = project_dir / "config.json"
        if config_path.exists():
            config = ConfigManager.load_config(str(config_path))
            if config:
                print("✅ Config loaded successfully!")
                print(f"   App name: {config.get('app', {}).get('name', 'N/A')}")
                print(f"   Version: {config.get('app', {}).get('version', 'N/A')}")
                print(f"   Models available: {len(config.get('models', {}))}")
                return True
            else:
                print("❌ Failed to parse config")
                return False
        else:
            print(f"⚠️ Config file not found: {config_path}")
            return False
            
    except Exception as e:
        print(f"❌ Error loading config: {e}")
        return False


def test_utils():
    """Test utility functions"""
    print("\n" + "=" * 50)
    print("🛠️ Testing Utilities...")
    print("=" * 50)
    
    try:
        from utils import ValidationUtils, ColorPalette, FPSCounter
        
        # Test ValidationUtils
        print("\n📋 Testing ValidationUtils:")
        print(f"   Supported image formats: {ValidationUtils.SUPPORTED_IMAGE_FORMATS}")
        print(f"   Supported video formats: {ValidationUtils.SUPPORTED_VIDEO_FORMATS}")
        print(f"   Max file size: {ValidationUtils.MAX_FILE_SIZE_MB}MB")
        
        # Test ColorPalette
        print("\n🎨 Testing ColorPalette:")
        color = ColorPalette.get_color("red")
        print(f"   Red color: {color}")
        
        # Test FPSCounter
        print("\n⏱️ Testing FPSCounter:")
        fps_counter = FPSCounter()
        print(f"   FPSCounter initialized: {fps_counter}")
        
        print("\n✅ All utilities working!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing utilities: {e}")
        return False


def test_gpu():
    """Test GPU availability"""
    print("\n" + "=" * 50)
    print("🖥️ Testing GPU Support...")
    print("=" * 50)
    
    try:
        import torch
        
        gpu_available = torch.cuda.is_available()
        if gpu_available:
            print(f"✅ GPU available!")
            print(f"   Device: {torch.cuda.get_device_name(0)}")
            print(f"   CUDA version: {torch.version.cuda}")
            print(f"   Total VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
        else:
            print("ℹ️ GPU not available - will use CPU")
            print("   (This is OK, but inference will be slower)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error checking GPU: {e}")
        return False


def run_all_tests():
    """Run semua tests"""
    print("\n")
    print("╔" + "=" * 48 + "╗")
    print("║" + " " * 48 + "║")
    print("║" + "  🧪 YOLO BISINDO - System Test Suite".center(48) + "║")
    print("║" + " " * 48 + "║")
    print("╚" + "=" * 48 + "╝")
    
    results = {
        "Imports": test_imports(),
        "Model Files": test_model_files(),
        "Config": test_config(),
        "Utilities": test_utils(),
        "GPU Support": test_gpu(),
        "Model Loading": test_model_loading(),
    }
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Summary")
    print("=" * 50)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:.<35} {status}")
    
    print("=" * 50)
    print(f"Total: {passed}/{total} tests passed")
    print("=" * 50)
    
    if passed == total:
        print("\n🎉 All tests passed! Your system is ready!")
        print("\nNext step: Run 'streamlit run yolo_bisindo.py'")
        return 0
    else:
        print(f"\n⚠️ {total - passed} test(s) failed.")
        print("Please check the errors above and install missing dependencies.")
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    
    # Keep window open on Windows
    if sys.platform == "win32":
        input("\nPress Enter to exit...")
    
    sys.exit(exit_code)
