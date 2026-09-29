# بررسی کامل فایل `scanner.py`

## مقدمه

در جلسه قبل فایل:

```text
src/validator.py
```

را بررسی کردیم.

یاد گرفتیم:

<p dir='rtl'>
• اعتبارسنجی چیست <br>
• IP چگونه بررسی می‌شود <br>
• Port Range چیست <br>
• Timeout چیست <br>
• Worker چیست
</p>

اما هنوز پورت اسکنری نساخته‌ایم.

تا اینجا فقط مطمئن می‌شدیم ورودی‌ها درست هستند.

از این جلسه وارد قلب واقعی پروژه می‌شویم.

فایلی که قرار است بررسی کنیم:

```text
src/scanner.py
```

این فایل مهم‌ترین فایل پروژه است.

اگر این فایل را حذف کنیم:

```text
پورت اسکنر دیگر قادر به اسکن هیچ پورتی نخواهد بود.
```

---

# محتوای فایل

```python
import socket
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


def scan_port(ip: str, port: int, timeout: float = 0.5) -> bool:
    """
    Scan a single TCP port.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
        return result == 0
    except socket.error:
        return False


def scan_range(ip: str, start_port: int, end_port: int, timeout: float = 0.5, workers: int = 100) -> list[int]:
    """
    Scan a range of TCP ports.
    """
    open_ports = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(scan_port, ip, port, timeout): port
            for port in range(start_port, end_port + 1)
        }
        for future in as_completed(futures):
            port = futures[future]
            if future.result():
                open_ports.append(port)
    return sorted(open_ports)
```

---

# اولین Import

```python
import socket
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
socket چیست؟
</p>

ماژول اصلی ارتباطات شبکه در پایتون.

تمام عملیات TCP و UDP در پروژه ما از طریق همین ماژول انجام می‌شود.

---

## چرا به socket نیاز داریم؟

زیرا برای فهمیدن باز یا بسته بودن یک پورت باید سعی کنیم به آن متصل شویم.

مثلاً:

```text
127.0.0.1:80
```

اگر اتصال برقرار شد:

```text
پورت باز است.
```

اگر اتصال برقرار نشد:

```text
پورت بسته است.
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import دوم
</p>

```python
from concurrent.futures import ThreadPoolExecutor
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
Thread چیست؟
</p>

فرض کن می‌خواهیم:

```text
1000 پورت
```

را اسکن کنیم.

اگر یکی یکی اسکن شوند:

```text
Port 1
Port 2
Port 3
...
Port 1000
```

زمان زیادی طول می‌کشد.

---

اما اگر چندین اسکن همزمان انجام شوند:

```text
Port 1
Port 2
Port 3
Port 4
Port 5
...
```

سرعت بسیار بیشتر می‌شود.

---

به هر اجرای همزمان:

```text
Thread
```

می‌گویند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
ThreadPoolExecutor چیست؟
</p>

ابزاری برای مدیریت تعداد زیادی Thread.

---

به جای اینکه خودمان 100 , Thread بسازیم:

```python
Thread(...)
Thread(...)
Thread(...)
```

پایتون این کار را برایمان انجام می‌دهد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import سوم
</p>

```python
from concurrent.futures import as_completed
```

---

## وظیفه این تابع چیست؟

منتظر می‌ماند تا Threadها کار خود را تمام کنند.

هر Thread که زودتر تمام شود:

```python
as_completed()
```

نتیجه آن را برمی‌گرداند.

---

# تابع اول

```python
def scan_port(ip: str, port: int, timeout: float = 0.5) -> bool:
```

---

## هدف تابع

اسکن یک پورت.

مثال:

```python
scan_port("127.0.0.1", 80)
```

---

# داک استرینگ

```python
"""
Scan a single TCP port.
"""
```

---

این تابع فقط یک پورت را بررسی می‌کند.

---

# شروع بلوک try

```python
try:
```

---

ممکن است خطاهای شبکه رخ دهند.

مثال:

<p dir='rtl'>
• Host در دسترس نباشد <br>
• IP اشتباه باشد <br>
• Timeout رخ دهد
</p>

برای جلوگیری از کرش برنامه از:

```python
try
except
```

استفاده می‌کنیم.

---

# ساخت Socket

```python
with socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
) as sock:
```

---

این مهم‌ترین خط کل پروژه است.

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
AF_INET چیست؟
</p>

یعنی:

```text
IPv4
```

---

مثال:

```text
127.0.0.1
192.168.1.1
8.8.8.8
```

همگی IPv4 هستند.

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
SOCK_STREAM چیست؟
</p>

یعنی:

```text
TCP
```

---

پروژه ما:

```text
TCP Port Scanner
```

است.

---

اگر UDP می‌خواستیم:

```python
socket.SOCK_DGRAM
```

استفاده می‌شد.

---

# چرا از with استفاده کردیم؟

```python
with socket.socket(...) as sock:
```

---

وقتی کار تمام شود:

```python
sock.close()
```

خودکار اجرا می‌شود.

---

مزیت:

<p dir='rtl'>
• مصرف حافظه کمتر <br>
• جلوگیری از Resource Leak <br>
• کد تمیزتر
</p>

---

# تعیین Timeout

```python
sock.settimeout(timeout)
```

---

مثال:

```python
0.5
```

---

یعنی:

```text
حداکثر نیم ثانیه منتظر پاسخ بمان.
```

---

اگر پاسخ نرسد:

```text
اتصال متوقف می‌شود.
```

---

# تلاش برای اتصال

```python
result = sock.connect_ex((ip, port))
```

---

این خط عملاً پورت را اسکن می‌کند.

---

مثال:

```python
sock.connect_ex(
    ("127.0.0.1", 80)
)
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
connect_ex چه تفاوتی با connect دارد؟
</p>

