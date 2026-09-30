<div dir="rtl" align="right">

## جلسه دهم: توسعه امن نرم‌افزار (Secure Development)

# مقدمه

تبریک!

اکنون به آخرین جلسه از فصل امنیت سایبری رسیده‌ایم.

تا اینجا با موضوعات مهمی آشنا شدیم:

<p dir='rtl'>
• امنیت سایبری چیست <br>
• مهاجمان چه کسانی هستند <br>
• آسیب‌پذیری چیست <br>
• چرخه امنیت <br>
• مدل‌سازی تهدید <br>
• احراز هویت و مجوزدهی <br>
• حملات Injection <br>
• اعتبارسنجی ورودی‌ها <br>
• Logging و Monitoring <br>
• Defense in Depth
</p>

اما هنوز یک سؤال مهم باقی مانده است:

> چگونه از همان روز اول برنامه‌ای بنویسیم که تا حد ممکن امن باشد؟

پاسخ این سؤال:

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Secure Development
</p>

است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Secure Development چیست؟
</p>

<p dir='rtl'>
Secure Development یعنی:
</p>

> توسعه نرم‌افزار با در نظر گرفتن امنیت از همان ابتدا

---

بسیاری از افراد ابتدا برنامه را می‌سازند و بعداً به فکر امنیت می‌افتند.

اما در دنیای واقعی این روش خطرناک است.

---

# دو روش مختلف

روش اشتباه:

```text
Build
↓
Deploy
↓
Security
```

---

روش حرفه‌ای:

```text
Design
↓
Build
↓
Security
↓
Test
↓
Deploy
```

---

در روش حرفه‌ای امنیت از همان ابتدا وجود دارد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Secure Coding چیست؟
</p>

<p dir='rtl'>
Secure Coding یعنی:
</p>

> نوشتن کد به شکلی که احتمال سوءاستفاده از آن کاهش پیدا کند.

---

مثال

کد ضعیف:

```python
ip = input()
```

استفاده مستقیم از ورودی

---

کد بهتر:

```python
ip = input()

validate_ip(ip)
```

---

این همان چیزی است که در Port Scanner انجام داده‌ایم.

---

# اصل اول

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Never Trust User Input
</p>

هرگز به ورودی کاربر اعتماد نکن.

---

مهم نیست:

<p dir='rtl'>
• کاربر عادی باشد <br>
• مدیر سیستم باشد <br>
• API باشد <br>
• فایل باشد
</p>

---

همه ورودی‌ها باید بررسی شوند.

---

# اصل دوم

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Least Privilege
</p>

قبلاً نیز با این مفهوم آشنا شدیم.

---

برنامه باید فقط دسترسی‌های موردنیاز را داشته باشد.

---

اشتباه:

```text
Administrator Everywhere
```

---

درست:

```text
Minimum Required Access
```

---

# اصل سوم

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Fail Securely
</p>

اگر خطایی رخ داد:

برنامه باید امن باقی بماند.

---

مثال بد:

```python
except:
    pass
```

---

خطا پنهان می‌شود.

---

مثال بهتر:

```python
except Exception as error:
    logger.error(error)
```

---

ثبت خطا

و ادامه کنترل‌شده برنامه

---

# اصل چهارم

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Keep It Simple
</p>

هرچه سیستم پیچیده‌تر شود:

احتمال خطا بیشتر می‌شود.

---

برنامه‌های ساده‌تر:

<p dir='rtl'>
• راحت‌تر تست می‌شوند <br>
• راحت‌تر نگهداری می‌شوند <br>
• امن‌تر هستند
</p>

---

# اصل پنجم

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Defense in Depth
</p>

قبلاً یاد گرفتیم.

---

هیچ‌وقت به یک لایه دفاعی اکتفا نکن.

---

مثال:

```text
Validation
+
Logging
+
Authentication
+
Monitoring
```

---

همگی با هم امنیت ایجاد می‌کنند.

---

# اصل ششم

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Secure Defaults
</p>

حالت پیش‌فرض باید امن باشد.

---

مثال:

اگر کاربر مقدار نامعتبر وارد کرد:

```text
Reject
```

---

نه اینکه:

```text
Guess
```

---

# اصل هفتم

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Keep Software Updated
</p>

بسیاری از حملات فقط به این دلیل موفق می‌شوند که:

سیستم به‌روزرسانی نشده است.

---

مثال:

```text
Python
Libraries
Frameworks
Operating System
```

---

باید مرتب به‌روز شوند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Dependency چیست؟
</p>

کتابخانه‌هایی که پروژه از آن‌ها استفاده می‌کند.

---

مثال:

```python
pytest
```

---

یک Dependency است.

---

اگر آسیب‌پذیری داشته باشد:

پروژه شما نیز آسیب‌پذیر خواهد شد.

---

# چرا باید Dependencyها را بررسی کنیم؟

گاهی هکرها:

کتابخانه‌های آلوده منتشر می‌کنند.

---

گاهی نیز:

