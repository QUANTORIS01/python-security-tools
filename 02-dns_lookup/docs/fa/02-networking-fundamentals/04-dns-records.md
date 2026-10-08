# درس 4: DNS Records (رکوردهای DNS)

## مقدمه

تا اینجا یاد گرفتیم که DNS وظیفه تبدیل نام دامنه به اطلاعات قابل استفاده را بر عهده دارد.

اما DNS فقط برای پیدا کردن IP یک سایت نیست.

هر دامنه می‌تواند اطلاعات مختلفی را در DNS ذخیره کند.

این اطلاعات در قالب:

```text
DNS Records
```

ذخیره می‌شوند.

---

<div align='right'>

# <span dir='rtl'>DNS Record چیست؟</span>

</div>

<p dir='rtl'>
DNS Record یک رکورد اطلاعاتی است که روی DNS Server ذخیره می‌شود.
</p>

هر رکورد نوع خاصی از اطلاعات را نگهداری می‌کند.

مثال:

```text
google.com
```

ممکن است رکوردهای زیر را داشته باشد:

```text
A
AAAA
MX
NS
TXT
CNAME
```

هر کدام کاربرد متفاوتی دارند.

---

# ساختار کلی رکورد DNS

به صورت ساده:

```text
NAME    TYPE    VALUE
```

مثال:

```text
google.com    A      216.239.38.120
```

---

در اینجا:

```text
NAME
```

دامنه است.

---

```text
TYPE
```

نوع رکورد است.

---

```text
VALUE
```

مقدار رکورد است.

---

# رکورد A

رایج‌ترین رکورد DNS است.

<p dir='rtl'>
A مخفف:
</p>

```text
Address
```

است.

این رکورد دامنه را به یک IPv4 Address متصل می‌کند.

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

نمایش رکورد:

```text
google.com    A    216.239.38.120
```

---

در پروژه ما:

```bash
python -m src.cli google.com A
```

دقیقاً همین رکورد را درخواست می‌کنیم.

---

# رکورد AAAA

این رکورد مشابه A است.

اما برای IPv6 استفاده می‌شود.

---

مثال:

```text
google.com
```

↓

```text
2001:4860:4802:32::78
```

---

نمایش:

```text
google.com    AAAA    2001:4860:4802:32::78
```

---

در پروژه:

```bash
python -m src.cli google.com AAAA
```

---

# تفاوت A و AAAA

<p dir='rtl'>
A:
</p>

```text
IPv4
```

مثال:

```text
8.8.8.8
```

---

<p dir='rtl'>
AAAA:
</p>

```text
IPv6
```

مثال:

```text
2001:4860:4860::8888
```

---

# رکورد MX

<p dir='rtl'>
MX مخفف:
</p>

```text
Mail Exchange
```

است.

---

این رکورد مشخص می‌کند ایمیل‌های یک دامنه به کدام Mail Server ارسال شوند.

---

مثال:

```text
google.com
```

↓

```text
smtp.google.com
```

---

نمونه واقعی:

```text
gmail.com MX alt1.gmail-smtp-in.l.google.com
```

---

کاربرد:

```text
Email Delivery
```

---

در پروژه:

```bash
python -m src.cli google.com MX
```

---

<div align='right'>

# <span dir='rtl'>Priority در رکورد MX</span>

</div>

رکوردهای MX معمولاً دارای اولویت هستند.

مثال:

```text
10 mail1.example.com
20 mail2.example.com
```

---

عدد کمتر:

```text
اولویت بیشتر
```

---

بنابراین:

```text
10
```

قبل از:

```text
20
```

استفاده می‌شود.

---

# رکورد NS

<p dir='rtl'>
NS مخفف:
</p>

```text
Name Server
```

است.

---

این رکورد مشخص می‌کند چه DNS Serverهایی مسئول پاسخگویی به دامنه هستند.

---

مثال:

```text
google.com
```

↓

```text
ns1.google.com
ns2.google.com
```

---

نمایش:

```text
google.com NS ns1.google.com
```

---

کاربرد:

```text
Delegation
```

و مدیریت DNS دامنه.

---

در پروژه:

```bash
python -m src.cli google.com NS
```

