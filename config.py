"""
Configuration settings for the Text-to-Video Generator
"""

import os
from pathlib import Path

class Config:
    """Configuration class for the application"""
    
    # API Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')
    
    # Video Settings
    DEFAULT_VIDEO_RESOLUTION = (1280, 720)  # 720p
    DEFAULT_CLIP_DURATION = 5  # seconds
    DEFAULT_MAX_CLIPS = 3
    DEFAULT_FPS = 24
    
    # Text Overlay Settings
    TEXT_FONT_SIZE = 50
    TEXT_COLOR = 'white'
    TEXT_STROKE_COLOR = 'black'
    TEXT_STROKE_WIDTH = 2
    TEXT_POSITION = 'center'
    TEXT_WIDTH_RATIO = 0.8  # 80% of video width
    
    # Pexels API Settings
    PEXELS_BASE_URL = "https://api.pexels.com/videos/search"
    PEXELS_VIDEOS_PER_KEYWORD = 2
    PEXELS_ORIENTATION = 'landscape'
    
    # OpenAI Settings
    OPENAI_MODEL = "gpt-3.5-turbo"
    OPENAI_MAX_TOKENS = 500
    
    # File Settings
    OUTPUT_DIR = Path("output")
    TEMP_DIR = Path("temp")
    DEFAULT_OUTPUT_NAME = "output_video.mp4"
    
    # Video Processing Settings
    VIDEO_CODEC = 'libx264'
    AUDIO_CODEC = 'aac'
    
    # Logging Settings
    LOG_LEVEL = 'INFO'
    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    
    @staticmethod
    def ensure_directories():
        """Create necessary directories if they don't exist"""
        Config.OUTPUT_DIR.mkdir(exist_ok=True)
        Config.TEMP_DIR.mkdir(exist_ok=True)
    
    @staticmethod
    def validate_api_keys():
        """Validate that required API keys are available"""
        missing_keys = []
        
        if not Config.OPENAI_API_KEY:
            missing_keys.append("OPENAI_API_KEY")
        
        if not Config.PEXELS_API_KEY:
            missing_keys.append("PEXELS_API_KEY")
        
        if missing_keys:
            raise ValueError(f"Missing required API keys: {', '.join(missing_keys)}")
        
        return True

# Video quality presets
VIDEO_PRESETS = {
    'low': {
        'resolution': (640, 360),
        'fps': 24,
        'bitrate': '500k'
    },
    'medium': {
        'resolution': (1280, 720),
        'fps': 24,
        'bitrate': '2500k'
    },
    'high': {
        'resolution': (1920, 1080),
        'fps': 30,
        'bitrate': '5000k'
    }
}

# Text style presets
TEXT_STYLES = {
    'minimal': {
        'fontsize': 40,
        'color': 'white',
        'stroke_color': 'black',
        'stroke_width': 1
    },
    'bold': {
        'fontsize': 60,
        'color': 'white',
        'stroke_color': 'black',
        'stroke_width': 3
    },
    'elegant': {
        'fontsize': 45,
        'color': '#f0f0f0',
        'stroke_color': '#333333',
        'stroke_width': 2
    }
}
