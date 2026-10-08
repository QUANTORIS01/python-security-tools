# درس 08: DNS Records in Real-World Infrastructure

## مقدمه

در درس 04 با انواع رکوردهای DNS آشنا شدیم:

<p dir='rtl'>
• A <br>
• AAAA <br>
• MX <br>
• NS <br>
• TXT <br>
• CNAME
</p>

اما دانستن تعریف یک Record کافی نیست.

یک سؤال مهم وجود دارد:

<div align='right' dir='rtl'>

```text
این Recordها در دنیای واقعی چگونه استفاده می‌شوند؟
```

</div>

در این درس خواهیم دید که تقریباً هر سرویس اینترنتی که روزانه استفاده می‌کنیم بر پایه همین Recordها ساخته شده است.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>A Record در وب‌سایت‌ها</span>

</div>

رایج‌ترین استفاده DNS:

```text
Website Hosting
```

است.

---

فرض کنید دامنه:

```text
example.com
```

وجود دارد.

---

رکورد DNS:

```text
example.com
→
93.184.216.34
```

---

به شکل زیر ذخیره می‌شود:

```text
A Record
```

---

زمانی که مرورگر باز می‌شود:

```text
https://example.com
```

ابتدا DNS Query انجام می‌شود.

---

پاسخ:

```text
93.184.216.34
```

برگردانده می‌شود.

---

سپس مرورگر به آن IP متصل می‌شود.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>AAAA Record در سرویس‌های مدرن</span>

</div>

امروزه بسیاری از سرویس‌ها IPv6 ارائه می‌کنند.

---

مثال:

```text
google.com
```

---

ممکن است:

```text
2001:4860:4802:32::78
```

را برگرداند.

---

این اطلاعات در:

```text
AAAA Record
```

ذخیره می‌شوند.

---

شرکت‌هایی مانند:

<p dir='rtl'>
• Google <br>
• Cloudflare <br>
• Microsoft <br>
• Amazon
</p>

به طور گسترده از IPv6 استفاده می‌کنند.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>MX Record و سیستم ایمیل</span>

</div>

فرض کنید کاربری ایمیلی به آدرس زیر ارسال می‌کند:

```text
user@example.com
```

---

<p dir='rtl'>
Mail Server باید بداند ایمیل را به کجا تحویل دهد.
</p>

---

ابتدا DNS Query انجام می‌شود:

```text
MX Record
```

---

مثال:

```text
example.com
```

---

پاسخ:

```text
10 mail1.example.com
20 mail2.example.com
```

---

سپس ایمیل به Mail Server مناسب ارسال می‌شود.

---

# اولویت در MX Record

عدد اول:

```text
Priority
```

است.

---

مثال:

```text
10 mail1.example.com
20 mail2.example.com
```

---

سرور با عدد کمتر:

<div align='right' dir='rtl'>

```text
اولویت بالاتر
```

</div>

دارد.

---

اگر سرور اول در دسترس نباشد:

```text
mail2.example.com
```

استفاده می‌شود.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>NS Record و مدیریت DNS</span>

</div>

هر دامنه باید مشخص کند:

<div align='right' dir='rtl'>

```text
چه سرورهایی مسئول DNS آن هستند؟
```

</div>

---

مثال:

```text
example.com
```

---

ممکن است:

```text
ns1.example.com
ns2.example.com
```

را برگرداند.

---

این اطلاعات در:

```text
NS Record
```

ذخیره می‌شوند.

---

بدون NS Record:

```text
DNS Resolution
```

امکان‌پذیر نیست.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>TXT Record در امنیت ایمیل</span>

</div>

<p dir='rtl'>
TXT یکی از مهم‌ترین Recordهای امروزی است.
</p>

---

در گذشته:

<div align='right' dir='rtl'>

```text
فقط متن ساده
```

</div>

نگهداری می‌کرد.

---

امروزه:

```text
SPF
DKIM
DMARC
```

بر پایه TXT Record ساخته شده‌اند.

---

<div align='right' dir='rtl'>

# SPF

</div>

<p dir='rtl'>
SPF مشخص می‌کند:
</p>

<div align='right' dir='rtl'>

```text
چه سرورهایی
مجاز به ارسال ایمیل هستند.
```

</div>

---

نمونه:

```text
v=spf1 include:_spf.google.com ~all
```

---

این رکورد داخل:

