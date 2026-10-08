# درس 11: DNS Lookup with Python

## مقدمه

تا اینجا تمام مفاهیم موردنیاز DNS را یاد گرفتیم:

<p dir='rtl'>
• DNS چیست <br>
• Domain چیست <br>
• DNS Query چگونه انجام می‌شود <br>
• DNS Recordها چه هستند <br>
• Recursive Resolver چیست <br>
• Public DNS Providerها چه هستند
</p>

اکنون وقت آن رسیده که وارد بخش عملی شویم.

در این درس یاد می‌گیریم چگونه با Python یک DNS Query واقعی انجام دهیم.

این دقیقاً همان دانشی است که برای ساخت ابزار:

```text
DNS Lookup Tool
```

از آن استفاده کرده‌ایم.

---

# چرا Python برای DNS مناسب است؟

<p dir='rtl'>
Python کتابخانه‌های متعددی برای کار با DNS دارد.
</p>

مشهورترین آن‌ها:

```text
dnspython
```

است.

---

این کتابخانه امکان:

<p dir='rtl'>
• ارسال DNS Query <br>
• دریافت پاسخ <br>
• کار با Recordهای مختلف <br>
• مدیریت خطاهای DNS
</p>

را فراهم می‌کند.

---

# نصب dnspython

در محیط مجازی:

```bash
pip install dnspython
```

---

سپس می‌توانیم آن را import کنیم:

```python
import dns.resolver
```

---

# اولین DNS Query

نمونه:

```python
import dns.resolver

answers = dns.resolver.resolve(
    "google.com",
    "A",
)
```

---

در این مثال:

```text
google.com
```

دامنه هدف است.

---

و:

```text
A
```

نوع رکورد موردنظر است.

---

# خواندن پاسخ

پاسخ یک لیست از Answerها است.

---

برای نمایش آن:

```python
for answer in answers:
    print(answer)
```

---

نمونه خروجی:

```text
216.239.38.120
```

---

یا:

```text
142.250.185.14
```

---

بسته به زمان و موقعیت جغرافیایی ممکن است IP متفاوت باشد.

---

# دریافت AAAA Record

مثال:

```python
answers = dns.resolver.resolve(
    "google.com",
    "AAAA",
)
```

---

خروجی:

```text
2001:4860:4802:32::78
```

---

این یک آدرس IPv6 است.

---

# دریافت MX Record

مثال:

```python
answers = dns.resolver.resolve(
    "google.com",
    "MX",
)
```

---

نمایش:

```python
for answer in answers:
    print(answer)
```

---

نمونه خروجی:

```text
10 smtp.google.com.
```

---

یا چند رکورد مختلف.

---

# دریافت NS Record

مثال:

```python
answers = dns.resolver.resolve(
    "google.com",
    "NS",
)
```

---

نمونه خروجی:

```text
ns1.google.com.
ns2.google.com.
ns3.google.com.
```

---

این‌ها Authoritative Name Serverهای دامنه هستند.

---

# دریافت TXT Record

مثال:

```python
answers = dns.resolver.resolve(
    "google.com",
    "TXT",
)
```

---

خروجی ممکن است شامل:

```text
SPF
Site Verification
Security Records
```

باشد.

---

# تبدیل پاسخ‌ها به رشته

در پروژه ما:

```python
[str(answer) for answer in answers]
```

استفاده شده است.

---

مثال:

```python
records = [
    str(answer)
    for answer in answers
]
```

---

خروجی:

```python
[
    "216.239.38.120"
]
```

---

این دقیقاً همان کاری است که در فایل:

```text
resolver.py
```

انجام داده‌ایم.

---

# تابع lookup_record

در پروژه:

```python
def lookup_record(
    domain,
    record_type,
):
```

---

وظیفه دارد:

```text
DNS Query
↓
Process Results
↓
Return List[str]
```

را انجام دهد.

---

نمونه:

```python
lookup_record(
    "google.com",
    "A",
)
```

---

خروجی:

```python
[
    "216.239.38.120"
]
```

---

# مدیریت خطاها

همیشه Query موفق نیست.

---

