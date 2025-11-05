# 🌐 Instant Multilingual Translator

A Windows desktop application that automatically translates any copied text into Arabic (or other languages) using the free LibreTranslate API.

## ✨ Features

- **Automatic Clipboard Monitoring**: Detects and translates text as soon as you copy it
- **Smart Language Detection**: Automatically detects the source language
- **Intelligent Translation**: Translates ANY language (except target language) to your selected target language
- **Skip Same Language**: Won't translate if text is already in the target language
- **Default Arabic Translation**: Translates to Arabic by default
- **Multi-Language Support**: Switch between 10+ languages (Arabic, English, Spanish, French, German, Russian, Chinese, Japanese, Italian, Portuguese)
- **Smart Text Detection**: Automatically skips URLs and code snippets
- **Formatting Preservation**: Maintains line breaks, punctuation, numbers, and special characters
- **Instant Popup Display**: Shows translations immediately in a convenient popup window
- **Language Info Display**: Shows source and target languages clearly
- **Free API**: Uses LibreTranslate's free API (no API key required)
- **Statistics Tracking**: Keeps count of translations performed
- **Bilingual Interface**: Arabic and English labels for better usability

## 📋 Requirements

- Windows OS
- Python 3.7 or higher
- Internet connection (for API calls)

## 🚀 Installation

### Step 1: Install Python

If you don't have Python installed:
1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, **check "Add Python to PATH"**
3. Complete the installation

### Step 2: Install Dependencies

Open Command Prompt or PowerShell in the project folder and run:

```bash
pip install -r requirements.txt
```

This will install:
- `pyperclip` - for clipboard monitoring
- `requests` - for API communication

### Step 3: Test the API (Optional)

Before running the main app, you can test if the API is working:

```bash
python test_translator.py
```

This will test translations from different languages to verify the API connection.

## 🎯 Usage

### Quick Start (Windows)

**Option 1: Using Batch File (Easiest)**
1. Double-click `install_dependencies.bat` (first time only)
2. Double-click `run_translator.bat` to start the app

**Option 2: Using Command Line**
1. Open Command Prompt or PowerShell in the project folder
2. Run the application:

```bash
python translator.py
```

### Using the Translator

1. **Click "▶ Start Monitoring"** to begin clipboard monitoring
2. **Copy any text** (Ctrl+C) from anywhere on your computer
3. **A popup window will appear** with the translation
4. **Change target language** from the dropdown if needed
5. **Click "⏸ Stop Monitoring"** to pause

### Features in Action

- **Copy Translation**: Click the "📋 Copy Translation" button in the popup to copy the translated text
- **Auto-Close**: Popups automatically close after 15 seconds
- **Statistics**: View the number of translations performed
- **Language Selection**: Choose from 10+ supported languages

## 🔧 Configuration

You can modify the following settings in `translator.py`:

```python
# Line 19-21
self.api_url = "https://libretranslate.com/translate"  # API endpoint
self.target_language = "ar"  # Default target language (ar = Arabic)
self.check_interval = 0.5  # Clipboard check interval in seconds
```

## 🌍 Supported Languages

- Arabic (العربية)
- English
- Spanish (Español)
- French (Français)
- German (Deutsch)
- Russian (Русский)
- Chinese (中文)
- Japanese (日本語)
- Italian (Italiano)
- Portuguese (Português)

## 🛡️ Smart Features

### What Gets Translated
- Regular text content
- Sentences and paragraphs
- Mixed content (text with URLs - only text is translated)

### What Gets Skipped
- URLs (preserved as-is)
- Code snippets (detected by patterns like `def`, `class`, `function`, etc.)
- Very short text (less than 2 characters)
- Pure URL strings

## 📝 Example Output

### Example 1: English to Arabic
When you copy: `"Hello, how are you?"`