```python
connect()
```

در صورت خطا Exception ایجاد می‌کند.

---

اما:

```python
connect_ex()
```

کد وضعیت برمی‌گرداند.

---

مثال:

```python
0
```

یعنی:

```text
اتصال موفق.
```

---

# بررسی نتیجه

```python
return result == 0
```

---

اگر:

```python
result
```

برابر صفر باشد:

```python
True
```

برمی‌گردد.

---

یعنی:

```text
پورت باز است.
```

---

در غیر این صورت:

```python
False
```

برمی‌گردد.

---

یعنی:

```text
پورت بسته است.
```

---

# مدیریت خطا

```python
except socket.error:
    return False
```

---

اگر هر خطای شبکه رخ دهد:

```python
False
```

برگردانده می‌شود.

---

# تابع دوم

```python
def scan_range(...)
```

---

## هدف تابع

اسکن تعداد زیادی پورت.

---

مثال:

```python
1 تا 1000
```

---

# ایجاد لیست نتایج

```python
open_ports = []
```

---

در این لیست:

```text
پورت‌های باز
```

ذخیره می‌شوند.

---

# ساخت Thread Pool

```python
with ThreadPoolExecutor(
    max_workers=workers
) as executor:
```

---

مثال:

```python
workers=100
```

---

یعنی:

```text
100 اسکن همزمان
```

---

# ساخت Taskها

```python
futures = {
    executor.submit(
        scan_port,
        ip,
        port,
        timeout
    ): port
    for port in range(
        start_port,
        end_port + 1
    )
}
```

---

این بخش یکی از حرفه‌ای‌ترین قسمت‌های پروژه است.

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
range
</p>

```python
range(
    start_port,
    end_port + 1
)
```

---

مثال:

```python
1
1000
```

---

خروجی:

```text
1
2
3
...
1000
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
submit
</p>

```python
executor.submit(...)
```

---

هر پورت را به یک Thread ارسال می‌کند.

---

مثال:

```python
scan_port(127.0.0.1, 80)
```

---

```python
scan_port(127.0.0.1, 81)
```

---

```python
scan_port(127.0.0.1, 82)
```

---

و همینطور ادامه پیدا می‌کند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Futures چیست؟
</p>

هر عملیات در حال اجرا:

```text
Future
```

نامیده می‌شود.

---

<p dir='rtl'>
Future یعنی:
</p>

```text
نتیجه‌ای که هنوز آماده نشده است.
```

---

# منتظر اتمام Threadها

```python
for future in as_completed(futures):
```

---

هر Thread که زودتر تمام شود:

```python
future
```

برگردانده می‌شود.

---

# پیدا کردن شماره پورت

```python
port = futures[future]
```

---

چون Future فقط نتیجه را دارد.

برای فهمیدن اینکه مربوط به کدام پورت بوده:

```python
futures
```

را نگهداری کرده‌ایم.

---

# بررسی نتیجه

```python
if future.result():
```

---

اگر خروجی:

```python
True
```

باشد:

---

یعنی:

```text
پورت باز است.
```

---

# افزودن به لیست

```python
open_ports.append(port)
```

---

مثال:

```python
[80, 443]
```

---

# مرتب‌سازی

```python
return sorted(open_ports)
```

---

چون Threadها نامنظم تمام می‌شوند.

ممکن است خروجی:

```python
[443, 80]
```

باشد.

---

پس مرتب می‌کنیم:

```python
[80, 443]
```

---

# نکته مهم معماری

این فایل فقط مسئول اسکن است.

---

وظایف زیر را انجام نمی‌دهد:

❌ نمایش خروجی

❌ ذخیره JSON

❌ ذخیره CSV

❌ دریافت Banner

❌ ثبت Log

---

این دقیقاً همان اصل مهم:

```text
Single Responsibility Principle
```

است.

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ Socket چیست <br>
✅ TCP چیست <br>
✅ AF_INET چیست <br>
✅ SOCK_STREAM چیست <br>
✅ Timeout چیست <br>
✅ connect_ex چگونه کار می‌کند <br>
✅ Thread چیست <br>
✅ ThreadPoolExecutor چیست <br>
✅ Future چیست <br>
✅ as_completed چیست <br>
✅ چگونه اسکن همزمان انجام می‌شود <br>
✅ چگونه نتایج مرتب می‌شوند
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
src/services.py
```

می‌شویم.

در آن یاد می‌گیریم:

<p dir='rtl'>
• Service Detection چیست <br>
• چرا پورت 80 معمولاً HTTP است <br>
• چرا پورت 443 معمولاً HTTPS است <br>
• IANA چیست <br>
• چگونه نام سرویس‌ها را تشخیص می‌دهیم
</p>

