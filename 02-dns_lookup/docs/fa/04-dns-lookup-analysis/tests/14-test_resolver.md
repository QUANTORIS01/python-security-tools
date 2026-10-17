# ۱۴. تست‌نویسی برای DNS Resolver در پایتون

## هدف درس

در این درس، فایل `tests/test_resolver.py` را بررسی می‌کنیم تا یاد بگیریم چگونه عملکرد تابع <span dir='ltr'>`lookup_record()`</span> را بدون ارسال درخواست واقعی به سرورهای DNS آزمایش کنیم.

موضوعات اصلی این درس:

<div align='right' dir="rtl">

<span dir='rtl'>• آشنایی با `monkeypatch` در `pytest`</span> <br>
<span dir='rtl'>• شبیه‌سازی پاسخ‌های DNS با کلاس‌های ساده</span> <br>
<span dir='rtl'>• آزمایش پاسخ‌های تکی و چندگانه</span> <br>
<span dir='rtl'>• آزمایش مدیریت خطاهای DNS</span> <br>
<span dir='rtl'>• بررسی تفاوت بین خطای DNS و خطای Timeout</span> <br>
<span dir='rtl'>• نوشتن تست‌هایی مستقل از شبکه و اینترنت</span>

</div>

## کد کامل فایل تست

```python id="f9gjpz"
import dns.resolver
import pytest

from src import lookup_record
from src.exception import DNSTimeoutError


def test_lookup_a_record(monkeypatch):
    class FakeAnswer:
        def __str__(self):
            return '1.1.1.1'

    monkeypatch.setattr('dns.resolver.resolve', lambda *args, **kwargs: [FakeAnswer()])
    result = lookup_record('example.com', 'A')
    assert result == ['1.1.1.1']


def test_lookup_multiple_records(monkeypatch):
    class FakeAnswer:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return self.value

    monkeypatch.setattr(
        'dns.resolver.resolve', lambda *args, **kwargs: [FakeAnswer('1.1.1.1'), FakeAnswer('8.8.8.8')]
    )
    result = lookup_record('example.com', 'A')
    assert result == ['1.1.1.1', '8.8.8.8']


def test_lookup_nonexistent_domain(monkeypatch):
    def fake_resolve(*args, **kwargs):
        raise dns.resolver.NXDOMAIN

    monkeypatch.setattr('dns.resolver.resolve', fake_resolve)
    result = lookup_record('does-not-exist.com', 'A')
    assert result == []


def test_lookup_record_handles_no_answer(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.NoAnswer

    monkeypatch.setattr(dns.resolver, 'resolve', fake_resolve)
    assert lookup_record('example.com', 'TXT') == []


def test_lookup_record_handles_nxdomain(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.NXDOMAIN

    monkeypatch.setattr(dns.resolver, 'resolve', fake_resolve)
    assert lookup_record('invalid.test', 'A') == []


def test_lookup_record_handles_timeout(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.LifetimeTimeout

    monkeypatch.setattr(dns.resolver, 'resolve', fake_resolve)
    with pytest.raises(DNSTimeoutError):
        lookup_record('google.com', 'MX')
```

## ۱. وارد کردن کتابخانه‌ها

```python
import dns.resolver
import pytest

from src import lookup_record
from src.exception import DNSTimeoutError
```

هر کدام از این importها نقش مشخصی دارند:

<div align='right' dir="rtl">

<span dir='rtl'>• `dns.resolver`: دسترسی به انواع پاسخ‌ها و استثناهای کتابخانه `dnspython`.</span> <br>
<span dir='rtl'>• `pytest`: فراهم کردن ابزارهای تست، از جمله `monkeypatch` و `pytest.raises`.</span> <br>
<span dir='rtl'>• `lookup_record`: تابع اصلی که قرار است آزمایش شود.</span> <br>
<span dir='rtl'>• `DNSTimeoutError`: استثنای اختصاصی پروژه برای نشان دادن پایان مهلت درخواست DNS.</span>

</div>

این تست‌ها به جای بررسی مجدد پیاده‌سازی تابع، رفتار قابل مشاهده آن را بررسی می‌کنند.

## ۲. مفهوم Mock و Monkeypatch

هنگام اجرای یک DNS Lookup واقعی، نتیجه به شبکه، سرور DNS و وضعیت دامنه وابسته است. این وابستگی‌ها می‌توانند باعث شوند تست‌ها کند، ناپایدار یا وابسته به اینترنت باشند.

برای جلوگیری از این مشکل، تست‌ها از **شبیه‌سازی رفتار وابستگی‌ها** استفاده می‌کنند.

