<div align='right'>

[🇬🇧 English](/02-dns_lookup/docs/en/03-cybersecurity-fundamentals/04-attack-surface.md)

</div>

# درس 04: Attack Surface

## مقدمه

یکی از اولین کارهایی که هر مهاجم انجام می‌دهد این است که بررسی کند:

<div align='right' dir='rtl'>

```text
از چه مسیرهایی می‌تواند به هدف نزدیک شود؟
```

</div>

---

مجموع تمام این مسیرها را:

```text
Attack Surface
```

می‌نامیم.

---

درک Attack Surface یکی از مهم‌ترین مهارت‌های امنیت سایبری است.

زیرا:

<div align='right' dir='rtl'>

```text
شما نمی‌توانید از چیزی دفاع کنید
که از وجود آن خبر ندارید.
```

</div>

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Attack Surface چیست؟</span>

</div>

<p dir='rtl'>
Attack Surface به تمام نقاطی گفته می‌شود که مهاجم می‌تواند از طریق آن‌ها با یک سیستم تعامل داشته باشد.
</p>

---

به بیان ساده:

<div align='right' dir='rtl'>

```text
تمام درها، پنجره‌ها و ورودی‌های سیستم
```

</div>

---

هر چه Attack Surface بزرگ‌تر باشد:

<div align='right' dir='rtl'>

```text
فرصت‌های بیشتری برای حمله وجود دارد.
```

</div>

---

# مثال ساده

فرض کنید یک سرور داریم.

---

روی این سرور سرویس‌های زیر فعال هستند:

<div align='center'>

```text
22   SSH
80   HTTP
443  HTTPS
3306 MySQL
```

</div>

---

هر سرویس:

<div align='right' dir='rtl'>

```text
یک نقطه ورود احتمالی
```

</div>

است.

---

در نتیجه:

<div align='right' dir='rtl'>

```text
جزئی از Attack Surface
```

</div>

محسوب می‌شود.

---

# اجزای Attack Surface

معمولاً Attack Surface به سه دسته تقسیم می‌شود.

---

<div align='right' dir='rtl'>

## <span dir='rtl'>1. Network Attack Surface</span>

</div>

هر چیزی که از طریق شبکه قابل دسترسی باشد.

---

مثال:

<p dir='rtl'>
• پورت‌های باز <br>
• سرویس‌های شبکه <br>
• DNS <br>
• VPN <br>
• APIها
</p>

---

نمونه:

<div align='center'>

```text
22/tcp
80/tcp
443/tcp
```

</div>

---

ابزار Port Scanner دقیقاً برای کشف این بخش استفاده می‌شود.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>2. Software Attack Surface</span>

</div>

ضعف‌های موجود در نرم‌افزارها.

---

مثال:

<p dir='rtl'>
• آسیب‌پذیری‌های برنامه <br>
• نسخه‌های قدیمی <br>
• تنظیمات اشتباه <br>
• کتابخانه‌های ناامن
</p>

---

نمونه:

```text
Apache 2.2
```

---

یا:

```text
WordPress Plugin Vulnerability
```

---

<div align='right' dir='rtl'>

# <span dir='rtl'>3. Human Attack Surface</span>

</div>

گاهی ضعیف‌ترین بخش سیستم:

<div align='right' dir='rtl'>

```text
انسان‌ها
```

</div>

هستند.

---

مثال:

<p dir='rtl'>
• رمز عبور ضعیف <br>
• کلیک روی لینک مخرب <br>
• افشای اطلاعات <br>
• مهندسی اجتماعی
</p>

---

نمونه:

```text
Password = 123456
```

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Attack Surface در یک شرکت</span>

</div>

فرض کنید یک شرکت داریم.

---

دارایی‌های آن:

```text
Website
Mail Server
VPN
Employees
DNS Records
Cloud Services
```

---

همه این موارد بخشی از Attack Surface هستند.

---

# چرا مهاجمان Attack Surface را بررسی می‌کنند؟

زیرا مهاجم به دنبال:

<div align='right' dir='rtl'>

```text
ساده‌ترین مسیر ورود
```

</div>

است.

---

اغلب مهاجمان:

<div align='right' dir='rtl'>

```text
سخت‌ترین هدف را انتخاب نمی‌کنند.
```

</div>

---

آن‌ها ضعیف‌ترین نقطه را پیدا می‌کنند.

---

# مثال

فرض کنید:

<div align='right' dir='rtl'>