```text
TXT Record
```

ذخیره می‌شود.

---

<div align='right' dir='rtl'>

# DKIM

</div>

<p dir='rtl'>
DKIM برای امضای دیجیتال ایمیل‌ها استفاده می‌شود.
</p>

---

کلید عمومی معمولاً در:

```text
TXT Record
```

قرار می‌گیرد.

---

هدف:

<div align='right' dir='rtl'>

```text
جلوگیری از جعل ایمیل
```

</div>

است.

---

<div align='right' dir='rtl'>

# DMARC

</div>

<p dir='rtl'>
DMARC سیاست‌های امنیت ایمیل را تعریف می‌کند.
</p>

---

نمونه:

```text
v=DMARC1; p=reject;
```

---

این رکورد نیز از نوع:

```text
TXT
```

است.

---

<div align='right' dir='rtl'>

# Domain Verification

</div>

بسیاری از سرویس‌های ابری از TXT استفاده می‌کنند.

---

مثال:

<p dir='rtl'>
• Google Workspace <br>
• Microsoft 365 <br>
• GitHub <br>
• Cloudflare
</p>

---

برای اثبات مالکیت دامنه.

---

نمونه:

```text
google-site-verification=
```

---

<div align='right' dir='rtl'>

# <span dir='rtl'>CNAME Record و CDNها</span>

</div>

یکی از رایج‌ترین استفاده‌های CNAME:

```text
CDN
```

است.

---

فرض کنید:

```text
www.example.com
```

---

به:

```text
cdn.provider.net
```

اشاره می‌کند.

---

این ارتباط از طریق:

```text
CNAME
```

انجام می‌شود.

---

# مزیت CNAME

به جای نگهداری مستقیم IP:

```text
Alias
```

ایجاد می‌شود.

---

اگر IP تغییر کند:

<div align='right' dir='rtl'>

```text
فقط مقصد اصلی تغییر می‌کند.
```

</div>

---

نیازی به تغییر همه رکوردها نیست.

---

# مثال Cloudflare

بسیاری از دامنه‌ها:

```text
www.example.com
```

را به:

```text
example.cloudflare.net
```

متصل می‌کنند.

---

این اتصال با:

```text
CNAME
```

انجام می‌شود.

---

# رکوردهای مورد استفاده در پروژه ما

ابزار DNS Lookup از این Recordها پشتیبانی می‌کند:

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

هر Record کاربرد واقعی خاص خود را دارد:

<div align='center'>

| Record | کاربرد |
|----------|----------|
| A | وب‌سایت‌ها |
| AAAA | IPv6 |
| MX | ایمیل |
| NS | مدیریت DNS |
| TXT | SPF / DKIM / DMARC |
| CNAME | CDN و Alias |

</div>

---

# ارتباط با پروژه

زمانی که کاربر اجرا می‌کند:

```bash
python -m src.cli google.com A
```

---

پروژه:

```python
lookup_record(
    "google.com",
    "A"
)
```

را اجرا می‌کند.

---

همین منطق برای:

```text
AAAA
MX
NS
TXT
CNAME
```

نیز استفاده می‌شود.

---

در نتیجه کاربر می‌تواند زیرساخت DNS یک دامنه را بررسی کند.

---

# خلاصه

در این درس یاد گرفتیم:

<p dir='rtl'>
• A Record در وب‌سایت‌ها چگونه استفاده می‌شود <br>
• AAAA Record چه کاربردی دارد <br>
• MX Record چگونه ایمیل را هدایت می‌کند <br>
• NS Record چه نقشی در DNS دارد <br>
• TXT Record چگونه در SPF و DKIM استفاده می‌شود <br>
• CNAME چگونه CDNها را پشتیبانی می‌کند <br>
• ارتباط این Recordها با ابزار DNS Lookup چیست
</p>

---

# درس بعدی

در درس بعدی به سراغ خطاها و پاسخ‌های DNS می‌رویم:

```text
DNS Errors and Failure Scenarios
```

و یاد می‌گیریم:

<p dir='rtl'>
• NXDOMAIN چیست <br>
• NoAnswer چیست <br>
• SERVFAIL چیست <br>
• Timeout چیست <br>
• NoNameservers چیست
</p>

همان خطاهایی که در فایل:

```text
resolver.py
```

پروژه مدیریت کرده‌ایم.
