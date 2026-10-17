# درس دوازدهم: تست خودکار اعتبارسنجی ورودی‌ها با pytest

**کدهای مورد آزمایش:** `src/validator.py`

## ۱. هدف درس

در این درس با تست خودکار در پایتون و روش بررسی رفتار توابع اعتبارسنجی آشنا می‌شویم.

در پروژه‌ی DNS Lookup، سه تابع اعتبارسنجی داریم:

<div align='right' dir="rtl">

<span dir='rtl'>• <span dir='ltr'>`validate_domain()`</span> برای بررسی قالب دامنه</span> <br>
<span dir='rtl'>• <span dir='ltr'>`validate_timeout()`</span> برای بررسی مثبت‌بودن timeout</span> <br>
<span dir='rtl'>• <span dir='ltr'>`validate_record_type()`</span> برای بررسی پشتیبانی از نوع رکورد DNS</span>

</div>

فایل `test_validator.py` رفتار این سه تابع را با مجموعه‌ای از ورودی‌های مختلف بررسی می‌کند.

## ۲. کد کامل فایل تست

```python
from src import (
    validate_domain,
    validate_timeout,
    validate_record_type,
)


def test_valid_domain():
    assert validate_domain('google.com')


def test_valid_subdomain():
    assert validate_domain('mail.google.com')


def test_invalid_domain_without_tld():
    assert not validate_domain('google')


def test_invalid_domain_with_protocol():
    assert not validate_domain('https://google.com')


def test_invalid_domain_with_space():
    assert not validate_domain('google .com')


def test_valid_timeout():
    assert validate_timeout(1.0)


def test_valid_timeout_boundary():
    assert validate_timeout(0.001)


def test_invalid_timeout():
    assert not validate_timeout(0)


def test_invalid_negative_timeout():
    assert not validate_timeout(-1)


def test_valid_record_type_a():
    assert validate_record_type('A')


def test_valid_record_type_lowercase():
    assert validate_record_type('mx')


def test_valid_record_type_aaaa():
    assert validate_record_type('AAAA')


def test_invalid_record_type():
    assert not validate_record_type('FTP')


def test_invalid_empty_record_type():
    assert not validate_record_type('')
```

## ۳. چرا تست خودکار می‌نویسیم؟

فرض کنیم تابع اعتبارسنجی دامنه را تغییر دهیم. ممکن است تغییر جدید یک ورودی معتبر را رد کند یا ورودی نامعتبری را بپذیرد.

با اجرای تست‌ها می‌توانیم بررسی کنیم که رفتارهای مورد انتظار همچنان برقرار هستند.

تست خودکار چند مزیت مهم دارد:

<p dir='rtl'>
• خطاهای احتمالی را زودتر آشکار می‌کند. <br>
• از رفتارهای مهم برنامه در برابر تغییرات ناخواسته محافظت می‌کند. <br>
• امکان اجرای مکرر بررسی‌ها را فراهم می‌سازد. <br>
• مستند می‌کند که از هر تابع چه رفتاری انتظار داریم.
</p>

در این پروژه از `pytest` استفاده می‌کنیم.

## ۴. وارد کردن توابع مورد آزمایش

```python
from src import (
    validate_domain,
    validate_timeout,
    validate_record_type,
)
```

این بخش سه تابع را از پکیج `src` وارد می‌کند.

این توابع در فایل `validator.py` تعریف شده‌اند و در `src/__init__.py` نیز در دسترس پکیج قرار گرفته‌اند.

به این ترتیب، تست‌ها رفتار توابعی را بررسی می‌کنند که از رابط عمومی پکیج قابل دسترسی هستند.

## ۵. ساختار یک تست با `assert`

اولین تست:

```python
def test_valid_domain():
    assert validate_domain('google.com')
```

این تابع یک تست برای دامنه‌ی معتبر است.

نام توابع تست با پیشوند <span dir='ltr'>`test_`</span> شروع می‌شود تا `pytest` بتواند آن‌ها را به‌صورت خودکار شناسایی کند.

عبارت `assert` شرطی را بررسی می‌کند:

<p dir='rtl'>
• اگر شرط درست باشد، تست ادامه پیدا می‌کند. <br>
• اگر شرط نادرست باشد، تست شکست می‌خورد و pytest اطلاعاتی درباره‌ی شکست نمایش می‌دهد.
</p>

در این مثال، انتظار داریم `validate_domain('google.com')` مقدار درست برگرداند.

نکته‌ی مهم: این تست فقط یک ورودی مشخص را بررسی می‌کند؛ موفقیت آن به‌تنهایی ثابت نمی‌کند که تابع برای تمام دامنه‌های ممکن درست عمل می‌کند.

## ۶. تست دامنه و زیردامنه

```python
def test_valid_domain():
    assert validate_domain('google.com')


def test_valid_subdomain():
    assert validate_domain('mail.google.com')
```

تست اول یک دامنه‌ی معمولی را بررسی می‌کند.

