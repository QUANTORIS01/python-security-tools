<div align='right' dir='rtl'>

# بررسی کامل فایل `test_services.py`

# مقدمه

در جلسه قبل یاد گرفتیم چگونه:

```python
scan_port()
```

و

```python
scan_range()
```

را تست کنیم.

---

در آن فایل:

```text
رفتار واقعی شبکه
```

را آزمایش کردیم.

---

اما در این جلسه وارد فایل ساده‌تر اما بسیار مهمی می‌شویم:

```text
test_services.py
```

---

این فایل وظیفه دارد:

```python
detect_service()
```

را تست کند.

---

اگر یادت باشد در فایل:

```text
src/services.py
```

تابع زیر را داشتیم:

```python
def detect_service(port: int) -> str:
```

---

وظیفه این تابع:

```text
تبدیل شماره پورت
به
نام سرویس
```

بود.

---

مثال:

```python
22
```

↓

```python
ssh
```

---

یا:

```python
80
```

↓

```python
http
```

---

یا:

```python
443
```

↓

```python
https
```

---

حالا باید مطمئن شویم این تابع واقعاً درست کار می‌کند.

---

# محتوای فایل

```python
from src import detect_service


def test_detect_known_ssh_service():

    assert detect_service(22) == "ssh"


def test_detect_known_http_service():

    assert detect_service(80) == "http"


def test_detect_known_https_service():

    assert detect_service(443) == "https"


def test_detect_unknown_service():

    assert detect_service(65000) == "unknown"
```

---

# هدف این فایل چیست؟

هدف:

```text
بررسی صحت Service Detection
```

است.

---

یعنی مطمئن شویم:

```python
socket.getservbyport()
```

همان چیزی را برمی‌گرداند که انتظار داریم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import
</p>

```python
from src import detect_service
```

---

تابعی که می‌خواهیم تست کنیم.

---

# نوع تست

این فایل نمونه‌ای از:

```text
Known Values Testing
```

است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Known Values Testing چیست؟
</p>

یکی از قدیمی‌ترین روش‌های تست.

---

ایده بسیار ساده است.

---

ما از قبل جواب را می‌دانیم.

---

مثلاً:

```python
22
```

همیشه:

```python
ssh
```

است.

---

یا:

```python
80
```

همیشه:

```python
http
```

است.

---

پس می‌توانیم نتیجه واقعی را با نتیجه مورد انتظار مقایسه کنیم.

---

# تست اول

```python
def test_detect_known_ssh_service():
```

---

هدف:

```text
بررسی پورت SSH
```

---

داخل تست:

```python
assert detect_service(22) == "ssh"
```

---

جریان اجرا:

```python
detect_service(22)
```

↓

```python
socket.getservbyport(
    22,
    "tcp"
)
```

↓

```python
"ssh"
```

---

سپس:

```python
assert
```

بررسی می‌کند:

```python
"ssh" == "ssh"
```

---

نتیجه:

```text
PASS
```

---

# چرا SSH انتخاب شده؟

زیرا:

```python
22
```

یکی از شناخته‌شده‌ترین پورت‌های TCP است.

---

تقریباً در تمام سیستم‌ها ثبت شده است.

---

# تست دوم

```python
def test_detect_known_http_service():
```

---

هدف:

```text
بررسی سرویس HTTP
```

---

کد:

```python
assert detect_service(80) == "http"
```

---

جریان اجرا:

```python
detect_service(80)
```

↓

```python
"http"
```

---

سپس:

```python
assert
```

بررسی می‌کند:

```python
"http" == "http"
```

---

نتیجه:

```text
PASS
```

---

# چرا HTTP مهم است؟

زیرا:

```python
80
```

معروف‌ترین پورت وب است.

---

تقریباً تمام دیتابیس‌های سرویس سیستم عامل آن را می‌شناسند.

---

# تست سوم

```python
def test_detect_known_https_service():
```

---

هدف:

```text
بررسی HTTPS
```

---

کد:

```python
assert detect_service(443) == "https"
```

---

جریان:

```python
detect_service(443)
```

↓

```python
"https"
```

---

سپس:

```python
assert
```

بررسی می‌کند:

```python
"https" == "https"
```

---

نتیجه:

```text
PASS
```

---

# چرا HTTPS انتخاب شده؟

چون:

```python
443
```

یکی از مهم‌ترین پورت‌های اینترنت است.

---

امروزه تقریباً تمام وب‌سایت‌ها روی آن اجرا می‌شوند.

---

# تست چهارم

```python
def test_detect_unknown_service():
```

---

این مهم‌ترین تست فایل است.

---

چرا؟

---

چون داریم:

```text
حالت خطا
```

را بررسی می‌کنیم.

---

# ورودی

```python
65000
```

---

چرا این عدد انتخاب شده؟

---

زیرا:

```python
65000
```

معمولاً سرویس استاندارد ثبت‌شده‌ای ندارد.

---

پس:

```python
socket.getservbyport()
```

نمی‌تواند نامی برای آن پیدا کند.

---

در نتیجه:

```python
OSError
```

پرتاب می‌شود.

---

اگر یادت باشد در:

```python
services.py
```

نوشتیم:

```python
except OSError:
    return "unknown"
```

---

پس انتظار داریم:

```python
detect_service(65000)
```

↓

```python
"unknown"
```

---

تست:

```python
assert detect_service(65000) == "unknown"
```

---

این رفتار را بررسی می‌کند.

---

# چرا تست حالت خطا مهم‌تر است؟

بسیاری از برنامه‌نویسان فقط:

```text
حالت موفق
```

را تست می‌کنند.

---

مثلاً:

```python
22
80
443
```

---

اما در عمل:

```text
خطاها مهم‌تر هستند.
```

---

زیرا بیشتر باگ‌ها در شرایط غیرعادی ظاهر می‌شوند.

---

به همین دلیل وجود این تست بسیار ارزشمند است.

---

# آیا این تست روی همه سیستم‌عامل‌ها کار می‌کند؟

تقریباً بله.

---

زیرا:

```python
ssh
http
https
```

جزو سرویس‌های استاندارد هستند.

---

اما در پروژه‌های بسیار بزرگ معمولاً برای جلوگیری از وابستگی به سیستم عامل از:

```text
Mock
```

استفاده می‌شود.

---

ما هنوز به آن مرحله نرسیده‌ایم.

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

# این فایل چه چیزی را آموزش می‌دهد؟

این فایل یک نمونه عالی از:

```text
Testing Known Values
```

است.

---

یعنی:

```text
ورودی مشخص
↓
خروجی مشخص
↓
مقایسه
```

---

این نوع تست در پروژه‌های واقعی بسیار زیاد استفاده می‌شود.

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ Service Detection چگونه تست می‌شود <br>
✅ Known Values Testing چیست <br>
✅ تست سرویس SSH <br>
✅ تست سرویس HTTP <br>
✅ تست سرویس HTTPS <br>
✅ تست حالت Unknown <br>
✅ اهمیت تست شرایط خطا <br>
✅ نقش assert در مقایسه خروجی‌ها
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
tests/test_exporter.py
```

می‌شویم.

---

در آن یاد می‌گیریم:

<p dir='rtl'>
✅ تست فایل‌های JSON <br>
✅ Temporary File چیست <br>
✅ چگونه فایل‌های خروجی را بررسی کنیم <br>
✅ چگونه محتوای JSON را اعتبارسنجی کنیم <br>
✅ تست I/O در پایتون چگونه انجام می‌شود
</p>

</div>