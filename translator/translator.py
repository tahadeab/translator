"""
Instant Multilingual Translator - Desktop Application
Automatically translates copied text to Arabic using LibreTranslate API
"""

import pyperclip
import tkinter as tk
from tkinter import ttk, messagebox
import requests
import time
import threading
import re
from typing import Optional, List, Tuple
import sys
import platform

# Try to import config, use defaults if not available
try:
    from config import *
except ImportError:
    # Default configuration if config.py is not found
    API_URL = "https://libretranslate.com/translate"
    DETECT_URL = "https://libretranslate.com/detect"
    DEFAULT_TARGET_LANGUAGE = "ar"
    DEFAULT_SOURCE_LANGUAGE = "auto"
    CHECK_INTERVAL = 0.5
    POPUP_AUTO_CLOSE_TIME = 15000
    SKIP_MESSAGE_AUTO_CLOSE_TIME = 5000
    MAIN_WINDOW_WIDTH = 400
    MAIN_WINDOW_HEIGHT = 500
    POPUP_WINDOW_WIDTH = 500
    POPUP_WINDOW_HEIGHT = 400
    MIN_TEXT_LENGTH = 2
    FALLBACK_API_URL = "https://api.mymemory.translated.net/get"
    USE_FALLBACK_API = True
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
    ]
    CODE_PATTERNS = [
        r'^\s*(def|class|function|var|let|const|import|from)\s+',
        r'^\s*[{}\[\]();]',
        r'^\s*//|^\s*/\*|^\s*#',
    ]
    COLOR_SUCCESS = "#4CAF50"
    COLOR_ERROR = "#f44336"
    COLOR_INFO = "#2196F3"
    COLOR_WARNING = "#FF9800"
    COLOR_NEUTRAL = "#9E9E9E"
    FONT_FAMILY = "Arial"
    FONT_SIZE_NORMAL = 10
    FONT_SIZE_LARGE = 12
    FONT_SIZE_TITLE = 16

