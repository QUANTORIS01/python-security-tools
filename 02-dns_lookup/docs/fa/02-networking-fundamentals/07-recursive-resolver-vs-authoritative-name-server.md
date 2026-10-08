# درس 07: Recursive Resolver vs Authoritative Name Server

## مقدمه

تا اینجا یاد گرفتیم:

<p dir='rtl'>
• DNS چیست <br>
• DNS Record چیست <br>
• DNS Query چگونه انجام می‌شود <br>
• Cache و TTL چگونه کار می‌کنند
</p>

اما هنوز یک سؤال مهم باقی مانده است:

<div align='right' dir='rtl'>

```text
چه کسی پاسخ نهایی DNS را تولید می‌کند؟
```

</div>

و

<div align='right' dir='rtl'>

```text
چه کسی آن پاسخ را برای ما پیدا می‌کند؟
```

</div>

برای پاسخ به این سؤال باید با دو مفهوم بسیار مهم آشنا شویم:

```text
Recursive Resolver
```

و

```text
Authoritative Name Server
```

---

<div align='right' dir='rtl'>

# <span dir='rtl'>DNS Query را چه کسی انجام می‌دهد؟</span>

</div>

فرض کنیم کاربر در مرورگر وارد می‌کند:

```text
google.com
```

مرورگر خودش نمی‌تواند مستقیماً تمام DNS اینترنت را جستجو کند.

بنابراین درخواست را به یک DNS Resolver ارسال می‌کند.

---

مثال:

```text
Client
  ↓
8.8.8.8
```

---

در این مثال:

```text
8.8.8.8
```

یک Resolver است.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Recursive Resolver چیست؟</span>

</div>

<p dir='rtl'>
Recursive Resolver سیستمی است که مسئول پیدا کردن پاسخ DNS برای کاربر است.
</p>

---

وظیفه آن:

<div align='right' dir='rtl'>

```text
پاسخ را پیدا کن
و به کاربر برگردان
```

</div>

است.

---

کاربر فقط یک درخواست ارسال می‌کند:

```text
google.com
```

---

<p dir='rtl'>
Resolver خودش تمام مراحل بعدی را انجام می‌دهد.
</p>

---

# چرا به آن Recursive می‌گویند؟

زیرا Resolver به صورت مرحله به مرحله در اینترنت جستجو می‌کند تا به پاسخ نهایی برسد.

---

مثال:

```text
Client
 ↓
Resolver
 ↓
Root Server
 ↓
TLD Server
 ↓
Authoritative Server
 ↓
Answer
```

---

تمام این مراحل توسط Resolver انجام می‌شود.

---

کاربر فقط نتیجه نهایی را دریافت می‌کند.

---

# نمونه Recursive Resolverها

مشهورترین Resolverهای عمومی:

<div align='right' dir='rtl'>

### Google DNS

</div>

```text
8.8.8.8
8.8.4.4
```

---

<div align='right' dir='rtl'>

### Cloudflare DNS

</div>

```text
1.1.1.1
1.0.0.1
```

---

<div align='right' dir='rtl'>

### Quad9

</div>

```text
9.9.9.9
```

---

<div align='right' dir='rtl'>

### OpenDNS

</div>

```text
208.67.222.222
```

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Authoritative Name Server چیست؟</span>

</div>

<p dir='rtl'>
Authoritative Server منبع اصلی اطلاعات DNS یک دامنه است.
</p>

---

اگر بخواهیم بدانیم:

```text
google.com
```

چه IPای دارد،

در نهایت باید از سروری سؤال کنیم که مالک اطلاعات DNS آن دامنه است.

---

آن سرور:

```text
Authoritative Name Server
```

نام دارد.

---

# مثال

فرض کنید دامنه:

```text
example.com
```

وجود دارد.

---

ممکن است Name Serverهای آن:

```text
ns1.example.com
ns2.example.com
```

باشند.

---

این سرورها رکوردهای واقعی دامنه را نگهداری می‌کنند.

---

مثال:

```text
example.com
→
93.184.216.34
```

---

این اطلاعات در Authoritative Server ذخیره شده‌اند.

---

# تفاوت Resolver و Authoritative Server

