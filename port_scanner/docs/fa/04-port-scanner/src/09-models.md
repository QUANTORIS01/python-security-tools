# بررسی کامل فایل `models.py`

# مقدمه

تا اینجای پروژه تقریباً تمام بخش‌های عملی پورت اسکنر را بررسی کرده‌ایم:

<p dir='rtl'>
✅ اعتبارسنجی ورودی‌ها <br>
✅ اسکن پورت‌ها <br>
✅ تشخیص سرویس‌ها <br>
✅ دریافت Banner <br>
✅ خروجی JSON <br>
✅ خروجی CSV <br>
✅ Logging
</p>

---

اما یک سؤال مهم وجود دارد.

---

فرض کن نتیجه اسکن یک پورت این باشد:

```python
80
```

---

فقط عدد 80 کافی نیست.

---

ما معمولاً چند اطلاعات مختلف داریم:

```python
80
http
Apache
```

---

یا:

```python
22
ssh
OpenSSH
```

---

سؤال:

چگونه این اطلاعات را در کنار هم نگهداری کنیم؟

---

یک راه:

```python
tuple
```

---

مثال:

```python
(
    80,
    "http",
    "Apache"
)
```

---

اما مشکل اینجاست:

```python
result[0]
```

---

این چیست؟

---

<p dir='rtl'>
Port؟ <br>
Service؟ <br>
Banner؟
</p>

---

مشخص نیست.

---

برای حل این مشکل از:

```text
Data Model
```

استفاده می‌کنیم.

---

فایل:

```text
src/models.py
```

دقیقاً برای همین ساخته شده است.

---

# محتوای فایل

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class ScanResult:
    """
    Represent the result of a scanned open port.
    """

    port: int
    service: str
    banner: str | None = None
```

---

# هدف این فایل چیست؟

هدف:

```text
ساخت یک مدل استاندارد برای نگهداری نتایج اسکن
```

است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Data Model چیست؟
</p>

<p dir='rtl'>
Data Model یعنی:
</p>

```text
تعریف ساختار داده
```

---

مثال:

اگر بخواهیم یک کاربر را نمایش دهیم:

```python
name
email
age
```

---

می‌توانیم یک مدل بسازیم.

---

اگر بخواهیم نتیجه اسکن را نمایش دهیم:

```python
port
service
banner
```

---

باز هم می‌توانیم یک مدل بسازیم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import
</p>

```python
from dataclasses import dataclass
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
Dataclass چیست؟
</p>

یکی از بهترین قابلیت‌های پایتون مدرن.

---

قبل از Dataclass برای ساخت یک کلاس ساده باید این کار را انجام می‌دادیم:

```python
class ScanResult:

    def __init__(
        self,
        port,
        service,
        banner
    ):
        self.port = port
        self.service = service
        self.banner = banner
```

---

کد زیاد.

---

تکراری.

---

خسته‌کننده.

---

اما Dataclass این کارها را خودکار انجام می‌دهد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Decorator
</p>

```python
@dataclass(
    frozen=True
)
```

---

قبل از ورود به کلاس اجرا می‌شود.

---

به این نوع ساختار:

```python
Decorator
```

می‌گوییم.

---

قبلاً در دوره پایتون گفتیم:

```text
Decorator رفتاری به کد اضافه می‌کند.
```

---

اینجا Dataclass قابلیت‌های زیادی اضافه می‌کند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Dataclass چه چیزهایی می‌سازد؟
</p>

به صورت خودکار:

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
__init__
</p>

```python
__init__()
```

---

یعنی:

```python
ScanResult(
    80,
    "http",
    "Apache"
)
```

---

<p dir='rtl'>
بدون اینکه خودمان __init__ بنویسیم.
</p>

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
__repr__
</p>

---

برای نمایش شیء.

---

مثال:

```python
print(result)
```

---

خروجی:

```python
ScanResult(
    port=80,
    service='http',
    banner='Apache'
)
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
__eq__
</p>

---

برای مقایسه دو شیء.

---

مثال:

```python
a == b
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
frozen=True چیست؟
</p>

این قسمت بسیار مهم است.

---

```python
@dataclass(
    frozen=True
)
```

---

یعنی:

```text
شیء غیرقابل تغییر باشد.
```

---

در دنیای برنامه‌نویسی:

```text
Immutable Object
```

---

نامیده می‌شود.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Immutable چیست؟
</p>

یعنی:

