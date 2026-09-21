<div dir="rtl" align="right">

## جلسه هشتم: لاگ‌برداری (Logging) و مانیتورینگ (Monitoring)

# مقدمه

تا اینجای مسیر یادگیری با موضوعات مهم امنیت آشنا شدیم:

<p dir='rtl'>
• امنیت سایبری چیست <br>
• مهاجمان چه کسانی هستند <br>
• آسیب‌پذیری چیست <br>
• چرخه امنیت <br>
• مدل‌سازی تهدید <br>
• احراز هویت و مجوزدهی <br>
• حملات Injection <br>
• اعتبارسنجی ورودی‌ها
</p>

اما یک سؤال مهم وجود دارد:

> اگر حمله‌ای اتفاق بیفتد، از کجا متوجه شویم؟

یا حتی مهم‌تر:

> بعد از وقوع حمله چگونه بفهمیم چه اتفاقی افتاده است؟

اینجاست که Logging و Monitoring وارد میدان می‌شوند.

---

# فرض کنید...

یک روز صبح وارد شرکت می‌شوید.

مدیر سیستم می‌گوید:

> دیشب سرور هک شده است.

اولین سؤال شما چیست؟

احتمالاً:

> دقیقاً چه اتفاقی افتاده؟

اما اگر هیچ اطلاعاتی ثبت نشده باشد:

هیچ‌کس پاسخ این سؤال را نمی‌داند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Logging چیست؟
</p>

<p dir='rtl'>
Logging یعنی:
</p>

> ثبت رویدادها و اتفاقات سیستم

---

به زبان ساده:

نوشتن تاریخچه اتفاقات.

---

# مثال دنیای واقعی

دوربین مداربسته را تصور کنید.

دوربین:

اتفاقات را ضبط می‌کند.

---

<p dir='rtl'>
Log نیز همین کار را انجام می‌دهد.
</p>

اما برای نرم‌افزارها و سیستم‌ها.

---

# مثال ساده

کاربر وارد سیستم می‌شود.

ثبت می‌کنیم:

```text
2025-01-01 10:00:00
User admin logged in
```

---

کاربر خارج می‌شود:

```text
2025-01-01 10:30:00
User admin logged out
```

---

این اطلاعات بعدها بسیار ارزشمند خواهند بود.

---

# چرا Logging مهم است؟

چند دلیل اصلی:

---

## 1. پیدا کردن خطاها

مثال:

برنامه کرش کرده است.

اگر Log داشته باشیم:

می‌توانیم علت را پیدا کنیم.

---

## 2. پیدا کردن حملات

مثال:

هزاران Login ناموفق ثبت شده‌اند.

ممکن است حمله Brute Force باشد.

---

## 3. تحلیل رخدادها

مثال:

هکر وارد سیستم شده است.

<p dir='rtl'>
Logها نشان می‌دهند:
</p>

<p dir='rtl'>
• از کجا آمده <br>
• چه زمانی آمده <br>
• چه کاری انجام داده
</p>

---

## 4. پاسخگویی قانونی

در بسیاری از سازمان‌ها:

ثبت رویدادها الزامی است.

---

# مثال از لاگ واقعی

```text
2025-01-01 12:30:00
INFO User login success
```

---

```text
2025-01-01 12:31:00
WARNING Invalid password
```

---

```text
2025-01-01 12:32:00
ERROR Database connection failed
```

---

# سطح‌های مختلف Log

معمولاً لاگ‌ها چند سطح دارند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
DEBUG
</p>

جزئیات بسیار زیاد

برای توسعه‌دهندگان

---

مثال:

```text
DEBUG Connecting to database
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
INFO
</p>

اطلاعات عادی

---

مثال:

```text
INFO User logged in
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
WARNING
</p>

اتفاق غیرعادی

اما نه بحرانی

---

مثال:

```text
WARNING Invalid login attempt
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
ERROR
</p>

خطای مهم

---

مثال:

```text
ERROR Database unavailable
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
CRITICAL
</p>

خطای بحرانی

---

مثال:

