# ۱۶. تست‌نویسی برای قالب‌بندی خروجی DNS در پایتون

## هدف درس

در این درس، فایل `tests/test_formatter.py` را بررسی می‌کنیم تا یاد بگیریم چگونه خروجی متنی یک تابع را با `pytest` آزمایش کنیم.

موضوعات اصلی:

<div align='right' dir="rtl">

<span dir='rtl'>• تست توابعی که رشته تولید می‌کنند</span> <br>
<span dir='rtl'>• بررسی وجود متن با `in`</span> <br>
<span dir='rtl'>• ساخت داده‌های آزمایشی با `DNSRecord`</span> <br>
<span dir='rtl'>• آزمایش رکوردهای مختلف DNS</span> <br>
<span dir='rtl'>• بررسی رفتار تابع هنگام دریافت لیست خالی</span> <br>
<span dir='rtl'>• تفاوت میان تست محتوای خروجی و تست قالب دقیق آن</span>

</div>

## کد کامل فایل تست

```python id="f9gjpz"
from src import DNSRecord, format_dns_results


def test_format_dns_results():
    results = [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        ),
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.4.4',
        ),
    ]
    output = format_dns_results(results)

    assert 'DOMAIN' in output
    assert 'TYPE' in output
    assert 'VALUE' in output

    assert 'google.com' in output
    assert '8.8.8.8' in output
    assert '8.8.4.4' in output


def test_format_dns_results_with_mx_record():
    results = [
        DNSRecord(
            domain='google.com',
            record_type='MX',
            value='smtp.google.com',
        )
    ]
    output = format_dns_results(results)
    assert 'MX' in output
    assert 'smtp.google.com' in output


def test_format_dns_results_empty():
    output = format_dns_results([])
    assert output == 'No DNS records found.'
```

## ۱. وارد کردن اجزای موردنیاز

```python
from src import DNSRecord, format_dns_results
```

در این فایل دو جزء از پروژه استفاده می‌شوند:

<div align='right' dir="rtl">

<span dir='rtl'>• `DNSRecord`: مدل داده‌ای که اطلاعات یک رکورد DNS را نگه می‌دارد.</span> <br>
<span dir='rtl'>• `format_dns_results`: تابعی که فهرستی از رکوردها را به متن مناسب نمایش در ترمینال تبدیل می‌کند.</span>

</div>

تابع <span dir='ltr'>`format_dns_results()`</span> در فایل `src/formatter.py` تعریف شده است. این تابع برای نتیجه‌های غیرخالی، یک جدول متنی می‌سازد و برای نتیجهٔ خالی، پیام مشخصی برمی‌گرداند.

## ۲. تست قالب‌بندی چند رکورد

کد تست:

```python
def test_format_dns_results():
    results = [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        ),
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.4.4',
        ),
    ]

    output = format_dns_results(results)

    assert 'DOMAIN' in output
    assert 'TYPE' in output
    assert 'VALUE' in output

    assert 'google.com' in output
    assert '8.8.8.8' in output
    assert '8.8.4.4' in output
```

### مرحلهٔ اول: ساخت داده‌های آزمایشی

در این قسمت، دو شیء `DNSRecord` ساخته می‌شوند. هر دو به دامنهٔ `google.com` و نوع رکورد `A` مربوط‌اند، اما مقادیر IP آن‌ها متفاوت است.

این داده‌ها مستقیماً در تست ساخته می‌شوند؛ بنابراین برای اجرای این تست به اینترنت یا درخواست DNS واقعی نیازی نیست.

### مرحلهٔ دوم: اجرای تابع قالب‌بندی

```python
output = format_dns_results(results)
```

تابع، لیست رکوردها را دریافت می‌کند و خروجی متنی را در متغیر `output` قرار می‌دهد.

برای مثال، خروجی می‌تواند به این شکل باشد:

```text
DOMAIN                         TYPE     VALUE
----------------------------------------------------------------------
google.com                     A        8.8.8.8
google.com                     A        8.8.4.4
```