تست دوم بررسی می‌کند که تابع یک زیردامنه را نیز بپذیرد.

این دو تست برای اطمینان از رفتار پایه‌ی اعتبارسنجی مفید هستند. همچنین نشان می‌دهند که تست‌ها می‌توانند نمونه‌های مختلفی از ورودی‌های معتبر را پوشش دهند.

## ۷. تست دامنه‌های نامعتبر

### دامنه بدون پسوند

```python
def test_invalid_domain_without_tld():
    assert not validate_domain('google')
```

در این تست، از `not` استفاده شده است.

انتظار داریم تابع برای رشته‌ی `google` مقدار `False` برگرداند؛ چون این ورودی با الگوی دامنه‌ی مورد انتظار در پیاده‌سازی فعلی سازگار نیست.

### دامنه همراه پروتکل

```python
def test_invalid_domain_with_protocol():
    assert not validate_domain('https://google.com')
```

در اینجا ورودی شامل <span dir='ltr'>`https://`</span> است.

تابع <span dir='ltr'>`validate_domain()`</span> برای اعتبارسنجی قالب نام دامنه طراحی شده، نه آدرس کامل URL؛ بنابراین انتظار داریم این ورودی رد شود.

### دامنه دارای فاصله

```python
def test_invalid_domain_with_space():
    assert not validate_domain('google .com')
```

این تست بررسی می‌کند که وجود فاصله در میان رشته باعث رد ورودی شود.

این سه تست نشان می‌دهند که اعتبارسنجی فقط به پذیرش نمونه‌های معتبر محدود نیست؛ ردکردن برخی ورودی‌های نامعتبر نیز بخشی از رفتار مورد انتظار است.

## ۸. تست تابع <span dir='ltr'>`validate_timeout()`</span>

### مقدار مثبت معمولی

```python
def test_valid_timeout():
    assert validate_timeout(1.0)
```

انتظار داریم timeout برابر با `1.0` پذیرفته شود؛ زیرا مقدار آن مثبت است.

### مقدار مثبت کوچک

```python
def test_valid_timeout_boundary():
    assert validate_timeout(0.001)
```

این تست یک مقدار مثبت کوچک را بررسی می‌کند.

نام تست از واژه‌ی *boundary* استفاده می‌کند، اما از نظر فنی این مقدار کوچک‌ترین مقدار مثبت ممکن برای نوع `float` نیست. این تست یک نمونه‌ی نزدیک به صفر را بررسی می‌کند تا مطمئن شویم تابع صرفاً به دلیل کوچک‌بودن مقدار، آن را رد نمی‌کند.

### صفر و مقدار منفی

```python
def test_invalid_timeout():
    assert not validate_timeout(0)


def test_invalid_negative_timeout():
    assert not validate_timeout(-1)
```

تابع <span dir='ltr'>`validate_timeout()`</span> در پیاده‌سازی فعلی این شرط را بررسی می‌کند:

```python
return timeout > 0
```

بنابراین:

<div align='center' dir="rtl">

| ورودی | نتیجه‌ی مورد انتظار |
|---:|---|
| `1.0` | پذیرفته شود |
| `0.001` | پذیرفته شود |
| `0` | رد شود |
| `-1` | رد شود |

</div>

این تست‌ها رفتار مثبت‌بودن مقدار را بررسی می‌کنند.

یک نکته‌ی آموزشی: تست‌های فعلی مقادیر مثبت، صفر و منفی را پوشش می‌دهند، اما رفتار ورودی‌هایی مانند `float('inf')`، `float('nan')` یا رشته‌ی متنی را بررسی نمی‌کنند. اگر لازم باشد تابع در برابر این ورودی‌ها نیز رفتار مشخصی داشته باشد، می‌توان تست‌های جداگانه‌ای برای آن‌ها نوشت.

## ۹. تست تابع <span dir='ltr'>`validate_record_type()`</span>

### نوع رکورد A

```python
def test_valid_record_type_a():
    assert validate_record_type('A')
```

این تست بررسی می‌کند که نوع رکورد `A` پذیرفته شود.

### نوع رکورد با حروف کوچک

```python
def test_valid_record_type_lowercase():
    assert validate_record_type('mx')
```

این تست نکته‌ی مهمی را بررسی می‌کند: تابع باید نوع رکورد `mx` را نیز بپذیرد، هرچند با حروف کوچک نوشته شده باشد.

علت این رفتار در پیاده‌سازی <span dir='ltr'>`validate_record_type()`</span> است:

```python
return record_type.upper() in SUPPORTED_RECORD_TYPES
```

متد <span dir='ltr'>`upper()`</span> رشته را به حروف بزرگ تبدیل می‌کند. بنابراین `mx` به `MX` تبدیل شده و با مجموعه‌ی انواع پشتیبانی‌شده مقایسه می‌شود.

این تست، یک رفتار مشخص و مهم را مستند می‌کند: اعتبارسنجی نوع رکورد نسبت به بزرگی و کوچکی حروف حساس نیست.

