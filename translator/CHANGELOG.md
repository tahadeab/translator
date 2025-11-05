# 📋 Changelog / سجل التغييرات

## Version 2.0.0 - Enhanced Translation Logic (2025-11-05)

### ✨ New Features / ميزات جديدة

#### Smart Language Detection / كشف اللغة الذكي
- ✅ Automatic source language detection using LibreTranslate API
- ✅ كشف تلقائي للغة المصدر باستخدام API من LibreTranslate

#### Intelligent Translation / ترجمة ذكية
- ✅ Translates ANY language (except target) to selected target language
- ✅ يترجم أي لغة (ماعدا المستهدفة) إلى اللغة المختارة
- ✅ Skips translation if text is already in target language
- ✅ يتخطى الترجمة إذا كان النص بالفعل باللغة المستهدفة

#### Enhanced UI / واجهة محسّنة
- ✅ Shows source and target languages clearly in popup
- ✅ يعرض لغة المصدر واللغة المستهدفة بوضوح في النافذة المنبثقة
- ✅ Bilingual interface (Arabic + English)
- ✅ واجهة ثنائية اللغة (عربي + إنجليزي)
- ✅ Better visual design with language indicators
- ✅ تصميم بصري أفضل مع مؤشرات اللغة

#### Configuration System / نظام التكوين
- ✅ New `config.py` file for easy customization
- ✅ ملف `config.py` جديد للتخصيص السهل
- ✅ Customizable popup durations, window sizes, and more
- ✅ مدد النوافذ المنبثقة وأحجام النوافذ قابلة للتخصيص

#### Quick Start Tools / أدوات البدء السريع
- ✅ `run_translator.bat` - Quick launch script
- ✅ `install_dependencies.bat` - Easy dependency installation
- ✅ `test_translator.py` - API testing tool
- ✅ `QUICK_START.md` - Quick start guide

#### Documentation / التوثيق
- ✅ Comprehensive English documentation (`README.md`)
- ✅ توثيق شامل بالإنجليزية
- ✅ Complete Arabic documentation (`README_AR.md`)
- ✅ توثيق كامل بالعربية
- ✅ Quick start guide in both languages
- ✅ دليل البدء السريع بكلا اللغتين

### 🔧 Improvements / التحسينات

#### Performance / الأداء
- ⚡ Faster language detection
- ⚡ كشف أسرع للغة
- ⚡ Optimized clipboard monitoring
- ⚡ مراقبة محسّنة للحافظة

#### User Experience / تجربة المستخدم
- 🎨 Better error messages in Arabic
- 🎨 رسائل خطأ أفضل بالعربية
- 🎨 Auto-close for skip messages (5 seconds)
- 🎨 إغلاق تلقائي لرسائل التخطي (5 ثوانٍ)
- 🎨 Improved button labels (bilingual)
- 🎨 تسميات أزرار محسّنة (ثنائية اللغة)

#### Code Quality / جودة الكود
- 🔨 Modular configuration system
- 🔨 نظام تكوين معياري
- 🔨 Better error handling
- 🔨 معالجة أفضل للأخطاء
- 🔨 Cleaner code structure
- 🔨 هيكل كود أنظف

### 🐛 Bug Fixes / إصلاح الأخطاء

- ✅ Fixed: Translation not working for non-English languages
- ✅ تم الإصلاح: الترجمة لا تعمل للغات غير الإنجليزية
- ✅ Fixed: Popup not showing language information
- ✅ تم الإصلاح: النافذة المنبثقة لا تعرض معلومات اللغة
- ✅ Fixed: Translation appearing for same language text
- ✅ تم الإصلاح: ظهور الترجمة لنص بنفس اللغة

### 📦 New Files / ملفات جديدة

```
config.py                  - Configuration settings
test_translator.py         - API testing tool
run_translator.bat         - Quick launch script
install_dependencies.bat   - Dependency installer
README_AR.md              - Arabic documentation
QUICK_START.md            - Quick start guide
CHANGELOG.md              - This file
```

---

## Version 1.0.0 - Initial Release (2025-11-05)

### ✨ Initial Features / الميزات الأولية

- ✅ Automatic clipboard monitoring
- ✅ مراقبة تلقائية للحافظة
- ✅ Translation to Arabic by default
- ✅ الترجمة إلى العربية افتراضياً
- ✅ Multi-language support (10+ languages)
- ✅ دعم متعدد اللغات (أكثر من 10 لغات)
- ✅ Smart text detection (skip URLs and code)
- ✅ كشف ذكي للنص (تخطي الروابط والكود)
- ✅ Popup display with translations
- ✅ عرض منبثق مع الترجمات
- ✅ Free LibreTranslate API integration
- ✅ تكامل مع API مجاني من LibreTranslate
- ✅ Copy translation feature
- ✅ ميزة نسخ الترجمة
- ✅ Statistics tracking
- ✅ تتبع الإحصائيات

---

## 🔮 Future Plans / الخطط المستقبلية

### Planned Features / ميزات مخططة

- 🔄 Translation history
- 🔄 سجل الترجمات
- 🔄 Favorite translations
- 🔄 الترجمات المفضلة
- 🔄 Keyboard shortcuts customization
- 🔄 تخصيص اختصارات لوحة المفاتيح
- 🔄 System tray icon
- 🔄 أيقونة في شريط المهام
- 🔄 Multiple translation services support
- 🔄 دعم خدمات ترجمة متعددة
- 🔄 Offline translation mode
- 🔄 وضع الترجمة دون اتصال
- 🔄 Voice pronunciation
- 🔄 النطق الصوتي

---

## 📝 Notes / ملاحظات

### Breaking Changes / تغييرات جذرية
- Version 2.0.0 introduces `config.py` - old settings in `translator.py` are now deprecated
- الإصدار 2.0.0 يقدم `config.py` - الإعدادات القديمة في `translator.py` أصبحت قديمة

### Migration Guide / دليل الترحيل
If upgrading from v1.0.0:
1. Keep your `translator.py` settings
2. Copy them to the new `config.py` file
3. Delete old settings from `translator.py`

إذا كنت تقوم بالترقية من v1.0.0:
1. احتفظ بإعداداتك في `translator.py`
2. انسخها إلى ملف `config.py` الجديد
3. احذف الإعدادات القديمة من `translator.py`

---

**Thank you for using Instant Multilingual Translator! / شكراً لاستخدام المترجم الفوري متعدد اللغات!** 🎉
