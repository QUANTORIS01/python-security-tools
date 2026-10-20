<div align='right'>

[🇬🇧 English](/02-dns_lookup/docs/en/04-dns-lookup-analysis/tests/19-test_logger.md)

</div>

# ۱۹. تست‌نویسی برای سیستم Logging در پایتون

## هدف درس

در این درس، فایل `tests/test_logger.py` را بررسی می‌کنیم تا یاد بگیریم چگونه سیستم ثبت رویدادهای برنامه را آزمایش کنیم.

موضوعات اصلی:

<div align='right' dir="rtl">

<span dir='rtl'>• آشنایی با `logging` و `Logger`</span> <br>
<span dir='rtl'>• بررسی ایجاد فایل لاگ</span> <br>
<span dir='rtl'>• خواندن و بررسی پیام‌های ثبت‌شده</span> <br>
<span dir='rtl'>• جلوگیری از ایجاد Handlerهای تکراری</span> <br>
<span dir='rtl'>• استفاده از Fixture در `pytest`</span> <br>
<span dir='rtl'>• پاک‌سازی منابع پس از اجرای تست‌ها</span> <br>
<span dir='rtl'>• درک نقش <span dir='ltr'>`flush()`</span>، <span dir='ltr'>`close()`</span> و <span dir='ltr'>`removeHandler()`</span></span>

</div>

## کد کامل فایل تست

```python id="f9gjpz"
import logging
import pytest

from src import setup_logger


def test_setup_logger_creates_log_file(tmp_path):
    log_file = (tmp_path / 'dns.log')
    logger = setup_logger(str(log_file))
    logger.info('Test message')
    for handler in logger.handlers:
        handler.flush()
    assert log_file.exists()


def test_setup_logger_writes_log_message(tmp_path):
    log_file = (tmp_path / 'dns.log')
    logger = setup_logger(str(log_file))
    logger.info('Test message')
    for handler in logger.handlers:
        handler.flush()
    content = log_file.read_text(encoding='utf-8')
    assert 'Test message' in content


def test_setup_logger_does_not_duplicate_handlers(tmp_path):
    log_file = (tmp_path / 'dns.log')
    logger = setup_logger(str(log_file))
    initial_count = len(logger.handlers)
    setup_logger(str(log_file))
    assert (len(logger.handlers) == initial_count)


@pytest.fixture(autouse=True)
def cleanup_logger():
    yield

    logger = logging.getLogger('dns_lookup')
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)
```

## ۱. وارد کردن کتابخانه‌ها

```python
import logging
import pytest

from src import setup_logger
```

هر کدام از این importها نقش مشخصی دارند:

<div align='right' dir="rtl">

<span dir='rtl'>• `logging`: کتابخانهٔ استاندارد پایتون برای ثبت پیام‌های برنامه.</span> <br>
<span dir='rtl'>• `pytest`: ابزار اجرای تست‌ها و تعریف Fixtureها.</span> <br>
<span dir='rtl'>• `setup_logger`: تابع پروژه که Logger را پیکربندی می‌کند.</span>

</div>

تابع <span dir='ltr'>`setup_logger()`</span> در فایل `src/logger.py` قرار دارد. این تابع Loggerای با نام `dns_lookup` ایجاد یا دریافت می‌کند، سطح ثبت پیام را تنظیم می‌کند و یک `FileHandler` برای نوشتن در فایل به آن اضافه می‌کند؛ مگر اینکه Handlerای با مسیر فایل موردنظر از قبل وجود داشته باشد.

## ۲. تست اول: بررسی ایجاد فایل لاگ

کد تست:

```python
def test_setup_logger_creates_log_file(tmp_path):
    log_file = tmp_path / 'dns.log'
    logger = setup_logger(str(log_file))

    logger.info('Test message')

    for handler in logger.handlers:
        handler.flush()

    assert log_file.exists()
```

### مرحلهٔ اول: ساخت مسیر فایل

```python
log_file = tmp_path / 'dns.log'
```

<div align='right' dir="rtl">

<span dir='rtl'>`tmp_path` یک Fixture آماده در `pytest` است که مسیر یک پوشهٔ موقت را فراهم می‌کند.</span>

</div>

با استفاده از آن، فایل `dns.log` در مسیر موقت ساخته خواهد شد؛ بنابراین تست به فایل لاگ واقعی پروژه وابسته نیست.

### مرحلهٔ دوم: دریافت Logger

