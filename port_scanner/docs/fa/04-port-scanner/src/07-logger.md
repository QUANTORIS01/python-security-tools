# بررسی کامل فایل `logger.py`

# مقدمه

در جلسه قبل فایل:

```text
src/csv_exporter.py
```

را بررسی کردیم.

یاد گرفتیم:

<p dir='rtl'>
• CSV چیست <br>
• تفاوت CSV و JSON <br>
• csv.writer چگونه کار می‌کند <br>
• Header چیست <br>
• newline="" چیست <br>
• چرا خروجی CSV برای Excel مناسب است
</p>

---

اما یک سؤال مهم:

اگر کاربر برنامه را اجرا کند و بعداً بخواهد بفهمد:

<p dir='rtl'>
• چه زمانی اسکن انجام شده؟ <br>
• چه IPای اسکن شده؟ <br>
• چه پورت‌هایی پیدا شده‌اند؟ <br>
• آیا خطایی رخ داده است؟
</p>

چه کار باید بکنیم؟

---

اگر فقط از:

```python
print()
```

استفاده کنیم، بعد از بسته شدن ترمینال همه چیز از بین می‌رود.

---

به همین دلیل در نرم‌افزارهای حرفه‌ای از:

```text
Logging
```

استفاده می‌شود.

---

فایل:

```text
src/logger.py
```

مسئول همین کار است.

---

# محتوای فایل

```python
import logging


def setup_logger(filename: str) -> logging.Logger:
    """
    Configure and return a file logger.
    """
    logger = logging.getLogger("port_scanner")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            if handler.baseFilename == filename:
                return logger

    handler = logging.FileHandler(
        filename,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
```

---

# هدف این فایل چیست؟

هدف:

```text
ساخت و پیکربندی سیستم لاگ پروژه
```

است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Logging چیست؟
</p>

<p dir='rtl'>
Logging یعنی:
</p>

```text
ثبت اتفاقات مهم برنامه
```

---

مثال:

```text
[10:30] Scan Started
[10:30] Target: 127.0.0.1
[10:31] Port 80 Open
[10:31] Port 443 Open
[10:32] Scan Finished
```

---

این اطلاعات در فایل ذخیره می‌شوند.

---

# چرا Logging مهم است؟

تقریباً تمام نرم‌افزارهای حرفه‌ای دنیا لاگ تولید می‌کنند.

---

مثال:

<p dir='rtl'>
• Linux <br>
• Windows <br>
• Apache <br>
• Nginx <br>
• Docker <br>
• Kubernetes <br>
• Nmap <br>
• Wireshark
</p>

---

بدون لاگ:

```text
عیب‌یابی تقریباً غیرممکن است.
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import
</p>

```python
import logging
```

---

این ماژول یکی از قدرتمندترین کتابخانه‌های استاندارد پایتون است.

---

وظیفه:

```text
مدیریت لاگ‌ها
```

---

# تعریف تابع

```python
def setup_logger(
    filename: str
) -> logging.Logger:
```

---

## ورودی

```python
filename
```

---

مثال:

```python
"scan.log"
```

---

## خروجی

```python
logging.Logger
```

---

یعنی:

```text
یک Logger آماده استفاده
```

---

# داک استرینگ

```python
"""
Configure and return a file logger.
"""
```

---

معنی:

```text
یک لاگر فایل را پیکربندی و برگردان.
```

---

# ساخت Logger

```python
logger = logging.getLogger(
    "port_scanner"
)
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
getLogger چیست؟
</p>

این تابع یک Logger ایجاد می‌کند یا اگر قبلاً ساخته شده باشد همان را برمی‌گرداند.

---

نام لاگر:

```python
"port_scanner"
```

---

مثل شناسه اختصاصی لاگر است.

---

می‌توان تصور کرد:

```text
Logger Name = Port Scanner
```

---

# تعیین سطح لاگ

```python
logger.setLevel(
    logging.INFO
)
```

---

در سیستم Logging چند سطح مختلف وجود دارد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
DEBUG
</p>

```python
logging.DEBUG
```

---

برای اطلاعات بسیار جزئی.

---

مثال:

```text
Socket Created
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
INFO
</p>

```python
logging.INFO
```

---

برای اطلاعات عمومی.

---

مثال:

```text
Scan Started
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
WARNING
</p>

```python
logging.WARNING
```

---

هشدارها.

---

مثال:

```text
Slow Response
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
ERROR
</p>

```python
logging.ERROR
```

---

خطاها.

---

مثال:

```text
Connection Failed
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
CRITICAL
</p>

```python
logging.CRITICAL
```

---

خطاهای بسیار شدید.

---

مثال:

```text
Database Corrupted
```

---

در پروژه ما:

```python
logging.INFO
```

انتخاب شده است.

---

یعنی:

```text
INFO و بالاتر ثبت شوند.
```

---

# جلوگیری از انتشار لاگ

```python
logger.propagate = False
```

---

این خط بسیار مهم است.

---

اگر:

```python
False
```

نباشد،

