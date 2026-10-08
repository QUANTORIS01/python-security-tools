# درس 09: DNS Errors and Failure Scenarios

## مقدمه

وقتی یک DNS Query ارسال می‌کنیم همیشه قرار نیست پاسخ موفق دریافت کنیم.

در دنیای واقعی مشکلات مختلفی ممکن است رخ دهند:

<p dir='rtl'>
• دامنه وجود نداشته باشد <br>
• رکورد موردنظر وجود نداشته باشد <br>
• DNS Server پاسخ ندهد <br>
• ارتباط شبکه قطع باشد <br>
• Name Serverهای دامنه خراب باشند
</p>

به همین دلیل ابزارهای DNS باید بتوانند این شرایط را مدیریت کنند.

در پروژه DNS Lookup نیز ما دقیقاً همین کار را در فایل:

```text
resolver.py
```

انجام داده‌ایم.

---

<div align='right' dir='rtl'>

# DNS Success Response

</div>

موفق‌ترین حالت:

```text
google.com
→
216.239.38.120
```

است.

---

در این حالت:

```python
answers = dns.resolver.resolve(
    "google.com",
    "A"
)
```

با موفقیت اجرا می‌شود.

---

پاسخ:

```python
[
    "216.239.38.120"
]
```

خواهد بود.

---

<div align='right' dir='rtl'>

# NXDOMAIN

</div>

یکی از رایج‌ترین خطاهای DNS:

```text
NXDOMAIN
```

است.

---

مخفف:

```text
Non-Existent Domain
```

است.

---

یعنی:

<div align='right' dir='rtl'>

```text
این دامنه وجود ندارد.
```

</div>

---

مثال:

```text
this-domain-does-not-exist-12345.com
```

---

در این حالت:

```python
dns.resolver.NXDOMAIN
```

ایجاد می‌شود.

---

در پروژه:

```python
except dns.resolver.NXDOMAIN:
```

را مدیریت کرده‌ایم.

---

# تفاوت NXDOMAIN با NoAnswer

بسیاری از افراد این دو را اشتباه می‌گیرند.

---

<p dir='rtl'>
NXDOMAIN:
</p>

<div align='right' dir='rtl'>

```text
دامنه وجود ندارد.
```

</div>

---

مثال:

```text
fake-domain-xyz.com
```

---

اما:

```text
NoAnswer
```

یعنی:

<div align='right' dir='rtl'>

```text
دامنه وجود دارد
اما آن رکورد خاص وجود ندارد.
```

</div>

---

مثال:

```text
google.com
```

وجود دارد.

---

اما:

```text
CNAME
```

ممکن است نداشته باشد.

---

در این حالت:

```python
dns.resolver.NoAnswer
```

رخ می‌دهد.

---

<div align='right' dir='rtl'>

# NoAnswer

</div>

نمونه:

```python
dns.resolver.resolve(
    "google.com",
    "CNAME"
)
```

---

اگر رکوردی وجود نداشته باشد:

```python
dns.resolver.NoAnswer
```

ایجاد می‌شود.

---

در پروژه:

```python
except dns.resolver.NoAnswer:
```

مدیریت شده است.

---

و خروجی:

```python
[]
```

برگردانده می‌شود.

---

<div align='right' dir='rtl'>

# Timeout

</div>

گاهی DNS Server پاسخ نمی‌دهد.

---

مثال:

```text
Network Problem
```

یا:

```text
Server Overloaded
```

---

در این حالت Query برای مدتی منتظر می‌ماند.

---

اگر پاسخی دریافت نشود:

```python
dns.resolver.LifetimeTimeout
```

رخ می‌دهد.

---

این همان خطایی بود که هنگام تست دستی پروژه مشاهده کردی:

```text
The resolution lifetime expired
```

---

# چرا Timeout مهم است؟

اگر این خطا مدیریت نشود:

<div align='right' dir='rtl'>

```text
برنامه Crash می‌کند.
```

</div>

---

به همین دلیل در پروژه:

```python
except dns.resolver.LifetimeTimeout:
```

