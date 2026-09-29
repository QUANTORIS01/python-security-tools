<div dir='rtl'>

# بررسی کامل فایل `banner.py`

# مقدمه

تا اینجای مسیر یاد گرفتیم:

### فصل پایتون

<p dir='rtl'>
• توابع <br>
• شرط‌ها <br>
• حلقه‌ها <br>
• Exceptionها <br>
• فایل‌ها <br>
• JSON <br>
• CSV <br>
• ماژول‌ها
</p>

---

### فصل شبکه

<p dir='rtl'>
• IP چیست <br>
• Port چیست <br>
• TCP چیست <br>
• Socket چیست <br>
• Client و Server چیست <br>
• سرویس‌ها چگونه کار می‌کنند
</p>

---

### فصل امنیت سایبری

<p dir='rtl'>
• Reconnaissance <br>
• Enumeration <br>
• Attack Surface <br>
• CIA Triad <br>
• Threat Modeling <br>
• Logging <br>
• Vulnerability Assessment
</p>

---

و در جلسات قبلی فصل پروژه یاد گرفتیم:

<p dir='rtl'>
• validate_ip <br>
• validate_port_range <br>
• scan_port <br>
• scan_range <br>
• detect_service <br>
• export_json <br>
• export_csv <br>
• setup_logger
</p>

---

اما هنوز یک مشکل بزرگ داریم.

---

فرض کن پورت:

```text
80
```

باز باشد.

---

ما فقط می‌فهمیم:

```text
Port 80 Open
```

---

اما نمی‌دانیم:

```text
Apache؟
Nginx؟
IIS؟
```

---

یا مثلاً:

```text
Port 22 Open
```

---

اما نمی‌دانیم:

```text
OpenSSH؟
Dropbear؟
Cisco SSH؟
```

---

برای همین از چیزی به نام:

```text
Banner Grabbing
```

استفاده می‌کنیم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Banner چیست؟
</p>

وقتی به برخی سرویس‌ها متصل می‌شویم،

آن‌ها اطلاعاتی از خودشان ارسال می‌کنند.

---

مثال:

```text
SSH-2.0-OpenSSH_9.5
```

---

یا:

```text
220 FTP Server Ready
```

---

یا:

```text
Apache/2.4.58
```

---

این اطلاعات را:

```text
Banner
```

می‌گویند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Banner Grabbing چیست؟
</p>

یعنی:

```text
گرفتن اطلاعات شناسایی سرویس
```

---

هدف:

```text
تشخیص دقیق‌تر سرویس
```

---

# چرا در امنیت مهم است؟

تقریباً تمام ابزارهای حرفه‌ای این کار را انجام می‌دهند.

---

مثال:

<p dir='rtl'>
• Nmap <br>
• Masscan <br>
• Nessus <br>
• OpenVAS <br>
• Metasploit
</p>

---

زیرا:

```text
Port Open
```

اطلاعات کمی می‌دهد.

---

اما:

```text
Apache 2.4.58
```

اطلاعات بسیار بیشتری می‌دهد.

---

# محتوای فایل

```python
import socket


def grab_banner(
    ip: str,
    port: int,
    timeout: float = 1.0
) -> str | None:
    """
    Attempt to retrieve a TCP service banner.
    """
    try:
        with socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        ) as sock:

            sock.settimeout(timeout)

            sock.connect((ip, port))

            banner = sock.recv(1024)

        return (
            banner
            .decode(
                "utf-8",
                errors="ignore"
            )
            .strip()
            or None
        )

    except (
        socket.timeout,
        socket.error
    ):
        return None
```

---

# هدف تابع چیست؟

هدف:

```text
دریافت Banner از سرویس
```

است.

---

# تعریف تابع

```python
def grab_banner(
    ip: str,
    port: int,
    timeout: float = 1.0
) -> str | None:
```

---

# پارامتر اول

```python
ip
```

---

مثال:

```python
"192.168.1.10"
```

---

# پارامتر دوم

