# درس 5: DNS Query Process (فرآیند کامل درخواست DNS)

## مقدمه

تا اینجا یاد گرفتیم:

<p dir='rtl'>
• DNS چیست <br>
• Domain چیست <br>
• IP Address چیست <br>
• رکوردهای DNS چه هستند
</p>

اما هنوز یک سؤال مهم باقی مانده است:

<div align='right'>

```text
وقتی در مرورگر google.com را وارد می‌کنیم،
دقیقاً چه اتفاقی می‌افتد؟
```

</div>

---

<div align='right'>

# <span dir='rtl'>DNS Query چیست؟</span>

</div>

<p dir='rtl'>
DNS Query همان درخواستی است که برای پیدا کردن اطلاعات یک دامنه ارسال می‌شود.
</p>

مثال:

```text
google.com
```

---

در اینجا سیستم از DNS می‌پرسد:

<div align='right' sir='rtl'>

```text
IP Address مربوط به google.com چیست؟
```

</div>

---

این سؤال یک:

```text
DNS Query
```

است.

---

# هدف DNS Query

تبدیل:

```text
Domain Name
```

به:

```text
IP Address
```

یا سایر رکوردهای DNS.

---

مثال:

```text
google.com
```

↓

```text
216.239.38.120
```

---

# چه کسی Query را ارسال می‌کند؟

معمولاً:

<p dir='rtl'>
• Browser <br>
• Operating System <br>
• Application <br>
• Script
</p>

---

در پروژه ما:

```python
dns.resolver.resolve()
```

ارسال‌کننده Query است.

---

مثال:

```python
dns.resolver.resolve(
    "google.com",
    "A"
)
```

---

<div align='right'>

# <span dir='rtl'>Resolver چیست؟</span>

</div>

<p dir='rtl'>
Resolver یک مؤلفه نرم‌افزاری است که Query را ارسال می‌کند.
</p>

---

وظیفه Resolver:

<div align='right'>

```text
ارسال سؤال DNS
دریافت پاسخ
برگرداندن نتیجه
```

</div>

---

در پروژه:

```python
lookup_record()
```

روی Resolver کتابخانه dnspython ساخته شده است.

---

# مسیر کامل یک درخواست DNS

فرض کنیم کاربر وارد می‌کند:

```text
google.com
```

---

مراحل:

```text
Browser
    ↓
Operating System
    ↓
DNS Resolver
    ↓
DNS Server
    ↓
Answer
```

---

سپس IP برگردانده می‌شود.

---

<div align='right'>

# DNS Cache

</div>

قبل از ارسال Query جدید، سیستم Cache را بررسی می‌کند.

---

اگر پاسخ قبلاً ذخیره شده باشد:

<div align='right'>

```text
نیازی به Query جدید نیست
```

</div>

---

این باعث افزایش سرعت می‌شود.

---

# مثال واقعی

کاربر:

```text
google.com
```

را باز می‌کند.

---

سیستم ابتدا بررسی می‌کند:

<div align='right'>

```text
آیا پاسخ در Cache وجود دارد؟
```

</div>

---

اگر وجود داشته باشد:

<div align='right' dir='rtl'>

```text
IP مستقیماً استفاده می‌شود
```

</div>

---

اگر وجود نداشته باشد:

<div align='right' dir='rtl'>

```text
DNS Query ارسال می‌شود
```

</div>

---

<div align='right'>

# <span dir='rtl'>Recursive Query چیست؟</span>

</div>

رایج‌ترین نوع Query.

---

در Recursive Query:

<p dir='rtl'>
Resolver می‌گوید:
</p>

<div align='right' dir='rtl'>

```text
پاسخ نهایی را پیدا کن و به من برگردان
```

</div>

---

مثال:

<div align='right' dir='rtl'>

```text
IP google.com چیست؟
```

</div>

---

<p dir='rtl'>
Resolver انتظار دارد:
</p>

<div align='right' dir='rtl'>

```text
پاسخ نهایی
```

</div>

را دریافت کند.

---

<div align='right'>

# Recursive Resolution

</div>

در این حالت Resolver فقط یک سؤال می‌پرسد.

بقیه کارها را DNS Server انجام می‌دهد.

---

نمایش:

```text
Client
  ↓
Resolver
  ↓
DNS Infrastructure
  ↓
Final Answer
```

---

<div align='right'>

# <span dir='rtl'>Iterative Query چیست؟</span>

</div>

در Iterative Query پاسخ نهایی الزاماً داده نمی‌شود.

---

<p dir='rtl'>
Server ممکن است بگوید:
</p>

<div align='right'>

```text
من پاسخ را نمی‌دانم،
از این DNS Server بپرس.
```

</div>