کتابخانه قدیمی دارای آسیب‌پذیری است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Code Review چیست؟
</p>

بازبینی کد توسط فرد دیگر.

---

یکی از مهم‌ترین مراحل توسعه حرفه‌ای.

---

چرا؟

زیرا:

همه انسان‌ها اشتباه می‌کنند.

---

ممکن است توسعه‌دهنده متوجه یک مشکل امنیتی نشود.

اما نفر دوم آن را پیدا کند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Security Testing چیست؟
</p>

تست امنیتی

---

یعنی:

بررسی کنیم آیا برنامه در برابر حملات مقاوم است یا خیر.

---

مثال‌ها:

<p dir='rtl'>
• Input Validation <br>
• Authentication <br>
• Authorization <br>
• Error Handling
</p>

---

# چرا این همه Test نوشتیم؟

در پروژه Port Scanner:

بیش از 50 تست نوشتیم.

---

دلیل:

اطمینان از عملکرد صحیح برنامه.

---

هر بار که قابلیت جدید اضافه می‌کنیم:

تست‌ها بررسی می‌کنند چیزی خراب نشده باشد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Shift Left Security
</p>

یکی از مفاهیم مدرن امنیت.

---

معنی:

امنیت را به ابتدای فرآیند توسعه منتقل کن.

---

روش قدیمی:

```text
Develop
↓
Deploy
↓
Test Security
```

---

روش جدید:

```text
Design
↓
Security
↓
Development
↓
Testing
```

---

این باعث کاهش هزینه و افزایش کیفیت می‌شود.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Secure Development Lifecycle
</p>

چرخه توسعه امن معمولاً شامل:

---

طراحی

```text
Design
```

---

پیاده‌سازی

```text
Development
```

---

تست

```text
Testing
```

---

بازبینی

```text
Review
```

---

استقرار

```text
Deployment
```

---

نگهداری

```text
Maintenance
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Port Scanner ما چه چیزهایی را رعایت کرده است؟
</p>

---

اعتبارسنجی ورودی‌ها

```text
Validation
```

---

ثبت رویدادها

```text
Logging
```

---

تست واحد

```text
Unit Testing
```

---

ساختار ماژولار

```text
Modular Design
```

---

مدیریت خطاها

```text
Exception Handling
```

---

خروجی‌های استاندارد

```text
JSON
CSV
```

---

تمام این موارد در پروژه‌های واقعی استفاده می‌شوند.

---

# آیا پروژه ما امن است؟

هیچ نرم‌افزاری 100٪ امن نیست.

---

اما پروژه ما نسبت به نسخه ابتدایی:

<p dir='rtl'>
• پایدارتر <br>
• قابل نگهداری‌تر <br>
• تست‌پذیرتر <br>
• امن‌تر
</p>

شده است.

---

# مهم‌ترین درس فصل امنیت

اگر فقط یک جمله از کل این فصل را به خاطر بسپارید:

> امنیت یک محصول نیست؛ یک فرآیند دائمی است.

---

هیچ روزی وجود ندارد که بتوان گفت:

```text
اکنون برای همیشه امن هستیم.
```

---

امنیت همیشه نیازمند:

<p dir='rtl'>
• یادگیری <br>
• بررسی <br>
• تست <br>
• بهبود
</p>

است.

---

# جمع‌بندی فصل امنیت سایبری

در این فصل یاد گرفتیم:

<p dir='rtl'>
• مفاهیم پایه امنیت <br>
• مهاجمان چگونه فکر می‌کنند <br>
• آسیب‌پذیری چیست <br>
• چرخه امنیت چگونه کار می‌کند <br>
• Threat Modeling چیست <br>
• Authentication و Authorization چیست <br>
• حملات Injection چگونه انجام می‌شوند <br>
• اعتبارسنجی ورودی‌ها چیست <br>
• Logging و Monitoring چیست <br>
• Defense in Depth چیست <br>
• Secure Development چیست
</p>

---

# در فصل بعد چه یاد می‌گیریم؟

اکنون تمام پیش‌نیازهای لازم را داریم.

ما:

<p dir='rtl'>
• پایتون را یاد گرفتیم <br>
• شبکه را یاد گرفتیم <br>
• امنیت را یاد گرفتیم
</p>

و حالا آماده‌ایم وارد مهم‌ترین بخش کل دوره شویم:

# فصل چهارم: Port Scanner

در این فصل پروژه‌ای که ساخته‌ایم را

**فایل به فایل**
و
**خط به خط**

بررسی خواهیم کرد.

یاد می‌گیریم:

<p dir='rtl'>
• هر فایل چرا ساخته شده است <br>
• هر تابع چه کاری انجام می‌دهد <br>
• هر خط کد چه نقشی دارد <br>
• معماری پروژه چگونه طراحی شده است <br>
• چگونه می‌توان پروژه را توسعه داد
</p>

از جلسه بعد وارد بررسی واقعی کدهای پروژه خواهیم شد.

</div>