```python
port
```

---

مثال:

```python
22
```

---

# پارامتر سوم

```python
timeout
```

---

مثال:

```python
1.0
```

---

یعنی:

```text
حداکثر ۱ ثانیه صبر کن
```

---

# خروجی

```python
str | None
```

---

در پایتون جدید:

```python
|
```

به معنای:

```python
Union
```

است.

---

یعنی:

```python
str
```

یا

```python
None
```

---

مثال:

```python
"SSH-2.0-OpenSSH_9.5"
```

---

یا:

```python
None
```

---

# داک استرینگ

```python
"""
Attempt to retrieve a TCP service banner.
"""
```

---

معنی:

```text
تلاش کن Banner سرویس را دریافت کنی.
```

---

دقت کن:

```text
Attempt
```

نوشته شده است.

---

چرا؟

چون هیچ تضمینی وجود ندارد که سرویس Banner بدهد.

---

# بلوک try

```python
try:
```

---

در عملیات شبکه همیشه احتمال خطا وجود دارد.

---

مثال:

<p dir='rtl'>
• Timeout <br>
• Connection Refused <br>
• Reset Connection
</p>

---

برای همین از:

```python
try
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

این قسمت را در فایل scanner.py یاد گرفتیم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
AF_INET
</p>

```python
socket.AF_INET
```

---

یعنی:

```text
IPv4
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
SOCK_STREAM
</p>

```python
socket.SOCK_STREAM
```

---

یعنی:

```text
TCP
```

---

پس:

```text
یک TCP Socket برای IPv4 بساز
```

---

# تنظیم Timeout

```python
sock.settimeout(timeout)
```

---

مثال:

```python
1.0
```

---

یعنی:

```text
بیشتر از یک ثانیه منتظر نمان
```

---

چرا مهم است؟

---

فرض کن:

```text
Server پاسخ نمی‌دهد
```

---

اگر Timeout نداشته باشیم:

```text
برنامه ممکن است مدت زیادی گیر کند.
```

---

# اتصال به سرویس

```python
sock.connect(
    (
        ip,
        port
    )
)
```

---

مثال:

```python
sock.connect(
    (
        "127.0.0.1",
        22
    )
)
```

---

یعنی:

```text
به SSH متصل شو.
```

---

# تفاوت connect و connect_ex

در scanner.py داشتیم:

```python
connect_ex()
```

---

اما اینجا داریم:

```python
connect()
```

---

چرا؟

---

زیرا:

```python
connect_ex()
```

فقط وضعیت اتصال را برمی‌گرداند.

---

اما:

```python
connect()
```

اتصال واقعی برقرار می‌کند.

---

و بعد از اتصال می‌توانیم داده دریافت کنیم.

---

# دریافت Banner

```python
banner = sock.recv(1024)
```

---

این مهم‌ترین خط فایل است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
recv چیست؟
</p>

مخفف:

```text
Receive
```

---

یعنی:

```text
دریافت داده
```

---

# عدد 1024 چیست؟

```python
recv(1024)
```

---

یعنی:

```text
حداکثر 1024 بایت دریافت کن
```

---

اگر سرویس این را ارسال کند:

```text
SSH-2.0-OpenSSH_9.5
```

---

در متغیر:

```python
banner
```

ذخیره می‌شود.

---

اما یک نکته مهم وجود دارد.

---

# نوع داده برگشتی

```python
recv()
```

رشته برنمی‌گرداند.

---

برمی‌گرداند:

```python
bytes
```

---

مثال:

```python
b"SSH-2.0-OpenSSH_9.5"
```

---

دقت کن:

```python
b
```

اول رشته وجود دارد.

---

یعنی:

```text
داده باینری
```

---

# تبدیل Bytes به String

```python
banner.decode(
    "utf-8",
    errors="ignore"
)
```

---

اینجا داده باینری تبدیل می‌شود به:

```python
str
```

---

مثال:

قبل:

```python
b"SSH-2.0-OpenSSH_9.5"
```