در `pytest`، ابزار `monkeypatch` امکان جایگزین کردن موقت یک تابع یا ویژگی را فراهم می‌کند.

برای مثال:

```python
monkeypatch.setattr(
    'dns.resolver.resolve',
    lambda *args, **kwargs: []
)
```

این دستور تابع `dns.resolver.resolve` را در طول تست با تابعی جایگزین می‌کند که یک لیست خالی برمی‌گرداند.

در نتیجه، هنگام اجرای <span dir='ltr'>`lookup_record()`</span> درخواست واقعی DNS ارسال نمی‌شود؛ بلکه نتیجه‌ای که تست تعیین کرده است برمی‌گردد.

پس از پایان تست، `pytest` تغییر ایجادشده را به‌صورت خودکار بازمی‌گرداند.

**نکته:** اصطلاح Mock به‌طور کلی به جایگزین‌های آزمایشی گفته می‌شود. در این فایل، از `monkeypatch` برای نصب این جایگزین‌ها استفاده شده است.

## ۳. آزمایش دریافت یک رکورد DNS

کد تست:

```python
def test_lookup_a_record(monkeypatch):
    class FakeAnswer:
        def __str__(self):
            return '1.1.1.1'

    monkeypatch.setattr(
        'dns.resolver.resolve',
        lambda *args, **kwargs: [FakeAnswer()]
    )

    result = lookup_record('example.com', 'A')

    assert result == ['1.1.1.1']
```

### بررسی مرحله‌به‌مرحله

**مرحله اول: ساخت پاسخ آزمایشی**

```python
class FakeAnswer:
    def __str__(self):
        return '1.1.1.1'
```

کلاس `FakeAnswer` یک پاسخ ساده و ساختگی ایجاد می‌کند.

متد ویژه <span dir='ltr'>`__str__()`</span> تعیین می‌کند که هنگام تبدیل شیء به رشته، مقدار `'1.1.1.1'` برگردانده شود.

این موضوع مهم است؛ زیرا تابع <span dir='ltr'>`lookup_record()`</span> در پیاده‌سازی پروژه از `str(answer)` استفاده می‌کند.

**مرحله دوم: جایگزینی تابع DNS**

```python
monkeypatch.setattr(
    'dns.resolver.resolve',
    lambda *args, **kwargs: [FakeAnswer()]
)
```

تابع اصلی DNS با یک تابع آزمایشی جایگزین می‌شود که یک پاسخ ساختگی برمی‌گرداند.

**مرحله سوم: اجرای تابع مورد آزمایش**

```python
result = lookup_record('example.com', 'A')
```

تابع <span dir='ltr'>`lookup_record()`</span> همان مسیری را طی می‌کند که در اجرای عادی طی می‌کرد، اما به جای شبکه با پاسخ ساختگی روبه‌رو می‌شود.

**مرحله چهارم: بررسی نتیجه**

```python
assert result == ['1.1.1.1']
```

این assertion بررسی می‌کند که خروجی تابع دقیقاً برابر با لیست مورد انتظار باشد.

## ۴. آزمایش چند رکورد DNS

کد تست:

```python
def test_lookup_multiple_records(monkeypatch):
    class FakeAnswer:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return self.value

    monkeypatch.setattr(
        'dns.resolver.resolve',
        lambda *args, **kwargs: [
            FakeAnswer('1.1.1.1'),
            FakeAnswer('8.8.8.8')
        ]
    )

    result = lookup_record('example.com', 'A')

    assert result == ['1.1.1.1', '8.8.8.8']
```

در این تست، کلاس `FakeAnswer` کمی انعطاف‌پذیرتر است:

```python
def __init__(self, value):
    self.value = value
```

مقدار پاسخ هنگام ساخت شیء تعیین می‌شود. متد <span dir='ltr'>`__str__()`</span> نیز همان مقدار را به شکل رشته برمی‌گرداند.

بنابراین می‌توان چند پاسخ متفاوت ساخت:

```python
FakeAnswer('1.1.1.1')
FakeAnswer('8.8.8.8')
```

این تست بررسی می‌کند که <span dir='ltr'>`lookup_record()`</span> همه پاسخ‌ها را به رشته تبدیل کند و آن‌ها را در قالب یک لیست برگرداند.

**چرا این تست مهم است؟**

یک DNS Query لزوماً فقط یک پاسخ ندارد. برای مثال، یک دامنه می‌تواند چند رکورد A داشته باشد. بنابراین تابع باید بتواند مجموعه‌ای از پاسخ‌ها را پردازش کند، نه فقط اولین پاسخ را.

## ۵. آزمایش دامنه‌ای که وجود ندارد

کد تست:

