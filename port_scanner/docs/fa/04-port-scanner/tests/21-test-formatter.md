# بررسی کامل فایل `test_formatter.py`

# مقدمه

به یکی از آخرین فایل‌های تست پروژه رسیدیم.

---

تا اینجا یاد گرفتیم:

✅ چگونه پورت‌ها اسکن می‌شوند

✅ چگونه سرویس‌ها تشخیص داده می‌شوند

✅ چگونه Banner دریافت می‌شود

✅ چگونه نتایج ساخته می‌شوند

---

اما هنوز یک سؤال باقی مانده است:

```text
این نتایج چگونه به کاربر نمایش داده می‌شوند؟
```

---

اگر یادت باشد در فایل:

```text
src/formatter.py
```

تابعی داشتیم:

```python
format_scan_results()
```

---

وظیفه این تابع:

```text
تبدیل نتایج اسکن
به یک جدول خوانا
```

بود.

---

مثلاً:

```python
[
    ScanResult(...),
    ScanResult(...)
]
```

---

را تبدیل می‌کرد به:

```text
PORT     STATUS   SERVICE      BANNER
------------------------------------------------------
22       OPEN     ssh          SSH-2.0-TestServer
80       OPEN     http         Apache/2.4.62
```

---

اکنون باید مطمئن شویم:

```python
format_scan_results()
```

در همه شرایط درست کار می‌کند.

---

محتوای فایل:

```python
from src import format_scan_results, ScanResult


def test_format_scan_results():
    results = [
        ScanResult(
            port=22,
            service="ssh",
            banner="SSH-2.0-TestServer",
        ),
        ScanResult(
            port=80,
            service="http",
            banner="Apache/2.4.62",
        ),
    ]
    output = format_scan_results(results)

    assert "PORT" in output
    assert "STATUS" in output
    assert "SERVICE" in output
    assert "BANNER" in output

    assert "22" in output
    assert "ssh" in output
    assert "SSH-2.0-TestServer" in output

    assert "80" in output
    assert "http" in output
    assert "Apache/2.4.62" in output


def test_format_scan_results_with_missing_banner():
    results = [
        ScanResult(
            port=53,
            service="domain",
            banner=None,
        )
    ]

    output = format_scan_results(results)

    assert "53" in output
    assert "domain" in output
    assert "-" in output


def test_format_scan_results_with_empty_results():
    output = format_scan_results([])
    assert output == "No open ports found."


def test_format_scan_results_truncates_long_banner():
    long_banner = "A" * 100
    results = [
        ScanResult(
            port=80,
            service="http",
            banner=long_banner,
        )
    ]
    output = format_scan_results(results)

    assert "..." in output
    assert long_banner not in output
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import ها
</p>

```python
from src import (
    format_scan_results,
    ScanResult
)
```

---

تابع مورد تست:

```python
format_scan_results()
```

---

و مدل داده:

```python
ScanResult
```

---

# هدف فایل چیست؟

بررسی:

✅ قالب‌بندی جدول

✅ نمایش اطلاعات پورت

✅ نمایش سرویس

✅ نمایش Banner

✅ مدیریت Banner خالی

✅ مدیریت لیست خالی

✅ کوتاه کردن Banner های طولانی

---

# تست اول

```python
def test_format_scan_results():
```

---

هدف:

```text
بررسی خروجی استاندارد جدول
```

است.

---

# ساخت داده تستی

```python
results = [
    ...
]
```

---

دو نتیجه اسکن می‌سازیم.

---

نتیجه اول:

```python
ScanResult(
    port=22,
    service="ssh",
    banner="SSH-2.0-TestServer"
)
```

---

نتیجه دوم:

```python
ScanResult(
    port=80,
    service="http",
    banner="Apache/2.4.62"
)
```

---

# اجرای تابع

```python
output =
    format_scan_results(
        results
    )
```

---

اکنون:

```python
output
```

یک رشته چندخطی است.

---

چیزی شبیه:

```text
PORT     STATUS   SERVICE      BANNER
------------------------------------------------------
22       OPEN     ssh          SSH-2.0-TestServer
80       OPEN     http         Apache/2.4.62
```

---

# بررسی Header

```python
assert "PORT" in output
```

---

بررسی می‌کنیم:

```text
ستون PORT
```

وجود داشته باشد.

---

همین کار برای:

```python
STATUS
```

---

```python
SERVICE
```

---

و

```python
BANNER
```

انجام می‌شود.

---

# چرا این تست مهم است؟

اگر کسی در آینده Header را تغییر دهد:

```python
"PORT"
↓
"PORTS"
```

---

این تست Fail می‌شود.

---

در نتیجه متوجه تغییر ناخواسته می‌شویم.

---

# بررسی اطلاعات پورت اول

```python
assert "22" in output
```

---

```python
assert "ssh" in output
```

---

```python
assert "SSH-2.0-TestServer" in output
```

---

یعنی:

```text
اطلاعات پورت 22
در جدول نمایش داده شده است.
```

---

# بررسی اطلاعات پورت دوم

```python
assert "80" in output
```

---

```python
assert "http" in output
```

---

```python
assert "Apache/2.4.62" in output
```

---

این تست مطمئن می‌شود:

```text
تمام داده‌ها
به خروجی منتقل شده‌اند.
```

---

# تست دوم

```python
def test_format_scan_results_with_missing_banner():
```

---

هدف:

```text
بررسی Banner خالی
```

است.

---

اگر یادت باشد در:

```python
formatter.py
```

داشتیم:

```python
banner =
    result.banner or "-"
