<div align='right'>

[🇬🇧 English](./README.md)

</div>

# ابزار DNS Lookup

یک ابزار سبک برای جست‌وجوی رکوردهای DNS که با پایتون نوشته شده است و برای یادگیری، آزمایش، خودکارسازی و گردش‌کارهای مرتبط با امنیت طراحی شده است.

این پروژه بر معماری تمیز، نتایج ساختاریافتهٔ DNS، تست خودکار، ثبت گزارش و قابلیت‌های خروجی‌گرفتن تمرکز دارد؛ در عین حال، ساختار آن به‌اندازه‌ای ساده است که بتوان آن را مطالعه و توسعه داد.

> **سلب مسئولیت:** این ابزار صرفاً برای اهداف آموزشی، مدیریتی و فعالیت‌های امنیتی مجاز در نظر گرفته شده است.

---

## مستندات

این پروژه دارای مستندات دوزبانه است:

<p dir='rtl'>
• مستندات انگلیسی <br>
• مستندات فارسی
</p>

مسیر آموزشی فارسی شامل بخش‌های زیر است:

<p dir='rtl'>
• مبانی پایتون <br>
• مبانی شبکه <br>
• مبانی DNS <br>
• مبانی امنیت سایبری <br>
• تحلیل گام‌به‌گام کد منبع
</p>

---

## قابلیت‌ها

<div align='right' dir="rtl">

<span dir='rtl'>• جست‌وجوی رکوردهای DNS</span> <br>
<span dir='rtl'>• پشتیبانی از رکوردهای `A`</span> <br>
<span dir='rtl'>• پشتیبانی از رکوردهای `AAAA`</span> <br>
<span dir='rtl'>• پشتیبانی از رکوردهای `MX`</span> <br>
<span dir='rtl'>• پشتیبانی از رکوردهای `NS`</span> <br>
<span dir='rtl'>• پشتیبانی از رکوردهای `TXT`</span> <br>
<span dir='rtl'>• پشتیبانی از رکوردهای `CNAME`</span> <br>
<span dir='rtl'>• اعتبارسنجی دامنه</span> <br>
<span dir='rtl'>• اعتبارسنجی نوع رکورد DNS</span> <br>
<span dir='rtl'>• نتایج ساختاریافتهٔ DNS با استفاده از `dataclass`های پایتون</span> <br>
<span dir='rtl'>• نمایش خوانا در ترمینال</span> <br>
<span dir='rtl'>• خروجی‌گرفتن در قالب JSON</span> <br>
<span dir='rtl'>• خروجی‌گرفتن در قالب CSV</span> <br>
<span dir='rtl'>• ثبت گزارش در فایل</span> <br>
<span dir='rtl'>• تست خودکار با `pytest`</span>

</div>

---

## ساختار پروژه

```text
02-dns_lookup/

├── README.md
├── CHANGELOG.md
├── requirements.txt
│
├── docs/
│   ├── en/
│   └── fa/
│
│
├── src/
│   ├── __init__.py
│   ├── validator.py
│   ├── results.py
│   ├── resolver.py
│   ├── models.py
│   ├── results.py
│   ├── formatter.py
│   ├── exporter.py
│   ├── csv_exporter.py
│   ├── logger.py
│   └── cli.py
│
└── tests/
```

---

## معماری

```text
CLI
 |
 ├── اعتبارسنجی
 |
 ├── Resolver
 |
 └── سازندهٔ نتایج
        |
        └── DNSRecord
                |
                ├── قالب‌بندی خروجی
                ├── خروجی JSON
                └── خروجی CSV

Logger
 └── ثبت رویدادهای چرخهٔ اجرای جست‌وجو
```

---

## پیش‌نیازها

<div align='right' dir="rtl">

<span dir='rtl'>• Python نسخهٔ 3.10 یا بالاتر</span> <br>
<span dir='rtl'>• `pytest` برای اجرای تست‌ها</span>

</div>

وابستگی اصلی:

<div align='right' dir="rtl">

<span dir='rtl'>• `dnspython`</span>

</div>

نصب وابستگی‌ها:

```bash
pip install -r requirements.txt
```

---

## نحوهٔ استفاده

جست‌وجوی رکورد `A`:

```bash
python -m src.cli google.com A
```

جست‌وجوی رکورد `MX`:

```bash
python -m src.cli google.com MX
```

جست‌وجوی رکورد `TXT`:

```bash
python -m src.cli google.com TXT
```

---

## خروجی‌گرفتن از نتایج

خروجی JSON:

```bash
python -m src.cli google.com A --json result.json
```

خروجی CSV:

```bash
python -m src.cli google.com A --csv result.csv
```

ذخیرهٔ هم‌زمان در هر دو قالب:

```bash
python -m src.cli google.com A --json result.json --csv result.csv
```

---

## ثبت گزارش

رویدادهای جست‌وجو در فایل زیر ثبت می‌شوند:

```text
dns.log
```

رویدادهای فعلی شامل موارد زیر هستند:

<p dir='rtl'>
• شروع جست‌وجو <br>
• پایان جست‌وجو
</p>

---

## اجرای تست‌ها

برای اجرای تمام تست‌های پروژه:

```bash
python -m pytest -v
```

---

## اهداف طراحی

۱. یادگیری مبانی DNS  
۲. تمرین کار با کتابخانه‌های شبکه در پایتون  
۳. ساخت نرم‌افزاری با قابلیت نگهداری مناسب  
۴. کار با مدل‌های دادهٔ ساختاریافته  
۵. تمرین تست خودکار  
۶. ساخت ابزارهای قابل استفادهٔ مجدد در حوزهٔ امنیت  

---

## محدودیت‌های فعلی

<p dir='rtl'>
• استفاده از پیکربندی DNS سیستم <br>
• نبود امکان انتخاب سرور DNS سفارشی <br>
• نبود اعتبارسنجی DNSSEC <br>
• نبود پشتیبانی از جست‌وجوی معکوس DNS <br>
• نبود قابلیت جست‌وجوی گروهی دامنه‌ها
</p>

---

## نقشهٔ راه

بهبودهای برنامه‌ریزی‌شده:

<p dir='rtl'>
• امکان انتخاب سرور DNS سفارشی <br>
• جست‌وجوی معکوس DNS <br>
• پردازش گروهی دامنه‌ها <br>
• بررسی DNSSEC <br>
• پشتیبانی از قالب‌های خروجی بیشتر <br>
• گزارش‌دهی پیشرفته‌تر
</p>

---

## مجوز

این پروژه تحت مجوز MIT منتشر شده است.
