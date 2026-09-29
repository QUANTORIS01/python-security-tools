<div align='right' dir='rtl'>

# بررسی کامل فایل `results.py`

# مقدمه

تا اینجای فصل پروژه تقریباً تمام قطعات اصلی پورت اسکنر را بررسی کرده‌ایم:

<p dir='rtl'>
✅ validator.py <br>
✅ scanner.py <br>
✅ services.py <br>
✅ exporter.py <br>
✅ csv_exporter.py <br>
✅ logger.py <br>
✅ banner.py <br>
✅ models.py
</p>

---

اما هنوز یک سؤال مهم باقی مانده است.

---

فرض کن اسکن انجام شده و این خروجی را داریم:

```python
[22, 80, 443]
```

---

این فقط یک لیست از شماره پورت‌ها است.

---

اما ما اطلاعات بیشتری می‌خواهیم.

---

برای هر پورت باید بدانیم:

```text
Port Number
Service Name
Banner
```

---

مثال:

```python
22 → ssh → OpenSSH
80 → http → Apache
443 → https → Nginx
```

---

سؤال:

چگونه این اطلاعات را کنار هم جمع کنیم؟

---

پاسخ:

```text
results.py
```

---

این فایل نقش:

```text
Data Processing Pipeline
```

را در پروژه بازی می‌کند.

---

# محتوای فایل

```python
from src import (
    grab_banner,
    ScanResult,
    detect_service
)


def build_scan_results(
    ip: str,
    open_ports: list[int],
    timeout: float = 1.0
) -> list[ScanResult]:
    """
    Build structured scan results for open ports.
    """

    results = []

    for port in open_ports:

        service = detect_service(port)

        banner = grab_banner(
            ip,
            port,
            timeout=timeout
        )

        results.append(
            ScanResult(
                port=port,
                service=service,
                banner=banner,
            )
        )

    return results
```

---

# هدف این فایل چیست؟

هدف:

```text
تبدیل لیست پورت‌های باز
به
نتایج ساختاریافته
```

است.

---

قبل:

```python
[22, 80, 443]
```

---

بعد:

