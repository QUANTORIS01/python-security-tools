# بررسی کامل فایل `test_validator.py`

# مقدمه

تبریک 🎉

ما وارد آخرین بخش دوره شدیم:

```text
tests/
```

---

تا اینجای مسیر یاد گرفتیم:

✅ پایتون

✅ شبکه

✅ امنیت سایبری

✅ تمام فایل‌های src

---

اما هنوز یک مهارت بسیار مهم باقی مانده است.

---

# چرا تست می‌نویسیم؟

فرض کن پروژه امروز درست کار می‌کند.

---

فردا می‌خواهی قابلیت جدید اضافه کنی.

---

مثلاً:

```text
IPv6 Support
```

---

یا:

```text
UDP Scan
```

---

یا:

```text
Banner Detection Improvement
```

---

سؤال:

از کجا بفهمیم قابلیت جدید باعث خراب شدن کدهای قبلی نشده است؟

---

پاسخ:

```text
Testing
```

---

# تست چیست؟

تست یعنی:

```text
بررسی خودکار صحت عملکرد برنامه
```

---

به جای اینکه هر بار دستی تست کنیم:

```text
آیا IP درست کار می‌کند؟
آیا Port Range درست کار می‌کند؟
آیا Timeout درست کار می‌کند؟
```

---

یک فایل تست می‌نویسیم.

---

سپس:

```bash
pytest
```

را اجرا می‌کنیم.

---

و تمام تست‌ها خودکار اجرا می‌شوند.

---

# محتوای فایل

```python
from src import (
    validate_ip,
    validate_port_range,
    validate_timeout,
    validate_workers,
)


def test_valid_ip():
    assert validate_ip("127.0.0.1")


def test_invalid_ip():
    assert not validate_ip("999.999.999.999")


def test_valid_port_range():
    assert validate_port_range(1, 1000)


def test_invalid_port_range():
    assert not validate_port_range(5000, 1000)


def test_valid_timeout():
    assert validate_timeout(0.5)
    assert validate_timeout(1.0)


def test_invalid_timeout():
    assert not validate_timeout(0)
    assert not validate_timeout(-1)


def test_valid_workers():
    assert validate_workers(1)
    assert validate_workers(100)


def test_invalid_workers():
    assert not validate_workers(0)
    assert not validate_workers(-5)


def test_valid_timeout_boundary():
    assert validate_timeout(0.001)


def test_valid_workers_boundary():
    assert validate_workers(1)
```

---

# هدف فایل چیست؟

هدف:

```text
تست تمام توابع validator.py
```

است.

---

یعنی بررسی کنیم:

```python
validate_ip()

validate_port_range()

validate_timeout()

validate_workers()
```

واقعاً درست کار می‌کنند یا نه.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import
</p>

```python
from src import (
    validate_ip,
    validate_port_range,
    validate_timeout,
    validate_workers,
)
```

---

از فایل:

```text
src/__init__.py
```

ایمپورت شده‌اند.

---

دقیقاً همان کاری که در کد اصلی پروژه انجام دادیم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
pytest چگونه تست‌ها را پیدا می‌کند؟
</p>

قاعده pytest:

---

نام فایل:

```python
test_*
```

---

یا:

```python
*_test.py
```

---

نام تابع:

```python
test_*
```

---

پس:

```python
def test_valid_ip():
```

به صورت خودکار توسط pytest اجرا می‌شود.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
assert چیست؟
</p>

مهم‌ترین کلمه کلیدی تست‌نویسی.

---

```python
assert
```

یعنی:

```text
این شرط باید درست باشد.
```

---

مثال:

```python
assert 1 == 1
```

---

قبول می‌شود.

---

اما:

```python
assert 1 == 2
```

---

تست Fail می‌شود.

---

# اولین تست

```python
def test_valid_ip():
```

---

هدف:

```text
بررسی IP معتبر
```

---

داخل تست:

```python
assert validate_ip(
    "127.0.0.1"
)
```

---

تابع:

```python
validate_ip()
```

باید:

```python
True
```

برگرداند.

---

اگر:

```python
True
```

برگردد:

```text
PASS
```

---

اگر:

```python
False
```

برگردد:

```text
FAIL
```

---

# تست دوم

```python
def test_invalid_ip():
```

---

هدف:

```text
بررسی IP نامعتبر
```

---

ورودی:

```python
999.999.999.999
```

---

چنین IP وجود ندارد.

---

پس انتظار داریم:

```python
False
```

برگردد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
not در assert
</p>

```python
assert not validate_ip(...)
```

---

معادل:

```python
assert validate_ip(...) == False
```

---

است.

---

# تست Port Range معتبر

```python
def test_valid_port_range():
```