```

---

یعنی:

```python
None
```

↓

```python
"-"
```

---

تبدیل می‌شود.

---

# داده تستی

```python
ScanResult(
    port=53,
    service="domain",
    banner=None
)
```

---

<p dir='rtl'>
Banner وجود ندارد.
</p>

---

# اجرای تابع

```python
output =
    format_scan_results(...)
```

---

# بررسی پورت

```python
assert "53" in output
```

---

# بررسی سرویس

```python
assert "domain" in output
```

---

# بررسی جایگزینی Banner

```python
assert "-" in output
```

---

این تست تضمین می‌کند:

```text
کاربر به جای None
علامت "-" را می‌بیند.
```

---

که بسیار خواناتر است.

---

# تست سوم

```python
def test_format_scan_results_with_empty_results():
```

---

هدف:

```text
بررسی حالت بدون پورت باز
```

است.

---

این حالت بسیار رایج است.

---

مثلاً:

```bash
python cli.py 192.168.1.50 1 100
```

---

و هیچ پورتی باز نباشد.

---

# اجرای تابع

```python
output =
    format_scan_results([])
```

---

لیست کاملاً خالی است.

---

# اگر یادت باشد

در:

```python
formatter.py
```

داشتیم:

```python
if not results:
    return "No open ports found."
```

---

# بررسی

```python
assert output ==
    "No open ports found."
```

---

این تست تضمین می‌کند:

```text
خروجی مناسبی
به کاربر نمایش داده می‌شود.
```

---

و جدول خالی تولید نمی‌شود.

---

# تست چهارم

```python
def test_format_scan_results_truncates_long_banner():
```

---

جذاب‌ترین تست فایل.

---

هدف:

```text
بررسی کوتاه‌سازی Banner های طولانی
```

است.

---

# ساخت Banner طولانی

```python
long_banner =
    "A" * 100
```

---

یعنی:

```text
AAAAAAAAAAAAAAAAAAAAAAAA...
```

---

صد کاراکتر A.

---

# ساخت نتیجه

```python
ScanResult(
    port=80,
    service="http",
    banner=long_banner
)
```

---

# اجرای تابع

```python
output =
    format_scan_results(...)
```

---

اگر یادت باشد در:

```python
formatter.py
```

داشتیم:

```python
if len(banner) > max_banner_length:
```

---

و سپس:

```python
banner =
    banner[: max_banner_length - 3]
    + "..."
```

---

یعنی:

```text
Banner کوتاه می‌شود.
```

---

# بررسی اول

```python
assert "..." in output
```

---

باید سه نقطه وجود داشته باشد.

---

# بررسی دوم

```python
assert long_banner not in output
```

---

این مهم‌ترین قسمت تست است.

---

یعنی:

```text
Banner کامل
نباید نمایش داده شود.
```

---

اگر کل رشته 100 کاراکتری هنوز در خروجی باشد:

```text
تست Fail می‌شود.
```

---

# چرا این قابلیت مهم است؟

فرض کن Banner این باشد:

```text
Microsoft-IIS/10.0 Build...
+ صدها کاراکتر دیگر
```

---

اگر کوتاه نشود:

```text
کل جدول ترمینال
به هم می‌ریزد.
```

---

برای همین:

```python
max_banner_length
```

تعریف کردیم.

---

# نوع تست‌های این فایل

این فایل چند نوع تست مختلف دارد:

---

<p dir='rtl' style='font-size:18px; font-wight:bold;'>
Content Testing
</p>

بررسی محتوا

```python
assert "ssh" in output
```

---

<p dir='rtl' style='font-size:18px; font-wight:bold;'>
Empty State Testing
</p>

بررسی حالت بدون داده

```python
[]
```

---

<p dir='rtl' style='font-size:18px; font-wight:bold;'>
Fallback Testing
</p>

بررسی مقدار جایگزین

```python
None
↓
"-"
```

---

<p dir='rtl' style='font-size:18px; font-wight:bold;'>
Truncation Testing
</p>

بررسی کوتاه‌سازی

```python
Long Banner
↓
...
```

---

# ارتباط این فایل با CLI

اگر یادت باشد در:

```python
cli.py
```

داشتیم:

```python
print(
    format_scan_results(
        results
    )
)
```

---

یعنی:

```python
format_scan_results()
```

آخرین مرحله قبل از نمایش خروجی است.

---

بنابراین اگر این تابع خراب شود:

```text
کل خروجی ترمینال خراب می‌شود.
```

---

برای همین وجود این تست‌ها بسیار مهم است.

---

# خروجی pytest

اگر همه چیز درست باشد:

```bash
pytest
```

---

خروجی:

```text
==== 4 passed ====
```

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ تست خروجی متنی <br>
✅ تست جدول ترمینال <br>
✅ تست Header ها <br>
✅ تست Banner خالی <br>
✅ تست لیست خالی <br>
✅ تست کوتاه‌سازی رشته‌های طولانی <br>
✅ Fallback Value چیست <br>
✅ Truncation چیست <br>
✅ اهمیت Formatter در CLI
</p>

---

# وضعیت فعلی پروژه

فایل‌های بررسی‌شده:

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
```

---

تقریباً به انتهای فصل تشریح تست‌ها رسیده‌ایم.

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
tests/test_csv_exporter.py
```

می‌شویم.

---

در آن یاد می‌گیریم:

✅ تست فایل‌های CSV

✅ تست محتوای CSV

✅ تست Header ها

✅ تست ردیف‌های خروجی

✅ کار با فایل‌های موقت در pytest

