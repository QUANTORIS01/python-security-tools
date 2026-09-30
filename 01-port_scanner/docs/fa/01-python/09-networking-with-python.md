<div dir="rtl">

# جلسه ۹: شبکه در پایتون و Socket

# چرا باید شبکه را یاد بگیریم؟

تا اینجای آموزش:

<p dir='rtl'>
• پایتون را شناختیم. <br>
• توابع را یاد گرفتیم. <br>
• ماژول‌ها را یاد گرفتیم. <br>
• مدیریت خطا را یاد گرفتیم. <br>
• فایل و JSON و CSV را یاد گرفتیم.
</p>

اما هنوز نمی‌دانیم:

> پورت اسکنر چگونه با یک کامپیوتر دیگر ارتباط برقرار می‌کند؟

پاسخ این سؤال:

```text
Socket
```

است.

---

# شبکه چیست؟

فرض کن دو کامپیوتر وجود دارد.

```text
Computer A
```

و

```text
Computer B
```

این دو کامپیوتر از طریق شبکه با یکدیگر ارتباط برقرار می‌کنند.

---

مثال:

<p dir='rtl'>
• مرورگر به وب‌سایت وصل می‌شود. <br>
• تلگرام به سرورهای تلگرام وصل می‌شود. <br>
• بازی آنلاین به سرور بازی وصل می‌شود.
</p>

همه این‌ها ارتباط شبکه‌ای هستند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
IP چیست؟
</p>

هر دستگاه در شبکه یک آدرس دارد.

مثال:

```text
192.168.1.1
```

یا

```text
8.8.8.8
```

یا

```text
127.0.0.1
```

---

<p dir='rtl'>
IP شبیه آدرس خانه است.
</p>

---

بدون آدرس:

نمی‌توانیم بدانیم پیام را باید به کجا بفرستیم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Port چیست؟
</p>

یک کامپیوتر ممکن است ده‌ها سرویس مختلف اجرا کند.

مثال:

```text
Web Server
SSH
Database
FTP
DNS
```

---

همه این سرویس‌ها یک IP دارند.

پس چگونه آن‌ها را از هم تشخیص دهیم؟

---

با Port

---

مثال:

```text
80   → HTTP
443  → HTTPS
22   → SSH
21   → FTP
53   → DNS
```

---

پس:

```text
IP = دستگاه

Port = سرویس روی دستگاه
```

---

# ارتباط واقعی

مثال:

```text
142.250.190.78:443
```

---

قسمت اول:

```text
142.250.190.78
```

آدرس دستگاه است.

---

قسمت دوم:

```text
443
```

پورت سرویس است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Socket چیست؟
</p>

<p dir='rtl'>
Socket دروازه ارتباط شبکه‌ای است.
</p>

---

وقتی برنامه می‌خواهد به یک سرویس وصل شود:

ابتدا یک Socket می‌سازد.

---

تصویر ذهنی:

```text
Application
     │
     ▼
 Socket
     │
     ▼
 Network
     │
     ▼
 Remote Server
```

---

# اولین Socket در پایتون

```python
import socket

sock = socket.socket()
```

---

معنی کد

```python
socket.socket()
```

یعنی:

> یک سوکت جدید بساز.

---

# اتصال به یک سرور

```python
import socket

sock = socket.socket()

sock.connect(("google.com", 80))

print("Connected")
```

---

اگر اتصال برقرار شود:

```text
Connected
```

نمایش داده می‌شود.

---

# ارسال داده

بعد از اتصال می‌توانیم داده ارسال کنیم.

---

مثال:

```python
sock.send(b"Hello")
```

---

حرف b یعنی:

```python
bytes
```

---

در شبکه داده‌ها به صورت بایت منتقل می‌شوند.

---

# دریافت داده

```python
data = sock.recv(1024)

print(data)
```

---

عدد:

```python
1024
```

یعنی:

حداکثر 1024 بایت دریافت کن.

---

# بستن اتصال