مثال:

```python
dns.resolver.resolve(
    "fake-domain.xyz",
    "A",
)
```

---

ممکن است:

```python
dns.resolver.NXDOMAIN
```

ایجاد کند.

---

بنابراین:

```python
try:
    ...
except:
    ...
```

ضروری است.

---

# مدیریت NXDOMAIN

نمونه:

```python
try:
    answers = dns.resolver.resolve(
        domain,
        record_type,
    )
except dns.resolver.NXDOMAIN:
    return []
```

---

# مدیریت NoAnswer

نمونه:

```python
except dns.resolver.NoAnswer:
    return []
```

---

این حالت زمانی رخ می‌دهد که:

<div align='right' dir='rtl'>

```text
دامنه وجود دارد
اما رکورد موردنظر وجود ندارد.
```

</div>

---

# مدیریت Timeout

نمونه:

```python
except dns.resolver.LifetimeTimeout:
    return []
```

---

این دقیقاً همان مشکلی بود که هنگام تست دستی پروژه مشاهده کردیم.

---

# طراحی حرفه‌ای

در ابزارهای واقعی:

```text
Exception
↓
Logging
↓
Graceful Handling
```

انجام می‌شود.

---

نه اینکه برنامه Crash کند.

---

به همین دلیل پروژه ما:

```python
[]
```

برمی‌گرداند.

---

و سپس:

```text
No DNS records found.
```

نمایش داده می‌شود.

---

# ارتباط با build_dns_results

در پروژه:

```python
lookup_record()
```

فقط داده خام برمی‌گرداند.

---

سپس:

```python
build_dns_results()
```

آن داده‌ها را به:

```python
DNSRecord
```

تبدیل می‌کند.

---

مثال:

```python
DNSRecord(
    domain="google.com",
    record_type="A",
    value="216.239.38.120",
)
```

---

این همان معماری چندلایه‌ای است که در Port Scanner نیز استفاده کردیم.

---

# ارتباط با CLI

کاربر اجرا می‌کند:

```bash
python -m src.cli google.com A
```

---

سپس:

```text
CLI
 ↓
build_dns_results()
 ↓
lookup_record()
 ↓
dnspython
 ↓
DNS Resolver
```

---

و پاسخ نهایی به کاربر نمایش داده می‌شود.

---

# خلاصه

در این درس یاد گرفتیم:

<p dir='rtl'>
• dnspython چیست <br>
• چگونه DNS Query انجام دهیم <br>
• چگونه A Record بخوانیم <br>
• چگونه AAAA Record بخوانیم <br>
• چگونه MX Record بخوانیم <br>
• چگونه NS Record بخوانیم <br>
• چگونه TXT Record بخوانیم <br>
• چگونه خطاها را مدیریت کنیم <br>
• پروژه DNS Lookup چگونه از dnspython استفاده می‌کند
</p>

---

# پایان فصل دوم

با پایان این درس، فصل:

```text
Networking Fundamentals
```

به پایان می‌رسد.

در این فصل یاد گرفتیم:

<p dir='rtl'>
• اینترنت چگونه کار می‌کند <br>
• IP Address چیست <br>
• Domain و FQDN چیست <br>
• DNS چیست <br>
• DNS Recordها چه هستند <br>
• DNS Query چگونه انجام می‌شود <br>
• DNS Cache چیست <br>
• Recursive Resolver چیست <br>
• DNS Providerها چه هستند <br>
• DNS Lookup چگونه در Python پیاده‌سازی می‌شود
</p>

---

# فصل بعدی

در فصل بعد وارد:

```text
Cybersecurity Fundamentals
```

می‌شویم.

و با مفاهیمی آشنا خواهیم شد که مستقیماً در ابزارهای امنیتی استفاده می‌شوند:

<p dir='rtl'>
• CIA Triad <br>
• Threats <br>
• Vulnerabilities <br>
• Reconnaissance <br>
• Enumeration <br>
• Attack Surface <br>
• Defense in Depth <br>
• Security Controls
</p>

و بسیاری از مفاهیم پایه‌ای دنیای امنیت سایبری.