ممکن است لاگ‌ها:

```text
دو بار
سه بار
چند بار
```

ثبت شوند.

---

به‌خصوص وقتی پروژه بزرگ شود.

---

این خط جلوی آن را می‌گیرد.

---

# بررسی Handlerهای موجود

```python
for handler in logger.handlers:
```

---

هر Logger می‌تواند چند Handler داشته باشد.

---

مثال:

```text
FileHandler
ConsoleHandler
NetworkHandler
...
```

---

این حلقه تمام Handlerها را بررسی می‌کند.

---

# بررسی نوع Handler

```python
if isinstance(
    handler,
    logging.FileHandler
):
```

---

یعنی:

```text
آیا این Handler از نوع FileHandler است؟
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
FileHandler چیست؟
</p>

<p dir='rtl'>
Handlerی که لاگ‌ها را داخل فایل ذخیره می‌کند.
</p>

---

# بررسی فایل

```python
if handler.baseFilename == filename:
```

---

یعنی:

```text
آیا همین فایل قبلاً ثبت شده است؟
```

---

مثال:

```python
scan.log
```

---

اگر قبلاً وجود داشته باشد:

---

```python
return logger
```

---

تابع همان Logger قبلی را برمی‌گرداند.

---

# چرا این کار مهم است؟

اگر این بخش وجود نداشت:

---

هر بار:

```python
setup_logger()
```

فراخوانی می‌شد،

یک FileHandler جدید ساخته می‌شد.

---

نتیجه:

```text
تکرار لاگ‌ها
```

---

مثال:

```text
Scan Started
Scan Started
Scan Started
```

---

این یکی از بهترین بخش‌های طراحی پروژه است.

---

# ساخت FileHandler

```python
handler = logging.FileHandler(
    filename,
    encoding="utf-8"
)
```

---

اینجا فایل لاگ ساخته می‌شود.

---

مثال:

```text
scan.log
```

---

تمام پیام‌ها داخل این فایل ذخیره خواهند شد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
UTF-8
</p>

```python
encoding="utf-8"
```

---

برای پشتیبانی از:

```text
فارسی
عربی
انگلیسی
```

---

است.

---

# ساخت Formatter

```python
formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(message)s"
)
```

---

<p dir='rtl'>
Formatter ظاهر لاگ‌ها را مشخص می‌کند.
</p>

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
asctime
</p>

```python
%(asctime)s
```

---

زمان ثبت لاگ.

---

مثال:

```text
2025-07-01 12:30:15
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
levelname
</p>

```python
%(levelname)s
```

---

سطح لاگ.

---

مثال:

```text
INFO
WARNING
ERROR
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
message
</p>

```python
%(message)s
```

---

متن پیام.

---

مثال:

```text
Scan Started
```

---

# نمونه خروجی واقعی

```text
2025-07-01 12:30:15 INFO Scan Started
```

---

# اتصال Formatter به Handler

```python
handler.setFormatter(
    formatter
)
```

---

از این لحظه:

تمام لاگ‌ها با همین قالب ذخیره می‌شوند.

---

# اتصال Handler به Logger

```python
logger.addHandler(
    handler
)
```

---

یعنی:

```text
این فایل را به Logger متصل کن.
```

---

از این لحظه Logger می‌تواند داخل فایل بنویسد.

---

# بازگرداندن Logger

```python
return logger
```

---

در نهایت Logger آماده استفاده به بخش‌های دیگر برنامه تحویل داده می‌شود.

---

# نمونه استفاده

```python
logger = setup_logger(
    "scan.log"
)
```

---

بعد:

```python
logger.info(
    "Scan Started"
)
```

---

فایل:

```text
scan.log
```

---

شامل:

```text
2025-07-01 12:30:15 INFO Scan Started
```

خواهد شد.

---

# نکته طراحی مهم

این فایل فقط یک وظیفه دارد:

```text
پیکربندی Logging
```

---

وظایف زیر را انجام نمی‌دهد:

❌ اسکن پورت

❌ تشخیص سرویس

❌ گرفتن بنر

❌ ذخیره JSON

❌ ذخیره CSV

---

این همان:

```text
Single Responsibility Principle
```

است.

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ Logging چیست <br>
✅ چرا لاگ مهم است <br>
✅ Logger چیست <br>
✅ Handler چیست <br>
✅ FileHandler چیست <br>
✅ Formatter چیست <br>
✅ INFO چیست <br>
✅ propagate چیست <br>
✅ addHandler چیست <br>
✅ ساختار یک فایل لاگ حرفه‌ای چگونه است
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
src/banner.py
```

می‌شویم.

در آن یاد می‌گیریم:

<p dir='rtl'>
• Banner Grabbing چیست <br>
• چرا هکرها و مدیران شبکه از آن استفاده می‌کنند <br>
• تفاوت Banner و Service چیست <br>
• Socket چگونه داده دریافت می‌کند <br>
• recv چیست <br>
• decode چیست <br>
• Timeout در Banner Grabbing چگونه کار می‌کند
</p>