```text
بعد از ساخت شیء نتوانیم مقادیرش را تغییر دهیم.
```

---

مثال:

```python
result = ScanResult(
    80,
    "http",
    "Apache"
)
```

---

اگر بنویسیم:

```python
result.port = 443
```

---

خطا می‌گیریم.

---

چرا؟

---

چون:

```python
frozen=True
```

قرار داده شده است.

---

# چرا Immutable خوب است؟

زیرا:

```text
نتایج اسکن نباید تغییر کنند.
```

---

فرض کن:

```python
Port 80 Open
```

---

بعداً کسی بنویسد:

```python
result.port = 22
```

---

تمام داده خراب می‌شود.

---

<p dir='rtl'>
Immutable جلوی این اتفاق را می‌گیرد.
</p>

---

# تعریف کلاس

```python
class ScanResult:
```

---

این کلاس نماینده:

```text
یک پورت باز
```

است.

---

دقت کن:

```text
یک پورت
```

نه کل اسکن.

---

مثال:

```python
80
http
Apache
```

---

یک شیء.

---

پورت بعدی:

```python
443
https
Nginx
```

---

یک شیء دیگر.

---

# داک استرینگ

```python
"""
Represent the result of a scanned open port.
"""
```

---

معنی:

```text
نماینده نتیجه یک پورت باز اسکن شده.
```

---

# فیلد اول

```python
port: int
```

---

نوع:

```python
int
```

---

مثال:

```python
80
```

---

یا:

```python
443
```

---

یا:

```python
22
```

---

# فیلد دوم

```python
service: str
```

---

نوع:

```python
str
```

---

مثال:

```python
"http"
```

---

یا:

```python
"https"
```

---

یا:

```python
"ssh"
```

---

# فیلد سوم

```python
banner: str | None = None
```

---

این قسمت از همه جالب‌تر است.

---

نوع:

```python
str | None
```

---

یعنی:

```python
"Apache"
```

---

یا:

```python
None
```

---

# مقدار پیش‌فرض

```python
= None
```

---

یعنی:

اگر Banner نداشتیم:

```python
banner
```

خودکار برابر:

```python
None
```

می‌شود.

---

مثال:

```python
ScanResult(
    port=53,
    service="domain"
)
```

---

در این حالت:

```python
banner
```

خودکار:

```python
None
```

است.

---

# ساخت یک شیء واقعی

```python
result = ScanResult(
    port=80,
    service="http",
    banner="Apache"
)
```

---

محتویات:

```python
result.port
```

↓

```python
80
```

---

```python
result.service
```

↓

```python
"http"
```

---

```python
result.banner
```

↓

```python
"Apache"
```

---

# نمونه دوم

```python
result = ScanResult(
    port=53,
    service="domain"
)
```

---

نتیجه:

```python
result.port
```

↓

```python
53
```

---

```python
result.service
```

↓

```python
"domain"
```

---

```python
result.banner
```

↓

```python
None
```

---

# چرا این طراحی حرفه‌ای است؟

به جای:

```python
{
    "port": 80,
    "service": "http",
    "banner": "Apache"
}
```

---

یا:

```python
(
    80,
    "http",
    "Apache"
)
```

---

یک مدل مشخص داریم:

```python
ScanResult
```

---

مزایا:

✅ خوانایی بیشتر

✅ تایپ بهتر

✅ تست آسان‌تر

✅ خطای کمتر

✅ توسعه‌پذیری بیشتر

---

به همین دلیل تقریباً تمام پروژه‌های حرفه‌ای از Data Model استفاده می‌کنند.

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ Data Model چیست <br>
✅ Dataclass چیست <br>
✅ Decorator چیست <br>
✅ __init__ چگونه خودکار ساخته می‌شود <br>
✅ __repr__ چیست <br>
✅ __eq__ چیست <br>
✅ Immutable چیست <br>
✅ frozen=True چیست <br>
✅ چرا ScanResult ساخته شده است <br>
✅ چرا استفاده از Model حرفه‌ای‌تر از Dictionary است
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
src/results.py
```

می‌شویم.

در آن یاد می‌گیریم:

<p dir='rtl'>
• چرا ScanResult ساخته شده است <br>
• چگونه Open Ports را به ScanResult تبدیل می‌کنیم <br>
• چگونه Service Detection و Banner Grabbing را با هم ترکیب می‌کنیم <br>
• List Comprehension چیست <br>
• Pipeline طراحی داده در پروژه چگونه کار می‌کند
</p>