فاصله‌های دقیق و نحوهٔ چینش ستون‌ها از رشته‌های قالب‌بندی‌شده در پیاده‌سازی تابع به دست می‌آیند.

### مرحلهٔ سوم: بررسی عنوان ستون‌ها

```python
assert 'DOMAIN' in output
assert 'TYPE' in output
assert 'VALUE' in output
```

عبارت `in` بررسی می‌کند که آیا یک رشته در رشتهٔ دیگری وجود دارد یا خیر.

برای نمونه:

```python
assert 'DOMAIN' in output
```

اگر عنوان `DOMAIN` در خروجی وجود نداشته باشد، تست شکست می‌خورد.

### مرحلهٔ چهارم: بررسی داده‌های رکوردها

```python
assert 'google.com' in output
assert '8.8.8.8' in output
assert '8.8.4.4' in output
```

این assertionها بررسی می‌کنند که نام دامنه و هر دو مقدار IP در خروجی حضور داشته باشند.

**نکته:** این تست وجود داده‌ها را بررسی می‌کند، نه ترتیب دقیق ستون‌ها، تعداد فاصله‌ها یا ساختار کامل جدول. بنابراین ممکن است بعضی تغییرات در ظاهر خروجی رخ دهند و تست همچنان موفق بماند.

## ۳. تست قالب‌بندی رکورد MX

کد تست:

```python
def test_format_dns_results_with_mx_record():
    results = [
        DNSRecord(
            domain='google.com',
            record_type='MX',
            value='smtp.google.com',
        )
    ]

    output = format_dns_results(results)

    assert 'MX' in output
    assert 'smtp.google.com' in output
```

این تست بررسی می‌کند که قالب‌بندی فقط برای رکوردهای `A` کار نمی‌کند و می‌تواند داده‌ای با نوع رکورد `MX` را نیز نمایش دهد.

رکوردهای MX برای مشخص کردن سرورهای دریافت ایمیل یک دامنه استفاده می‌شوند. در این تست، مقدار `smtp.google.com` صرفاً دادهٔ نمونه برای آزمایش قالب‌بندی است.

دو assertion پایانی بررسی می‌کنند که نوع رکورد و مقدار آن در خروجی وجود داشته باشند.

این تست همچنین نشان می‌دهد که تابع قالب‌بندی، داده‌ها را از فیلدهای `DNSRecord` دریافت می‌کند و برای نمایش آن‌ها به نوع خاصی از رکورد محدود نشده است.

## ۴. تست نتیجهٔ خالی

کد تست:

```python
def test_format_dns_results_empty():
    output = format_dns_results([])
    assert output == 'No DNS records found.'
```

در این حالت، تابع یک لیست خالی دریافت می‌کند:

```python
[]
```

انتظار می‌رود خروجی دقیقاً برابر با رشتهٔ زیر باشد:

```text
No DNS records found.
```

برخلاف تست‌های قبلی، در اینجا از عملگر `==` استفاده شده است:

```python
assert output == 'No DNS records found.'
```

این مقایسه، برابری کامل دو رشته را بررسی می‌کند؛ بنابراین وجود فاصله یا خط جدید اضافی در خروجی نیز می‌تواند باعث شکست تست شود.

این رفتار با تست‌های قبلی تفاوت دارد:

<div align='right' dir="rtl">

<span dir='rtl'>• `in`: بررسی می‌کند که بخشی از متن در خروجی وجود داشته باشد.</span> <br>
<span dir='rtl'>• `==`: بررسی می‌کند که مقدار کامل خروجی با مقدار مورد انتظار برابر باشد.</span>

</div>

## ۵. ارتباط تست‌ها با فایل Formatter

تابع <span dir='ltr'>`format_dns_results()`</span> دو مسیر اصلی دارد.

### مسیر اول: لیست خالی

اگر هیچ رکوردی وجود نداشته باشد، تابع پیام زیر را برمی‌گرداند:

```python
'No DNS records found.'
```

تست <span dir='ltr'>`test_format_dns_results_empty()`</span> همین رفتار را به‌طور دقیق بررسی می‌کند.

