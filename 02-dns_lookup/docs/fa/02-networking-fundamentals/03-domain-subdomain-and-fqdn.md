# درس 3: Domain, Subdomain و FQDN

## مقدمه

در درس قبل با IP Address آشنا شدیم.

اما انسان‌ها به خاطر سپردن آدرس‌هایی مثل:

```text
142.250.186.14
```

راحت نیستند.

به همین دلیل از نام‌های قابل فهم استفاده می‌کنیم:

```text
google.com
github.com
python.org
```

این نام‌ها توسط DNS به IP تبدیل می‌شوند.

برای درک بهتر DNS باید ابتدا با ساختار نام دامنه‌ها آشنا شویم.

---

<div align='right'>

# <span dir='rtl'>Domain چیست؟</span>

</div>

<p dir='rtl'>
Domain Name یک نام قابل خواندن برای انسان است که به یک یا چند IP اشاره می‌کند.
</p>

مثال:

```text
google.com
```

زمانی که این نام را وارد می‌کنیم:

```text
google.com
```

<p dir='rtl'>
DNS آن را به IP تبدیل می‌کند.
</p>

مثال:

```text
216.239.38.120
```

---

## چرا Domain اختراع شد؟

تصور کنید بخواهید آدرس همه سایت‌های دنیا را به شکل IP حفظ کنید:

```text
142.250.186.14
151.101.193.140
140.82.121.3
```

تقریباً غیرممکن است.

<p dir='rtl'>
Domain باعث می‌شود کاربران بتوانند به جای IP از نام‌های معنادار استفاده کنند.
</p>

---

# ساختار Domain

مثال:

```text
google.com
```

این نام از دو بخش تشکیل شده:

```text
google
com
```

---

<div align='right'>

## Top-Level Domain (TLD)

</div>

بخش آخر دامنه:

```text
.com
```

را:

```text
Top-Level Domain
```

یا به اختصار:

```text
TLD
```

می‌نامیم.

---

### نمونه TLDها

```text
.com
.org
.net
.edu
.gov
```

---

<div align='right'>

### <span dir='rtl'>TLDهای کشوری</span>

</div>

هر کشور نیز TLD مخصوص خود را دارد.

مثال:

```text
.ir
.uk
.de
.fr
.jp
```

---

نمونه:

```text
google.ir
bbc.co.uk
```

---

<div align='right'>

# Second-Level Domain

</div>

در دامنه:

```text
google.com
```

بخش:

```text
google
```

را Second-Level Domain می‌نامیم.

---

مثال:

```text
python.org
```

در اینجا:

```text
python
```

نام دامنه اصلی است.

---

<div align='right'>

# <span dir='rtl'>Subdomain چیست؟</span>

</div>

می‌توان زیرمجموعه‌هایی برای دامنه تعریف کرد.

مثال:

```text
mail.google.com
```

در اینجا:

```text
mail
```

یک Subdomain است.

---

ساختار:

```text
mail.google.com
│
├── Subdomain
├── Domain
└── TLD
```

---

## نمونه‌های رایج Subdomain

<div align='right'>

### Mail Server

</div>

```text
mail.google.com
```

---

<div align='right'>

### API Server

</div>

```text
api.example.com
```

---

<div align='right'>

### Documentation

</div>

```text
docs.python.org
```

---

<div align='right'>

### Blog

</div>

```text
blog.example.com
```

---

## آیا Subdomain محدودیت دارد؟

خیر.

می‌توان چندین سطح Subdomain داشت.

مثال:

```text
dev.api.example.com
```

---

ساختار:

```text
dev
api
example
com
```

---

<div align='right'>

# <span dir='rtl'>Root Domain چیست؟</span>

</div>

در رأس DNS چیزی وجود دارد به نام:

```text
Root Domain
```

که با:

```text
.
```

نمایش داده می‌شود.

در واقع:

```text
google.com.
```

فرم کامل دامنه است.

اما معمولاً نقطه پایانی نوشته نمی‌شود.

---

<div align='right'>

# <span dir='rtl'>FQDN چیست؟</span>

</div>

مخفف:

```text
Fully Qualified Domain Name
```

است.

یعنی نام دامنه کامل و دقیق.

مثال:

```text
mail.google.com.
```

این یک FQDN محسوب می‌شود.

---

## تفاوت Domain و FQDN

<p dir='rtl'>
Domain:
</p>

```text
google.com
```

---

<p dir='rtl'>
FQDN:
</p>

```text
mail.google.com.
```

---

<p dir='rtl'>
FQDN مسیر کامل را از Root DNS مشخص می‌کند.
</p>

---

# سلسله مراتب DNS

ساختار DNS شبیه یک درخت بزرگ است.

مثال:

```text
.
│
└── com
     │
     └── google
             │
             └── mail
```

---

برای دامنه:

```text
mail.google.com
```

مسیر به صورت زیر است:

```text
Root
↓
com
↓
google
↓
mail
```

---

# ارتباط با DNS Lookup

در پروژه ما:

```bash
python -m src.cli google.com A
```

ورودی:

```text
google.com
```

یک Domain است.

---

مثال دیگر:

```bash
python -m src.cli docs.python.org AAAA
```

در اینجا:

```text
docs
```

یک Subdomain است.

---

و:

```text
python.org
```

دامنه اصلی محسوب می‌شود.

---

# اعتبارسنجی دامنه در پروژه

در فایل:

```text
validator.py
```

تابعی نوشتیم:

```python
validate_domain()
```

که بررسی می‌کند:

<p dir='rtl'>
• ساختار دامنه معتبر باشد <br>
• حروف غیرمجاز وجود نداشته باشند <br>
• فرمت کلی صحیح باشد
</p>

---

نمونه معتبر:

```text
google.com
```

```text
docs.python.org
```

```text
mail.yahoo.com
```

---

نمونه نامعتبر:

```text
google
```

```text
.com
```

```text
!!!.com
```

```text
google..com
```

---

# دامنه و رکوردهای DNS

هر دامنه می‌تواند رکوردهای مختلفی داشته باشد.

مثال:

```text
google.com
```

ممکن است دارای:

```text
A
AAAA
MX
TXT
NS
```

باشد.

---

در واقع کاری که DNS Lookup انجام می‌دهد این است:

```text
Domain
↓
DNS Query
↓
Record Type
↓
Result
```

---

مثال:

```text
google.com
↓
MX
↓
Mail Servers
```

---

یا:

```text
google.com
↓
A
↓
IPv4 Address
```

---

# جمع‌بندی

در این درس یاد گرفتیم:

<p dir='rtl'>
• Domain چیست <br>
• TLD چیست <br>
• Second-Level Domain چیست <br>
• Subdomain چیست <br>
• Root Domain چیست <br>
• FQDN چیست <br>
• ساختار سلسله مراتبی DNS چگونه کار می‌کند <br>
• این مفاهیم چه ارتباطی با پروژه DNS Lookup دارند
</p>

---

# درس بعدی

در درس بعد وارد هسته واقعی DNS می‌شویم و یاد می‌گیریم:

<p dir='rtl'>
• DNS Record چیست <br>
• انواع رکوردهای DNS <br>
• رکوردهای A ،AAAA ،MX ،NS ،TXT و CNAME <br>
• هر رکورد چه کاربردی دارد
</p>

این درس مستقیماً به قابلیت‌های ابزار DNS Lookup مربوط است.
