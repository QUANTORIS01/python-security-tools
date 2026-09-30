<div dir="rtl" align="right">

## جلسه ششم: احراز هویت (Authentication) و مجوزدهی (Authorization)

# مقدمه

تا اینجای مسیر یادگیری با موارد مهمی آشنا شدیم:

<p dir='rtl'>
• امنیت سایبری چیست <br>
• مهاجمان چه کسانی هستند <br>
• آسیب‌پذیری چیست <br>
• چرخه امنیت چگونه کار می‌کند <br>
• مدل‌سازی تهدید چیست
</p>

اکنون به یکی از مهم‌ترین بخش‌های امنیت نرم‌افزار می‌رسیم.

تقریباً هر برنامه‌ای که امروزه می‌بینید از این مفاهیم استفاده می‌کند:

<p dir='rtl'>
• اینستاگرام <br>
• تلگرام <br>
• جیمیل <br>
• گیت‌هاب <br>
• دیجی‌کالا <br>
• آمازون <br>
• بانک‌های اینترنتی
</p>

اگر این بخش اشتباه پیاده‌سازی شود، کل سیستم ممکن است به خطر بیفتد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Authentication چیست؟
</p>

<p dir='rtl'>
Authentication یعنی:
</p>

> اثبات هویت

یا به زبان ساده:

> «تو واقعاً چه کسی هستی؟»

---

# مثال دنیای واقعی

فرض کنید وارد بانک می‌شوید.

کارمند بانک می‌پرسد:

<p dir='rtl'>
• کارت ملی دارید؟ <br>
• شماره حساب چیست؟
</p>

هدف چیست؟

اثبات هویت شما.

این همان Authentication است.

---

# مثال در اینترنت

هنگام ورود به جیمیل:

```text
Username
Password
```

گوگل بررسی می‌کند:

آیا واقعاً صاحب این حساب هستید؟

اگر بله:

اجازه ورود می‌دهد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Authorization چیست؟
</p>

<p dir='rtl'>
Authorization یعنی:
</p>

> تعیین سطح دسترسی

یا:

> بعد از اینکه فهمیدیم چه کسی هستی، حالا چه کارهایی اجازه داری انجام دهی؟

---

# مثال دنیای واقعی

شما وارد یک شرکت شده‌اید.

<p dir='rtl'>
Authentication:
</p>

بررسی می‌شود که شما کارمند هستید.

<p dir='rtl'>
Authorization:
</p>

مشخص می‌شود به کدام اتاق‌ها اجازه ورود دارید.

---

# تفاوت اصلی

<p dir='rtl'>
Authentication:
</p>

```text
Who are you?
```

<p dir='rtl'>
Authorization:
</p>

```text
What can you do?
```

---

# مثال ساده

فرض کنید وارد پنل مدیریت سایت شده‌ایم.

کاربر اول:

```text
admin
```

کاربر دوم:

```text
user
```

هر دو Login کرده‌اند.

اما فقط مدیر می‌تواند:

<p dir='rtl'>
• حذف کاربران <br>
• تغییر تنظیمات <br>
• مشاهده گزارش‌ها
</p>

را انجام دهد.

---

# پس...

<p dir='rtl'>
Authentication:
</p>

ورود به سیستم

<p dir='rtl'>
Authorization:
</p>

سطح دسترسی داخل سیستم

---

# مراحل Login چگونه است؟

معمولاً به این شکل:

```text
User
 |
 v
Username + Password
 |
 v
Server
 |
 v
Database
 |
 v
Success / Fail
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Password چگونه نگهداری می‌شود؟
</p>

یکی از بزرگ‌ترین اشتباهات برنامه‌نویسان مبتدی:

ذخیره رمز عبور به صورت متن ساده است.

مثال خطرناک:

```text
password123
```

در دیتابیس.

---

# چرا خطرناک است؟

اگر دیتابیس نشت کند:

تمام رمزها لو می‌روند.

---

# راه حل چیست؟

<p dir='rtl'>
Hash
</p>

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Hash چیست؟
</p>

<p dir='rtl'>
Hash یک تابع یک‌طرفه است.
</p>

مثال:

```text
password123
```

تبدیل می‌شود به:

```text
482c811da5d5b4bc6d497ffa98491e38
```

---

# ویژگی Hash

می‌توان:

```text
Password
→ Hash
```

را انجام داد.

اما برعکس آن تقریباً غیرممکن است.

---

# الگوریتم‌های رایج

قدیمی:

```text
MD5
SHA1
```

امروزه توصیه نمی‌شوند.

---

الگوریتم‌های مناسب:

```text
bcrypt
scrypt
Argon2
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Session چیست؟
</p>

