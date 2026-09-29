# بررسی کامل فایل `test_logger.py`

# مقدمه

به یکی از حرفه‌ای‌ترین بخش‌های پروژه رسیدیم.

---

تا اینجا یاد گرفتیم:

✅ اسکن پورت

✅ تشخیص سرویس

✅ دریافت Banner

✅ ساخت نتایج

✅ نمایش خروجی

✅ ذخیره JSON

✅ ذخیره CSV

---

اما هنوز یک قابلیت مهم باقی مانده بود:

```text
Logging
```

---

اگر یادت باشد در فایل:

```text
src/logger.py
```

تابع زیر را ساخته بودیم:

```python
setup_logger()
```

---

وظیفه این تابع:

```text
ثبت رویدادهای برنامه
در فایل لاگ
```

بود.

---

مثلاً:

```text
Scan started
```

---

یا:

```text
Scan completed
```

---

در فایل:

```text
scan.log
```

ذخیره می‌شدند.

---

اکنون باید مطمئن شویم:

<p dir='rtl'>
✅ فایل لاگ ساخته می‌شود <br>
✅ پیام‌ها داخل فایل ذخیره می‌شوند <br>
✅ Handler تکراری ایجاد نمی‌شود <br>
✅ تست‌ها روی هم اثر نمی‌گذارند
</p>

---

محتوای فایل:

```python
import logging

import pytest

from src import setup_logger


def test_setup_logger_creates_log_file(tmp_path):
    log_file = tmp_path / "scan.log"
    logger = setup_logger(str(log_file))
    logger.info("Test message")
    for handler in logger.handlers:
        handler.flush()
    assert log_file.exists()


def test_setup_logger_writes_log_message(tmp_path):
    log_file = tmp_path / "scan.log"
    logger = setup_logger(str(log_file))
    logger.info("Test message")
    for handler in logger.handlers:
        handler.flush()
    content = log_file.read_text(encoding="utf-8")
    assert "Test message" in content
    for handler in logger.handlers:
        handler.close()
    logger.handlers.clear()


def test_setup_logger_does_not_duplicate_handlers(tmp_path):
    log_file = tmp_path / "scan.log"
    logger = setup_logger(str(log_file))
    initial_handler_count = len(logger.handlers)
    setup_logger(str(log_file))
    assert len(logger.handlers) == initial_handler_count


@pytest.fixture(autouse=True)
def cleanup_logger():
    yield
    logger = logging.getLogger("port_scanner")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import ها
</p>

```python
import logging

import pytest

from src import setup_logger
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import اول
</p>

```python
import logging
```

---

برای دسترسی به Logger پروژه.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import دوم
</p>

```python
import pytest
```

---

برای Fixture ها.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import سوم
</p>

```python
from src import setup_logger
```

---

تابعی که قرار است تست شود.

---

# هدف فایل چیست؟

بررسی سه موضوع اصلی:

```text
ایجاد فایل لاگ
```

---

```text
ثبت پیام‌ها
```

---

```text
مدیریت Handler ها
```

---

# تست اول

```python
def test_setup_logger_creates_log_file(
    tmp_path
):
```

---

هدف:

```text
بررسی ساخته شدن فایل لاگ
```

است.

---

# ساخت مسیر فایل

```python
log_file =
    tmp_path / "scan.log"
```

---

مثلاً:

```text
/tmp/.../scan.log
```

---

# ساخت Logger

```python
logger =
    setup_logger(
        str(log_file)
    )
```

---

اگر یادت باشد:

```python
setup_logger()
```

یک:

```python
FileHandler
```

می‌ساخت.

---

# ثبت پیام

```python
logger.info(
    "Test message"
)
```

---

در این لحظه پیام باید در فایل ذخیره شود.

---

# چرا Flush لازم است؟

```python
for handler in logger.handlers:
    handler.flush()
```

---

نکته بسیار مهم.

---

سیستم Logging معمولاً داده‌ها را مستقیم روی دیسک نمی‌نویسد.

---