```python
logger = setup_logger(str(log_file))
```

تابع <span dir='ltr'>`setup_logger()`</span> یک Logger پیکربندی‌شده را برمی‌گرداند.

تبدیل `log_file` به رشته با <span dir='ltr'>`str()`</span> باعث می‌شود مسیر فایل به شکلی که تابع انتظار دارد ارسال شود.

### مرحلهٔ سوم: ثبت پیام

```python
logger.info('Test message')
```

متد <span dir='ltr'>`info()`</span> یک پیام با سطح اهمیت `INFO` ثبت می‌کند.

در تنظیمات پروژه، سطح Logger روی `logging.INFO` قرار دارد؛ بنابراین این پیام برای ثبت شدن واجد شرایط است.

### مرحلهٔ چهارم: اطمینان از نوشتن داده‌ها

```python
for handler in logger.handlers:
    handler.flush()
```

متد <span dir='ltr'>`flush()`</span> از Handler می‌خواهد داده‌های بافرشده را به مقصد منتقل کند.

این کار کمک می‌کند قبل از بررسی فایل، پیام‌های ثبت‌شده به فایل نوشته شده باشند.

### مرحلهٔ پنجم: بررسی وجود فایل

```python
assert log_file.exists()
```

این assertion بررسی می‌کند که مسیر فایل وجود داشته باشد.

نکتهٔ مهم: این تست به‌تنهایی محتوای فایل یا صحت پیام ثبت‌شده را بررسی نمی‌کند؛ این مسئولیت تست دوم است.

## ۳. تست دوم: بررسی نوشته شدن پیام در فایل

کد تست:

```python
def test_setup_logger_writes_log_message(tmp_path):
    log_file = tmp_path / 'dns.log'
    logger = setup_logger(str(log_file))

    logger.info('Test message')

    for handler in logger.handlers:
        handler.flush()

    content = log_file.read_text(encoding='utf-8')

    assert 'Test message' in content
```

این تست علاوه بر ایجاد فایل، بررسی می‌کند که پیام ثبت‌شده واقعاً در محتوای آن وجود داشته باشد.

### خواندن فایل

```python
content = log_file.read_text(encoding='utf-8')
```

متد <span dir='ltr'>`read_text()`</span> محتوای فایل را به‌صورت یک رشته می‌خواند.

استفاده از <span dir='ltr'>`encoding='utf-8'`</span> کدگذاری متن را مشخص می‌کند.

### بررسی پیام

```python
assert 'Test message' in content
```

عملگر `in` بررسی می‌کند که متن موردنظر در محتوای فایل وجود داشته باشد.

فایل لاگ پروژه علاوه بر پیام، اطلاعات دیگری مانند زمان ثبت و سطح اهمیت را نیز می‌تواند داشته باشد. به همین دلیل تست فقط وجود متن پیام را بررسی می‌کند، نه برابری کامل محتوای فایل با یک رشتهٔ ثابت.

## ۴. تست سوم: جلوگیری از Handlerهای تکراری

کد تست:

```python
def test_setup_logger_does_not_duplicate_handlers(tmp_path):
    log_file = tmp_path / 'dns.log'

    logger = setup_logger(str(log_file))
    initial_count = len(logger.handlers)

    setup_logger(str(log_file))

    assert len(logger.handlers) == initial_count
```

این تست رفتار مهمی از تابع <span dir='ltr'>`setup_logger()`</span> را بررسی می‌کند.

### مشکل Handlerهای تکراری چیست؟

در پایتون، فراخوانی دوبارهٔ `logging.getLogger('dns_lookup')` معمولاً همان شیء Logger نام‌گذاری‌شده را برمی‌گرداند.

اگر هر بار اجرای <span dir='ltr'>`setup_logger()`</span> یک Handler جدید به آن اضافه شود، ممکن است یک پیام چند بار در فایل ثبت شود.

برای جلوگیری از این وضعیت، پیاده‌سازی پروژه Handlerهای موجود را بررسی می‌کند:

```python
for handler in logger.handlers:
    if isinstance(handler, logging.FileHandler):
        if handler.baseFilename == filename:
            return logger
```

اگر Handler فایل با مسیر موردنظر از قبل وجود داشته باشد، تابع همان Logger را برمی‌گرداند و Handler دیگری اضافه نمی‌کند.

### چرا تعداد Handlerها را مقایسه می‌کنیم؟

```python
initial_count = len(logger.handlers)
```

