# 🚀 دليل البدء السريع / Quick Start Guide

## العربية

### التثبيت (مرة واحدة فقط)
1. انقر نقراً مزدوجاً على `install_dependencies.bat`
2. انتظر حتى يكتمل التثبيت

### التشغيل
1. انقر نقراً مزدوجاً على `run_translator.bat`
2. انقر على زر "▶ Start Monitoring"
3. انسخ أي نص (Ctrl+C)
4. ستظهر الترجمة تلقائياً!

### الميزات الرئيسية
✅ يترجم من **أي لغة** إلى **اللغة المختارة**  
✅ يتخطى الترجمة إذا كان النص **بنفس اللغة المستهدفة**  
✅ يعرض **لغة المصدر** و **اللغة المستهدفة** بوضوح  
✅ **نافذة منبثقة فورية** مع الترجمة  
✅ **نسخ الترجمة** بنقرة واحدة  

### تغيير اللغة المستهدفة
- اختر من القائمة المنسدلة "Target Language"
- اللغة الافتراضية: العربية

### التخصيص
- افتح `config.py` لتعديل الإعدادات
- يمكنك تغيير: اللغة الافتراضية، مدة النافذة، حجم النوافذ، وأكثر

---

## English

### Installation (One Time Only)
1. Double-click `install_dependencies.bat`
2. Wait for installation to complete

### Running
1. Double-click `run_translator.bat`
2. Click "▶ Start Monitoring" button
3. Copy any text (Ctrl+C)
4. Translation appears automatically!

### Key Features
✅ Translates from **ANY language** to **selected target language**  
✅ Skips translation if text is **already in target language**  
✅ Shows **source language** and **target language** clearly  
✅ **Instant popup** with translation  
✅ **Copy translation** with one click  

### Change Target Language
- Select from "Target Language" dropdown
- Default language: Arabic

### Customization
- Open `config.py` to modify settings
- You can change: default language, popup duration, window sizes, and more

---

## 📝 Examples / أمثلة

### Example 1: English → Arabic
**Copy:** "Hello, how are you?"  
**Result:** "مرحبا، كيف حالك؟"

### Example 2: Spanish → Arabic
**Copy:** "Hola, ¿cómo estás?"  
**Result:** "مرحبا، كيف حالك؟"

### Example 3: French → Arabic
**Copy:** "Bonjour, comment allez-vous?"  
**Result:** "مرحبا، كيف حالك؟"

### Example 4: Arabic → English (change target to English)
**Copy:** "مرحبا، كيف حالك؟"  
**Result:** "Hello, how are you?"

---

## 🔧 Troubleshooting / استكشاف الأخطاء

### Problem: Translation not appearing / المشكلة: الترجمة لا تظهر
**Solution / الحل:**
- Make sure "Start Monitoring" is clicked / تأكد من النقر على "Start Monitoring"
- Check internet connection / تحقق من اتصال الإنترنت
- Text must be at least 2 characters / يجب أن يكون النص حرفين على الأقل

### Problem: Same language message / المشكلة: رسالة نفس اللغة
**Solution / الحل:**
- This is normal! The app detected the text is already in the target language
- هذا طبيعي! اكتشف التطبيق أن النص بالفعل باللغة المستهدفة

### Problem: Module not found / المشكلة: Module not found
**Solution / الحل:**
```bash
pip install -r requirements.txt
```

---

## 📚 More Information / مزيد من المعلومات

- **English Documentation:** `README.md`
- **Arabic Documentation:** `README_AR.md`
- **Test API:** Run `python test_translator.py`

---

**Enjoy! / استمتع!** 🎉