The popup shows:
```
🔄 English ➜ Arabic (العربية)

📝 النص الأصلي (English):
Hello, how are you?

✅ الترجمة (Arabic):
مرحبا، كيف حالك؟
```

### Example 2: Spanish to Arabic
When you copy: `"Hola, ¿cómo estás?"`

The popup shows:
```
🔄 Spanish (Español) ➜ Arabic (العربية)

📝 النص الأصلي (Spanish):
Hola, ¿cómo estás?

✅ الترجمة (Arabic):
مرحبا، كيف حالك؟
```

### Example 3: Same Language (Skipped)
When you copy Arabic text while Arabic is the target language:

The popup shows:
```
ℹ️ النص بالفعل باللغة المستهدفة (Arabic)
```
(Auto-closes after 5 seconds)

## 🔍 Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### "Connection error"
- Check your internet connection
- Verify that https://libretranslate.com is accessible
- The free API may have rate limits; wait a moment and try again

### Clipboard not working
- Make sure no other clipboard managers are interfering
- Restart the application
- Check that you have clipboard access permissions

### Translation not appearing
- Ensure "Start Monitoring" is clicked
- Check that the copied text is not a URL or code
- Verify the text is at least 2 characters long

## 🎨 Customization

You can customize the application by editing `config.py`:

### Change Default Language
```python
DEFAULT_TARGET_LANGUAGE = "es"  # Change to Spanish
```

### Adjust Popup Duration
```python
POPUP_AUTO_CLOSE_TIME = 20000  # 20 seconds (in milliseconds)
SKIP_MESSAGE_AUTO_CLOSE_TIME = 3000  # 3 seconds
```

### Change Window Sizes
```python
MAIN_WINDOW_WIDTH = 450
MAIN_WINDOW_HEIGHT = 550
POPUP_WINDOW_WIDTH = 600
POPUP_WINDOW_HEIGHT = 450
```

### Adjust Clipboard Check Speed
```python
CHECK_INTERVAL = 0.3  # Check every 0.3 seconds (faster but uses more CPU)
```

### Add More Languages
```python
SUPPORTED_LANGUAGES = [
    ("Arabic (العربية)", "ar"),
    ("English", "en"),
    # Add your language here:
    ("Swedish (Svenska)", "sv"),
]
```

### Change Minimum Text Length
```python
MIN_TEXT_LENGTH = 3  # Require at least 3 characters
```

## 🔒 Privacy & Security

- All translations are processed through LibreTranslate's API
- No data is stored locally or logged
- Clipboard content is only read when monitoring is active
- You can stop monitoring at any time

## 📦 Project Structure

```
trinsloit/
│
├── translator.py              # Main application file
├── config.py                  # Configuration settings (customizable)
├── test_translator.py         # API testing script
├── requirements.txt           # Python dependencies
├── run_translator.bat         # Quick start script (Windows)
├── install_dependencies.bat   # Dependency installer (Windows)
└── README.md                 # This file
```

## 🔄 How It Works

1. **Clipboard Monitoring**: The app continuously monitors your clipboard for new text
2. **Language Detection**: When text is copied, it detects the source language using LibreTranslate's detection API
3. **Smart Translation Logic**:
   - If source language = target language → Skip translation (show info message)
   - If source language ≠ target language → Translate to target language
4. **Instant Display**: Shows a popup with the translation, source language, and target language
5. **Auto-Close**: Popup closes automatically after 15 seconds (5 seconds for skip messages)

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

This project is open source and available for personal and educational use.

## 🙏 Credits

- **LibreTranslate**: Free and open-source translation API
- **pyperclip**: Cross-platform clipboard module
- **tkinter**: Python's standard GUI library

## 💡 Tips

1. **Keep the main window open** while monitoring (you can minimize it)
2. **Use keyboard shortcuts** (Ctrl+C) for quick copying
3. **Change languages on-the-fly** without restarting
4. **Copy translations** directly from the popup for reuse

---

**Enjoy automatic translations! 🎉**
