# ۱۵. تست‌نویسی برای ساخت نتایج DNS در پایتون

## هدف درس

در این درس، فایل `tests/test_results.py` را بررسی می‌کنیم تا یاد بگیریم چگونه تابع <span dir='ltr'>`build_dns_results()`</span> را با استفاده از `pytest` آزمایش کنیم.

موضوعات اصلی:

<div align='right' dir="rtl">

<span dir='rtl'>• تست توابعی که به توابع دیگر وابسته‌اند</span> <br>
<span dir='rtl'>• استفاده از `monkeypatch` برای شبیه‌سازی خروجی یک تابع</span> <br>
<span dir='rtl'>• بررسی ساخت اشیای `DNSRecord`</span> <br>
<span dir='rtl'>• تست نتایج تکی، چندگانه و خالی</span> <br>
<span dir='rtl'>• مقایسهٔ لیست‌ها و اشیای پایتون با `assert`</span>

</div>

## کد کامل فایل تست

```python id="f9gjpz"
from src import DNSRecord, build_dns_results


def test_build_dns_results(monkeypatch):
    monkeypatch.setattr('src.results.lookup_record', lambda domain, record_type: ['8.8.8.8'])
    results = build_dns_results('google.com', 'A')
    assert results == [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        )
    ]


def test_build_dns_results_multiple_records(monkeypatch):
    monkeypatch.setattr('src.results.lookup_record', lambda domain, record_type: ['8.8.8.8', '8.8.4.4'])
    results = build_dns_results('google.com', 'A')
    assert results == [
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


def test_build_dns_results_empty(monkeypatch):
    monkeypatch.setattr('src.results.lookup_record', lambda domain, record_type: [])
    results = build_dns_results('google.com', 'A')
    assert results == []
```

## ۱. وارد کردن اجزای موردنیاز

```python
from src import DNSRecord, build_dns_results
```

در این فایل، دو جزء از پروژه وارد می‌شوند:

<div align='right' dir="rtl">

<span dir='rtl'>• `DNSRecord`: مدل داده‌ای که اطلاعات هر رکورد DNS را نگه می‌دارد.</span> <br>
<span dir='rtl'>• `build_dns_results`: تابعی که خروجی Resolver را به مجموعه‌ای از اشیای `DNSRecord` تبدیل می‌کند.</span>

</div>

رفتار تابع مورد آزمایش در فایل `src/results.py` به این صورت است:

```python
def build_dns_results(domain: str, record_type: str) -> list[DNSRecord]:
    values = lookup_record(domain, record_type)
    return [
        DNSRecord(
            domain=domain,
            record_type=record_type,
            value=value,
        )
        for value in values
    ]
```

این تابع ابتدا <span dir='ltr'>`lookup_record()`</span> را فراخوانی می‌کند و سپس برای هر مقدار دریافتی، یک شیء `DNSRecord` می‌سازد.

## ۲. چرا باید وابستگی تابع را شبیه‌سازی کنیم؟

تابع <span dir='ltr'>`build_dns_results()`</span> به تابع <span dir='ltr'>`lookup_record()`</span> وابسته است. اگر هنگام تست، Resolver واقعی اجرا شود، تست ممکن است به شبکه و پاسخ سرورهای DNS وابسته شود.

اما هدف این فایل، آزمایش خودِ فرایند ساخت نتایج است؛ نه آزمایش ارتباط شبکه‌ای.

بنابراین، خروجی <span dir='ltr'>`lookup_record()`</span> را شبیه‌سازی می‌کنیم تا بتوانیم دقیقاً مشخص کنیم تابع چه داده‌ای دریافت کند.

برای این کار از `monkeypatch` استفاده شده است.

## ۳. تست ساخت یک نتیجه

کد تست:

```python
def test_build_dns_results(monkeypatch):
    monkeypatch.setattr(
        'src.results.lookup_record',
        lambda domain, record_type: ['8.8.8.8']
    )

    results = build_dns_results('google.com', 'A')

    assert results == [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        )
    ]
```

### مرحلهٔ اول: جایگزینی تابع وابسته

```python
monkeypatch.setattr(
    'src.results.lookup_record',
    lambda domain, record_type: ['8.8.8.8']
)
```