---

# رکورد TXT

<p dir='rtl'>
TXT برای ذخیره متن دلخواه استفاده می‌شود.
</p>

---

مثال:

```text
google.com TXT "verification-code"
```

---

امروزه کاربردهای مهمی دارد:

---

<div align='right'>

## SPF

</div>

جلوگیری از جعل ایمیل

---

مثال:

```text
v=spf1 include:_spf.google.com ~all
```

---

<div align='right'>

## DKIM

</div>

اعتبارسنجی امضای ایمیل

---

<div align='right'>

## Domain Verification

</div>

اثبات مالکیت دامنه

---

مثال:

```text
google-site-verification=abc123
```

---

در پروژه:

```bash
python -m src.cli google.com TXT
```

---

# رکورد CNAME

<p dir='rtl'>
CNAME مخفف:
</p>

```text
Canonical Name
```

است.

---

برای ایجاد Alias استفاده می‌شود.

---

مثال:

```text
www.example.com
```

↓

```text
example.com
```

---

نمایش:

```text
www.example.com CNAME example.com
```

---

یعنی:

```text
www.example.com
```

نام مستعار:

```text
example.com
```

است.

---

در پروژه:

```bash
python -m src.cli www.example.com CNAME
```

---

# چرا CNAME مهم است؟

فرض کنید IP اصلی سایت تغییر کند.

اگر از CNAME استفاده شده باشد:

```text
www.example.com
```

به صورت خودکار مقصد جدید را دنبال می‌کند.

---

# مقایسه رکوردها

<div align='center'>

| Record | Purpose |
|----------|----------|
| A | IPv4 Address |
| AAAA | IPv6 Address |
| MX | Mail Server |
| NS | Name Server |
| TXT | Text Information |
| CNAME | Alias |

</div>

---

# ارتباط مستقیم با پروژه

در فایل:

```python
validator.py
```

رکوردهای مجاز را تعریف کردیم:

```python
SUPPORTED_RECORD_TYPES
```

---

مقادیر:

```python
{
    "A",
    "AAAA",
    "MX",
    "NS",
    "TXT",
    "CNAME",
}
```

---

تابع:

```python
validate_record_type()
```

بررسی می‌کند فقط همین رکوردها پذیرفته شوند.

---

در فایل:

```python
resolver.py
```

نوع رکورد مستقیماً به DNS Resolver ارسال می‌شود:

```python
lookup_record(
    domain,
    record_type,
)
```

---

بنابراین:

```bash
python -m src.cli google.com MX
```

و

```bash
python -m src.cli google.com A
```

در واقع دو Query کاملاً متفاوت به DNS ارسال می‌کنند.

---

# چرا بعضی Queryها نتیجه نمی‌دهند؟

احتمالاً هنگام تست دیده‌ای:

```bash
python -m src.cli google.com MX
```

گاهی:

```text
No DNS records found.
```

نمایش داده می‌شود.

---

علت می‌تواند یکی از موارد زیر باشد:

<p dir='rtl'>
• Timeout <br>
• DNS Server Failure <br>
• No Answer <br>
• Resolver Misconfiguration <br>
• Network Issues
</p>

---

در پروژه این موارد را در:

```python
resolver.py
```

هندل کردیم.

---

# جمع‌بندی

در این درس یاد گرفتیم:

<p dir='rtl'>
• DNS Record چیست <br>
• رکورد A چیست <br>
• رکورد AAAA چیست <br>
• رکورد MX چیست <br>
• رکورد NS چیست <br>
• رکورد TXT چیست <br>
• رکورد CNAME چیست <br>
• هر رکورد چه کاربردی دارد <br>
• این رکوردها چگونه در پروژه DNS Lookup استفاده می‌شوند
</p>

---

# درس بعدی

در درس بعدی یاد می‌گیریم:

<p dir='rtl'>
• DNS Query چیست <br>
• Recursive Query <br>
• Iterative Query <br>
• Resolver چگونه کار می‌کند <br>
• مسیر کامل یک درخواست DNS از مرورگر تا DNS Server
</p>

این درس یکی از مهم‌ترین بخش‌های Networking Fundamentals است.
