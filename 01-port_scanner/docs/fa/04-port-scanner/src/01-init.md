<div dir="rtl">

# آشنایی با فایل <span dir='ltr'>`__init__.py`</span>

## مقدمه

تا اینجای دوره یاد گرفتیم:

<p dir='rtl'>
• پایتون چیست <br>
• شبکه چیست <br>
• امنیت سایبری چیست <br>
• پورت اسکنر چیست <br>
• چگونه پروژه Port Scanner را طراحی کردیم
</p>

از این جلسه وارد کدهای واقعی پروژه می‌شویم.

اولین فایلی که بررسی می‌کنیم:

```text
src/__init__.py
```

شاید این فایل در نگاه اول بسیار ساده به نظر برسد، اما نقش مهمی در معماری پروژه دارد.

---

## محتوای فایل

```python
from src.validator import validate_ip, validate_port_range, validate_timeout, validate_workers

from src.scanner import scan_port, scan_range

from src.services import detect_service

from src.exporter import export_json

from src.csv_exporter import export_csv

from src.logger import setup_logger

from src.banner import grab_banner

from src.models import ScanResult

from src.results import build_scan_results

from src.formatter import format_scan_results
```

---

# اصلاً فایل <span dir='ltr'>`__init__.py`</span> چیست؟

هر زمان در یک پوشه فایل:

```text
__init__.py
```

وجود داشته باشد، پایتون آن پوشه را به عنوان یک Package شناسایی می‌کند.

مثال:

```text
src/
│
├── __init__.py
├── validator.py
├── scanner.py
└── services.py
```

پایتون متوجه می‌شود که:

```text
src
```

یک پکیج است.

---

# چرا این فایل را خالی نگذاشتیم؟

بسیاری از پروژه‌ها فایل <span dir='ltr'>`__init__.py`</span> را خالی می‌گذارند.

اما ما از آن برای ساخت یک API داخلی استفاده کرده‌ایم.

یعنی می‌خواهیم کاربر بتواند بنویسد:

```python
from src import scan_range
```

به جای:

```python
from src.scanner import scan_range
```

---

# بررسی خط اول

```python
from src.validator import validate_ip, validate_port_range, validate_timeout, validate_workers
```

---

## این خط چه می‌کند؟

این خط چهار تابع را از فایل:

```text
validator.py
```

وارد پکیج می‌کند.

توابع:

```python
validate_ip
validate_port_range
validate_timeout
validate_workers
```

---

## نتیجه چیست؟

اکنون می‌توانیم بنویسیم:

```python
from src import validate_ip
```

به جای:

```python
from src.validator import validate_ip
```

---

# بررسی خط دوم

```python
from src.scanner import scan_port, scan_range
```

---

## این خط چه می‌کند؟

دو تابع اصلی اسکن را وارد می‌کند.

تابع اول:

```python
scan_port()
```

برای اسکن یک پورت.

تابع دوم:

```python
scan_range()
```

برای اسکن بازه‌ای از پورت‌ها.

---

# بررسی خط سوم

```python
from src.services import detect_service
```

---

## وظیفه این تابع چیست؟

زمانی که یک پورت باز پیدا شود:

```text
80
```

این تابع تشخیص می‌دهد که سرویس احتمالی آن چیست.

مثال:

```python
detect_service(80)
```

خروجی:

```python
"http"
```

---

# بررسی خط چهارم

```python
from src.exporter import export_json
```

---

## وظیفه این تابع چیست؟

نتایج اسکن را در فایل:

```text
JSON
```

ذخیره می‌کند.

مثال:

```python
export_json(data, "result.json")
```

---

# بررسی خط پنجم

```python
from src.csv_exporter import export_csv
```

---

## وظیفه این تابع چیست؟

خروجی را در فایل:

```text
CSV
```

ذخیره می‌کند.

مثال:

```text
port,service
80,http
443,https
```

---

# بررسی خط ششم

```python
from src.logger import setup_logger
```

---

## وظیفه این تابع چیست؟

سیستم ثبت لاگ را راه‌اندازی می‌کند.

مثال:

```text
scanner.log
```

---

# بررسی خط هفتم

```python
from src.banner import grab_banner
```

---

## وظیفه این تابع چیست؟

بنر سرویس را دریافت می‌کند.

مثال:

```text
SSH-2.0-OpenSSH_9.3
```

یا

```text
Apache/2.4.58
```

---

# بررسی خط هشتم

```python
from src.models import ScanResult
```

---

## این مورد تابع نیست

این یک کلاس است.

از آن برای نگهداری نتایج اسکن استفاده می‌کنیم.

مثال:

```python
ScanResult(
    port=80,
    service="http",
    banner="Apache"
)
```

---

# بررسی خط نهم

```python
from src.results import build_scan_results
```

---

## وظیفه این تابع چیست؟

خروجی خام اسکن را تبدیل به آبجکت‌های:

```python
ScanResult
```

می‌کند.

---

# بررسی خط دهم

```python
from src.formatter import format_scan_results
```

---

## وظیفه این تابع چیست؟

نتایج را برای نمایش در ترمینال آماده می‌کند.

مثال:

```text
PORT     STATUS   SERVICE
80       OPEN     http
443      OPEN     https
```

---

# چرا `cli.py` را اینجا Import نکردیم؟

فایل:

```text
cli.py
```

نقطه ورود برنامه است.

این فایل مستقیماً توسط کاربر اجرا می‌شود.

در تست‌ها نیز مستقیماً از خودش استفاده می‌کنیم.

به همین دلیل آن را داخل:

```python
__init__.py
```

قرار ندادیم.

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

✅ فایل `__init__.py` چیست

✅ پکیج در پایتون چیست

✅ چگونه توابع را Export می‌کنیم

✅ چرا Importها را متمرکز کردیم

✅ هر Import موجود در فایل چه کاربردی دارد

✅ چرا `cli.py` داخل این فایل قرار نگرفته است

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد اولین فایل واقعی پروژه می‌شویم:

```text
src/validator.py
```

در آن یاد می‌گیریم:

<p dir='rtl'>
• اعتبارسنجی چیست <br>
• چرا نباید به ورودی کاربر اعتماد کنیم <br>
• چگونه IP را بررسی می‌کنیم <br>
• چگونه Port Range را بررسی می‌کنیم <br>
• چگونه Timeout را بررسی می‌کنیم <br>
• چگونه Worker Count را بررسی می‌کنیم
</p>

</div>