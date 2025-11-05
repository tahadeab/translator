"""
Configuration file for the translator application
You can modify these settings according to your preferences
"""

# API Configuration
# Primary API: LibreTranslate (Free, no API key required)
API_URL = "https://libretranslate.com/translate"
DETECT_URL = "https://libretranslate.com/detect"

# Fallback API: MyMemory (Free, no API key required, higher rate limits)
FALLBACK_API_URL = "https://api.mymemory.translated.net/get"
USE_FALLBACK_API = True  # Set to True to use fallback if primary fails

# Default Settings
DEFAULT_TARGET_LANGUAGE = "ar"  # Arabic by default
DEFAULT_SOURCE_LANGUAGE = "auto"  # Auto-detect

# Clipboard Monitoring
CHECK_INTERVAL = 0.1  # Check clipboard every 0.3 seconds (faster = more responsive, catches Ctrl+C better)

# Popup Settings
POPUP_AUTO_CLOSE_TIME = 15000  # Auto-close popup after 15 seconds (in milliseconds)
SKIP_MESSAGE_AUTO_CLOSE_TIME = 5000  # Auto-close skip messages after 5 seconds

# Window Settings
MAIN_WINDOW_WIDTH = 400
MAIN_WINDOW_HEIGHT = 500
POPUP_WINDOW_WIDTH = 500
POPUP_WINDOW_HEIGHT = 400

# Text Detection Settings
MIN_TEXT_LENGTH = 2  # Minimum text length to translate

# Supported Languages
# Format: (Display Name, Language Code)
SUPPORTED_LANGUAGES = [
    ("Arabic (العربية)", "ar"),
    ("English", "en"),
    ("Spanish (Español)", "es"),
    ("French (Français)", "fr"),
    ("German (Deutsch)", "de"),
    ("Russian (Русский)", "ru"),
    ("Chinese (中文)", "zh"),
    ("Japanese (日本語)", "ja"),
    ("Italian (Italiano)", "it"),
    ("Portuguese (Português)", "pt"),
    ("Turkish (Türkçe)", "tr"),
    ("Korean (한국어)", "ko"),
    ("Hindi (हिन्दी)", "hi"),
    ("Dutch (Nederlands)", "nl"),
    ("Polish (Polski)", "pl"),
]

# Code Detection Patterns (to skip translation)
CODE_PATTERNS = [
    r'^\s*(def|class|function|var|let|const|import|from)\s+',
    r'^\s*[{}\[\]();]',
    r'^\s*//|^\s*/\*|^\s*#',
]

# UI Colors
COLOR_SUCCESS = "#4CAF50"
COLOR_ERROR = "#f44336"
COLOR_INFO = "#2196F3"
COLOR_WARNING = "#FF9800"
COLOR_NEUTRAL = "#9E9E9E"

# Font Settings
FONT_FAMILY = "Arial"
FONT_SIZE_NORMAL = 10
FONT_SIZE_LARGE = 12
FONT_SIZE_TITLE = 16