بلکه ابتدا در:

```text
Buffer
```

نگهداری می‌کند.

---

برای همین قبل از تست:

```python
flush()
```

فراخوانی می‌شود.

---

تا مطمئن شویم:

```text
همه داده‌ها روی فایل نوشته شده‌اند.
```

---

# بررسی فایل

```python
assert log_file.exists()
```

---

اگر فایل ساخته شده باشد:

```text
PASS
```

---

# این تست چه چیزی را ثابت می‌کند؟

این تست تضمین می‌کند:

```text
FileHandler
```

به درستی ایجاد شده است.

---

# تست دوم

```python
def test_setup_logger_writes_log_message(
    tmp_path
):
```

---

هدف:

```text
بررسی محتوای فایل لاگ
```

است.

---

تست قبلی فقط وجود فایل را بررسی می‌کرد.

---

اما:

```text
وجود فایل کافی نیست.
```

---

ممکن است فایل ساخته شود اما:

```text
خالی باشد.
```

---

برای همین این تست اضافه شده است.

---

# ساخت Logger

```python
logger =
    setup_logger(...)
```

---

# ثبت پیام

```python
logger.info(
    "Test message"
)
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Flush
</p>

```python
handler.flush()
```

---

تا پیام واقعاً روی دیسک ذخیره شود.

---

# خواندن فایل

```python
content =
    log_file.read_text(
        encoding="utf-8"
    )
```

---

اکنون کل محتوای فایل در:

```python
content
```

قرار دارد.

---

# بررسی محتوا

```python
assert "Test message" in content
```

---

اگر پیام داخل فایل باشد:

```text
PASS
```

---

# چرا این تست مهم است؟

چون بررسی می‌کند:

```text
Logger فقط فایل نمی‌سازد
بلکه واقعاً داده می‌نویسد.
```

---

# بستن Handler ها

```python
for handler in logger.handlers:
    handler.close()
```

---

سپس:

```python
logger.handlers.clear()
```

---

چرا؟

---

چون:

```python
Logger
```

در پایتون:

```text
Singleton-like
```

رفتار می‌کند.

---

یعنی:

```python
logging.getLogger(
    "port_scanner"
)
```

---

همیشه همان Logger قبلی را برمی‌گرداند.

---

اگر Handler ها بسته نشوند:

```text
تست‌های بعدی به مشکل می‌خورند.
```

---

# تست سوم

```python
def test_setup_logger_does_not_duplicate_handlers(
    tmp_path
):
```

---

مهم‌ترین تست فایل.

---

هدف:

```text
جلوگیری از Handler تکراری
```

است.

---

اگر یادت باشد در:

```python
logger.py
```

داشتیم:

```python
for handler in logger.handlers:
```

---

سپس:

```python
if isinstance(
    handler,
    logging.FileHandler
):
```

---

و:

```python
if handler.baseFilename == filename:
    return logger
```

---

این بخش برای جلوگیری از:

```text
Duplicate Handler
```

نوشته شده بود.

---

# مشکل چیست؟

فرض کن این اتفاق بیفتد:

```python
setup_logger("scan.log")
```

---

سپس دوباره:

```python
setup_logger("scan.log")
```

---

اگر کنترل نکنیم:

```text
دو FileHandler
```

ساخته می‌شود.

---

نتیجه:

```text
هر پیام
دو بار نوشته می‌شود.
```

---

مثلاً:

```text
Scan started
Scan started
```

---

که یک باگ بسیار رایج در Logging است.

---

# ساخت Logger

```python
logger =
    setup_logger(...)
```

---

# شمارش Handler ها

```python
initial_handler_count =
    len(logger.handlers)
```

---

مثلاً:

```python
1
```

---

# فراخوانی مجدد

```python
setup_logger(...)
```

---

اگر کد درست باشد:

```text
هیچ Handler جدیدی ساخته نمی‌شود.
```

---

# بررسی

```python
assert len(
    logger.handlers
) == initial_handler_count
```

---

اگر تعداد تغییر نکند:

```text
PASS
```

---

این تست تضمین می‌کند:

```text
Logger پروژه
دچار Handler Duplication نمی‌شود.
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Fixture پایانی
</p>