```python
def test_lookup_nonexistent_domain(monkeypatch):
    def fake_resolve(*args, **kwargs):
        raise dns.resolver.NXDOMAIN

    monkeypatch.setattr(
        'dns.resolver.resolve',
        fake_resolve
    )

    result = lookup_record('does-not-exist.com', 'A')

    assert result == []
```

در اینجا تابع جایگزین به جای برگرداندن پاسخ، استثنای `dns.resolver.NXDOMAIN` را ایجاد می‌کند.

<div align='right' dir="rtl">

<span dir='rtl'>`NXDOMAIN` بیان می‌کند که نام دامنه مورد درخواست در DNS وجود ندارد.</span>

</div>

طبق پیاده‌سازی `src/resolver.py`، این استثنا مدیریت می‌شود و تابع لیست خالی برمی‌گرداند:

```python
except (
    dns.resolver.NXDOMAIN,
    dns.resolver.NoAnswer,
    dns.resolver.NoNameservers
):
    return []
```

بنابراین تست بررسی می‌کند که نبودن دامنه، به‌جای متوقف کردن برنامه با یک استثنای مدیریت‌نشده، به نتیجه‌ای قابل استفاده تبدیل شود.

## ۶. آزمایش نبود پاسخ برای نوع رکورد درخواستی

کد تست:

```python
def test_lookup_record_handles_no_answer(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.NoAnswer

    monkeypatch.setattr(
        dns.resolver,
        'resolve',
        fake_resolve
    )

    assert lookup_record('example.com', 'TXT') == []
```

این حالت با `NXDOMAIN` تفاوت دارد.

<div align='right' dir="rtl">

<span dir='rtl'>• `NXDOMAIN`: نام دامنه در DNS وجود ندارد.</span> <br>
<span dir='rtl'>• `NoAnswer`: برای پرس‌وجوی انجام‌شده، پاسخ مورد انتظار موجود نیست.</span>

</div>

در تست بالا، تابع جایگزین استثنای `NoAnswer` را ایجاد می‌کند و تست بررسی می‌کند که خروجی <span dir='ltr'>`lookup_record()`</span> یک لیست خالی باشد.

در اینجا از شکل دیگری از <span dir='ltr'>`monkeypatch.setattr()`</span> استفاده شده است:

```python
monkeypatch.setattr(
    dns.resolver,
    'resolve',
    fake_resolve
)
```

در این شکل، به جای نام مسیر به صورت رشته، خود شیء `dns.resolver` و نام ویژگی `'resolve'` جداگانه ارائه می‌شوند.

هر دو روش برای جایگزین کردن این تابع قابل استفاده‌اند.

## ۷. آزمایش دوباره خطای NXDOMAIN

کد تست:

```python
def test_lookup_record_handles_nxdomain(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.NXDOMAIN

    monkeypatch.setattr(
        dns.resolver,
        'resolve',
        fake_resolve
    )

    assert lookup_record('invalid.test', 'A') == []
```

این تست نیز همان رفتار `NXDOMAIN` را بررسی می‌کند؛ با این تفاوت که نام تست و دامنه مورد استفاده متفاوت است.

از نظر پوشش رفتار، تست قبلی `test_lookup_nonexistent_domain` نیز همین حالت اصلی را بررسی می‌کند. وجود هر دو تست می‌تواند به خوانایی و نام‌گذاری صریح‌تر سناریوها کمک کند، اما هر دو خط اصلی مدیریت `NXDOMAIN` را هدف می‌گیرند.

این نکته نشان می‌دهد که **تعداد تست‌ها به‌تنهایی معیار کامل کیفیت نیست**؛ مهم است که هر تست چه رفتار مستقلی را بررسی می‌کند.

## ۸. آزمایش Timeout و استثنای اختصاصی پروژه

کد تست:

```python
def test_lookup_record_handles_timeout(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.LifetimeTimeout

    monkeypatch.setattr(
        dns.resolver,
        'resolve',
        fake_resolve
    )

    with pytest.raises(DNSTimeoutError):
        lookup_record('google.com', 'MX')
```

این تست مهم‌ترین تفاوت رفتاری در مدیریت خطاها را بررسی می‌کند.

در پروژه، تابع <span dir='ltr'>`lookup_record()`</span> هنگام وقوع `dns.resolver.LifetimeTimeout` چنین رفتاری دارد:

```python
except dns.resolver.LifetimeTimeout as exc:
    raise DNSTimeoutError('DNS query timed out') from exc
```

یعنی خطای کتابخانه `dnspython` به یک استثنای اختصاصی پروژه تبدیل می‌شود.

### چرا از <span dir='ltr'>`pytest.raises()`</span> استفاده می‌کنیم؟

