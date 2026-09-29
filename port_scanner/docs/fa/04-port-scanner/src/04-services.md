<div align='right' dir='rtl'>

# بررسی کامل فایل `services.py`

## مقدمه

در جلسه قبل مهم‌ترین فایل پروژه یعنی:

```text
src/scanner.py
```

را بررسی کردیم.

یاد گرفتیم:

<p dir='rtl'>
• Socket چیست <br>
• TCP چیست <br>
• چگونه یک پورت اسکن می‌شود <br>
• چگونه چندین پورت به صورت همزمان اسکن می‌شوند <br>
• ThreadPoolExecutor چیست <br>
• Future چیست
</p>

اما یک مشکل وجود داشت.

فرض کن خروجی اسکن این باشد:

```text
80
443
22
53
```

این اعداد به تنهایی اطلاعات زیادی به ما نمی‌دهند.

یک متخصص شبکه وقتی پورت:

```text
80
```

را می‌بیند فوراً متوجه می‌شود:

```text
HTTP
```

روی آن اجرا می‌شود.

اما یک کاربر عادی چنین چیزی را نمی‌داند.

برای حل این مشکل فایل:

```text
services.py
```

را ساختیم.

---

# محتوای فایل

```python
import socket


def detect_service(port: int) -> str:
    """
    Detect the registered TCP service for a port.
    """
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"
```

---

# هدف این فایل چیست؟

این فایل مسئول:

```text
Service Detection
```

است.

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
Service Detection چیست؟
</p>

تشخیص اینکه پشت یک پورت چه سرویسی قرار دارد.

مثال:

```text
22
```

معمولاً:

```text
SSH
```

---

```text
80
```

معمولاً:

```text
HTTP
```

---

```text
443
```

معمولاً:

```text
HTTPS
```

---

```text
53
```

معمولاً:

```text
DNS
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import
</p>

```python
import socket
```

---

## چرا دوباره socket؟

در فایل Scanner از Socket برای اتصال استفاده می‌کردیم.

اما اینجا از قابلیت دیگری از همین ماژول استفاده می‌کنیم.

---

# تعریف تابع

```python
def detect_service(port: int) -> str:
```

---

## ورودی

```python
port: int
```

مثال:

```python
80
```

یا:

```python
443
```

---

## خروجی

```python
str
```

یعنی:

```python
"http"
```

یا:

```python
"https"
```

یا:

```python
"unknown"
```

---

# داک استرینگ

```python
"""
Detect the registered TCP service for a port.
"""
```

---

معنی:

```text
تشخیص سرویس TCP ثبت‌شده برای یک پورت.
```

---

# شروع بلوک try

```python
try:
```

---

چرا؟

چون ممکن است پورتی وجود داشته باشد که هیچ سرویس شناخته‌شده‌ای برای آن ثبت نشده باشد.

---

مثال:

```python
12345
```

---

در چنین شرایطی پایتون خطا تولید می‌کند.

---

# مهم‌ترین خط فایل

```python
return socket.getservbyport(port, "tcp")
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
getservbyport چیست؟
</p>

این تابع از پایگاه داده سرویس‌های شناخته‌شده سیستم عامل استفاده می‌کند.

---

مثال:

```python
socket.getservbyport(80, "tcp")
```

خروجی:

```python
"http"
```

---

مثال:

```python
socket.getservbyport(443, "tcp")
```

خروجی:

```python
"https"
```

---

مثال:

```python
socket.getservbyport(22, "tcp")
```

خروجی:

```python
"ssh"
```

---

# این اطلاعات از کجا می‌آیند؟

بسیاری از پورت‌های معروف توسط:

```text
IANA
```

ثبت شده‌اند.

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
IANA چیست؟
</p>

مخفف:

```text
Internet Assigned Numbers Authority
```

---

این سازمان مسئول مدیریت بسیاری از استانداردهای اینترنت است.

از جمله:

<p dir='rtl'>
• شماره پورت‌ها <br>
• آدرس‌های IP <br>
• DNS Root Zone <br>
• Protocol Numbers
</p>

---

# چند نمونه از پورت‌های مشهور

| Port | Service |
|--------|--------|
| 20 | FTP Data |
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 3306 | MySQL |
| 5432 | PostgreSQL |

---

# چرا "tcp" را مشخص کرده‌ایم؟

```python
socket.getservbyport(
    port,
    "tcp"
)
```

---

زیرا برخی پورت‌ها می‌توانند برای TCP و UDP معانی متفاوتی داشته باشند.

---

مثال:

```python
53
```

هم برای:

```text
TCP
```

و هم برای:

```text
UDP
```

استفاده می‌شود.

---

به همین دلیل نوع پروتکل را مشخص کرده‌ایم.

---

# مدیریت خطا

```python
except OSError:
```

---

اگر پورت در پایگاه داده سرویس‌ها وجود نداشته باشد:

```python
getservbyport()
```

خطا تولید می‌کند.

---

مثال:

```python
socket.getservbyport(
    55555,
    "tcp"
)
```

---

ممکن است چنین خطایی ایجاد شود:

```text
OSError
```

---

# خروجی در زمان خطا

```python
return "unknown"
```

---

اگر سرویس مشخص نباشد:

```text
unknown
```

برگردانده می‌شود.

---

مثال:

```python
detect_service(55555)
```

خروجی:

```python
"unknown"
```

---

# چرا این طراحی خوب است؟

اگر Exception را مدیریت نمی‌کردیم:

```python
detect_service(55555)
```

کل برنامه متوقف می‌شد.

---

اما اکنون:

```text
پروژه پایدارتر شده است.
```

---

# مثال واقعی

فرض کن Scanner این پورت‌ها را پیدا کند:

```python
[22, 80, 443]
```

---

سپس:

```python
detect_service(22)
```

خروجی:

```python
"ssh"
```

---

```python
detect_service(80)
```

خروجی:

```python
"http"
```

---

```python
detect_service(443)
```

خروجی:

```python
"https"
```

---

نتیجه نهایی:

```text
PORT     SERVICE
22       ssh
80       http
443      https
```

---

# نکته مهم امنیتی

دقت کن:

```text
Service Detection
```

به معنای:

```text
تشخیص واقعی سرویس در حال اجرا
```

نیست.

---

مثال:

ممکن است برنامه‌نویس یک وب سرور را روی:

```text
8080
```

اجرا کرده باشد.

---

در این حالت:

```python
detect_service(8080)
```

ممکن است:

```python
"unknown"
```

برگرداند.

---

اما در واقع:

```text
یک وب سرور HTTP روی آن اجرا می‌شود.
```

---

پس این فایل فقط:

```text
تشخیص سرویس بر اساس شماره پورت استاندارد
```

را انجام می‌دهد.

---

تشخیص واقعی سرویس در فصل‌های بعدی و هنگام بررسی:

```text
banner.py
```

بسیار دقیق‌تر انجام می‌شود.

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ Service Detection چیست <br>
✅ تابع detect_service چگونه کار می‌کند <br>
✅ getservbyport چیست <br>
✅ IANA چیست <br>
✅ چرا TCP را مشخص کرده‌ایم <br>
✅ چرا Exception را مدیریت کرده‌ایم <br>
✅ تفاوت Service Detection و Banner Grabbing چیست
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
src/exporter.py
```

می‌شویم.

در آن یاد می‌گیریم:

<p dir='rtl'>
• JSON چیست <br>
• چرا خروجی JSON تولید می‌کنیم <br>
• Serialization چیست <br>
• چگونه نتایج اسکن را ذخیره می‌کنیم <br>
• کاربرد JSON در ابزارهای امنیتی چیست
</p>

</div>