### مسیر دوم: لیست دارای رکورد

اگر لیست خالی نباشد، تابع:

<div align='right' dir="rtl">

<span dir='rtl'>1. عنوان ستون‌های `DOMAIN`، `TYPE` و `VALUE` را می‌سازد.</span> <br>
<span dir='rtl'>2. یک خط جداکننده اضافه می‌کند.</span> <br>
<span dir='rtl'>3. برای هر رکورد، یک خط متنی تولید می‌کند.</span> <br>
<span dir='rtl'>4. خطوط را با <span dir='ltr'>`'\n'.join(lines)`</span> به یک رشته تبدیل می‌کند.</span>

</div>

تست‌های اول و دوم بررسی می‌کنند که محتوای مورد انتظار در این رشته وجود داشته باشد.

## ۶. آیا تست‌ها ظاهر جدول را به‌طور کامل بررسی می‌کنند؟

در وضعیت فعلی، تست‌ها روی **وجود محتوای مهم** تمرکز دارند. این روش در برابر تغییرات جزئی قالب‌بندی انعطاف‌پذیر است.

با این حال، اگر هدف این باشد که فاصله‌گذاری و ترتیب دقیق ستون‌ها نیز تضمین شود، می‌توان تست جداگانه‌ای برای خروجی کامل نوشت.

برای مثال، یک تست تکمیلی می‌تواند بررسی کند که خروجی دقیقاً با یک رشتهٔ مورد انتظار برابر باشد. چنین تستی باید خط جداکننده، فاصله‌ها و خط‌های جدید را هم در نظر بگیرد.

این کار زمانی مفید است که شکل خروجی ترمینال بخشی از قرارداد برنامه باشد و تغییر ناخواسته در ظاهر جدول قابل قبول نباشد.

## ۷. اجرای تست‌ها

برای اجرای فقط تست‌های Formatter:

```powershell
pytest tests/test_formatter.py
```

برای مشاهدهٔ نام تست‌ها و نتیجهٔ هرکدام:

```powershell
pytest -v tests/test_formatter.py
```

برای اجرای همهٔ تست‌های پروژه:

```powershell
pytest
```

## ۸. تمرین‌های پیشنهادی

۱. یک تست اضافه کنید که وجود یک رکورد `AAAA` را در خروجی بررسی کند.

۲. یک تست بنویسید که چند دامنهٔ متفاوت را به تابع بدهد و وجود همهٔ دامنه‌ها را در خروجی بررسی کند.

۳. توضیح دهید چرا تست نتیجهٔ خالی از `==` استفاده می‌کند، اما تست عنوان ستون‌ها از `in` استفاده می‌کند.

۴. بررسی کنید اگر یکی از عنوان‌های ستون از `VALUE` به `DATA` تغییر کند، کدام تست شکست می‌خورد و چرا.

۵. یک تست تکمیلی طراحی کنید که خروجی کامل جدول را با یک رشتهٔ مورد انتظار مقایسه کند. چه مزیتی دارد و چه هزینه‌ای از نظر نگهداری تست ایجاد می‌کند؟

## جمع‌بندی

در این درس یاد گرفتیم که:

<div align='right' dir="rtl">

<span dir='rtl'>• می‌توان داده‌های آزمایشی را مستقیماً با ساخت اشیای `DNSRecord` ایجاد کرد.</span> <br>
<span dir='rtl'>• عملگر `in` برای بررسی وجود بخش مشخصی از خروجی مناسب است.</span> <br>
<span dir='rtl'>• عملگر `==` برابری کامل خروجی را بررسی می‌کند.</span> <br>
<span dir='rtl'>• تست‌های فعلی، عنوان ستون‌ها و مقادیر رکوردها را بررسی می‌کنند.</span> <br>
<span dir='rtl'>• تابع Formatter برای لیست خالی پیام مشخصی ارائه می‌دهد.</span> <br>
<span dir='rtl'>• تست محتوای خروجی با تست قالب دقیق جدول دو هدف متفاوت دارد.</span>

</div>