```text
وب‌سایت کاملاً امن است.
```

</div>

---

اما:

```text
SSH Password
=
admin123
```

---

در این حالت:

```text
SSH
```

به مسیر ورود تبدیل می‌شود.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Attack Surface و Reconnaissance</span>

</div>

اولین مرحله اکثر حملات:

```text
Reconnaissance
```

است.

---

در این مرحله مهاجم تلاش می‌کند:

<p dir='rtl'>
• دامنه‌ها را پیدا کند <br>
• DNS Records را بررسی کند <br>
• پورت‌های باز را پیدا کند <br>
• سرویس‌ها را شناسایی کند
</p>

---

همه این فعالیت‌ها برای شناخت Attack Surface انجام می‌شوند.

---

# ارتباط با DNS Lookup

ابزار DNS Lookup ما می‌تواند اطلاعاتی مانند:

```text
A Records
AAAA Records
MX Records
NS Records
TXT Records
```

را نمایش دهد.

---

این اطلاعات بخشی از Attack Surface را آشکار می‌کنند.

---

مثال:

```text
mail.example.com
```

---

یا:

```text
vpn.example.com
```

---

وجود این رکوردها می‌تواند سرنخ‌های مهمی درباره زیرساخت سازمان بدهد.

---

# ارتباط با Port Scanner

<p dir='rtl'>
Port Scanner یکی از مهم‌ترین ابزارهای شناسایی Attack Surface است.
</p>

---

نمونه خروجی:

```text
22/tcp
80/tcp
443/tcp
```

---

اکنون می‌دانیم:

<div align='right' dir='rtl'>

```text
چه سرویس‌هایی در دسترس هستند.
```

</div>

---

این دقیقاً بخشی از Attack Surface است.

---

# کاهش Attack Surface

یکی از مهم‌ترین اصول امنیت:

```text
Attack Surface Reduction
```

است.

---

یعنی:

<div align='right' dir='rtl'>

```text
کم کردن نقاط ورود غیرضروری
```

</div>

---

# مثال‌ها

## بستن پورت‌های غیرضروری

اگر از FTP استفاده نمی‌کنید:

```text
Port 21
```

را ببندید.

---

## حذف سرویس‌های بلااستفاده

هر سرویس اضافی:

<div align='right' dir='rtl'>

```text
ریسک اضافی
```

</div>

است.

---

## حذف حساب‌های قدیمی

کاربران بلااستفاده می‌توانند مسیر حمله باشند.

---

## حذف زیر دامنه‌های قدیمی

نمونه:

```text
old.example.com
```

---

اگر دیگر استفاده نمی‌شود:

<div align='right' dir='rtl'>

```text
حذف شود.
```

</div>

---

# اصل مهم

بسیاری از سازمان‌ها تصور می‌کنند:

<div align='right' dir='rtl'>

```text
باید همه چیز را محافظت کنیم.
```

</div>

---

اما در عمل:

<div align='right' dir='rtl'>

```text
اگر چیزی لازم نیست
آن را حذف کن.
```

</div>

---

این رویکرد معمولاً مؤثرتر است.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Attack Surface و پروژه‌های ما</span>

</div>

تا اینجا دو ابزار ساخته‌ایم:

---

<div align='right' dir='rtl'>

## Port Scanner

</div>

برای کشف:

```text
Open Ports
Services
```

---

<div align='right' dir='rtl'>

## DNS Lookup

</div>

برای کشف:

```text
DNS Infrastructure
```

---

هر دو ابزار در واقع برای تحلیل:

```text
Attack Surface
```

طراحی شده‌اند.

---

# خلاصه

در این درس یاد گرفتیم:

<p dir='rtl'>
• Attack Surface چیست <br>
• چرا مهم است <br>
• انواع Attack Surface <br>
• نقش Reconnaissance در کشف آن <br>
• ارتباط DNS Lookup و Port Scanner با Attack Surface <br>
• روش‌های کاهش Attack Surface
</p>

---

# درس بعدی

در درس بعدی وارد یکی از مهم‌ترین مراحل چرخه حمله می‌شویم:

```text
Reconnaissance
```

و یاد می‌گیریم:

<p dir='rtl'>
• Reconnaissance چیست <br>
• Passive Recon چیست <br>
• Active Recon چیست <br>
• مهاجمان چگونه اطلاعات جمع‌آوری می‌کنند <br>
• ابزارهای ما در کدام بخش این فرآیند قرار می‌گیرند
</p>
