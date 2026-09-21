<div dir="rtl">

# جلسه ۳: تهدیدها، آسیب‌پذیری‌ها و حملات

# مقدمه

در جلسه قبل یاد گرفتیم:

```text
هکر کیست؟
```

و فهمیدیم که:

```text
امنیت سایبری فقط هک کردن نیست
```

---

اما هنوز یک سؤال مهم باقی مانده است:

---

اصلاً مهاجم چگونه وارد یک سیستم می‌شود؟

---

پاسخ این سؤال در سه مفهوم مهم نهفته است:

```text
Threat
Vulnerability
Attack
```

---

اگر این سه مفهوم را درک کنیم:

---

تقریباً پایه تمام امنیت سایبری را درک کرده‌ایم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Threat چیست؟
</p>

<p dir='rtl'>
Threat یعنی:
</p>

```text
تهدید
```

---

هر چیزی که بتواند به سیستم آسیب برساند.

---

مثال:

```text
Hacker
Malware
Virus
Ransomware
Insider
```

---

همگی:

```text
Threat
```

هستند.

---

# مثال واقعی

فرض کن یک خانه داری.

---

یک دزد در محله وجود دارد.

---

حتی اگر هنوز وارد خانه نشده باشد:

---

او یک:

```text
Threat
```

است.

---

زیرا پتانسیل آسیب رساندن دارد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Vulnerability چیست؟
</p>

<p dir='rtl'>
Vulnerability یعنی:
</p>

```text
آسیب‌پذیری
```

یا

```text
نقطه ضعف
```

---

ضعفی که بتوان از آن سوءاستفاده کرد.

---

مثال:

```text
رمز عبور ضعیف
```

---

یا:

```text
نرم‌افزار قدیمی
```

---

یا:

```text
پورت باز بدون محافظت
```

---

همگی آسیب‌پذیری هستند.

---

# مثال خانه

درب خانه را تصور کن.

---

اگر درب قفل نداشته باشد:

---

این:

```text
Vulnerability
```

است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Attack چیست؟
</p>

<p dir='rtl'>
Attack یعنی:
</p>

```text
حمله
```

---

زمانی اتفاق می‌افتد که مهاجم از یک آسیب‌پذیری استفاده کند.

---

مثال:

```text
Weak Password
```

<p dir='rtl'>
↓
</p>

```text
Password Guessing
```

<p dir='rtl'>
↓
</p>

```text
Unauthorized Access
```

---

این یک:

```text
Attack
```

است.

---

# ارتباط این سه مفهوم

تقریباً تمام حملات امنیتی به شکل زیر هستند:

---

```text
Threat
+
Vulnerability
=
Attack
```

---

مثال:

```text
Hacker
+
Weak Password
=
Login Attack
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Exploit چیست؟
</p>

اصطلاح مهم بعدی:

```text
Exploit
```

---

ابزاری یا روشی که برای سوءاستفاده از یک آسیب‌پذیری استفاده می‌شود.

---

مثال:

---

فرض کن برنامه‌ای دارای یک ضعف امنیتی است.

---

کدی که از آن ضعف استفاده کند:

```text
Exploit
```

نامیده می‌شود.

---

# مثال واقعی

آسیب‌پذیری:

```text
SQL Injection
```

---

کد حمله:

```text
Exploit
```

---

نتیجه:

```text
دسترسی غیرمجاز
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Malware چیست؟
</p>

<p dir='rtl'>
Malware مخفف:
</p>

```text
Malicious Software
```

است.

---

یعنی:

```text
نرم‌افزار مخرب
```

---

هدف:

```text
آسیب رساندن
```

یا

```text
سوءاستفاده
```

است.

---

# انواع Malware

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
Virus
</p>

ویروس

---

خود را به فایل‌ها متصل می‌کند.

---

و هنگام اجرا منتشر می‌شود.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Worm
</p>

کرم

---

برای انتشار:

```text
نیازی به دخالت کاربر ندارد
```

---

از شبکه استفاده می‌کند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Trojan
</p>

اسب تروا

---

ظاهر مفید دارد.

---

اما در پشت صحنه:

```text
رفتار مخرب
```

انجام می‌دهد.

---

مثال:

```text
Game.exe
```

---

اما در واقع:

```text
Malware
```

است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Spyware
</p>

جاسوس‌افزار

---