class TranslatorApp:
    def __init__(self):
        # Configuration from config file
        self.api_url = API_URL
        self.detect_url = DETECT_URL
        self.target_language = DEFAULT_TARGET_LANGUAGE
        self.source_language = DEFAULT_SOURCE_LANGUAGE
        self.check_interval = CHECK_INTERVAL
        self.last_clipboard = ""
        self.is_running = False
        
        # Main window
        self.root = tk.Tk()
        self.root.title("🌐 Instant Translator - مترجم فوري")
        self.root.geometry(f"{MAIN_WINDOW_WIDTH}x{MAIN_WINDOW_HEIGHT}")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Setup UI
        self.setup_ui()
        
        # Popup window reference
        self.popup = None
        
    def setup_ui(self):
        """Setup the main control window UI"""
        # Title
        title_label = tk.Label(
            self.root, 
            text="🌐 Instant Translator", 
            font=("Arial", 16, "bold"),
            pady=10
        )
        title_label.pack()
        
        # Status frame
        status_frame = tk.LabelFrame(self.root, text="Status", padx=10, pady=10)
        status_frame.pack(fill="x", padx=10, pady=5)
        
        self.status_label = tk.Label(
            status_frame, 
            text="⚫ Stopped", 
            font=("Arial", 10),
            fg="red"
        )
        self.status_label.pack()
        
        # Control buttons
        button_frame = tk.Frame(self.root, pady=10)
        button_frame.pack()
        
        self.start_button = tk.Button(
            button_frame,
            text="▶ Start Monitoring",
            command=self.start_monitoring,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5
        )
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.stop_button = tk.Button(
            button_frame,
            text="⏸ Stop Monitoring",
            command=self.stop_monitoring,
            bg="#f44336",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5,
            state="disabled"
        )
        self.stop_button.grid(row=0, column=1, padx=5)
        
        # Language settings
        lang_frame = tk.LabelFrame(self.root, text="Translation Settings", padx=10, pady=10)
        lang_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(lang_frame, text="Target Language:").grid(row=0, column=0, sticky="w", pady=5)
        
        self.language_var = tk.StringVar(value=DEFAULT_TARGET_LANGUAGE)
        languages = SUPPORTED_LANGUAGES
        
        self.lang_dropdown = ttk.Combobox(
            lang_frame,
            textvariable=self.language_var,
            values=[f"{name}" for name, code in languages],
            state="readonly",
            width=25
        )
        self.lang_dropdown.grid(row=0, column=1, pady=5, padx=5)
        self.lang_dropdown.current(0)
        self.lang_dropdown.bind("<<ComboboxSelected>>", self.on_language_change)
        
        # Store language codes mapping
        self.lang_codes = {name: code for name, code in languages}
        self.code_to_name = {code: name for name, code in languages}
        
        # Statistics
        stats_frame = tk.LabelFrame(self.root, text="Statistics", padx=10, pady=10)
        stats_frame.pack(fill="x", padx=10, pady=5)
        
        self.translations_count = 0
        self.stats_label = tk.Label(
            stats_frame,
            text=f"Translations: {self.translations_count}",
            font=("Arial", 10)
        )
        self.stats_label.pack()
        
        # Instructions
        info_frame = tk.LabelFrame(self.root, text="كيفية الاستخدام / How to Use", padx=10, pady=10)
        info_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        instructions = """
1. اضغط 'Start Monitoring' للبدء
2. انسخ أي نص (Ctrl+C)
3. ستظهر نافذة الترجمة تلقائياً
4. غيّر اللغة المستهدفة في أي وقت
5. اضغط 'Stop Monitoring' للإيقاف

✅ يترجم من أي لغة إلى اللغة المختارة
✅ يتخطى النص إذا كان بنفس اللغة المستهدفة
        """
        
        info_label = tk.Label(
            info_frame,
            text=instructions,
            justify="right",
            font=("Arial", 9)
        )
        info_label.pack()
        
    def get_language_name(self, code: str) -> str:
        """Get language name from code"""
        return self.code_to_name.get(code, code.upper())
    
    def on_language_change(self, event=None):
        """Handle language selection change"""
        selected = self.lang_dropdown.get()
        self.target_language = self.lang_codes.get(selected, "ar")
        
    def start_monitoring(self):
        """Start clipboard monitoring"""
        self.is_running = True
        self.status_label.config(text="🟢 Running", fg="green")
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        
        # Start monitoring thread
        self.monitor_thread = threading.Thread(target=self.monitor_clipboard, daemon=True)
        self.monitor_thread.start()
        
    def stop_monitoring(self):
        """Stop clipboard monitoring"""
        self.is_running = False
        self.status_label.config(text="⚫ Stopped", fg="red")
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        
    def monitor_clipboard(self):
        """Monitor clipboard for changes with improved Ctrl+C detection"""
        consecutive_same = 0
        max_consecutive = 3
        
        while self.is_running:
            try:
                # Multiple attempts to catch clipboard changes
                # This significantly improves Ctrl+C detection
                attempts = 0
                current_clipboard = None
                
                while attempts < 3 and self.is_running:
                    try:
                        clipboard_content = pyperclip.paste()
                        if clipboard_content:
                            current_clipboard = clipboard_content
                            break
                    except:
                        pass
                    attempts += 1
                    time.sleep(0.02)  # Very short delay between attempts
                
                # Check if clipboard has changed and is not empty
                if current_clipboard and current_clipboard != self.last_clipboard:
                    # Verify it's real content (not empty or whitespace only)
                    if len(current_clipboard.strip()) > 0:
                        # Reset consecutive counter
                        consecutive_same = 0
                        
                        # Update last clipboard
                        self.last_clipboard = current_clipboard
                        
                        print(f"📋 Clipboard changed! Length: {len(current_clipboard)}")
                        
                        # Process the copied text
                        if self.should_translate(current_clipboard):
                            self.translate_and_show(current_clipboard)
                        else:
                            print(f"⏭️ Skipped: Not suitable for translation")
                else:
                    consecutive_same += 1
                    # Clear last_clipboard if same content repeated too many times
                    # This helps catch re-copying the same text
                    if consecutive_same > max_consecutive:
                        consecutive_same = 0
                        
            except Exception as e:
                print(f"Clipboard monitoring error: {e}")
                
            # Shorter sleep for better responsiveness
            time.sleep(self.check_interval)
            
    def should_translate(self, text: str) -> bool:
        """Determine if text should be translated"""
        # Skip very short text
        if len(text.strip()) < MIN_TEXT_LENGTH:
            return False
            
        # Skip if text is only URLs
        url_pattern = r'^https?://[^\s]+$'
        if re.match(url_pattern, text.strip()):
            return False
            
        # Skip if text looks like code (contains common code patterns)
        for pattern in CODE_PATTERNS:
            if re.search(pattern, text, re.MULTILINE):
                return False
                
        return True
        
    def clean_text_for_translation(self, text: str) -> Tuple[str, List[str]]:
        """Clean text and extract URLs/code to preserve them"""
        # Extract URLs
        url_pattern = r'https?://[^\s]+'
        urls = re.findall(url_pattern, text)
        
        # Replace URLs with placeholders
        cleaned_text = text
        for i, url in enumerate(urls):
            cleaned_text = cleaned_text.replace(url, f"__URL_{i}__")
            
        return cleaned_text, urls
        
    def restore_urls(self, text: str, urls: List[str]) -> str:
        """Restore URLs in translated text"""
        restored_text = text
        for i, url in enumerate(urls):
            restored_text = restored_text.replace(f"__URL_{i}__", url)
        return restored_text
        
    def detect_language(self, text: str) -> Optional[str]:
        """Detect the language of the text"""
        try:
            payload = {"q": text}
            response = requests.post(self.detect_url, json=payload, timeout=5)
            
            if response.status_code == 200:
                result = response.json()
                if result and len(result) > 0:
                    return result[0].get("language", "unknown")
            return "unknown"
        except:
            return "unknown"
    
    def translate_with_mymemory(self, text: str, source_lang: str, target_lang: str) -> Optional[dict]:
        """Translate using MyMemory API as fallback"""
        try:
            # MyMemory uses different language codes
            lang_pair = f"{source_lang}|{target_lang}"
            
            params = {
                "q": text,
                "langpair": lang_pair
            }
            
            response = requests.get(FALLBACK_API_URL, params=params, timeout=10)
            print(f"MyMemory response status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                if result.get("responseStatus") == 200:
                    translated = result.get("responseData", {}).get("translatedText", "")
                    return {
                        "original": text,
                        "translated": translated,
                        "detected_language": source_lang,
                        "source_lang_name": self.get_language_name(source_lang),
                        "target_lang_name": self.get_language_name(target_lang)
                    }
            return None
        except Exception as e:
            print(f"MyMemory API error: {e}")
            return None
    
    def translate_text(self, text: str) -> Optional[dict]:
        """Translate text using LibreTranslate API"""
        try:
            # Clean text and preserve URLs
            cleaned_text, urls = self.clean_text_for_translation(text)
            
            # Detect source language first
            detected_lang = self.detect_language(cleaned_text)
            print(f"Detected language: {detected_lang}")
            
            # Skip translation if text is already in target language
            if detected_lang == self.target_language:
                return {
                    "error": f"النص بالفعل باللغة المستهدفة ({self.get_language_name(detected_lang)})",
                    "skip": True
                }
            
            # Prepare request
            payload = {
                "q": cleaned_text,
                "source": detected_lang if detected_lang != "unknown" else "auto",
                "target": self.target_language,
                "format": "text"
            }
            
            # Make API request
            print(f"Sending request: {payload}")
            response = requests.post(self.api_url, json=payload, timeout=10)
            print(f"Response status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                translated = result.get("translatedText", "")
                
                # Restore URLs
                translated = self.restore_urls(translated, urls)
                
                return {
                    "original": text,
                    "translated": translated,
                    "detected_language": detected_lang,
                    "source_lang_name": self.get_language_name(detected_lang),
                    "target_lang_name": self.get_language_name(self.target_language)
                }
            else:
                error_msg = f"فشل الترجمة: {response.status_code}"
                try:
                    error_detail = response.json()
                    print(f"Error detail: {error_detail}")
                    if "error" in error_detail:
                        error_msg = f"خطأ: {error_detail['error']}"
                except Exception as e:
                    print(f"Could not parse error: {e}")
                    pass
                
                # If rate limited, provide helpful message
                if response.status_code == 429:
                    error_msg = "تم تجاوز حد الاستخدام. انتظر قليلاً وحاول مرة أخرى.\nRate limit exceeded. Wait a moment and try again."
                elif response.status_code == 403:
                    error_msg = "الوصول مرفوض. قد يكون الخادم مشغولاً.\nAccess denied. Server may be busy."
                elif response.status_code >= 500:
                    error_msg = "خطأ في الخادم. حاول مرة أخرى لاحقاً.\nServer error. Try again later."
                
                # Try fallback API if enabled
                if USE_FALLBACK_API:
                    print("Trying fallback API (MyMemory)...")
                    fallback_result = self.translate_with_mymemory(
                        cleaned_text, 
                        detected_lang if detected_lang != "unknown" else "en",
                        self.target_language
                    )
                    if fallback_result:
                        # Restore URLs in fallback result
                        fallback_result["translated"] = self.restore_urls(fallback_result["translated"], urls)
                        fallback_result["original"] = text
                        return fallback_result
                    
                return {"error": error_msg}
                
        except requests.exceptions.Timeout:
            # Try fallback on timeout
            if USE_FALLBACK_API:
                try:
                    cleaned_text, urls = self.clean_text_for_translation(text)
                    detected_lang = self.detect_language(cleaned_text)
                    fallback_result = self.translate_with_mymemory(
                        cleaned_text,
                        detected_lang if detected_lang != "unknown" else "en",
                        self.target_language
                    )
                    if fallback_result:
                        fallback_result["translated"] = self.restore_urls(fallback_result["translated"], urls)
                        fallback_result["original"] = text
                        return fallback_result
                except:
                    pass
            return {"error": "انتهت مهلة الترجمة. حاول مرة أخرى.\nTranslation timeout. Try again."}
            
        except requests.exceptions.ConnectionError:
            # Try fallback on connection error
            if USE_FALLBACK_API:
                try:
                    cleaned_text, urls = self.clean_text_for_translation(text)
                    detected_lang = self.detect_language(cleaned_text)
                    fallback_result = self.translate_with_mymemory(
                        cleaned_text,
                        detected_lang if detected_lang != "unknown" else "en",
                        self.target_language
                    )
                    if fallback_result:
                        fallback_result["translated"] = self.restore_urls(fallback_result["translated"], urls)
                        fallback_result["original"] = text
                        return fallback_result
                except:
                    pass
            return {"error": "خطأ في الاتصال. تحقق من اتصال الإنترنت.\nConnection error. Check internet."}
            
        except Exception as e:
            print(f"Unexpected error: {e}")
            return {"error": f"خطأ في الترجمة: {str(e)}"}
            
    def get_alternative_translations(self, text: str) -> List[str]:
        """Get alternative translations for short phrases"""
        # For short text, we could provide context-based alternatives
        # Since LibreTranslate doesn't provide alternatives, we'll return the main translation
        # In a production app, you could use multiple translation services
        alternatives = []
        
        # You can add logic here to provide alternatives based on context
        # For now, we'll just return an empty list
        
        return alternatives
        
    def translate_and_show(self, text: str):
        """Translate text and show popup"""
        # Translate
        result = self.translate_text(text)
        
        if result:
            # Update statistics
            self.translations_count += 1
            self.stats_label.config(text=f"Translations: {self.translations_count}")
            
            # Show popup
            self.root.after(0, lambda: self.show_popup(result))
            
    def show_popup(self, result: dict):
        """Show translation popup window"""
        # Close existing popup if any
        if self.popup and self.popup.winfo_exists():
            self.popup.destroy()
            
        # Create popup window
        self.popup = tk.Toplevel(self.root)
        self.popup.title("الترجمة / Translation")
        self.popup.geometry(f"{POPUP_WINDOW_WIDTH}x{POPUP_WINDOW_HEIGHT}")
        self.popup.attributes('-topmost', True)
        
        # Position popup in top-right corner
        screen_width = self.popup.winfo_screenwidth()
        self.popup.geometry(f"+{screen_width - POPUP_WINDOW_WIDTH - 20}+50")
        
        # Check for errors
        if "error" in result:
            # Check if it's a "skip" error (same language)
            if result.get("skip"):
                error_label = tk.Label(
                    self.popup,
                    text=f"ℹ️ {result['error']}",
                    font=("Arial", 11),
                    fg="#FF9800",
                    wraplength=450,
                    pady=20
                )
            else:
                error_label = tk.Label(
                    self.popup,
                    text=f"❌ {result['error']}",
                    font=("Arial", 10),
                    fg="red",
                    wraplength=450,
                    pady=20
                )
            error_label.pack()
            
            close_btn = tk.Button(
                self.popup,
                text="إغلاق / Close",
                command=self.popup.destroy,
                bg="#f44336",
                fg="white",
                padx=20,
                pady=5
            )
            close_btn.pack(pady=10)
            
            # Auto-close after configured time for skip messages
            if result.get("skip"):
                self.popup.after(SKIP_MESSAGE_AUTO_CLOSE_TIME, lambda: self.popup.destroy() if self.popup.winfo_exists() else None)
            return
            
        # Language info header
        source_lang = result.get("source_lang_name", "Unknown")
        target_lang = result.get("target_lang_name", "Arabic")
        
        info_label = tk.Label(
            self.popup,
            text=f"🔄 {source_lang} ➜ {target_lang}",
            font=("Arial", 11, "bold"),
            fg="#1976D2",
            pady=5
        )
        info_label.pack()
        
        # Original text section
        original_frame = tk.LabelFrame(
            self.popup, 
            text=f"📝 النص الأصلي ({source_lang})", 
            padx=10, 
            pady=10,
            font=("Arial", 9, "bold")
        )
        original_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        original_text = tk.Text(
            original_frame,
            height=6,
            wrap="word",
            font=("Arial", 10),
            bg="#f5f5f5"
        )
        original_text.pack(fill="both", expand=True)
        original_text.insert("1.0", result["original"])
        original_text.config(state="disabled")
        
        # Translated text section
        translated_frame = tk.LabelFrame(
            self.popup, 
            text=f"✅ الترجمة ({target_lang})", 
            padx=10, 
            pady=10,
            font=("Arial", 9, "bold")
        )
        translated_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        translated_text = tk.Text(
            translated_frame,
            height=6,
            wrap="word",
            font=("Arial", 12, "bold"),
            bg="#e8f5e9",
            fg="#1B5E20"
        )
        translated_text.pack(fill="both", expand=True)
        translated_text.insert("1.0", result["translated"])
        translated_text.config(state="disabled")
        
        # Buttons
        button_frame = tk.Frame(self.popup)
        button_frame.pack(pady=10)
        
        copy_btn = tk.Button(
            button_frame,
            text="📋 نسخ الترجمة / Copy",
            command=lambda: self.copy_translation(result["translated"]),
            bg="#2196F3",
            fg="white",
            font=("Arial", 9, "bold"),
            padx=15,
            pady=5
        )
        copy_btn.grid(row=0, column=0, padx=5)
        
        close_btn = tk.Button(
            button_frame,
            text="✖ إغلاق / Close",
            command=self.popup.destroy,
            bg="#9E9E9E",
            fg="white",
            font=("Arial", 9, "bold"),
            padx=15,
            pady=5
        )
        close_btn.grid(row=0, column=1, padx=5)
        
        # Auto-close after configured time
        self.popup.after(POPUP_AUTO_CLOSE_TIME, lambda: self.popup.destroy() if self.popup.winfo_exists() else None)
        
    def copy_translation(self, text: str):
        """Copy translation to clipboard"""
        # Temporarily stop monitoring to avoid re-triggering
        was_running = self.is_running
        if was_running:
            self.is_running = False
            
        pyperclip.copy(text)
        
        # Show confirmation
        if self.popup and self.popup.winfo_exists():
            messagebox.showinfo("تم النسخ / Copied", "تم نسخ الترجمة!\nTranslation copied to clipboard!", parent=self.popup)
            
        # Resume monitoring after a short delay
        if was_running:
            time.sleep(1)
            self.is_running = True
            
    def on_closing(self):
        """Handle window closing"""
        self.is_running = False
        self.root.quit()
        self.root.destroy()
        
    def run(self):
        """Run the application"""
        self.root.mainloop()


def main():
    """Main entry point"""
    print("Starting Instant Translator...")
    print("LibreTranslate API: https://libretranslate.com")
    
    app = TranslatorApp()
    app.run()


if __name__ == "__main__":
    main()