---

بعد:

```python
"SSH-2.0-OpenSSH_9.5"
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
UTF-8
</p>

```python
"utf-8"
```

---

مشخص می‌کند:

```text
چگونه بایت‌ها را تبدیل کنیم.
```

---

<p align='right' dir='ltr' style='font-size:32px; font-wight:bold;'>
errors="ignore"
</p>

این قسمت بسیار مهم است.

---

برخی سرویس‌ها داده خراب ارسال می‌کنند.

---

مثال:

```python
b"\xff\xfe\xab"
```

---

اگر بنویسیم:

```python
decode("utf-8")
```

ممکن است خطا بگیریم.

---

اما:

```python
errors="ignore"
```

باعث می‌شود:

```text
بایت‌های خراب نادیده گرفته شوند.
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
strip
</p>

```python
.strip()
```

---

حذف:

```text
Space
Tab
Newline
```

از ابتدا و انتهای رشته.

---

مثال:

قبل:

```python
"SSH-2.0-OpenSSH_9.5\r\n"
```

---

بعد:

```python
"SSH-2.0-OpenSSH_9.5"
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
or None
</p>

```python
or None
```

---

این بخش بسیار هوشمندانه است.

---

فرض کن:

```python
banner = ""
```

---

بعد از decode و strip:

```python
""
```

---

رشته خالی در پایتون:

```python
False
```

محسوب می‌شود.

---

پس:

```python
"" or None
```

برابر است با:

```python
None
```

---

یعنی:

```text
اگر Banner خالی بود، None برگردان.
```

---

# مدیریت خطاها

```python
except (
    socket.timeout,
    socket.error
):
```

---

دو خطای مهم مدیریت می‌شوند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Timeout
</p>

```python
socket.timeout
```

---

مثال:

```text
Server پاسخ نداد.
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Socket Error
</p>

```python
socket.error
```

---

مثال:

```text
Connection Refused
```

یا:

```text
Network Unreachable
```

---

# خروجی هنگام خطا

```python
return None
```

---

یعنی:

```text
Banner پیدا نشد.
```

---

# نمونه اجرای واقعی

فرض کن:

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

# یک نکته امنیتی مهم

<p dir='rtl'>
Banner همیشه قابل اعتماد نیست.
</p>

---

بعضی مدیران سیستم عمداً آن را تغییر می‌دهند.

---

مثال:

واقعیت:

```text
Apache
```

---

<p dir='rtl'>
Banner جعلی:
</p>

```text
Nginx
```

---

به همین دلیل ابزارهای حرفه‌ای فقط به Banner اعتماد نمی‌کنند.

---

آن‌ها:

<p  dir='rtl'>
• Banner <br>
• Fingerprinting <br>
• Protocol Analysis <br>
• Active Probing
</p>

را ترکیب می‌کنند.

---

اما برای پروژه فعلی ما:

```text
Banner Grabbing
```

یک قابلیت بسیار ارزشمند و حرفه‌ای است.

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p  dir='rtl'>
✅ Banner چیست <br>
✅ Banner Grabbing چیست <br>
✅ recv چیست <br>
✅ bytes چیست <br>
✅ decode چیست <br>
✅ UTF-8 چیست <br>
✅ <span dir='ltr'>errors="ignore"</span> چیست <br>
✅ strip چیست <br>
✅ or None چگونه کار می‌کند <br>
✅ connect و connect_ex چه تفاوتی دارند <br>
✅ مدیریت خطاهای شبکه چگونه انجام می‌شود
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
src/models.py
```

می‌شویم.

در آن یاد می‌گیریم:

<p  dir='rtl'>
• Data Model چیست <br>
• Dataclass چیست <br>
• چرا از کلاس استفاده کردیم <br>
• Immutable Object چیست <br>
• ScanResult چگونه طراحی شده است <br>
• چرا این طراحی برای پروژه‌های حرفه‌ای اهمیت دارد
</p>

</div>