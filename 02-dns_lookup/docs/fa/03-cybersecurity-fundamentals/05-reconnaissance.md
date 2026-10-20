<div align='right'>

[🇬🇧 English](/02-dns_lookup/docs/en/03-cybersecurity-fundamentals/05-reconnaissance.md)

</div>

# درس 05: Reconnaissance

## مقدمه

تقریباً هیچ مهاجمی حمله را مستقیماً آغاز نمی‌کند.

---

قبل از هر حمله موفق معمولاً مرحله‌ای وجود دارد به نام:

```text
Reconnaissance
```

---

که به آن:

```text
Recon
```

نیز گفته می‌شود.

---

هدف Reconnaissance:

<div align='right' dir='rtl'>

```text
جمع‌آوری اطلاعات درباره هدف
```

</div>

است.

---

هرچه اطلاعات بیشتری جمع‌آوری شود:

<div align='right' dir='rtl'>

```text
احتمال موفقیت حمله بیشتر می‌شود.
```

</div>

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Reconnaissance چیست؟</span>

</div>

<p dir='rtl'>
Reconnaissance فرآیند شناسایی و جمع‌آوری اطلاعات درباره یک هدف است.
</p>

---

این اطلاعات می‌توانند شامل موارد زیر باشند:

<p dir='rtl'>
• دامنه‌ها <br>
• زیر دامنه‌ها <br>
• آدرس‌های IP <br>
• DNS Records <br>
• سرویس‌های شبکه <br>
• تکنولوژی‌های استفاده شده <br>
• ایمیل‌ها <br>
• اطلاعات کارکنان
</p>

---

به بیان ساده:

<div align='right' dir='rtl'>

```text
شناخت هدف قبل از حمله
```

</div>

---

# چرا Recon مهم است؟

فرض کنید مهاجم هیچ اطلاعاتی درباره هدف ندارد.

---

در این حالت:

<div align='right' dir='rtl'>

```text
حمله تقریباً کورکورانه خواهد بود.
```

</div>

---

اما اگر مهاجم بداند:

<div align='right' dir='rtl'>

```text
هدف چه سرویس‌هایی دارد؟
چه DNS Recordهایی دارد؟
چه فناوری‌هایی استفاده می‌کند؟
```

</div>

---

می‌تواند حملات بسیار مؤثرتری طراحی کند.

---

# انواع Reconnaissance

<p dir='rtl'>
Recon معمولاً به دو دسته تقسیم می‌شود:
</p>

```text
Passive Reconnaissance
Active Reconnaissance
```

---

<div align='right' dir='rtl'>

# Passive Reconnaissance

</div>

در Passive Recon مهاجم اطلاعات را جمع‌آوری می‌کند بدون اینکه مستقیماً با هدف تعامل داشته باشد.

---

هدف:

<div align='right' dir='rtl'>

```text
جمع‌آوری اطلاعات
بدون جلب توجه
```

</div>

---

# مثال‌ها

## جستجو در موتورهای جستجو

نمونه:

```text
site:example.com
```

---

## بررسی شبکه‌های اجتماعی

نمونه:

<p dir='rtl'>
• LinkedIn <br>
• X <br>
• GitHub
</p>

---

## بررسی اطلاعات WHOIS

نمونه:

```text
Domain Registration Data
```

---

## بررسی Certificate Transparency Logs

برای یافتن زیر دامنه‌ها.

---

# مزیت Passive Recon

<div align='right' dir='rtl'>

```text
هدف معمولاً متوجه فعالیت مهاجم نمی‌شود.
```

</div>

---

<div align='right' dir='rtl'>

# Active Reconnaissance

</div>

در Active Recon مهاجم مستقیماً با سیستم هدف ارتباط برقرار می‌کند.

---

مثال:

<p dir='rtl'>
• ارسال DNS Query <br>
• Port Scanning <br>
• Banner Grabbing <br>
• Service Detection
</p>

---

در این حالت:

<div align='right' dir='rtl'>

```text
هدف ممکن است فعالیت را ثبت کند.
```

</div>

---

# مثال

وقتی اجرا می‌کنیم:

```bash
python -m src.cli example.com A
```

---

ابزار DNS Lookup یک DNS Query واقعی ارسال می‌کند.

---

این فعالیت:

```text
Active Recon
```

محسوب می‌شود.

---

# مثال دیگر

<p dir='rtl'>
Port Scanner:
</p>

```text
TCP Connection
```

برقرار می‌کند.

---

این نیز:

```text
Active Recon
```

است.

---

# اطلاعاتی که در Recon جمع‌آوری می‌شوند

