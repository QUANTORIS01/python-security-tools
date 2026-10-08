# درس 10: Public DNS Providers

## مقدمه

تا اینجا یاد گرفتیم:

<p dir='rtl'>
• DNS چیست <br>
• DNS Query چگونه انجام می‌شود <br>
• Recursive Resolver چیست <br>
• Authoritative Server چیست <br>
• DNS Cache چگونه کار می‌کند
</p>

اما یک سؤال مهم باقی مانده است:

<div align='right' dir='rtl'>

```text
وقتی DNS Query ارسال می‌کنیم،
در واقع از چه DNS Serverی استفاده می‌کنیم؟
```

</div>

پاسخ این است:

<div align='right' dir='rtl'>

```text
بستگی دارد.
```

</div>

ممکن است از DNS ارائه‌دهنده اینترنت (ISP) استفاده کنیم یا از DNS Serverهای عمومی.

در این درس با مشهورترین DNS Providerهای عمومی آشنا می‌شویم.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>DNS Provider چیست؟</span>

</div>

<p dir='rtl'>
DNS Provider سیستمی است که درخواست‌های DNS کاربران را دریافت و پاسخ مناسب را پیدا می‌کند.
</p>

---

به عبارت دیگر:

```text
Recursive Resolver
```

ای که قبلاً یاد گرفتیم معمولاً توسط یک DNS Provider ارائه می‌شود.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>DNS پیش‌فرض ISP</span>

</div>

در بسیاری از شبکه‌ها:

<div align='center' dir='rtl'>

```text
مودم
↓
ISP DNS
```

</div>

استفاده می‌شود.

---

مثال:

```text
Home Router
↓
ISP DNS
```

---

مزیت:

<p dir='rtl'>
• نیاز به تنظیم دستی ندارد <br>
• به صورت خودکار کار می‌کند
</p>

---

معایب:

<p dir='rtl'>
• ممکن است کند باشد <br>
• ممکن است محدودیت‌هایی داشته باشد <br>
• ممکن است لاگ بیشتری نگهداری کند
</p>

---

<div align='right' dir='rtl'>

# Google Public DNS

</div>

یکی از معروف‌ترین DNS Serverهای جهان:

```text
Google Public DNS
```

است.

---

آدرس‌ها:

```text
8.8.8.8
8.8.4.4
```

---

ویژگی‌ها:

<p dir='rtl'>
• سرعت بالا <br>
• زیرساخت جهانی <br>
• پایداری زیاد <br>
• پشتیبانی از DNSSEC
</p>

---

مثال تنظیم:

```text
Primary:
8.8.8.8

Secondary:
8.8.4.4
```

---

<div align='right' dir='rtl'>

# Cloudflare DNS

</div>

یکی از محبوب‌ترین DNS Providerهای امروزی:

```text
Cloudflare
```

است.

---

آدرس‌ها:

```text
1.1.1.1
1.0.0.1
```

---

تمرکز اصلی:

```text
Privacy
```

است.

---

<p dir='rtl'>
Cloudflare ادعا می‌کند:
</p>

<div align='right' dir='rtl'>

```text
لاگ‌های شناسایی‌کننده کاربران
برای مدت طولانی نگهداری نمی‌شوند.
```

</div>

---

مزایا:

<p dir='rtl'>
• سرعت بسیار بالا <br>
• تمرکز بر حریم خصوصی <br>
• پشتیبانی از DNSSEC <br>
• پشتیبانی از DNS over HTTPS
</p>

---

<div align='right' dir='rtl'>

# Quad9

</div>

آدرس:

```text
9.9.9.9
```

---

ویژگی مهم:

```text
Security Filtering
```

---

<p dir='rtl'>
Quad9 برخی دامنه‌های مخرب شناخته‌شده را مسدود می‌کند.
</p>

---

مثال:

```text
Malware Domains
Phishing Domains
```

---

مزایا:

<p dir='rtl'>
• تمرکز بر امنیت <br>
• رایگان <br>
• پشتیبانی از DNSSEC
</p>

---

<div align='right' dir='rtl'>

# OpenDNS

</div>

متعلق به:

```text
Cisco
```

است.

---

آدرس‌ها:

```text
208.67.222.222
208.67.220.220
```

---

قابلیت‌ها:

<p dir='rtl'>
• DNS Filtering <br>
• Parental Control <br>
• Security Features
</p>