بسیاری از افراد این دو را با هم اشتباه می‌گیرند.

---

<p dir='rtl'>
Resolver:
</p>

<div align='right' dir='rtl'>

```text
دنبال پاسخ می‌گردد.
```

</div>

---

<p dir='rtl'>
Authoritative Server:
</p>

<div align='right' dir='rtl'>

```text
مالک پاسخ است.
```

</div>

---

به عبارت دیگر:

```text
Resolver = Finder
Authoritative = Source
```

---

# مثال واقعی

کاربر:

```text
google.com
```

را درخواست می‌کند.

---

<p dir='rtl'>
Resolver:
</p>

```text
8.8.8.8
```

شروع به جستجو می‌کند.

---

در نهایت به Name Serverهای Google می‌رسد.

---

آن Name Serverها می‌گویند:

```text
google.com
=
216.239.38.120
```

---

سپس Resolver پاسخ را به کاربر بازمی‌گرداند.

---

# نقش Cache در Resolver

اکثر Resolverها Cache دارند.

---

مثال:

```text
google.com
```

قبلاً درخواست شده است.

---

<p dir='rtl'>
Resolver پاسخ را ذخیره می‌کند.
</p>

---

در درخواست بعدی:

<div align='right' dir='rtl'>

```text
بدون مراجعه به اینترنت
```

</div>

پاسخ را از Cache برمی‌گرداند.

---

این کار باعث:

<p dir='rtl'>
• افزایش سرعت <br>
• کاهش ترافیک <br>
• کاهش بار DNS
</p>

می‌شود.

---

# آیا Authoritative Server هم Cache دارد؟

ممکن است برخی کش‌های داخلی داشته باشد.

اما وظیفه اصلی آن:

<div align='right' dir='rtl'>

```text
نگهداری رکوردهای اصلی
```

</div>

است.

---

برخلاف Resolver که تمرکز آن روی:

```text
Caching
```

است.

---

# ارتباط با پروژه DNS Lookup

در پروژه ما:

```python
dns.resolver.resolve(
    domain,
    record_type,
)
```

استفاده می‌شود.

---

کتابخانه:

```text
dnspython
```

در پشت صحنه از Resolver سیستم استفاده می‌کند.

---

<p dir='rtl'>
Resolver سیستم ممکن است:
</p>

<p dir='rtl'>
• Resolver محلی <br>
• Resolver شرکت ارائه‌دهنده اینترنت <br>
• Google DNS <br>
• Cloudflare DNS
</p>

باشد.

---

ابزار ما مستقیماً با Authoritative Server صحبت نمی‌کند.

---

بلکه از Resolver موجود استفاده می‌کند.

---

# چرا این موضوع مهم است؟

زیرا هنگام عیب‌یابی DNS باید بدانیم:

<div align='right' dir='rtl'>

```text
مشکل از Resolver است؟
```

</div>

یا

<div align='right' dir='rtl'>

```text
مشکل از Authoritative Server است؟
```

</div>

---

این دو سناریو کاملاً متفاوت هستند.

---

# خلاصه

در این درس یاد گرفتیم:

<p dir='rtl'>
• Recursive Resolver چیست <br>
• Authoritative Name Server چیست <br>
• تفاوت آن‌ها چیست <br>
• Resolver چگونه پاسخ را پیدا می‌کند <br>
• Authoritative Server چگونه پاسخ را نگهداری می‌کند <br>
• نقش Cache در Resolver چیست <br>
• پروژه DNS Lookup از کدام بخش استفاده می‌کند
</p>

---

# درس بعدی

در درس بعدی بررسی می‌کنیم که رکوردهای DNS در دنیای واقعی چگونه استفاده می‌شوند:

```text
DNS Records in Real-World Infrastructure
```

و خواهیم دید:

<p dir='rtl'>
• وب‌سایت‌ها چگونه از A Record استفاده می‌کنند <br>
• سرویس‌های ایمیل چگونه از MX استفاده می‌کنند <br>
• CDNها چگونه از CNAME استفاده می‌کنند <br>
• SPF و DKIM چگونه از TXT استفاده می‌کنند
</p>
