<div align='right'>

[🇬🇧 English](/02-dns_lookup/docs/en/03-cybersecurity-fundamentals/03-threats-vulnerabilities-and-risks.md)

</div>

# درس 03: Threats, Vulnerabilities and Risks

## مقدمه

سه واژه وجود دارند که تقریباً در تمام شاخه‌های امنیت سایبری استفاده می‌شوند:

```text
Threat
Vulnerability
Risk
```

---

بسیاری از افراد این سه مفهوم را با یکدیگر اشتباه می‌گیرند.

در حالی که هر کدام معنی متفاوتی دارند و درک تفاوت آن‌ها برای یک متخصص امنیت ضروری است.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Threat چیست؟</span>

</div>

<p dir='rtl'>
Threat به هر چیزی گفته می‌شود که بتواند به یک دارایی آسیب برساند.
</p>

---

به بیان ساده:

<div align='right' dir='rtl'>

```text
یک عامل بالقوه برای ایجاد خسارت
```

</div>

---

# مثال

نمونه‌هایی از Threat:

<p dir='rtl'>
• هکرها <br>
• بدافزارها <br>
• باج‌افزارها <br>
• حملات DDoS <br>
• کارکنان ناراضی <br>
• خطاهای انسانی <br>
• بلایای طبیعی
</p>

---

همه این موارد می‌توانند باعث آسیب به سیستم شوند.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Vulnerability چیست؟</span>

</div>

<p dir='rtl'>
Vulnerability یعنی:
</p>

<div align='right' dir='rtl'>

```text
ضعف یا نقصی
که توسط Threat قابل سوءاستفاده باشد.
```

</div>

---

به عبارت دیگر:

<div align='right' dir='rtl'>

```text
درِ باز
برای ورود مهاجم
```

</div>

---

# مثال

فرض کن یک وب‌سایت:

```text
Admin Panel
```

دارد.

---

و رمز عبور مدیر:

```text
123456
```

است.

---

این یک:

```text
Vulnerability
```

است.

---

زیرا مهاجم می‌تواند از آن سوءاستفاده کند.

---

# مثال دیگر

نسخه قدیمی یک نرم‌افزار:

```text
Outdated Software
```

---

ممکن است دارای آسیب‌پذیری شناخته‌شده باشد.

---

در این حالت:

<div align='right' dir='rtl'>

```text
نسخه قدیمی = Vulnerability
```

</div>

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Threat بدون Vulnerability</span>

</div>

فرض کن:

<div align='right' dir='rtl'>

```text
یک مهاجم وجود دارد
```

</div>

اما سیستم هیچ ضعفی ندارد.

---

در این حالت:

```text
Threat Exists
```

اما احتمال موفقیت حمله پایین است.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Vulnerability بدون Threat</span>

</div>

فرض کن:

<div align='right' dir='rtl'>

```text
سیستم آفلاین است
و هیچ مهاجمی وجود ندارد.
```

</div>

---

در این حالت:

```text
Vulnerability Exists
```

اما تهدید فعالی وجود ندارد.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Risk چیست؟</span>

</div>

<p dir='rtl'>
Risk زمانی ایجاد می‌شود که:
</p>

```text
Threat
+
Vulnerability
```

با هم ترکیب شوند.

---

فرمول ساده:

```text
Risk = Threat + Vulnerability
```

---

# مثال

دارایی:

<div align='right' dir='rtl'>

```text
وب‌سایت شرکت
```

</div>

---

<p dir='rtl'>
Threat:
</p>

<div align='right' dir='rtl'>

```text
مهاجم اینترنتی
```

</div>

---

<p dir='rtl'>
Vulnerability:
</p>

<div align='right' dir='rtl'>

```text
رمز عبور ضعیف
```

</div>

---

نتیجه:

```text
Risk
```

---

زیرا مهاجم می‌تواند از ضعف موجود سوءاستفاده کند.

---

# مثال دنیای واقعی

دارایی:

```text
Database Server
```

---

<p dir='rtl'>
Threat:
</p>

```text
Ransomware
```

---

<p dir='rtl'>
Vulnerability:
</p>

<div align='right' dir='rtl'>

```text
عدم نصب Patchهای امنیتی
```

</div>

---

نتیجه:

```text
Risk of Compromise
```

---

# شدت ریسک

همه ریسک‌ها یکسان نیستند.

---

دو عامل مهم:

```text
Likelihood
Impact
```

