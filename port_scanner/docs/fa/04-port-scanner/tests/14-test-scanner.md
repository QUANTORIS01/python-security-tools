<div align='right' dir='rtl'>

# بررسی کامل فایل `test_scanner.py`

# مقدمه

تا اینجا اولین تست‌های پروژه را بررسی کردیم:

```text
test_validator.py
```

---

در آن فایل:

```text
توابع ساده
```

را تست می‌کردیم.

---

مثلاً:

```python
validate_timeout()
```

---

یا:

```python
validate_workers()
```

---

اما اکنون وارد بخش جذاب‌تر تست‌نویسی می‌شویم.

---

فایل:

```text
test_scanner.py
```

---

چرا جذاب‌تر است؟

---

چون این بار داریم:

```text
کدهای شبکه‌ای (Networking Code)
```

را تست می‌کنیم.

---

و تست کردن کدهای شبکه‌ای همیشه سخت‌تر از توابع عادی است.

---

# هدف فایل چیست؟

هدف:

```text
تست scanner.py
```

است.

---

یعنی بررسی کنیم:

```python
scan_port()
```

و

```python
scan_range()
```

واقعاً درست کار می‌کنند.

---

# محتوای فایل

```python
import socket
import threading

from src import scan_port, scan_range
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import اول
</p>

```python
import socket
```

---

برای ساخت سرور تستی.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import دوم
</p>

```python
import threading
```

---

برای اجرای سرور در Thread جداگانه.

---

# چرا Thread لازم داریم؟

فرض کن این کد اجرا شود:

```python
server.accept()
```

---

این دستور:

```text
منتظر اتصال می‌ماند.
```

---

تا زمانی که یک Client وصل نشود:

```python
accept()
```

برنمی‌گردد.

---

اگر در همان Thread اجرا شود:

```text
کل تست قفل می‌شود.
```

---

برای همین از:

```python
Thread
```

استفاده می‌کنیم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import از پروژه
</p>

```python
from src import (
    scan_port,
    scan_range
)
```

---

توابعی که می‌خواهیم تست کنیم.

---

# تابع create_test_server

```python
def create_test_server():
```

---

این تابع:

```text
یک سرور TCP موقت
```

می‌سازد.

---

تمام تست‌های بعدی از این تابع استفاده می‌کنند.

---

# ساخت Socket

```python
server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
```

---

اگر یادت باشد در فصل شبکه گفتیم:

---

```python
AF_INET
```

↓

IPv4

---

```python
SOCK_STREAM
```

↓

TCP

---

پس:

```python
TCP Server
```

ساخته می‌شود.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Bind
</p>

```python
server.bind(
    ("127.0.0.1", 0)
)
```

---

نکته بسیار مهم:

```python
0
```

---

چرا پورت صفر؟

---

سیستم عامل خودش یک پورت آزاد انتخاب می‌کند.

---

مثلاً:

```text
54321
```

---

یا:

```text
61500
```

---

یا هر پورت آزاد دیگر.

---

مزیت:

```text
تست‌ها با هم تداخل ندارند.
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Listen
</p>

```python
server.listen(1)
```

---

یعنی:

```text
منتظر اتصال باش.
```

---

# گرفتن پورت واقعی

```python
port =
    server.getsockname()[1]
```

---

مثلاً:

```python
54321
```

---

حالا می‌دانیم سرور روی چه پورتی اجرا شده است.

---

# تابع داخلی

```python
def accept_connection():
```

---

وظیفه:

```text
پذیرفتن یک اتصال
```

---

# پذیرش اتصال

```python
connection, _ =
    server.accept()
```

---

زمانی که Scanner وصل شود:

```python
accept()
```

برمی‌گردد.

---

# بستن اتصال

```python
connection.close()
```

---

برای آزاد کردن منابع.

---

# مدیریت خطا

```python
except OSError:
```

---

اگر سرور بسته شود:

```python
accept()
```

ممکن است خطا بدهد.

---

این خطا نادیده گرفته می‌شود.

---

# ساخت Thread

```python
thread = threading.Thread(
```

---

هدف:

```text
اجرای سرور در پس‌زمینه
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
daemon=True
</p>

```python
daemon=True
```

---

یعنی:

```text
اگر برنامه تمام شد
این Thread هم متوقف شود.
```

---

# شروع Thread

```python
thread.start()
```

---

سرور اکنون فعال است.

---

# خروجی تابع

```python
return (
    server,
    port,
    thread
)
```

---

برای استفاده در تست‌ها.

---

# تست اول

```python
def test_scan_open_port():
```

---

هدف:

```text
بررسی تشخیص پورت باز
```

---

# ساخت سرور

```python
server, port, _ =
    create_test_server()