معمولاً مهاجم به دنبال پاسخ این پرسش‌ها است:

---

## هدف چه دامنه‌هایی دارد؟

نمونه:

```text
example.com
```

---

## چه زیر دامنه‌هایی وجود دارند؟

نمونه:

```text
mail.example.com

vpn.example.com

api.example.com
```

---

## چه IPهایی استفاده می‌شوند؟

نمونه:

```text
93.184.216.34
```

---

## چه سرویس‌هایی اجرا می‌شوند؟

نمونه:

```text
SSH
HTTP
HTTPS
SMTP
```

---

## چه فناوری‌هایی استفاده می‌شوند؟

نمونه:

```text
Apache
Nginx
WordPress
```

---

# ارتباط Recon با Attack Surface

در درس قبل یاد گرفتیم:

```text
Attack Surface
```

---

<p dir='rtl'>
Recon فرآیندی است که برای کشف Attack Surface انجام می‌شود.
</p>

---

به بیان ساده:

```text
Recon
=
Discovery of Attack Surface
```

---

# ابزارهای Recon

برخی ابزارهای رایج:

<p dir='rtl'>
• DNS Lookup <br>
• Port Scanner <br>
• Whois Tools <br>
• Subdomain Finder <br>
• Network Mapper
</p>

---

جالب است بدانید:

<div align='right' dir='rtl'>

```text
دو ابزار اول را
خودمان ساخته‌ایم.
```

</div>

---

# مثال عملی

فرض کنید:

```text
example.com
```

را بررسی می‌کنیم.

---

<p dir='rtl'>
DNS Lookup:
</p>

```text
MX Record
```

را پیدا می‌کند.

---

خروجی:

```text
mail.example.com
```

---

اکنون مهاجم می‌داند:

```text
Mail Server
```

وجود دارد.

---

سپس با Port Scanner:

```text
mail.example.com
```

را اسکن می‌کند.

---

و متوجه می‌شود:

```text
25/tcp
465/tcp
587/tcp
```

باز هستند.

---

این اطلاعات می‌توانند برای مراحل بعدی حمله استفاده شوند.

---

# آیا Recon غیرقانونی است؟

پاسخ:

<div align='right' dir='rtl'>

```text
بستگی دارد.
```

</div>

---

اگر روی سیستم‌هایی انجام شود که مالک آن نیستید یا مجوز ندارید:

ممکن است مشکلات قانونی ایجاد کند.

---

به همین دلیل در تمام ابزارهای امنیتی ما تأکید شده است:

```text
Only use on systems
you own or have permission to test.
```

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Recon و Blue Team</span>

</div>

<p dir='rtl'>
Recon فقط برای مهاجمان نیست.
</p>

---

مدافعان نیز از Recon استفاده می‌کنند.

---

برای مثال:

<p dir='rtl'>
• کشف سرویس‌های فراموش‌شده <br>
• یافتن زیر دامنه‌های قدیمی <br>
• بررسی Attack Surface سازمان
</p>

---

# نکته مهم

بیشتر حملات موفق:

<div align='right' dir='rtl'>

```text
با Exploitation شروع نمی‌شوند.
```

</div>

---

بلکه با:

```text
Reconnaissance
```

شروع می‌شوند.

---

زیرا:

<div align='right' dir='rtl'>

```text
اطلاعات
قدرت است.
```

</div>

---

# ارتباط با پروژه‌های ما

<div align='right' dir='rtl'>

## Port Scanner

</div>

استفاده برای:

```text
Service Discovery
```

---

<div align='right' dir='rtl'>

## DNS Lookup

</div>

استفاده برای:

```text
DNS Recon
```

---

هر دو ابزار در فاز Reconnaissance قرار می‌گیرند.

---

# خلاصه

در این درس یاد گرفتیم:

<p dir='rtl'>
• Reconnaissance چیست <br>
• Passive Recon چیست <br>
• Active Recon چیست <br>
• مهاجمان چه اطلاعاتی جمع‌آوری می‌کنند <br>
• Recon چگونه Attack Surface را آشکار می‌کند <br>
• نقش DNS Lookup و Port Scanner در Recon چیست
</p>

---

# درس بعدی

در درس بعدی وارد مرحله بعد از Recon می‌شویم:

```text
Enumeration
```

و یاد می‌گیریم:

<p dir='rtl'>
• Enumeration چیست <br>
• چه تفاوتی با Recon دارد <br>
• چرا مهاجمان پس از Recon وارد Enumeration می‌شوند <br>
• چگونه اطلاعات خام را به اطلاعات قابل استفاده تبدیل می‌کنند
</p>