این دستور، نام `lookup_record` را در فضای نام ماژول `src.results` موقتاً با یک تابع ساده جایگزین می‌کند.

تابع جایگزین با دریافت دامنه و نوع رکورد، همیشه این لیست را برمی‌گرداند:

```python
['8.8.8.8']
```

نکتهٔ مهم این است که مسیر جایگزینی، `src.results.lookup_record` است؛ یعنی همان نامی که تابع <span dir='ltr'>`build_dns_results()`</span> در ماژول `src.results` از آن استفاده می‌کند.

### مرحلهٔ دوم: اجرای تابع مورد آزمایش

```python
results = build_dns_results('google.com', 'A')
```

تابع، دامنهٔ `google.com` و نوع رکورد `A` را دریافت می‌کند. سپس مقدار شبیه‌سازی‌شده را به یک شیء `DNSRecord` تبدیل می‌کند.

### مرحلهٔ سوم: بررسی نتیجه

```python
assert results == [
    DNSRecord(
        domain='google.com',
        record_type='A',
        value='8.8.8.8',
    )
]
```

این دستور بررسی می‌کند که خروجی دقیقاً شامل یک شیء با سه مقدار مورد انتظار باشد:

<div align='center' dir="rtl">

| فیلد | مقدار مورد انتظار |
|---|---|
| `domain` | `google.com` |
| `record_type` | `A` |
| `value` | `8.8.8.8` |

</div>

چون `DNSRecord` با <span dir='ltr'>`@dataclass`</span> تعریف شده است، مقایسهٔ اشیا بر اساس مقادیر فیلدهای آن‌ها انجام می‌شود. بنابراین لازم نیست در این تست هر فیلد را جداگانه بررسی کنیم.

## ۴. تست ساخت چند نتیجه

کد تست:

```python
def test_build_dns_results_multiple_records(monkeypatch):
    monkeypatch.setattr(
        'src.results.lookup_record',
        lambda domain, record_type: ['8.8.8.8', '8.8.4.4']
    )

    results = build_dns_results('google.com', 'A')

    assert results == [
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
```

در این تست، تابع جایگزین دو مقدار برمی‌گرداند:

```python
['8.8.8.8', '8.8.4.4']
```

تابع <span dir='ltr'>`build_dns_results()`</span> باید برای هر مقدار، یک شیء جداگانه بسازد.

نتیجهٔ مورد انتظار شامل دو شیء `DNSRecord` است که هر دو دامنه و نوع رکورد یکسان دارند، اما مقدار `value` آن‌ها متفاوت است.

این تست دو ویژگی را بررسی می‌کند:

<p dir='rtl'>
1. برای هر مقدار دریافتی، یک شیء ساخته شود. <br>
2. ترتیب نتایج حفظ شود.
</p>

در پیاده‌سازی فعلی، این رفتار با استفاده از list comprehension انجام می‌شود:

```python
return [
    DNSRecord(
        domain=domain,
        record_type=record_type,
        value=value,
    )
    for value in values
]
```

عبارت `for value in values` باعث می‌شود تابع به ترتیب روی مقادیر حرکت کند و برای هر مقدار یک شیء بسازد.

## ۵. تست نتیجهٔ خالی

کد تست:

```python
def test_build_dns_results_empty(monkeypatch):
    monkeypatch.setattr(
        'src.results.lookup_record',
        lambda domain, record_type: []
    )

    results = build_dns_results('google.com', 'A')

    assert results == []
```

در این تست، تابع شبیه‌سازی‌شده هیچ مقداری برنمی‌گرداند.

بنابراین، `values` برابر با یک لیست خالی خواهد بود:

```python
[]
```

وقتی list comprehension روی لیست خالی اجرا شود، هیچ شیئی ساخته نمی‌شود و خروجی نیز لیست خالی خواهد بود.

این تست تضمین می‌کند که تابع در نبود پاسخ DNS، همچنان یک خروجی معتبر و قابل پیش‌بینی ارائه دهد.

## ۶. ارتباط این تست‌ها با معماری پروژه

جریان داده در این بخش از پروژه به شکل زیر است:

<div align='right' dir="rtl">

