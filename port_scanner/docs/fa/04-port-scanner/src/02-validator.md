# بررسی کامل فایل `validator.py`

## مقدمه

در جلسه قبل با فایل:

```text
src/__init__.py
```

آشنا شدیم.

یاد گرفتیم که چگونه تمام توابع مهم پروژه را در یک نقطه متمرکز کردیم تا استفاده از آن‌ها راحت‌تر شود.

در این جلسه اولین فایل واقعی پروژه را بررسی می‌کنیم:

```text
src/validator.py
```

این فایل مسئول یکی از مهم‌ترین بخش‌های هر نرم‌افزار است:

```text
اعتبارسنجی ورودی‌ها (Validation)
```

---

# چرا اعتبارسنجی مهم است؟

فرض کن کاربر این دستور را اجرا کند:

```bash
python -m src.cli hello 80 443
```

یا:

```bash
python -m src.cli 192.168.1.1 -10 999999
```

یا:

```bash
python -m src.cli 192.168.1.1 1 1000 --workers -5
```

اگر برنامه این مقادیر را بررسی نکند:

<p dir='rtl'>
• خطا ایجاد می‌شود <br>
• برنامه کرش می‌کند <br>
• نتایج اشتباه تولید می‌شود <br>
• امنیت نرم‌افزار کاهش پیدا می‌کند
</p>

به همین دلیل قبل از انجام هر کاری باید مطمئن شویم ورودی‌ها معتبر هستند.

---

# محتوای فایل

```python
import socket


def validate_ip(ip: str) -> bool:
    """
    Validate IPv4 address.
    """
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def validate_port_range(start_port: int, end_port: int) -> bool:
    """
    Validate port range.
    """
    if not (0 <= start_port <= 65535):
        return False

    if not (0 <= end_port <= 65535):
        return False

    if start_port > end_port:
        return False

    return True


def validate_timeout(timeout: float) -> bool:
    """
    Validate connection timeout.
    """
    return timeout > 0


def validate_workers(workers: int) -> bool:
    """
    Validate number of concurrent workers.
    """
    return workers > 0
```

---

# خط اول

```python
import socket
```

---

## این خط چه کاری انجام می‌دهد؟

ماژول:

```python
socket
```

یکی از مهم‌ترین ماژول‌های استاندارد پایتون برای کارهای شبکه است.

پورت اسکنر ما نیز بر پایه همین ماژول ساخته شده است.

---

## کاربردهای socket

با این ماژول می‌توان:

<p dir='rtl'>
• اتصال شبکه برقرار کرد <br>
• IP را بررسی کرد <br>
• پورت‌ها را اسکن کرد <br>
• سرورها را پیدا کرد <br>
• اطلاعات شبکه را دریافت کرد
</p>

---

# تابع اول

```python
def validate_ip(ip: str) -> bool:
```

---

## هدف تابع

بررسی معتبر بودن IP.

---

## ورودی

```python
ip: str
```

یعنی:

```python
"127.0.0.1"
```

یا:

```python
"192.168.1.1"
```

---

## خروجی

```python
bool
```

یعنی:

```python
True
```

یا:

```python
False
```

---

# داک استرینگ

```python
"""
Validate IPv4 address.
"""
```

---

## داک استرینگ چیست؟

توضیحی است که برای برنامه‌نویسان نوشته می‌شود.

وقتی بعدها کسی پروژه را مطالعه کند متوجه می‌شود هدف این تابع چیست.

---

# بلوک try

```python
try:
```

---

## چرا از try استفاده می‌کنیم؟

ممکن است کاربر IP نامعتبر وارد کند.

مثال:

```python
"hello"
```

یا:

```python
"999.999.999.999"
```

در چنین شرایطی تابع شبکه خطا تولید می‌کند.

برای جلوگیری از توقف برنامه از:

```python
try
except
```

استفاده می‌کنیم.

---

# مهم‌ترین خط تابع

```python
socket.inet_aton(ip)
```

---

## این تابع چه کاری انجام می‌دهد؟

پایتون تلاش می‌کند IP را به فرمت باینری شبکه تبدیل کند.

اگر IP معتبر باشد:

```python
socket.inet_aton("127.0.0.1")
```

بدون خطا اجرا می‌شود.

---

## مثال