اکنون می‌رسیم به حرفه‌ای‌ترین بخش فایل.

---

```python
@pytest.fixture(
    autouse=True
)
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Fixture چیست؟
</p>

در pytest:

```text
کدی که قبل یا بعد از تست اجرا می‌شود.
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
autouse=True
</p>

یعنی:

```text
نیازی نیست دستی صدا زده شود.
```

---

قبل و بعد از هر تست:

```python
cleanup_logger()
```

اجرا می‌شود.

---

# ساختار Fixture

```python
def cleanup_logger():
```

---

# بخش اول

```python
yield
```

---

این یعنی:

```text
اول تست اجرا شود.
```

---

بعد از پایان تست:

```text
کدهای بعد از yield
اجرا شوند.
```

---

# گرفتن Logger

```python
logger =
    logging.getLogger(
        "port_scanner"
    )
```

---

همان Logger پروژه.

---

# حلقه پاکسازی

```python
for handler in logger.handlers[:]:
```

---

دقت کن:

```python
[:]
```

---

یک کپی از لیست می‌سازد.

---

چرا؟

---

چون همزمان:

```python
removeHandler()
```

در حال حذف عناصر است.

---

# بستن Handler

```python
handler.close()
```

---

فایل را می‌بندد.

---

# حذف Handler

```python
logger.removeHandler(
    handler
)
```

---

کاملاً از Logger حذف می‌شود.

---

# چرا این Fixture مهم است؟

بدون این Fixture:

```text
تست اول
```

↓

```text
Handler می‌سازد
```

↓

```text
تست دوم
```

↓

```text
همان Handler را می‌بیند
```

↓

```text
نتایج اشتباه
```

---

اما این Fixture تضمین می‌کند:

```text
هر تست
محیط کاملاً تمیز
و مستقل داشته باشد.
```

---

# مفاهیم حرفه‌ای که در این فایل یاد گرفتیم

<p dir='rtl'>
✅ FileHandler <br>
✅ Buffer <br>
✅ Flush <br>
✅ Log File Testing <br>
✅ Handler Management <br>
✅ Duplicate Handler Prevention <br>
✅ Fixture <br>
✅ autouse=True <br>
✅ yield Fixture <br>
✅ Test Isolation
</p>

---

# خروجی pytest

اگر همه چیز درست باشد:

```bash
pytest
```

---

خروجی:

```text
==== 3 passed ====
```

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ چگونه Logger را تست کنیم <br>
✅ چگونه فایل لاگ را بررسی کنیم <br>
✅ چگونه محتوای لاگ را اعتبارسنجی کنیم <br>
✅ Handler چیست <br>
✅ Duplicate Handler چیست <br>
✅ Fixture چیست <br>
✅ autouse=True چه کاری انجام می‌دهد <br>
✅ Test Isolation چیست <br>
✅ چرا پاکسازی بعد از تست اهمیت دارد
</p>

---

# وضعیت فعلی پروژه

فایل‌های تست بررسی‌شده:

```text
test_validator.py
test_scanner.py
test_services.py
test_exporter.py
test_cli.py
test_banner.py
test_models.py
test_results.py
test_formatter.py
test_csv_exporter.py
test_logger.py
```

---

تقریباً در آخرین قدم‌های فصل تشریح پروژه قرار داریم.

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

اگر فایل دیگری در پوشه:

```text
tests/
```

باقی مانده است، آن را بررسی می‌کنیم.

---

در غیر این صورت وارد:

```text
جلسه جمع‌بندی نهایی پروژه
```

خواهیم شد و کل معماری پورت اسکنر را از ابتدا تا انتها مرور می‌کنیم:

```text
CLI
↓
Validation
↓
Scanner
↓
Services
↓
Banner
↓
Results
↓
Formatter
↓
Exporter
↓
Logger
```