<span dir='rtl'>1. <span dir='ltr'>`lookup_record()`</span> مقادیر DNS را به صورت رشته برمی‌گرداند.</span> <br>
<span dir='rtl'>2. <span dir='ltr'>`build_dns_results()`</span> هر مقدار را در یک شیء `DNSRecord` قرار می‌دهد.</span> <br>
<span dir='rtl'>3. بخش‌های دیگر برنامه می‌توانند به‌جای کار با رشته‌های خام، با داده‌های ساخت‌یافته کار کنند.</span>

</div>

برای مثال، مقدار خام زیر:

```python
'8.8.8.8'
```

پس از پردازش به شیئی با فیلدهای مشخص تبدیل می‌شود:

```python
DNSRecord(
    domain='google.com',
    record_type='A',
    value='8.8.8.8',
)
```

این جداسازی باعث می‌شود مسئولیت دریافت پاسخ DNS از مسئولیت ساخت داده‌های نهایی جدا باشد.

## ۷. چرا این تست‌ها مفیدند؟

این سه تست، حالت‌های مهم تابع را پوشش می‌دهند:

<div align='center' dir="rtl">

| تست | رفتار بررسی‌شده |
|---|---|
| `test_build_dns_results` | ساخت یک رکورد |
| `test_build_dns_results_multiple_records` | ساخت چند رکورد و حفظ ترتیب |
| `test_build_dns_results_empty` | مدیریت نتیجهٔ خالی |

</div>

همچنین با شبیه‌سازی <span dir='ltr'>`lookup_record()`</span>، تست‌ها مستقل از درخواست واقعی DNS هستند. در نتیجه، تغییر وضعیت شبکه نباید باعث تغییر نتیجهٔ این تست‌ها شود.

البته این تست‌ها به‌تنهایی صحت ارتباط واقعی با DNS را تضمین نمی‌کنند؛ آن مسئولیت در تست‌های Resolver بررسی می‌شود.

## ۸. اجرای تست‌ها

برای اجرای تست‌های این فایل:

```powershell
pytest tests/test_results.py
```

برای اجرای تست‌ها همراه با نام هر تست:

```powershell
pytest -v tests/test_results.py
```

برای اجرای کل مجموعهٔ تست‌ها:

```powershell
pytest
```

## ۹. تمرین‌های پیشنهادی

۱. تستی اضافه کنید که تابع <span dir='ltr'>`build_dns_results()`</span> را با نوع رکورد `MX` اجرا کند و مقدار `record_type` را بررسی کند.

۲. یک تست بنویسید که سه مقدار ساختگی دریافت کند و بررسی کند خروجی دقیقاً شامل سه شیء `DNSRecord` باشد.

۳. توضیح دهید چرا در این فایل، <span dir='ltr'>`lookup_record()`</span> را شبیه‌سازی می‌کنیم، اما در تست‌های Resolver خود تابع <span dir='ltr'>`lookup_record()`</span> را اجرا می‌کنیم.

۴. اگر تابع <span dir='ltr'>`build_dns_results()`</span> به‌اشتباه فقط اولین مقدار را پردازش کند، کدام تست فعلی احتمالاً این مشکل را آشکار می‌کند؟ دلیل خود را توضیح دهید.

۵. تفاوت میان خروجی `list[str]` و `list[DNSRecord]` را توضیح دهید و بگویید استفاده از مدل داده‌ای چه کمکی به بخش‌های بعدی برنامه می‌کند.

## جمع‌بندی

در این درس یاد گرفتیم که:

<div align='right' dir="rtl">

<span dir='rtl'>• `monkeypatch` می‌تواند وابستگی‌های یک تابع را برای تست جایگزین کند.</span> <br>
<span dir='rtl'>• تست‌ها باید رفتار تابع موردنظر را جدا از مسئولیت‌های وابسته به آن بررسی کنند.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`build_dns_results()`</span> هر رشتهٔ دریافتی را به یک شیء `DNSRecord` تبدیل می‌کند.</span> <br>
<span dir='rtl'>• تست چند رکورد، تعداد و ترتیب نتایج را بررسی می‌کند.</span> <br>
<span dir='rtl'>• تست نتیجهٔ خالی تضمین می‌کند که تابع در نبود داده نیز خروجی معتبری داشته باشد.</span>

</div>