این خط تعداد Handlerهای فعلی را ذخیره می‌کند.

سپس تابع دوباره فراخوانی می‌شود:

```python
setup_logger(str(log_file))
```

در پایان:

```python
assert len(logger.handlers) == initial_count
```

تست بررسی می‌کند که تعداد Handlerها افزایش پیدا نکرده باشد.

این تست از تغییرات ناخواسته در پیکربندی Logger جلوگیری می‌کند؛ هرچند به‌تنهایی تضمین نمی‌کند که تمام جزئیات Handlerها درست باشند یا پیام‌ها دقیقاً یک بار نوشته شوند.

<div align='right' dir="rtl">

## <span dir='rtl'>۵. Fixture پاک‌سازی: `cleanup_logger`</span>

</div>

بخش پایانی فایل تست:

```python
@pytest.fixture(autouse=True)
def cleanup_logger():
    yield

    logger = logging.getLogger('dns_lookup')
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)
```

این بخش از مهم‌ترین قسمت‌های تست است، زیرا منابعی را که Logger در اختیار گرفته است، پس از هر تست پاک‌سازی می‌کند.

<div align='right' dir="rtl">

### `@pytest.fixture`

</div>

<div align='right' dir="rtl">

<span dir='rtl'>Fixture در `pytest` می‌تواند کد آماده‌سازی یا پاک‌سازی را در اختیار تست‌ها قرار دهد.</span>

</div>

<div align='right' dir="rtl">

### `autouse=True`

</div>

این گزینه باعث می‌شود Fixture بدون نیاز به نوشتن نام آن در آرگومان تک‌تک تست‌ها اجرا شود.

بنابراین `cleanup_logger` به‌صورت خودکار برای تست‌های این مجموعه اعمال می‌شود.

### نقش `yield`

در Fixture، کد پیش از `yield` مرحلهٔ آماده‌سازی و کد پس از آن مرحلهٔ پس از اجرا را تشکیل می‌دهد.

در این فایل، کد پیش از `yield` کاری انجام نمی‌دهد. پس از پایان هر تست، اجرای Fixture از `yield` ادامه پیدا می‌کند و پاک‌سازی انجام می‌شود.

### دریافت Logger

```python
logger = logging.getLogger('dns_lookup')
```

همان Logger نام‌گذاری‌شده‌ای دریافت می‌شود که تابع پروژه از آن استفاده می‌کند.

### چرا از <span dir='ltr'>`logger.handlers[:]`</span> استفاده شده است؟

```python
for handler in logger.handlers[:]:
```

عبارت <span dir='ltr'>`logger.handlers[:]`</span> یک کپی از لیست Handlerها ایجاد می‌کند.

در ادامه، Handlerها از لیست اصلی حذف می‌شوند. پیمایش روی کپی کمک می‌کند هنگام تغییر لیست اصلی، حلقه دچار مشکل نشود.

### بستن و حذف Handler

```python
handler.close()
logger.removeHandler(handler)
```

این دو عملیات وظایف متفاوتی دارند:

<div align='right' dir="rtl">

<span dir='rtl'>• <span dir='ltr'>`close()`</span> منابع Handler، مانند فایل بازشده، را آزاد می‌کند.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`removeHandler()`</span> آن Handler را از Logger جدا می‌کند.</span>

</div>

اگر Handlerها پاک‌سازی نشوند، ممکن است تست‌های بعدی از Handlerهای باقی‌مانده استفاده کنند یا فایل‌ها بیش از حد انتظار باز بمانند.

## ۶. تفاوت <span dir='ltr'>`flush()`</span> و <span dir='ltr'>`close()`</span>

این دو متد هر دو به مدیریت نوشتن و منابع کمک می‌کنند، اما یکسان نیستند.

<div align='center' dir="rtl">

| متد | وظیفه |
|---|---|
| <span dir='ltr'>`flush()`</span> |<span dir='rtl'> انتقال داده‌های بافرشده به مقصد</span> |
| <span dir='ltr'>`close()`</span> |<span dir='rtl'> بستن Handler و آزاد کردن منابع آن</span> |
| <span dir='ltr'>`removeHandler()`</span> |<span dir='rtl'> جدا کردن Handler از Logger </span>|

</div>

در دو تست اول، <span dir='ltr'>`flush()`</span> پیش از خواندن فایل استفاده شده است.

در Fixture پاک‌سازی، <span dir='ltr'>`close()`</span> و <span dir='ltr'>`removeHandler()`</span> برای پایان دادن به استفاده از Handlerها و جدا کردن آن‌ها از Logger به کار می‌روند.