بعد از پایان کار:

```python
sock.close()
```

---

باید اتصال را ببندیم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Timeout چیست؟
</p>

گاهی سرور پاسخ نمی‌دهد.

اگر Timeout نداشته باشیم:

برنامه ممکن است برای همیشه منتظر بماند.

---

مثال:

```python
sock.settimeout(1)
```

---

یعنی:

```text
حداکثر یک ثانیه صبر کن
```

---

اگر پاسخی نرسید:

خطا تولید کن.

---

# چرا Timeout در پورت اسکنر مهم است؟

فرض کن داریم:

```text
65535
```

پورت را اسکن می‌کنیم.

---

اگر هر پورت:

```text
30 ثانیه
```

معطل شود:

اسکن چند روز طول می‌کشد.

---

برای همین در پروژه ما داریم:

```python
timeout=0.5
```

---

# بررسی باز بودن پورت

ایده اصلی Port Scanner بسیار ساده است.

---

اگر بتوانیم به پورت وصل شویم:

```text
OPEN
```

---

اگر نتوانیم:

```text
CLOSED
```

---

نمونه ساده:

```python
import socket

sock = socket.socket()

result = sock.connect_ex(
    ("127.0.0.1", 80)
)

print(result)
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
connect_ex چیست؟
</p>

نسخه مناسب‌تر connect

---

اگر اتصال موفق باشد:

```text
0
```

برمی‌گرداند.

---

اگر اتصال شکست بخورد:

عدد دیگری برمی‌گرداند.

---

# نمونه

```python
if result == 0:
    print("OPEN")
else:
    print("CLOSED")
```

---

این دقیقاً قلب پورت اسکنر است.

---

# ارتباط با پروژه ما

در فایل:

```text
scanner.py
```

تقریباً همین اتفاق رخ می‌دهد.

---

مراحل:

```text
ساخت Socket

↓

تنظیم Timeout

↓

اتصال به پورت

↓

بررسی نتیجه

↓

بستن Socket
```

---

# مثال کامل

```python
import socket

sock = socket.socket()

sock.settimeout(1)

result = sock.connect_ex(
    ("127.0.0.1", 80)
)

if result == 0:
    print("OPEN")
else:
    print("CLOSED")

sock.close()
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Banner Grabbing چگونه کار می‌کند؟
</p>

بعد از اتصال:

```python
sock.recv()
```

استفاده می‌کنیم.

---

بعضی سرویس‌ها اطلاعاتی ارسال می‌کنند.

مثال:

```text
Apache
nginx
OpenSSH
Microsoft IIS
```

---

این همان چیزی است که در:

```text
banner.py
```

پیاده‌سازی کرده‌ایم.

---

# چیزی که امروز یاد گرفتیم

<p dir='rtl'>
✓ شبکه  <br>
✓ IP چیست <br>
✓ Port چیست <br>
✓ Socket چیست <br>
✓ ساخت Socket <br>
✓ connect <br>
✓ connect_ex <br>
✓ send <br>
✓ recv <br>
✓ close <br>
✓ timeout <br>
✓ ارتباط مستقیم با scanner.py <br>
✓ ارتباط مستقیم با banner.py
</p>

---

# تمرین

برنامه‌ای بنویس که:

<p dir='rtl'>
1. به
</p>

```text
google.com
```

روی پورت

```text
80
```

وصل شود.

<p dir='rtl'>
2. در صورت موفقیت:
</p>

```text
Connected
```

را نمایش دهد.

<p dir='rtl'>
3. در غیر این صورت:
</p>

```text
Connection Failed
```

را نمایش دهد.

---

جلسه بعد:

<p align='right' dir='ltr' style='font-size:32px; font-wight:bold'>
10-python-for-port-scanner.md
</p>

در این جلسه تمام دانشی که تاکنون یاد گرفته‌ایم را کنار هم قرار می‌دهیم و اولین نسخه ساده Port Scanner را از صفر می‌سازیم.

</div>