بعد از Login قرار نیست کاربر هر ثانیه رمز عبور وارد کند.

بنابراین سرور چیزی به نام Session ایجاد می‌کند.

---

# مثال

```text
User Login
```

↓

```text
Session Created
```

↓

```text
Session ID
```

↓

```text
Browser
```

---

کاربر تا زمانی که Session معتبر باشد دوباره Login نمی‌کند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Cookie چیست؟
</p>

معمولاً Session ID داخل Cookie ذخیره می‌شود.

---

مثال:

```text
session_id=abc123xyz
```

مرورگر این مقدار را ذخیره می‌کند.

---

# هر درخواست بعدی

```text
GET /profile
```

همراه Session ارسال می‌شود.

سرور متوجه می‌شود:

این همان کاربر قبلی است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
JWT چیست؟
</p>

<p dir='rtl'>
JWT مخفف:
</p>

```text
JSON Web Token
```

است.

---

در سیستم‌های مدرن بسیار استفاده می‌شود.

مثلاً:

<p dir='rtl'>
• APIها <br>
• Microservices <br>
• Mobile Apps
</p>

---

# ساختار JWT

سه بخش دارد:

```text
Header
Payload
Signature
```

---

نمونه:

```text
xxxxx.yyyyy.zzzzz
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Payload چیست؟
</p>

اطلاعات کاربر:

مثلاً:

```json
{
  "id": 5,
  "role": "admin"
}
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Signature چیست؟
</p>

امضا

برای جلوگیری از دستکاری اطلاعات.

---

# حمله Brute Force

یکی از معروف‌ترین حملات Login.

---

هکر تلاش می‌کند:

```text
123456
12345678
password
admin
qwerty
```

و هزاران رمز دیگر را امتحان کند.

---

# راه مقابله

<p dir='rtl'>
• محدود کردن تعداد تلاش <br>
• Captcha <br>
• MFA <br>
• قفل موقت حساب
</p>

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
MFA چیست؟
</p>

<p dir='rtl'>
Multi-Factor Authentication
</p>

یا:

احراز هویت چندمرحله‌ای

---

مثال:

<p dir='rtl'>
1. رمز عبور <br>
2. کد پیامک
</p>

---

یا:

<p dir='rtl'>
1. رمز عبور <br>
2. Google Authenticator
</p>

---

# چرا MFA مهم است؟

حتی اگر رمز عبور لو برود:

هنوز مرحله دوم وجود دارد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Principle of Least Privilege
</p>

یکی از مهم‌ترین قوانین امنیت.

---

معنی:

> هر کاربر فقط به اندازه نیازش دسترسی داشته باشد.

---

اشتباه:

```text
همه = Administrator
```

---

درست:

```text
هرکس فقط دسترسی موردنیاز خود را داشته باشد.
```

---

# مثال در Port Scanner

فرض کنیم نسخه وب ساخته‌ایم.

کاربر عادی:

<p dir='rtl'>
• اجرای اسکن
</p>

---

مدیر:

<p dir='rtl'>
• مشاهده لاگ‌ها <br>
• حذف کاربران <br>
• تنظیمات سیستم
</p>

---

این یعنی Authorization.

---

# اشتباه رایج برنامه‌نویسان

بررسی سطح دسترسی فقط در Front-End.

---

مثال:

دکمه حذف را مخفی می‌کنند.

اما API همچنان فعال است.

---

هکر مستقیماً API را صدا می‌زند.

---

سطح دسترسی باید در سرور بررسی شود.

همیشه.

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
• Authentication چیست <br>
• Authorization چیست <br>
• تفاوت آن‌ها چیست <br>
• Login چگونه کار می‌کند <br>
• Hash چیست <br>
• Session چیست <br>
• Cookie چیست <br>
• JWT چیست <br>
• MFA چیست <br>
• Brute Force چیست <br>
• اصل Least Privilege چیست
</p>

---

# در جلسه بعد چه یاد می‌گیریم؟

در جلسه هفتم وارد یکی از خطرناک‌ترین و معروف‌ترین حملات دنیای امنیت می‌شویم:

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Input Validation و Injection Attacks
</p>

یاد می‌گیریم:

<p dir='rtl'>
• چرا هر ورودی کاربر خطرناک است <br>
• SQL Injection چیست <br>
• Command Injection چیست <br>
• Path Traversal چیست <br>
• چگونه ورودی‌ها را امن کنیم
</p>

این مبحث مستقیماً به پروژه Port Scanner ما نیز مرتبط است؛ چون ما نیز ورودی‌هایی مانند IP، پورت و تنظیمات را از کاربر دریافت می‌کنیم.

</div>