```

---

یک پورت باز واقعی داریم.

---

مثلاً:

```python
54321
```

---

# اجرای اسکن

```python
result =
    scan_port(
        "127.0.0.1",
        port
    )
```

---

چون پورت باز است:

```python
True
```

انتظار داریم.

---

# بررسی نتیجه

```python
assert result is True
```

---

اگر:

```python
False
```

برگردد:

```text
تست شکست می‌خورد.
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
finally
</p>

```python
finally:
    server.close()
```

---

بسیار مهم.

---

حتی اگر تست Fail شود:

```text
سرور بسته می‌شود.
```

---

# تست دوم

```python
def test_scan_closed_port():
```

---

هدف:

```text
بررسی تشخیص پورت بسته
```

---

# ساخت پورت

```python
server.bind(...)
```

---

# گرفتن شماره پورت

```python
port =
    server.getsockname()[1]
```

---

# بستن سرور

```python
server.close()
```

---

حالا:

```text
پورت بسته شده است.
```

---

# اسکن

```python
scan_port(...)
```

---

انتظار داریم:

```python
False
```

برگردد.

---

# تست سوم

```python
test_scan_single_port_range()
```

---

هدف:

```text
اسکن بازه‌ای شامل فقط یک پورت
```

---

مثال:

```python
1000
تا
1000
```

---

یعنی:

```text
فقط یک پورت
```

---

# انتظار

```python
[port]
```

---

خروجی باید دقیقاً شامل همان پورت باشد.

---

# تست چهارم

```python
test_scan_range_returns_sorted_ports()
```

---

یکی از مهم‌ترین تست‌های فایل.

---

# ساخت دو سرور

```python
server1
server2
```

---

مثلاً:

```python
55000
```

و

```python
53000
```

---

# تعیین بازه

```python
start_port =
    min(...)
```

---

```python
end_port =
    max(...)
```

---

# اجرای اسکن

```python
scan_range(...)
```

---

# انتظار

```python
sorted([
    port1,
    port2
])
```

---

چرا؟

---

چون در:

```python
scanner.py
```

در انتها نوشتیم:

```python
return sorted(open_ports)
```

---

این تست دقیقاً همان رفتار را بررسی می‌کند.

---

# تست پنجم

```python
test_scan_with_custom_timeout()
```

---

هدف:

```text
بررسی Timeout سفارشی
```

---

ورودی:

```python
timeout=1.0
```

---

انتظار:

```python
True
```

---

این تست بررسی می‌کند:

```text
تابع پارامتر timeout را درست دریافت می‌کند.
```

---

# تست ششم

```python
test_scan_with_different_worker_count()
```

---

هدف:

```text
بررسی Workers سفارشی
```

---

ورودی:

```python
workers=1
```

---

یعنی:

```text
بدون Parallel Scan
```

---

اگر تابع درست طراحی شده باشد:

```python
[port]
```

برمی‌گردد.

---

# نکته بسیار مهم

دقت کن.

---

این فایل:

```text
Mock
```

استفاده نمی‌کند.

---

و این کاملاً عمدی است.

---

چرا؟

---

چون:

```text
ما می‌خواهیم رفتار واقعی شبکه را تست کنیم.
```

---

برای همین:

```python
Socket واقعی
```

ساخته شده است.

---

به این نوع تست معمولاً می‌گویند:

```text
Integration-like Unit Test
```

---

یعنی:

```text
تست واحد
با استفاده از منابع واقعی
```

---

# خروجی pytest

اگر همه تست‌ها موفق شوند:

```bash
pytest
```

---

خروجی:

```text
====== 6 passed ======
```

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ تست کدهای شبکه‌ای <br>
✅ ساخت TCP Server موقت <br>
✅ Thread چیست <br>
✅ daemon Thread چیست <br>
✅ تست پورت باز <br>
✅ تست پورت بسته <br>
✅ تست Port Range <br>
✅ تست مرتب بودن خروجی <br>
✅ تست Timeout <br>
✅ تست Worker Count <br>
✅ تفاوت Mock و Real Resource Testing
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
tests/test_services.py
```

می‌شویم.

---

در آن یاد می‌گیریم:

<p dir='rtl'>
✅ چگونه Service Detection را تست کنیم <br>
✅ تست توابع وابسته به سیستم عامل <br>
✅ مفهوم Known Values Testing <br>
✅ چرا تست سرویس‌های معروف مثل HTTP و SSH مهم است
</p>

</div>