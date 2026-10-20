<div align='right'>

[🇬🇧 English](/02-dns_lookup/docs/en/04-dns-lookup-analysis/tests/13-test_models.md)

</div>

# درس سیزدهم: تست مدل‌های داده و تغییرناپذیری در پایتون

**کد مورد آزمایش:** `src/models.py`

## ۱. هدف درس

در این درس یاد می‌گیریم چگونه با تست خودکار، رفتار یک مدل داده را بررسی کنیم.

در پروژه‌ی DNS Lookup، کلاس `DNSRecord` با استفاده از `dataclass` تعریف شده و ویژگی `frozen=True` دارد. تست‌های این درس بررسی می‌کنند که:

<div align='right' dir="rtl">

<span dir='rtl'>• یک رکورد DNS با مقادیر مورد انتظار ساخته شود.</span> <br>
<span dir='rtl'>• فیلدهای رکورد پس از ساخت قابل تغییر نباشند.</span> <br>
<span dir='rtl'>• مدل بتواند نمونه‌ای با نوع رکورد `MX` نیز نگه‌داری کند.</span>

</div>

## ۲. کد کامل فایل تست

```python id="f9gjpz"
import pytest

from src import DNSRecord


def test_dns_record_creation():
    record = DNSRecord(domain='google.com', record_type='A', value='8.8.8.8')
    assert record.domain == 'google.com'
    assert record.record_type == 'A'
    assert record.value == '8.8.8.8'


def test_dns_record_is_immutable():
    record = DNSRecord(domain='google.com', record_type='A', value='8.8.8.8')

    with pytest.raises(AttributeError):
        record.value = '1.1.1.1'


def test_dns_record_with_mx_record():
    record = DNSRecord(domain='google.com', record_type='MX', value='smtp.google.com')
    assert record.record_type == 'MX'
```

## ۳. وارد کردن ابزارهای موردنیاز

```python id="0mxq0x"
import pytest

from src import DNSRecord
```

### ماژول `pytest`

<div align='right' dir="rtl">

<span dir='rtl'>`pytest` ابزار اجرای تست‌ها و بررسی نتایج آن‌هاست. در این فایل، علاوه بر اجرای تست‌ها، از قابلیت <span dir='ltr'>`pytest.raises()`</span> برای بررسی رخ‌دادن یک استثنا استفاده شده است.</span>

</div>

### کلاس `DNSRecord`

این کلاس از پکیج `src` وارد می‌شود. تعریف آن در فایل `models.py` قرار دارد:

```python id="2cr47g"
from dataclasses import dataclass


@dataclass(frozen=True)
class DNSRecord:
    """
    Represent a DNS record.
    """
    domain: str
    record_type: str
    value: str
```

این مدل سه فیلد دارد:

<div align='right' dir="rtl">

<span dir='rtl'>• `domain`: نام دامنه</span> <br>
<span dir='rtl'>• `record_type`: نوع رکورد DNS</span> <br>
<span dir='rtl'>• `value`: مقدار رکورد</span>

</div>

ویژگی `frozen=True` نیز باعث می‌شود انتساب مقدار جدید به فیلدهای نمونه پس از ساخت، مجاز نباشد.

## ۴. تست ساخت رکورد DNS

```python id="b8m8p4"
def test_dns_record_creation():
    record = DNSRecord(
        domain='google.com',
        record_type='A',
        value='8.8.8.8'
    )
    assert record.domain == 'google.com'
    assert record.record_type == 'A'
    assert record.value == '8.8.8.8'
```

این تست ابتدا یک شیء `DNSRecord` می‌سازد و سپس مقدار هر فیلد را بررسی می‌کند.

### ساخت نمونه

```python id="t7k39h"
record = DNSRecord(
    domain='google.com',
    record_type='A',
    value='8.8.8.8'
)
```