اطلاعات کاربر را جمع‌آوری می‌کند.

---

مثال:

```text
Passwords
Browser History
Cookies
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Keylogger
</p>

نوعی Spyware.

---

تمام کلیدهای فشرده شده توسط کاربر را ثبت می‌کند.

---

مثال:

---

وقتی رمز عبور تایپ می‌کنی.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Ransomware
</p>

یکی از خطرناک‌ترین انواع Malware.

---

فایل‌ها را:

```text
Encrypt
```

می‌کند.

---

سپس درخواست پول می‌کند.

---

مثال:

```text
Pay 1000$
or
Lose Your Files
```

---

# چرا Ransomware خطرناک است؟

زیرا ممکن است:

---

کل اطلاعات شرکت را قفل کند.

---

نمونه‌های واقعی:

```text
WannaCry
LockBit
Conti
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Social Engineering چیست؟
</p>

گاهی مهاجم اصلاً سیستم را هک نمی‌کند.

---

بلکه:

```text
انسان را هک می‌کند
```

---

به این روش:

```text
Social Engineering
```

می‌گویند.

---

# مثال

پیام:

```text
حساب شما مسدود شده است.
برای فعال‌سازی اینجا کلیک کنید.
```

---

کاربر کلیک می‌کند.

---

رمز عبور را وارد می‌کند.

---

حمله موفق می‌شود.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Phishing چیست؟
</p>

معروف‌ترین نوع Social Engineering.

---

هدف:

```text
سرقت اطلاعات
```

---

از طریق:

```text
Email
SMS
Website
```

---

# آیا Port Scanner هم حمله است؟

خیر.

---

پورت اسکن معمولاً:

```text
Reconnaissance
```

است.

---

یعنی:

```text
جمع‌آوری اطلاعات
```

---

قبل از حمله.

---

مثال:

---

ابتدا مهاجم بررسی می‌کند:

```text
چه پورت‌هایی باز هستند؟
```

---

بعد تصمیم می‌گیرد:

```text
آیا آسیب‌پذیری وجود دارد؟
```

---

# نقش پروژه ما

پروژه‌ای که ساخته‌ایم:

```text
Port Scanner
```

---

در اولین مرحله چرخه امنیت قرار می‌گیرد:

---

```text
Information Gathering
```

---

یا:

```text
Reconnaissance
```

---

# سناریوی واقعی

فرض کن مهاجم یک سرور پیدا کرده است.

---

ابتدا:

```text
Port Scan
```

انجام می‌دهد.

---

نتیجه:

```text
22
80
3306
```

---

باز هستند.

---

اکنون می‌داند:

```text
SSH
HTTP
MySQL
```

فعال هستند.

---

سپس شروع به بررسی آسیب‌پذیری‌ها می‌کند.

---

# چیزی که امروز یاد گرفتیم

<p dir='rtl'>
✅ Threat چیست <br>
✅ Vulnerability چیست <br>
✅ Attack چیست <br>
✅ Exploit چیست <br>
✅ Malware چیست <br>
✅ Virus چیست <br>
✅ Worm چیست <br>
✅ Trojan چیست <br>
✅ Spyware چیست <br>
✅ Keylogger چیست <br>
✅ Ransomware چیست <br>
✅ Social Engineering چیست <br>
✅ Phishing چیست <br>
✅ جایگاه Port Scanner در فرآیند حمله
</p>

---

# تمرین

برای هر مورد مشخص کن:

```text
Threat
یا
Vulnerability
یا
Attack
```

---

### مثال اول

```text
Password = 123456
```

---

### مثال دوم

```text
Ransomware
```

---

### مثال سوم

```text
استفاده از رمز ضعیف و ورود به حساب
```

---

### مثال چهارم

```text
SQL Injection Exploit
```

---

# جلسه بعد

فایل:

```text
04-security-lifecycle.md
```

موضوع:

**چرخه کامل حمله و دفاع در امنیت سایبری**

در جلسه بعد یاد می‌گیریم:

<p dir='rtl'>
• Reconnaissance <br>
• Scanning <br>
• Enumeration <br>
• Exploitation <br>
• Privilege Escalation <br>
• Persistence <br>
• Covering Tracks
</p>

و دقیقاً خواهیم دید Port Scanner در کدام مرحله از یک حمله یا تست نفوذ قرار می‌گیرد.

</div>