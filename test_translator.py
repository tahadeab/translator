"""
Quick test script for the translator API
"""

import requests

def test_detect_language(text):
    """Test language detection"""
    try:
        url = "https://libretranslate.com/detect"
        payload = {"q": text}
        response = requests.post(url, json=payload, timeout=5)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Detected language: {result}")
            return result[0].get("language") if result else "unknown"
        else:
            print(f"❌ Detection failed: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def test_translate(text, source_lang, target_lang):
    """Test translation"""
    try:
        url = "https://libretranslate.com/translate"
        payload = {
            "q": text,
            "source": source_lang,
            "target": target_lang,
            "format": "text"
        }
        response = requests.post(url, json=payload, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            translated = result.get("translatedText", "")
            print(f"✅ Translation: {translated}")
            return translated
        else:
            print(f"❌ Translation failed: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    print("=" * 50)
    print("Testing LibreTranslate API")
    print("=" * 50)
    
    # Test 1: English to Arabic
    print("\n📝 Test 1: English to Arabic")
    text1 = "Hello, how are you?"
    detected = test_detect_language(text1)
    if detected:
        test_translate(text1, detected, "ar")
    
    # Test 2: Arabic to English
    print("\n📝 Test 2: Arabic to English")
    text2 = "مرحبا، كيف حالك؟"
    detected = test_detect_language(text2)
    if detected:
        test_translate(text2, detected, "en")
    
    # Test 3: Spanish to Arabic
    print("\n📝 Test 3: Spanish to Arabic")
    text3 = "Hola, ¿cómo estás?"
    detected = test_detect_language(text3)
    if detected:
        test_translate(text3, detected, "ar")
    
    # Test 4: French to Arabic
    print("\n📝 Test 4: French to Arabic")
    text4 = "Bonjour, comment allez-vous?"
    detected = test_detect_language(text4)
    if detected:
        test_translate(text4, detected, "ar")
    
    print("\n" + "=" * 50)
    print("✅ Testing complete!")
    print("=" * 50)