---

ورودی:

```python
1
1000
```

---

چون:

```python
1 <= 1000
```

---

و هر دو در بازه معتبر هستند.

---

باید:

```python
True
```

برگردد.

---

# تست Port Range نامعتبر

```python
def test_invalid_port_range():
```

---

ورودی:

```python
5000
1000
```

---

مشکل:

```python
start_port > end_port
```

---

پس باید:

```python
False
```

برگردد.

---

# تست Timeout معتبر

```python
def test_valid_timeout():
```

---

دو مقدار تست شده‌اند:

```python
0.5
```

---

و:

```python
1.0
```

---

هر دو:

```python
> 0
```

هستند.

---

پس معتبرند.

---

# چرا چند مقدار تست شده؟

این نکته بسیار مهم است.

---

برنامه‌نویسان حرفه‌ای فقط:

```python
یک مقدار
```

را تست نمی‌کنند.

---

بلکه:

```text
چند نمونه مختلف
```

را بررسی می‌کنند.

---

# تست Timeout نامعتبر

```python
def test_invalid_timeout():
```

---

ورودی اول:

```python
0
```

---

ورودی دوم:

```python
-1
```

---

تابع ما گفته بود:

```python
timeout > 0
```

---

پس هر دو باید:

```python
False
```

باشند.

---

# تست Worker معتبر

```python
def test_valid_workers():
```

---

مقدار اول:

```python
1
```

---

مقدار دوم:

```python
100
```

---

هر دو معتبر هستند.

---

# تست Worker نامعتبر

```python
def test_invalid_workers():
```

---

مقدار اول:

```python
0
```

---

مقدار دوم:

```python
-5
```

---

هر دو نامعتبر هستند.

---

# تست Boundary

حالا می‌رسیم به مهم‌ترین بخش فایل.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Boundary Testing چیست؟
</p>

یکی از مهم‌ترین تکنیک‌های تست‌نویسی.

---

معمولاً خطاها در:

```text
لبه‌های محدوده
```

رخ می‌دهند.

---

مثال:

```python
timeout > 0
```

---

سؤال:

کوچک‌ترین مقدار معتبر چیست؟

---

پاسخ:

```python
0.001
```

---

برای همین تست زیر نوشته شده است:

```python
def test_valid_timeout_boundary():
```

---

داخل آن:

```python
assert validate_timeout(
    0.001
)
```

---

این تست:

```text
مرز اعتبار Timeout
```

را بررسی می‌کند.

---

# تست مرز Worker

```python
def test_valid_workers_boundary():
```

---

تابع ما گفته بود:

```python
workers > 0
```

---

پس:

```python
1
```

کوچک‌ترین مقدار معتبر است.

---

برای همین:

```python
assert validate_workers(1)
```

نوشته شده است.

---

# چرا Boundary Test مهم است؟

فرض کن برنامه‌نویس اشتباه کند و بنویسد:

```python
workers >= 2
```

---

در این حالت:

```python
workers=1
```

خراب می‌شود.

---

اما تست Boundary سریعاً مشکل را پیدا می‌کند.

---

# خروجی pytest

اگر همه تست‌ها موفق شوند:

```bash
pytest
```

---

خروجی:

```text
========== 10 passed ==========
```

---

اگر یکی خراب شود:

```text
FAILED
```

نمایش داده می‌شود.

---

# این فایل چه نوع تستی است؟

این فایل:

```text
Unit Test
```

است.

---

چرا؟

---

چون هر تابع را:

```text
به صورت مستقل
```

تست می‌کند.

---

مثال:

```python
validate_ip()
```

---

بدون وابستگی به:

```python
scanner.py
```

---

یا:

```python
cli.py
```

---

# مزایای این فایل

✅ سریع

✅ ساده

✅ مستقل

✅ قابل فهم

✅ مناسب برای Regression Testing

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ Testing چیست <br>
✅ pytest چگونه کار می‌کند <br>
✅ assert چیست <br>
✅ Unit Test چیست <br>
✅ Boundary Testing چیست <br>
✅ تست مثبت (Positive Test) چیست <br>
✅ تست منفی (Negative Test) چیست <br>
✅ چگونه validator.py را تست کرده‌ایم
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
tests/test_scanner.py
```

می‌شویم.

---

آنجا یاد می‌گیریم:

<p dir='rtl'>
✅ Mock چیست <br>
✅ Monkeypatch چیست <br>
✅ چرا نباید در تست واقعاً شبکه را اسکن کنیم <br>
✅ چگونه Socket را شبیه‌سازی کنیم <br>
✅ تست حرفه‌ای توابع شبکه‌ای چگونه نوشته می‌شود
</p>