---

<div align='right' dir='rtl'>

# Likelihood

</div>

احتمال وقوع حادثه.

---

مثال:

```text
Weak Password
```

احتمال سوءاستفاده بالایی دارد.

---

<div align='right' dir='rtl'>

# Impact

</div>

شدت خسارت.

---

مثال:

نشت اطلاعات بانکی:

```text
High Impact
```

---

# نمونه مقایسه

## ریسک اول

<p dir='rtl'>
Threat:
</p>

```text
Script Kiddie
```

---

<p dir='rtl'>
Vulnerability:
</p>

```text
Password = admin
```

---

<p dir='rtl'>
Likelihood:
</p>

```text
High
```

---

<p dir='rtl'>
Impact:
</p>

```text
Medium
```

---

## ریسک دوم

<p dir='rtl'>
Threat:
</p>

```text
Nation State Actor
```

---

<p dir='rtl'>
Vulnerability:
</p>

```text
Zero-Day Vulnerability
```

---

<p dir='rtl'>
Likelihood:
</p>

```text
Medium
```

---

<p dir='rtl'>
Impact:
</p>

```text
Very High
```

---

# کاهش ریسک

هدف امنیت:

<div align='right' dir='rtl'>

```text
حذف تمام ریسک‌ها نیست
```

</div>

---

زیرا این کار تقریباً غیرممکن است.

---

هدف:

```text
Risk Reduction
```

است.

---

# روش‌های کاهش ریسک

نمونه‌ها:

<p dir='rtl'>
• نصب Patchها <br>
• استفاده از MFA <br>
• Backup <br>
• محدودسازی دسترسی‌ها <br>
• مانیتورینگ <br>
• آموزش کاربران
</p>

---

# مثال عملی

رمز عبور:

```text
123456
```

---

<p dir='rtl'>
Threat:
</p>

```text
Brute Force Attack
```

---

<p dir='rtl'>
Vulnerability:
</p>

```text
Weak Password
```

---

راه‌حل:

```text
Strong Password
+
MFA
```

---

در نتیجه:

```text
Risk ↓
```

کاهش پیدا می‌کند.

---

# ارتباط با Port Scanner

وقتی در Port Scanner یک پورت باز پیدا می‌کنیم:

```text
Open Port
```

---

این به خودی خود Vulnerability نیست.

---

اما می‌تواند نشانه‌ای از:

```text
Attack Surface
```

باشد.

---

سپس باید بررسی کنیم:

<div align='right' dir='rtl'>

```text
آیا سرویس آسیب‌پذیر است؟
```

</div>

---

# ارتباط با DNS Lookup

در DNS Lookup نیز ممکن است اطلاعاتی پیدا کنیم که به مهاجم کمک کند.

---

مثال:

```text
TXT Records
```

---

یا:

```text
Internal Hostnames
```

---

این اطلاعات مستقیماً آسیب‌پذیری نیستند.

اما می‌توانند در مراحل بعدی حمله مفید باشند.

---

# اشتباه رایج

بسیاری از افراد می‌گویند:

```text
Open Port = Vulnerability
```

---

این همیشه درست نیست.

---

یا:

```text
Threat = Risk
```

---

که آن هم اشتباه است.

---

تفاوت را به خاطر بسپار:

<div align='center' dir='rtl'>

```text
Threat
=
عامل تهدیدکننده

Vulnerability
=
ضعف

Risk
=
احتمال خسارت ناشی از سوءاستفاده
```

</div>

---

# خلاصه

در این درس یاد گرفتیم:

<p dir='rtl'>
• Threat چیست <br>
• Vulnerability چیست <br>
• Risk چیست <br>
• رابطه بین این سه مفهوم <br>
• چگونه ریسک ایجاد می‌شود <br>
• چگونه ریسک کاهش پیدا می‌کند <br>
• ارتباط این مفاهیم با ابزارهای امنیتی ما
</p>

---

# درس بعدی

در درس بعدی وارد یکی از مهم‌ترین مفاهیم امنیت تهاجمی و تدافعی می‌شویم:

```text
Attack Surface
```

و یاد می‌گیریم:

<p dir='rtl'>
• Attack Surface چیست <br>
• چگونه شناسایی می‌شود <br>
• چرا مهاجمان ابتدا آن را بررسی می‌کنند <br>
• ابزارهایی مانند Port Scanner و DNS Lookup چه نقشی در کشف آن دارند
</p>
