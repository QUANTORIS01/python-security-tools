# درس 02: CIA Triad

## مقدمه

تقریباً تمام مفاهیم امنیت سایبری به یک مدل بسیار مهم برمی‌گردند:

```text
CIA Triad
```

---

این مدل پایه و اساس بسیاری از تصمیمات امنیتی است.

زمانی که یک سیستم طراحی می‌شود یا یک کنترل امنیتی پیاده‌سازی می‌شود، معمولاً هدف محافظت از یک یا چند بخش از CIA Triad است.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>CIA مخفف چیست؟</span>

</div>

<p dir='rtl'>
CIA مخفف سه مفهوم اصلی است:
</p>

```text
Confidentiality
Integrity
Availability
```

---

به فارسی:

<div align='right' dir='rtl'>

```text
محرمانگی
یکپارچگی
دسترس‌پذیری
```

</div>

---

<div align='right' dir='rtl'>

# Confidentiality

</div>

## محرمانگی چیست؟

محرمانگی یعنی:

<div align='right' dir='rtl'>

```text
فقط افراد مجاز
به اطلاعات دسترسی داشته باشند.
```

</div>

---

هدف:

<div align='right' dir='rtl'>

```text
جلوگیری از افشای اطلاعات
```

</div>

است.

---

# مثال

فرض کن یک پایگاه داده شامل اطلاعات مشتریان داریم:

```text
Names
Emails
Phone Numbers
Passwords
```

---

این اطلاعات نباید در اختیار افراد غیرمجاز قرار بگیرند.

---

اگر مهاجم بتواند این اطلاعات را مشاهده کند:

```text
Confidentiality Breach
```

رخ داده است.

---

# روش‌های محافظت از محرمانگی

نمونه‌ها:

<p dir='rtl'>
• رمزنگاری (Encryption) <br>
• احراز هویت (Authentication) <br>
• کنترل دسترسی (Access Control) <br>
• مدیریت مجوزها (Authorization)
</p>

---

مثال:

```text
HTTPS
```

باعث می‌شود اطلاعات در مسیر انتقال رمزنگاری شوند.

---

<div align='right' dir='rtl'>

# Integrity

</div>

## یکپارچگی چیست؟

یکپارچگی یعنی:

<div align='right' dir='rtl'>

```text
اطلاعات بدون تغییر
و صحیح باقی بمانند.
```

</div>

---

هدف:

<div align='right' dir='rtl'>

```text
جلوگیری از دستکاری اطلاعات
```

</div>

است.

---

# مثال

فرض کن موجودی حساب بانکی:

```text
1000$
```

است.

---

اگر مهاجم مقدار را به:

```text
100000$
```

تغییر دهد:

```text
Integrity Violation
```

رخ داده است.

---

# مثال دیگر

فایل نرم‌افزار:

```text
installer.exe
```

---

اگر فایل در مسیر دانلود دستکاری شود:

```text
Integrity
```

از بین رفته است.

---

# روش‌های محافظت از Integrity

نمونه‌ها:

<p dir='rtl'>
• Hashing <br>
• Checksums <br>
• Digital Signatures <br>
• Version Control
</p>

---

مثال:

```text
SHA256
```

برای بررسی تغییر نکردن فایل استفاده می‌شود.

---

<div align='right' dir='rtl'>

# Availability

</div>

## دسترس‌پذیری چیست؟

<p dir='rtl'>
Availability یعنی:
</p>

<div align='right' dir='rtl'>

```text
سیستم و داده‌ها
در زمان موردنیاز
در دسترس باشند.
```

</div>

---

هدف:

<div align='right' dir='rtl'>

```text
جلوگیری از اختلال در سرویس
```

</div>

است.

---

# مثال

فرض کن وب‌سایت شرکت:

```text
example.com
```

---

به دلیل حمله:

```text
DDoS
```

از دسترس خارج شود.

---

در این حالت:

```text
Availability Failure
```

رخ داده است.

---

# مثال دیگر

خرابی هارد دیسک:

```text
Disk Failure
```

---

ممکن است باعث از دسترس خارج شدن داده‌ها شود.

---

# روش‌های محافظت از Availability

نمونه‌ها:

<p dir='rtl'>
• Backup <br>
• Redundancy <br>
• Load Balancing <br>
• Disaster Recovery <br>
• High Availability Systems
</p>

---

# مثال واقعی

فرض کن یک سامانه بانکی داریم.

---

محرمانگی:

<div align='right' dir='rtl'>

```text
فقط صاحب حساب
اطلاعات حساب را ببیند.
```

</div>

---

یکپارچگی:

<div align='right' dir='rtl'>

```text
موجودی حساب
به درستی ثبت شود.
```

</div>

---

دسترس‌پذیری:

<div align='right' dir='rtl'>

```text
بانک 24 ساعته
در دسترس باشد.
```

</div>

---

# آیا هر سه همیشه مهم هستند؟

بله.

اما اهمیت آن‌ها در سیستم‌های مختلف متفاوت است.

---

مثال:

سیستم نظامی:

```text
Confidentiality
```

بسیار مهم است.

---

مثال:

سیستم کنترل ترافیک هوایی:

```text
Availability
```

اهمیت بسیار بالایی دارد.

---

مثال:

سیستم مالی:

```text
Integrity
```

اولویت بالایی دارد.

---

# ارتباط با ابزارهای ما

<div align='right' dir='rtl'>

## Port Scanner

</div>

در Port Scanner بیشتر با:

```text
Availability
```

کار داشتیم.

---

چون بررسی می‌کردیم:

<div align='right' dir='rtl'>

```text
کدام سرویس‌ها
در دسترس هستند.
```

</div>

---

<div align='right' dir='rtl'>

## DNS Lookup

</div>

در DNS Lookup نیز:

```text
Availability
```

اهمیت دارد.

---

اگر DNS Server پاسخ ندهد:

```text
Domain Resolution
```

انجام نمی‌شود.

---

# ارتباط با حملات

تقریباً تمام حملات سایبری یکی از این سه بخش را هدف قرار می‌دهند.

---

سرقت اطلاعات:

```text
Confidentiality
```

---

دستکاری داده:

```text
Integrity
```

---

اختلال در سرویس:

```text
Availability
```

---

# چرا CIA Triad مهم است؟

زیرا هنگام طراحی هر سیستم امنیتی می‌توانیم بپرسیم:

<div align='right' dir='rtl'>

```text
آیا محرمانگی حفظ شده؟
آیا یکپارچگی حفظ شده؟
آیا دسترس‌پذیری حفظ شده؟
```

</div>

---

اگر پاسخ هر سه سؤال مثبت باشد:

<div align='right' dir='rtl'>

```text
سیستم امنیتی قوی‌تر خواهد بود.
```

</div>

---

# خلاصه

در این درس یاد گرفتیم:

<p dir='rtl'>
• CIA Triad چیست <br>
• Confidentiality چیست <br>
• Integrity چیست <br>
• Availability چیست <br>
• هر بخش چه تهدیدهایی دارد <br>
• چگونه از هر بخش محافظت می‌شود <br>
• ارتباط CIA Triad با ابزارهای امنیتی چیست
</p>

---

# درس بعدی

در درس بعدی وارد یکی از مهم‌ترین مفاهیم امنیت می‌شویم:

```text
Threats, Vulnerabilities and Risks
```

و یاد می‌گیریم:

<p dir='rtl'>
• Threat چیست <br>
• Vulnerability چیست <br>
• Risk چیست <br>
• تفاوت این سه مفهوم در چیست <br>
• چرا بیشتر افراد آن‌ها را با هم اشتباه می‌گیرند
</p>