### نوع رکورد AAAA

```python
def test_valid_record_type_aaaa():
    assert validate_record_type('AAAA')
```

این تست بررسی می‌کند که نوع رکورد `AAAA` نیز در میان انواع پشتیبانی‌شده باشد.

### نوع رکورد نامعتبر

```python
def test_invalid_record_type():
    assert not validate_record_type('FTP')
```

در این تست انتظار داریم `FTP` رد شود؛ زیرا در مجموعه‌ی انواع پشتیبانی‌شده‌ی پروژه قرار ندارد.

### رشته‌ی خالی

```python
def test_invalid_empty_record_type():
    assert not validate_record_type('')
```

این تست ورودی خالی را بررسی می‌کند.

از آنجا که رشته‌ی خالی پس از تبدیل با <span dir='ltr'>`upper()`</span> همچنان خالی است و در مجموعه‌ی انواع پشتیبانی‌شده وجود ندارد، انتظار داریم تابع `False` برگرداند.

## ۱۰. این تست‌ها چه چیزی را پوشش می‌دهند؟

فایل حاضر در مجموع ۱۴ تست دارد:

<div align='center' dir="rtl">

| بخش | تعداد تست | موارد بررسی‌شده |
|---|---:|---|
| دامنه | ۵ | دامنه‌ی معمولی، زیردامنه و سه ورودی نامعتبر |
| timeout | ۴ | مقدار مثبت، مقدار مثبت کوچک، صفر و مقدار منفی |
| نوع رکورد | ۵ | انواع معتبر، حروف کوچک، نوع نامعتبر و رشته‌ی خالی |
| **مجموع** | **۱۴** | **سه تابع اعتبارسنجی** |

</div>

این مجموعه، رفتارهای پایه‌ی مهمی را پوشش می‌دهد. البته تعداد تست‌ها به‌تنهایی معیار کامل کیفیت نیست؛ مهم است که سناریوهای مهم و حالت‌های مرزی مورد نیاز نیز در نظر گرفته شوند.

## ۱۱. اجرای تست‌ها

برای اجرای همین فایل از ریشه‌ی پروژه، می‌توان از این فرمان استفاده کرد:

```powershell
python -m pytest tests/test_validator.py
```

برای اجرای کل تست‌های پروژه:

```powershell
python -m pytest
```

در خروجی pytest، معمولاً نتیجه‌ی هر تست و تعداد تست‌های موفق یا ناموفق نمایش داده می‌شود.

اگر تستی شکست بخورد، اطلاعات آن کمک می‌کند مشخص کنیم کدام انتظار برقرار نبوده است.

## ۱۲. فرصت‌های توسعه‌ی تست‌ها

تست‌های فعلی رفتارهای پایه را به‌خوبی مشخص می‌کنند. برای گسترش پوشش می‌توان سناریوهای زیر را در آینده اضافه کرد:

<div align='right' dir="rtl">

<span dir='rtl'>• دامنه‌هایی با طول بسیار زیاد</span> <br>
<span dir='rtl'>• برچسب دامنه‌ای که با خط تیره تمام می‌شود</span> <br>
<span dir='rtl'>• timeoutهای غیرمتناهی مانند `float('inf')`</span> <br>
<span dir='rtl'>• timeout از نوع `NaN`</span> <br>
<span dir='rtl'>• ورودی‌های غیررشته‌ای برای توابعی که رشته انتظار دارند</span> <br>
<span dir='rtl'>• انواع رکورد معتبر با شکل‌های مختلف حروف</span>

</div>

این موارد پیشنهادهایی برای افزایش پوشش تست هستند. اضافه‌کردن هر تست باید بر اساس قرارداد مورد انتظار تابع انجام شود؛ ابتدا باید مشخص کنیم ورودی موردنظر باید پذیرفته شود یا رد شود، سپس آن رفتار را با تست ثبت کنیم.

## ۱۳. جمع‌بندی

در این درس یاد گرفتیم که تست خودکار فقط اجرای تابع و دیدن خروجی نیست؛ بلکه تعریف انتظار روشن درباره‌ی رفتار تابع است.

مفاهیم اصلی:

<div align='right' dir="rtl">

<span dir='rtl'>• شناسایی تست‌ها با نام‌هایی که با <span dir='ltr'>`test_`</span> شروع می‌شوند</span> <br>
<span dir='rtl'>• استفاده از `assert` برای بررسی نتیجه</span> <br>
<span dir='rtl'>• بررسی ورودی‌های معتبر و نامعتبر</span> <br>
<span dir='rtl'>• تست مقادیر مرزی</span> <br>
<span dir='rtl'>• مستندسازی رفتار مورد انتظار توابع</span> <br>
<span dir='rtl'>• اجرای تست‌ها با `pytest`</span>

</div>

در پروژه‌ی DNS Lookup، این فایل کمک می‌کند رفتار سه تابع اعتبارسنجی در برابر مجموعه‌ای از ورودی‌های مشخص، قابل بررسی و تکرار باشد.