به دلیل استفاده از `dataclass`، نیازی نیست سازنده‌ی <span dir='ltr'>`__init__()`</span> را خودمان بنویسیم. پایتون آن را به‌صورت خودکار برای فیلدهای تعریف‌شده ایجاد می‌کند.

### بررسی با `assert`

```python id="0w0n1b"
assert record.domain == 'google.com'
```

این عبارت بررسی می‌کند که مقدار فیلد `domain` برابر با مقدار مورد انتظار باشد.

دو `assert` بعدی نیز همین کار را برای `record_type` و `value` انجام می‌دهند.

اگر هرکدام از این شرط‌ها برقرار نباشد، تست شکست می‌خورد.

**نکته‌ی مهم:** این تست مقادیر ذخیره‌شده در شیء را بررسی می‌کند؛ به‌تنهایی صحت واقعی اطلاعات DNS یا اعتبارسنجی ورودی‌ها را آزمایش نمی‌کند. این مسئولیت‌ها در بخش‌های دیگر پروژه قرار دارند.

## ۵. تست تغییرناپذیری رکورد

```python id="j2p4n0"
def test_dns_record_is_immutable():
    record = DNSRecord(
        domain='google.com',
        record_type='A',
        value='8.8.8.8'
    )

    with pytest.raises(AttributeError):
        record.value = '1.1.1.1'
```

این تست ویژگی `frozen=True` را بررسی می‌کند.

### تغییر مقدار فیلد

```python id="q8j3v5"
record.value = '1.1.1.1'
```

اگر `DNSRecord` یک dataclass معمولی و تغییرپذیر بود، این انتساب می‌توانست مقدار فیلد را تغییر دهد.

اما چون مدل با `frozen=True` تعریف شده است، تلاش برای انتساب مقدار جدید به فیلد، استثنای `AttributeError` ایجاد می‌کند.

### نقش <span dir='ltr'>`pytest.raises()`</span>

```python id="k1v8n2"
with pytest.raises(AttributeError):
    record.value = '1.1.1.1'
```

این ساختار به pytest می‌گوید که اجرای کد داخل بلوک باید استثنای مشخص‌شده را ایجاد کند.

دو حالت را در نظر بگیریم:

<div align='right' dir="rtl">

<span dir='rtl'>• اگر `AttributeError` رخ دهد، این بخش از تست موفق است.</span> <br>
<span dir='rtl'>• اگر انتساب بدون آن استثنا انجام شود، تست شکست می‌خورد.</span>

</div>

به این ترتیب، تست فقط بررسی نمی‌کند که ساخت شیء موفق است؛ بلکه رفتار آن را در برابر یک عملیات غیرمجاز نیز بررسی می‌کند.

### چرا تغییرناپذیری مفید است؟

در جریان کاری ابزار DNS Lookup، یک رکورد پس از ساخته‌شدن می‌تواند بین بخش‌های مختلف برنامه جابه‌جا شود؛ برای مثال، از بخش ساخت نتایج به formatter یا مرحله‌ی خروجی‌گیری.

تغییرناپذیری کمک می‌کند مقادیر فیلدهای یک رکورد به‌طور تصادفی بازنویسی نشوند. این ویژگی می‌تواند درک جریان داده‌ها و عیب‌یابی را ساده‌تر کند.

نکته‌ی فنی: `frozen=True` به معنای تغییرناپذیری عمیق تمام اشیای مرتبط نیست؛ بلکه انتساب مجدد فیلدهای نمونه را محدود می‌کند. در مدل فعلی، هر سه فیلد از نوع رشته هستند که انتخاب مناسبی برای چنین رکوردی است.

## ۶. تست رکورد از نوع MX

```python id="r6u3c9"
def test_dns_record_with_mx_record():
    record = DNSRecord(
        domain='google.com',
        record_type='MX',
        value='smtp.google.com'
    )
    assert record.record_type == 'MX'
```

این تست نمونه‌ای از `DNSRecord` را با نوع رکورد `MX` می‌سازد و مقدار فیلد `record_type` را بررسی می‌کند.