```python
with pytest.raises(DNSTimeoutError):
    lookup_record('google.com', 'MX')
```

این عبارت بررسی می‌کند که اجرای کد داخل بلوک `with`، استثنای `DNSTimeoutError` را ایجاد کند.

اگر تابع بدون این استثنا برگردد یا استثنای دیگری ایجاد کند، تست موفق نخواهد بود.

همچنین توجه کنید که تست فقط نوع استثنا را بررسی می‌کند؛ متن پیام خطا یا زنجیره استثناها را بررسی نمی‌کند.

### چرا Timeout با پاسخ خالی تفاوت دارد؟

در طراحی فعلی پروژه:

<div align='right' dir="rtl">

<span dir='rtl'>• نبود دامنه، نبود پاسخ یا در دسترس نبودن نام‌سرورها به لیست خالی منتهی می‌شود.</span> <br>
<span dir='rtl'>• پایان مهلت درخواست DNS به استثنای `DNSTimeoutError` منتهی می‌شود.</span>

</div>

این تصمیم باعث می‌شود فراخواننده بتواند میان «پاسخی پیدا نشد» و «درخواست در مهلت تعیین‌شده کامل نشد» تفاوت بگذارد.

## ۹. ارتباط تست‌ها با معماری پروژه

جریان ساده عملکرد چنین است:

<div align='right' dir="rtl">

<span dir='rtl'>1. <span dir='ltr'>`lookup_record()`</span> درخواست DNS را از طریق <span dir='ltr'>`dns.resolver.resolve()`</span> انجام می‌دهد.</span> <br>
<span dir='rtl'>2. پاسخ‌های موفق به رشته تبدیل می‌شوند.</span> <br>
<span dir='rtl'>3. بعضی خطاهای DNS به لیست خالی تبدیل می‌شوند.</span> <br>
<span dir='rtl'>4. خطای Timeout به `DNSTimeoutError` تبدیل می‌شود.</span> <br>
<span dir='rtl'>5. فایل `test_resolver.py` این رفتارها را بدون نیاز به ارسال درخواست واقعی DNS بررسی می‌کند.</span>

</div>

این جداسازی ارزشمند است؛ چون منطق برنامه را می‌توان مستقل از وضعیت اینترنت آزمایش کرد.

## ۱۰. اجرای تست‌ها

برای اجرای فقط تست‌های Resolver:

```powershell
pytest tests/test_resolver.py
```

برای اجرای همه تست‌های پروژه:

```powershell
pytest
```

برای مشاهده جزئیات هر تست:

```powershell
pytest -v tests/test_resolver.py
```

## ۱۱. تمرین‌های پیشنهادی

۱. تستی اضافه کنید که وقتی <span dir='ltr'>`dns.resolver.resolve()`</span> یک لیست خالی برمی‌گرداند، خروجی <span dir='ltr'>`lookup_record()`</span> نیز لیست خالی باشد.

۲. تستی بنویسید که استثنای `dns.resolver.NoNameservers` را شبیه‌سازی کند و خروجی خالی را بررسی کند.

۳. در تست Timeout، علاوه بر نوع استثنا، پیام `DNS query timed out` را نیز بررسی کنید.

۴. تستی طراحی کنید که بررسی کند <span dir='ltr'>`lookup_record()`</span> با دو پاسخ ساختگی، هر دو مقدار را به همان ترتیب دریافت‌شده برمی‌گرداند.

۵. توضیح دهید چرا استفاده از `monkeypatch` باعث می‌شود تست‌ها کمتر به اینترنت و وضعیت سرورهای DNS وابسته باشند.

## جمع‌بندی

در این درس یاد گرفتیم که:

<div align='right' dir="rtl">

<span dir='rtl'>• `monkeypatch` برای جایگزینی موقت وابستگی‌ها در تست‌ها استفاده می‌شود.</span> <br>
<span dir='rtl'>• کلاس‌های ساده مانند `FakeAnswer` می‌توانند پاسخ‌های ساختگی اما قابل کنترل تولید کنند.</span> <br>
<span dir='rtl'>• تست‌های موفق، پردازش یک پاسخ و چند پاسخ را بررسی می‌کنند.</span> <br>
<span dir='rtl'>• خطاهای `NXDOMAIN` و `NoAnswer` در طراحی فعلی به لیست خالی تبدیل می‌شوند.</span> <br>
<span dir='rtl'>• خطای Timeout به استثنای اختصاصی `DNSTimeoutError` تبدیل می‌شود.</span> <br>
<span dir='rtl'>• تست‌های مستقل از شبکه، اجرای سریع‌تر و قابل تکرارتری دارند.</span>

</div>