```python
[
    ScanResult(
        port=22,
        service="ssh",
        banner="OpenSSH"
    ),

    ScanResult(
        port=80,
        service="http",
        banner="Apache"
    )
]
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Importها
</p>

```python
from src import (
    grab_banner,
    ScanResult,
    detect_service
)
```

---

اگر یادت باشد در فایل:

```python
src/__init__.py
```

تمام توابع مهم پروژه را Export کردیم.

---

برای همین اینجا به جای:

```python
from src.banner import grab_banner
from src.models import ScanResult
from src.services import detect_service
```

---

فقط می‌نویسیم:

```python
from src import ...
```

---

این یکی از مزایای ساختن یک Package واقعی است.

---

# تابع اصلی

```python
def build_scan_results(
```

---

اسم تابع:

```python
build_scan_results
```

---

معنی:

```text
نتایج نهایی اسکن را بساز
```

---

# پارامتر اول

```python
ip: str
```

---

مثال:

```python
"127.0.0.1"
```

---

یا:

```python
"192.168.1.10"
```

---

این IP برای Banner Grabbing استفاده می‌شود.

---

# پارامتر دوم

```python
open_ports: list[int]
```

---

مثال:

```python
[22, 80, 443]
```

---

خروجی فایل:

```python
scanner.py
```

همین است.

---

# پارامتر سوم

```python
timeout: float = 1.0
```

---

برای:

```python
grab_banner()
```

استفاده می‌شود.

---

# خروجی تابع

```python
list[ScanResult]
```

---

یعنی:

```python
[
    ScanResult(...),
    ScanResult(...),
]
```

---

نه:

```python
list[int]
```

---

نه:

```python
dict
```

---

بلکه:

```python
لیستی از مدل‌های ScanResult
```

---

# داک استرینگ

```python
"""
Build structured scan results for open ports.
"""
```

---

معنی:

```text
برای پورت‌های باز نتایج ساختاریافته ایجاد کن.
```

---

# ساخت لیست نتایج

```python
results = []
```

---

در ابتدا لیست خالی است.

---

مثال:

```python
[]
```

---

بعداً نتایج در آن ذخیره می‌شوند.

---

# شروع حلقه

```python
for port in open_ports:
```

---

فرض کن:

```python
open_ports = [22, 80]
```

---

دور اول:

```python
port = 22
```

---

دور دوم:

```python
port = 80
```

---

# تشخیص سرویس

```python
service = detect_service(port)
```

---

مثال:

```python
22
```

↓

```python
"ssh"
```

---

یا:

```python
80
```

↓

```python
"http"
```

---

این همان تابعی است که در:

```python
services.py
```

بررسی کردیم.

---

# گرفتن Banner

```python
banner = grab_banner(
    ip,
    port,
    timeout=timeout
)
```

---

مثال:

```python
grab_banner(
    "127.0.0.1",
    22
)
```

---

خروجی:

```python
"SSH-2.0-OpenSSH_9.5"
```

---

یا:

```python
None
```

---

این همان تابعی است که در:

```python
banner.py
```

بررسی کردیم.

---

# ساخت مدل

```python
ScanResult(
```

---

اینجا وارد مهم‌ترین بخش فایل می‌شویم.

---

اطلاعات جمع‌آوری‌شده:

```python
port
service
banner
```

---

داخل مدل قرار می‌گیرند.

---

# مقدار اول

```python
port=port
```

---

مثال:

```python
22
```

---

# مقدار دوم

```python
service=service
```

---

مثال:

```python
"ssh"
```

---

# مقدار سوم

```python
banner=banner
```

---

مثال:

```python
"OpenSSH"
```

---

یا:

```python
None
```

---

# نتیجه نهایی

```python
ScanResult(
    port=22,
    service="ssh",
    banner="OpenSSH"
)
```

---

# اضافه کردن به لیست

```python
results.append(...)
```

---

این شیء جدید به لیست نتایج اضافه می‌شود.

---

بعد از اولین دور:

```python
[
    ScanResult(...)
]
```

---

بعد از دومین دور:

```python
[
    ScanResult(...),
    ScanResult(...)
]
```

---

و همینطور ادامه پیدا می‌کند.

---

# پایان حلقه

وقتی همه پورت‌ها پردازش شدند:

```python
results
```

شامل تمام اطلاعات خواهد بود.

---

# بازگرداندن نتیجه

```python
return results
```

---

مثال:

```python
[
    ScanResult(
        port=22,
        service="ssh",
        banner="OpenSSH"
    ),

    ScanResult(
        port=80,
        service="http",
        banner="Apache"
    ),

    ScanResult(
        port=443,
        service="https",
        banner=None
    )
]
```

---

# چرا این فایل مهم است؟

این فایل نقش:

```text
Orchestrator
```

را دارد.

---

یعنی چند ماژول مختلف را به هم متصل می‌کند.

---

ارتباطات:

```text
scanner.py
      ↓

results.py

      ↓

services.py
      ↓

banner.py
      ↓

models.py
```

---

این فایل مرکز جمع‌آوری اطلاعات پروژه است.

---

# الگوی طراحی مورد استفاده

این فایل نمونه‌ای از:

```text
Data Transformation Pipeline
```

است.

---

ورودی:

```python
[22, 80, 443]
```

---

خروجی:

```python
[
    ScanResult(...),
    ScanResult(...),
]
```

---

یعنی داده خام تبدیل می‌شود به داده ساختاریافته.

---

این دقیقاً همان چیزی است که در پروژه‌های حرفه‌ای اتفاق می‌افتد.

---

# نکته معماری مهم

دقت کن:

---

این فایل:

<p dir='rtl'>
❌ پورت اسکن نمی‌کند <br>
❌ سرویس تشخیص نمی‌دهد <br>
❌ Banner نمی‌گیرد <br>
❌ خروجی ذخیره نمی‌کند
</p>

---

فقط:

```text
هماهنگ‌کننده اطلاعات
```

است.

---

این همان:

```text
Separation of Concerns
```

است که در معماری نرم‌افزار بسیار مهم است.

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ نقش فایل results.py چیست <br>
✅ چرا build_scan_results ساخته شده است <br>
✅ چگونه Service Detection انجام می‌شود <br>
✅ چگونه Banner Grabbing انجام می‌شود <br>
✅ چگونه ScanResult ساخته می‌شود <br>
✅ append چگونه کار می‌کند <br>
✅ Data Transformation Pipeline چیست <br>
✅ Orchestrator چیست <br>
✅ Separation of Concerns چیست
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
src/formatter.py
```

می‌شویم.

در آن یاد می‌گیریم:

<p dir='rtl'>
• چگونه خروجی را زیبا نمایش دهیم <br>
• Table Formatting چیست <br>
• String Formatting چیست <br>
• f-string چگونه کار می‌کند <br>
• چرا Banner کوتاه می‌شود <br>
• چرا Formatter یکی از مهم‌ترین بخش‌های تجربه کاربری است
</p>

</div>