## ۷. ارتباط تست‌ها با معماری پروژه

فایل `src/logger.py` مسئول پیکربندی Logger است؛ اما فایل `tests/test_logger.py` رفتار آن را از بیرون بررسی می‌کند.

این تست‌ها سه جنبهٔ مهم را پوشش می‌دهند:

<div align='right' dir="rtl">

<span dir='rtl'>1. **ایجاد فایل:** Logger می‌تواند مقصد فایل خود را ایجاد کند.</span> <br>
<span dir='rtl'>2. **ثبت پیام:** پیام ثبت‌شده واقعاً در فایل دیده می‌شود.</span> <br>
<span dir='rtl'>3. **پیکربندی تکرارپذیر:** فراخوانی دوبارهٔ تابع برای همان مسیر، Handler تکراری اضافه نمی‌کند.</span>

</div>

<p dir='rtl'>
Fixture پاک‌سازی نیز کمک می‌کند تست‌ها منابع مشترک Logger را پس از اجرا آزاد کنند.
</p>

این موضوع به‌ویژه در پروژه‌هایی مهم است که چندین تست از یک Logger نام‌گذاری‌شده استفاده می‌کنند؛ زیرا Loggerها در سیستم `logging` معمولاً میان فراخوانی‌های مختلف برنامه به اشتراک گذاشته می‌شوند.

## ۸. نکتهٔ فنی دربارهٔ مسیر فایل

پیاده‌سازی فعلی، مسیر فایل Handler را با رشتهٔ ورودی مقایسه می‌کند:

```python
handler.baseFilename == filename
```

در برخی شرایط، مسیر نسبی و مسیر مطلق ممکن است به یک فایل اشاره کنند اما رشته‌های متفاوتی داشته باشند. در آن حالت، این مقایسه ممکن است Handler موجود را تشخیص ندهد.

این موضوع در تست فعلی که از مسیر `tmp_path` استفاده می‌کند لزوماً مشکل ایجاد نمی‌کند، اما می‌تواند فرصت مناسبی برای بهبود آینده باشد؛ مثلاً با یکسان‌سازی مسیرها پیش از مقایسه.

## ۹. اجرای تست‌ها

برای اجرای تست‌های Logger:

```powershell
pytest tests/test_logger.py
```

برای مشاهدهٔ نتیجهٔ تک‌تک تست‌ها:

```powershell
pytest -v tests/test_logger.py
```

برای اجرای تمام تست‌های پروژه:

```powershell
pytest
```

## ۱۰. تمرین‌های پیشنهادی

۱. تستی اضافه کنید که بررسی کند پیام ثبت‌شده شامل سطح `INFO` باشد.

۲. یک تست طراحی کنید که Logger را دو بار برای یک فایل تنظیم کند و سپس بررسی کند پیام آزمایشی دوبار در فایل نوشته نشده باشد.

۳. توضیح دهید چرا تست سوم تعداد Handlerها را قبل و بعد از فراخوانی دوباره مقایسه می‌کند.

۴. بررسی کنید اگر Fixture پاک‌سازی وجود نداشته باشد، چه مشکلی ممکن است هنگام اجرای چند تست پشت سر هم ایجاد شود.

۵. توضیح دهید چرا <span dir='ltr'>`handler.close()`</span> به‌تنهایی با `logger.removeHandler(handler)` یکسان نیست.

## جمع‌بندی

در این درس یاد گرفتیم که:

<div align='right' dir="rtl">

<span dir='rtl'>• `logging` برای ثبت رویدادهای برنامه استفاده می‌شود.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`flush()`</span> کمک می‌کند پیام‌های بافرشده پیش از خواندن فایل نوشته شوند.</span> <br>
<span dir='rtl'>• تست‌های Logger باید هم ایجاد فایل و هم محتوای آن را بررسی کنند.</span> <br>
<span dir='rtl'>• جلوگیری از Handlerهای تکراری، از ثبت چندبارهٔ پیام‌ها جلوگیری می‌کند.</span> <br>
<span dir='rtl'>• Fixture با `autouse=True` می‌تواند پاک‌سازی را به‌صورت خودکار انجام دهد.</span> <br>
<span dir='rtl'>• بستن Handler و جدا کردن آن از Logger دو مرحلهٔ متفاوت در مدیریت منابع هستند.</span>

</div>