```text
CRITICAL Server compromised
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Logging در پروژه Port Scanner
</p>

ما قبلاً قابلیت Logging را پیاده‌سازی کردیم.

---

نمونه:

```text
scan.log
```

---

وقتی اسکن انجام می‌شود:

می‌توانیم اطلاعاتی مثل:

<p dir='rtl'>
• زمان اسکن <br>
• هدف اسکن <br>
• نتیجه اسکن
</p>

را ثبت کنیم.

---

# چرا این قابلیت مهم است؟

اگر بعداً بخواهیم بفهمیم:

چه زمانی چه چیزی اسکن شده است

می‌توانیم به Logها مراجعه کنیم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Monitoring چیست؟
</p>

<p dir='rtl'>
Monitoring یعنی:
</p>

> مشاهده و بررسی مداوم وضعیت سیستم

---

<p dir='rtl'>
Logging:
</p>

ثبت اتفاقات

---

<p dir='rtl'>
Monitoring:
</p>

بررسی دائمی اتفاقات

---

# مثال

فرض کنید دمای موتور خودرو ثبت می‌شود.

این می‌شود:

<p dir='rtl'>
Logging
</p>

---

اگر دائماً دما بررسی شود و هشدار داده شود:

این می‌شود:

<p dir='rtl'>
Monitoring
</p>

---

# تفاوت Logging و Monitoring

<p dir='rtl'>
Logging:
</p>

```text
Record Events
```

---

<p dir='rtl'>
Monitoring:
</p>

```text
Watch Events
```

---

# مثال در شبکه

ثبت اتصال‌ها:

```text
Logging
```

---

هشدار هنگام حمله:

```text
Monitoring
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Alert چیست؟
</p>

<p dir='rtl'>
Alert یعنی:
</p>

> هشدار امنیتی

---

مثال:

اگر بیشتر از 1000 =>Login ناموفق ثبت شد:

هشدار ارسال شود.

---

# نمونه Alert

```text
High Failed Login Attempts
```

---

یا:

```text
Possible Brute Force Attack
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
SIEM چیست؟
</p>

یکی از مهم‌ترین مفاهیم امنیت.

---

مخفف:

```text
Security Information and Event Management
```

---

سیستمی که:

<p dir='rtl'>
• Logها را جمع‌آوری می‌کند <br>
• آن‌ها را تحلیل می‌کند <br>
• هشدار تولید می‌کند
</p>

---

# مثال‌های معروف SIEM

<p dir='rtl'>
• Splunk <br>
• QRadar <br>
• ArcSight <br>
• Elastic SIEM
</p>

---

# چگونه SIEM کار می‌کند؟

صدها سرور Log تولید می‌کنند.

↓

<p dir='rtl'>
SIEM همه را جمع می‌کند.
</p>

↓

الگوها را بررسی می‌کند.

↓

حملات را شناسایی می‌کند.

↓

هشدار می‌دهد.

---

# مثال واقعی

اگر مشاهده شود:

```text
500 Login Failed
```

در یک دقیقه

ممکن است:

```text
Brute Force Attack
```

تشخیص داده شود.

---

# چرا مهاجمان Logها را حذف می‌کنند؟

زیرا Logها مدرک هستند.

---

پس از نفوذ:

بعضی مهاجمان تلاش می‌کنند:

```text
Delete Logs
```

---

تا ردپای خود را پاک کنند.

---

# بهترین راهکار

ثبت لاگ در سرور جداگانه

---

یعنی:

اگر سرور اصلی هک شد

هنوز Logها محفوظ باشند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Incident Detection چیست؟
</p>

تشخیص رخداد امنیتی

---

هدف:

پیدا کردن حملات در سریع‌ترین زمان ممکن.

---

هرچه زودتر حمله شناسایی شود:

خسارت کمتر خواهد بود.

---

# یک قانون مهم

در امنیت سایبری می‌گویند:

> شما نمی‌توانید از چیزی دفاع کنید که آن را نمی‌بینید.

---

به همین دلیل:

<p dir='rtl'>
Logging و Monitoring جزو مهم‌ترین ابزارهای دفاعی هستند.
</p>

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
• Logging چیست <br>
• چرا لاگ‌ها مهم هستند <br>
• انواع سطح‌های Log <br>
• Monitoring چیست <br>
• تفاوت Logging و Monitoring <br>
• Alert چیست <br>
• SIEM چیست <br>
• Incident Detection چیست <br>
• چرا مهاجمان Logها را حذف می‌کنند <br>
• نقش Logging در پروژه Port Scanner
</p>

---

# در جلسه بعد چه یاد می‌گیریم؟

در جلسه نهم وارد یکی از جذاب‌ترین مباحث امنیت می‌شویم:

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Defense in Depth
</p>

یا

# دفاع چندلایه

یاد می‌گیریم:

<p dir='rtl'>
• چرا یک لایه امنیت کافی نیست <br>
• فایروال چه نقشی دارد <br>
• آنتی‌ویروس چه نقشی دارد <br>
• احراز هویت چه نقشی دارد <br>
• چگونه سازمان‌های بزرگ امنیت خود را لایه‌لایه طراحی می‌کنند
</p>

این مفهوم یکی از مهم‌ترین اصول معماری امنیت در جهان است.

</div>