را اضافه کردیم.

---

<div align='right' dir='rtl'>

# NoNameservers

</div>

گاهی دامنه وجود دارد اما Name Serverهای آن پاسخگو نیستند.

---

مثال:

```text
Broken DNS Configuration
```

---

یا:

```text
Name Servers Offline
```

---

در این شرایط:

```python
dns.resolver.NoNameservers
```

رخ می‌دهد.

---

در پروژه نیز این Exception را مدیریت کرده‌ایم.

---

<div align='right' dir='rtl'>

# SERVFAIL

</div>

یکی دیگر از پاسخ‌های DNS:

```text
SERVFAIL
```

است.

---

معنی:

```text
Server Failure
```

---

یعنی DNS Server تلاش کرده پاسخ را پیدا کند اما موفق نشده است.

---

مثال:

```text
Resolver Error
```

یا:

```text
Upstream Failure
```

---

بسیاری از Resolverها این خطا را به شکل:

```python
NoNameservers
```

یا خطاهای مشابه نمایش می‌دهند.

---

<div align='right' dir='rtl'>

# REFUSED

</div>

برخی DNS Serverها درخواست را رد می‌کنند.

---

مثال:

```text
Access Denied
```

---

در این حالت پاسخ:

```text
REFUSED
```

است.

---

معمولاً در DNS Serverهای خصوصی مشاهده می‌شود.

---

<div align='right' dir='rtl'>

# DNS Failure Flow

</div>

یک DNS Query می‌تواند به شکل زیر پایان یابد:

```text
DNS Query
    │
    ├── Success
    │
    ├── NXDOMAIN
    │
    ├── NoAnswer
    │
    ├── Timeout
    │
    ├── NoNameservers
    │
    └── SERVFAIL
```

---

# مدیریت خطاها در پروژه

در فایل:

```python
resolver.py
```

ما نوشتیم:

```python
except (
    dns.resolver.NXDOMAIN,
    dns.resolver.NoAnswer,
    dns.resolver.NoNameservers,
    dns.resolver.LifetimeTimeout,
):
    return []
```

---

هدف:

<div align='right' dir='rtl'>

```text
جلوگیری از Crash شدن برنامه
```

</div>

است.

---

در نتیجه:

```bash
python -m src.cli google.com MX
```

به جای نمایش Traceback:

```text
No DNS records found.
```

نمایش داده می‌شود.

---

# چرا این طراحی خوب است؟

زیرا:

<p dir='rtl'>
• برنامه پایدار می‌ماند <br>
• کاربر خطاهای داخلی Python را نمی‌بیند <br>
• تجربه کاربری بهتر می‌شود <br>
• ابزار حرفه‌ای‌تر رفتار می‌کند
</p>

---

# ارتباط با تست‌ها

برای هر خطا تست جداگانه نوشتیم:

```python
test_lookup_record_handles_nxdomain()
```

---

```python
test_lookup_record_handles_no_answer()
```

---

```python
test_lookup_record_handles_timeout()
```

---

این تست‌ها تضمین می‌کنند که برنامه در شرایط خطا نیز رفتار صحیحی دارد.

---

# خلاصه

در این درس یاد گرفتیم:

<p dir='rtl'>
• NXDOMAIN چیست <br>
• NoAnswer چیست <br>
• Timeout چیست <br>
• NoNameservers چیست <br>
• SERVFAIL چیست <br>
• تفاوت NXDOMAIN و NoAnswer چیست <br>
• چرا مدیریت Exceptionها اهمیت دارد <br>
• پروژه DNS Lookup چگونه این خطاها را مدیریت می‌کند
</p>

---

# درس بعدی

در درس بعدی با DNS Serverهای عمومی آشنا می‌شویم:

```text
Public DNS Providers
```

و بررسی می‌کنیم:

<p dir='rtl'>
• Google DNS <br>
• Cloudflare DNS <br>
• Quad9 <br>
• OpenDNS
</p>

چه تفاوت‌هایی با یکدیگر دارند و Resolver سیستم ما معمولاً از کدام استفاده می‌کند.