---

سپس Resolver مرحله بعدی را ادامه می‌دهد.

---

# تفاوت Recursive و Iterative

<p dir='rtl'>
Recursive:
</p>

<div align='right'>

```text
پاسخ نهایی را برایم پیدا کن
```

</div>

---

<p dir='rtl'>
Iterative:
</p>

<div align='right'>

```text
اگر نمی‌دانی،
بگو از چه کسی بپرسم
```

</div>

---

# نقش Root DNS Server

وقتی هیچ اطلاعاتی وجود نداشته باشد:

<p dir='rtl'>
Resolver از Root Server شروع می‌کند.
</p>

---

<p dir='rtl'>
Root Server می‌گوید:
</p>

<div align='right'>

```text
برای .com
به TLD Server مراجعه کن
```

</div>

---

<div align='right'>

# <span dir='rtl'>TLD Server چیست؟</span>

</div>

<p dir='rtl'>
TLD یعنی:
</p>

```text
Top Level Domain
```

---

مثال:

```text
.com
.net
.org
```

---

<p dir='rtl'>
TLD Server مسئول این دامنه‌هاست.
</p>

---

# ادامه مسیر

برای:

```text
google.com
```

مسیر به شکل زیر است:

```text
Root
 ↓
.com TLD
 ↓
Google Name Server
 ↓
Answer
```

---

<div align='right'>

# <span dir='rtl'>Authoritative DNS Server چیست؟</span>

</div>

آخرین مرجع پاسخ.

---

این سرور مالک اطلاعات واقعی دامنه است.

---

مثال:

```text
ns1.google.com
```

---

پاسخ نهایی از این سرور دریافت می‌شود.

---

# مسیر کامل Resolution

```text
Client
 ↓
Resolver
 ↓
Root Server
 ↓
TLD Server
 ↓
Authoritative DNS
 ↓
Answer
```

---

# نمونه واقعی

کاربر:

```text
google.com
```

را درخواست می‌کند.

---

<p dir='rtl'>
Resolver:
</p>

<div align='right' dir='rtl'>

```text
IP google.com چیست؟
```

</div>

---

<p dir='rtl'>
Root:
</p>

<div align='right' dir='rtl'>

```text
از .com بپرس
```

</div>

---

<p dir='rtl'>
TLD:
</p>

<div align='right' dir='rtl'>

```text
از DNSهای گوگل بپرس
```

</div>

---

<p dir='rtl'>
Authoritative DNS:
</p>

```text
216.239.38.120
```

---

پاسخ به کاربر برمی‌گردد.

---

# ارتباط با پروژه

در فایل:

```python
resolver.py
```

کد زیر را داریم:

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

تمام مراحل Resolution را برای ما انجام می‌دهد.

---

ما فقط:

```python
google.com
```

و

```python
A
```

را ارسال می‌کنیم.

---

<p dir='rtl'>
Resolver:
</p>

<p dir='rtl'>
• Query می‌سازد <br>
• DNS Server را پیدا می‌کند <br>
• پاسخ را دریافت می‌کند <br>
• نتیجه را برمی‌گرداند
</p>

---

# چرا Timeout رخ می‌دهد؟

احتمالاً هنگام تست پروژه دیده‌ای:

```text
LifetimeTimeout
```

---

این یعنی:

<div align='right' dir='rtl'>

```text
Resolver در زمان مشخص
پاسخی دریافت نکرده است.
```

</div>

---

علل رایج:

<p dir='rtl'>
• DNS Server Down <br>
• Firewall <br>
• Network Issue <br>
• Packet Loss <br>
• Slow DNS Response
</p>

---

در پروژه این خطا را هندل کردیم:

```python
dns.resolver.LifetimeTimeout
```

---

# جمع‌بندی

در این درس یاد گرفتیم:

<p dir='rtl'>
• DNS Query چیست <br>
• Resolver چیست <br>
• Recursive Query چیست <br>
• Iterative Query چیست <br>
• Root DNS Server چیست <br>
• TLD Server چیست <br>
• Authoritative DNS Server چیست <br>
• مسیر کامل تبدیل Domain به IP چگونه انجام می‌شود <br>
• کتابخانه dnspython چگونه این فرآیند را برای ما انجام می‌دهد
</p>

---

# درس بعدی

در درس بعدی وارد یکی از مهم‌ترین مباحث DNS می‌شویم:

```text
DNS Caching & TTL
```

یعنی:

<p dir='rtl'>
• DNS Cache چیست <br>
• TTL چیست <br>
• چرا DNS سریع است <br>
• چگونه Cache روی عملکرد DNS اثر می‌گذارد <br>
• ارتباط TTL با امنیت و مدیریت DNS
</p>