در تست قبلی، نوع رکورد `A` بود. اینجا یک نوع دیگر را آزمایش می‌کنیم تا نشان دهیم مدل صرفاً برای یک مقدار مشخص طراحی نشده است.

کلاس `DNSRecord` مسئول نگه‌داری اطلاعات رکورد است؛ فهرست انواع پشتیبانی‌شده و اعتبارسنجی آن‌ها در تابع <span dir='ltr'>`validate_record_type()`</span> قرار دارند.

بنابراین، تست حاضر بررسی می‌کند که مدل بتواند مقدار `MX` را ذخیره کند؛ نه اینکه این مقدار از نظر DNS معتبر است یا رکورد واقعی و قابل دسترسی‌ای وجود دارد.

## ۷. این سه تست چه چیزی را پوشش می‌دهند؟

<div align='center' dir="rtl">

| نام تست | رفتار مورد بررسی |
|---|---|
| `test_dns_record_creation` | ساخت رکورد و مقدار صحیح فیلدها |
| `test_dns_record_is_immutable` | جلوگیری از انتساب مجدد به فیلد |
| `test_dns_record_with_mx_record` |<span dir='rtl'> نگه‌داری مقدار نوع رکورد `MX`</span> |

</div>

این مجموعه سه سناریوی مشخص را پوشش می‌دهد: ساخت صحیح شیء، محدودیت تغییر فیلدها و استفاده از نوع رکورد دیگری.

## ۸. اجرای تست‌ها

برای اجرای همین فایل از ریشه‌ی پروژه:

```powershell
python -m pytest tests/test_models.py
```

برای اجرای تمام تست‌های پروژه:

```powershell
python -m pytest
```

اگر تست تغییرناپذیری شکست بخورد، باید بررسی کنیم که آیا تعریف مدل همچنان `frozen=True` دارد یا رفتار مورد انتظار تغییر کرده است.

## ۹. تمرین‌های آموزشی

### تمرین اول: بررسی فیلدها

یک نمونه‌ی `DNSRecord` با مقادیر دلخواه بسازید و برای هر سه فیلد یک `assert` بنویسید.

### تمرین دوم: تغییر دامنه

پس از ساخت رکورد، تلاش کنید مقدار `record.domain` را تغییر دهید.

<p dir='rtl'>
• چه استثنایی رخ می‌دهد؟ <br>
• چرا انتظار داریم این عملیات با خطا مواجه شود؟
</p>

### تمرین سوم: بررسی فیلدهای دیگر

تست تغییرناپذیری را برای `record_type` نیز بنویسید.

### تمرین چهارم: تفکیک مسئولیت‌ها

توضیح دهید تفاوت وظیفه‌ی `DNSRecord` با <span dir='ltr'>`validate_record_type()`</span> چیست.

## ۱۰. جمع‌بندی

در این درس یاد گرفتیم که تست مدل داده فقط بررسی ساخته‌شدن یک شیء نیست. می‌توانیم مقدار فیلدها و محدودیت‌های رفتاری آن را نیز آزمایش کنیم.

مفاهیم کلیدی:

<div align='right' dir="rtl">

<span dir='rtl'>• استفاده از `dataclass` برای تعریف مدل داده</span> <br>
<span dir='rtl'>• بررسی مقدار فیلدها با `assert`</span> <br>
<span dir='rtl'>• استفاده از <span dir='ltr'>`pytest.raises()`</span> برای آزمایش استثناها</span> <br>
<span dir='rtl'>• بررسی رفتار `frozen=True`</span> <br>
<span dir='rtl'>• تفکیک مسئولیت مدل داده از اعتبارسنجی ورودی‌ها</span>

</div>

در پروژه‌ی DNS Lookup، `DNSRecord` یک ساختار ساده و مشخص برای نگه‌داری اطلاعات رکورد فراهم می‌کند. این تست‌ها کمک می‌کنند رفتار اصلی مدل در برابر تغییرات آینده حفظ شود.