---

در محیط‌های سازمانی بسیار محبوب است.

---

# مقایسه Providerها

<div align='center'>

| Provider | Primary IP |
|-----------|-----------|
| Google DNS | 8.8.8.8 |
| Cloudflare DNS | 1.1.1.1 |
| Quad9 | 9.9.9.9 |
| OpenDNS | 208.67.222.222 |

</div>

---

<div align='right' dir='rtl'>

# DNSSEC Support

</div>

امروزه تقریباً تمام DNS Providerهای معتبر:

```text
DNSSEC
```

را پشتیبانی می‌کنند.

---

هدف DNSSEC:

<div align='right' dir='rtl'>

```text
اعتبارسنجی پاسخ DNS
```

</div>

است.

---

این موضوع را در فصل امنیت سایبری مفصل بررسی خواهیم کرد.

---

<div align='right' dir='rtl'>

# DNS over HTTPS (DoH)

</div>

برخی Providerها از:

```text
DNS over HTTPS
```

پشتیبانی می‌کنند.

---

به جای:

```text
UDP/53
```

درخواست‌ها از طریق HTTPS ارسال می‌شوند.

---

مزایا:

<p dir='rtl'>
• افزایش حریم خصوصی <br>
• جلوگیری از شنود ساده DNS
</p>

---

<p dir='rtl'>
Google و Cloudflare از معروف‌ترین ارائه‌دهندگان DoH هستند.
</p>

---

<div align='right' dir='rtl'>

# DNS over TLS (DoT)

</div>

روش دیگری برای رمزنگاری DNS:

```text
DNS over TLS
```

است.

---

هدف:

<div align='right' dir='rtl'>

```text
محافظت از DNS Queryها
```

</div>

است.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Resolver سیستم ما از کدام DNS استفاده می‌کند؟</span>

</div>

وقتی در پروژه نوشتیم:

```python
dns.resolver.resolve(
    domain,
    record_type,
)
```

---

کتابخانه:

```text
dnspython
```

به صورت پیش‌فرض از Resolver سیستم استفاده می‌کند.

---

بنابراین:

<div align='right' dir='rtl'>

```text
نتیجه Query
```

</div>

وابسته به تنظیمات DNS سیستم عامل است.

---

# مشاهده DNS فعلی در ویندوز

در PowerShell:

```powershell
ipconfig /all
```

---

یا:

```powershell
Get-DnsClientServerAddress
```

---

خروجی:

```text
DNS Servers
```

را نمایش می‌دهد.

---

# مشاهده DNS فعلی در لینوکس

مثال:

```bash
cat /etc/resolv.conf
```

---

نمونه:

```text
nameserver 8.8.8.8
```

---

# چرا این موضوع برای پروژه مهم است؟

گاهی یک Query در سیستم شما کار می‌کند اما در سیستم شخص دیگری نه.

---

دلیل می‌تواند:

<div align='right' dir='rtl'>

```text
Resolver متفاوت
```

</div>

باشد.

---

یا:

```text
DNS Filtering
```

در Provider مورد استفاده.

---

بنابراین هنگام عیب‌یابی DNS باید بدانیم:

<div align='right' dir='rtl'>

```text
از چه DNS Serverی استفاده می‌کنیم؟
```

</div>

---

# خلاصه

در این درس یاد گرفتیم:

<p dir='rtl'>
• DNS Provider چیست <br>
• Google DNS چیست <br>
• Cloudflare DNS چیست <br>
• Quad9 چیست <br>
• OpenDNS چیست <br>
• DNS over HTTPS چیست <br>
• DNS over TLS چیست <br>
• سیستم عامل چگونه DNS Resolver را انتخاب می‌کند <br>
• پروژه DNS Lookup از Resolver سیستم استفاده می‌کند
</p>

---

# درس بعدی

در درس بعدی وارد اولین بخش کاملاً عملی مرتبط با پروژه می‌شویم:

```text
DNS Lookup with Python
```

و یاد می‌گیریم:

<p dir='rtl'>
• کتابخانه dnspython چیست <br>
• چگونه DNS Query ارسال کنیم <br>
• چگونه A Record دریافت کنیم <br>
• چگونه MX و TXT را بخوانیم <br>
• چگونه نتایج را پردازش کنیم
</p>

همان چیزی که هسته اصلی ابزار DNS Lookup ما را تشکیل می‌دهد.