```python
socket.inet_aton("192.168.1.1")
```

موفق.

---

اما:

```python
socket.inet_aton("hello")
```

خطا تولید می‌کند.

---

# در صورت موفقیت

```python
return True
```

---

یعنی:

```text
IP معتبر است.
```

---

# در صورت خطا

```python
except socket.error:
```

---

اگر تبدیل IP ناموفق باشد وارد این بخش می‌شویم.

---

سپس:

```python
return False
```

---

یعنی:

```text
IP معتبر نیست.
```

---

# تابع دوم

```python
def validate_port_range(start_port: int, end_port: int) -> bool:
```

---

## هدف تابع

بررسی معتبر بودن بازه پورت.

---

# محدوده مجاز پورت

در TCP و UDP:

```text
0
تا
65535
```

مجاز هستند.

---

# شرط اول

```python
if not (0 <= start_port <= 65535):
    return False
```

---

## معنی شرط

اگر پورت شروع خارج از محدوده باشد:

```python
-1
```

یا:

```python
70000
```

نامعتبر است.

---

# شرط دوم

```python
if not (0 <= end_port <= 65535):
    return False
```

---

همین بررسی برای پورت پایان انجام می‌شود.

---

# شرط سوم

```python
if start_port > end_port:
    return False
```

---

## چرا این شرط مهم است؟

این بازه اشتباه است:

```python
1000
100
```

چون شروع از پایان بزرگ‌تر است.

---

# در نهایت

```python
return True
```

---

یعنی:

```text
بازه پورت معتبر است.
```

---

# تابع سوم

```python
def validate_timeout(timeout: float) -> bool:
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Timeout چیست؟
</p>

مدتی که برنامه برای پاسخ منتظر می‌ماند.

مثال:

```python
0.5
```

یعنی:

```text
نیم ثانیه
```

---

# بررسی

```python
return timeout > 0
```

---

اگر مقدار:

```python
0
```

یا:

```python
-1
```

باشد:

```python
False
```

برمی‌گردد.

---

چون زمان انتظار منفی یا صفر معنی ندارد.

---

# تابع چهارم

```python
def validate_workers(workers: int) -> bool:
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Worker چیست؟
</p>

تعداد Threadها یا کارگرهای همزمان.

---

مثال:

```python
100
```

یعنی:

```text
100 عملیات همزمان
```

---

# بررسی

```python
return workers > 0
```

---

اگر مقدار:

```python
0
```

یا:

```python
-10
```

باشد:

```python
False
```

برمی‌گردد.

---

## چرا این بررسی مهم است؟

اگر تعداد Workerها صفر باشد:

```text
هیچ اسکنی انجام نمی‌شود.
```

---

اگر منفی باشد:

```text
از نظر منطقی غیرممکن است.
```

---

# طراحی جالب این فایل

نکته مهمی که در این فایل دیده می‌شود:

تمام توابع فقط یک وظیفه دارند.

مثال:

```python
validate_ip()
```

فقط IP را بررسی می‌کند.

---

```python
validate_timeout()
```

فقط Timeout را بررسی می‌کند.

---

این روش یکی از اصول مهم طراحی نرم‌افزار است:

```text
Single Responsibility Principle
```

یعنی:

```text
هر تابع فقط یک مسئولیت داشته باشد.
```

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

✅ اعتبارسنجی چیست

✅ چرا اعتبارسنجی مهم است

✅ ماژول socket چیست

✅ تابع validate_ip چگونه کار می‌کند

✅ تابع validate_port_range چگونه کار می‌کند

✅ تابع validate_timeout چگونه کار می‌کند

✅ تابع validate_workers چگونه کار می‌کند

✅ اصل Single Responsibility چیست

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد قلب اصلی پورت اسکنر می‌شویم:

```text
src/scanner.py
```

در آن یاد می‌گیریم:

<p dir='rtl'>
• Socket چگونه ساخته می‌شود <br>
• چگونه به یک پورت وصل می‌شویم <br>
• چگونه تشخیص می‌دهیم پورت باز است یا بسته <br>
• Timeout چگونه اعمال می‌شود <br>
• ThreadPoolExecutor چگونه کار می‌کند <br>
• اسکن همزمان پورت‌ها چگونه انجام می‌شود
</p>

