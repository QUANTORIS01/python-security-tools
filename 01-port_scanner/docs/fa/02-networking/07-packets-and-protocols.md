<div dir="rtl">

# جلسه ۷: Packet و Protocol چیستند؟

# مقدمه

تا اینجا یاد گرفتیم:

<p dir='rtl'>
✅ IP چیست <br>
✅ Port چیست <br>
✅ TCP چیست <br>
✅ UDP چیست <br>
✅ DNS چیست <br>
✅ Client و Server چیستند
</p>

---

اما هنوز یک سؤال مهم باقی مانده:

وقتی داده‌ای در شبکه ارسال می‌شود، واقعاً چه اتفاقی می‌افتد؟

---

فرض کن در مرورگر می‌نویسی:

```text
google.com
```

یا در پروژه خودمان:

```python
socket.connect()
```

---

آیا کل اطلاعات به صورت یکجا منتقل می‌شوند؟

خیر.

---

شبکه تقریباً هیچ وقت داده‌ها را به صورت یک تکه عظیم جابه‌جا نمی‌کند.

بلکه آن‌ها را به قطعات کوچک‌تری تقسیم می‌کند.

به این قطعات می‌گوییم:

```text
Packet
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Packet چیست؟
</p>

<p dir='rtl'>
Packet کوچک‌ترین واحدی است که در شبکه جابه‌جا می‌شود.
</p>

---

مثال:

فرض کن می‌خواهی یک فایل:

```text
10 MB
```

ارسال کنی.

---

معمولاً فایل به تعداد زیادی Packet تقسیم می‌شود.

---

شکل ساده:

```text
File
 │
 ├── Packet 1
 ├── Packet 2
 ├── Packet 3
 ├── Packet 4
 └── ...
```

---

سپس این Packet ها از شبکه عبور می‌کنند.

---

# چرا Packet داریم؟

اگر شبکه مجبور بود فایل‌ها را یکجا ارسال کند:

---

اگر فقط یک بخش کوچک خراب می‌شد:

```text
کل فایل دوباره ارسال می‌شد
```

---

اما با Packet:

فقط همان قسمت خراب دوباره ارسال می‌شود.

---

هم سریع‌تر است.

---

هم بهینه‌تر است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Packet از چه بخش‌هایی تشکیل شده است؟
</p>

یک Packet معمولاً دو قسمت اصلی دارد:

```text
Header
```

و

```text
Payload
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Header چیست؟
</p>

<p dir='rtl'>
Header اطلاعات مدیریتی Packet را نگهداری می‌کند.
</p>

---

مثل:

```text
Source IP
Destination IP
Protocol
Port
Flags
Length
```

---

در واقع Header به شبکه می‌گوید:

```text
این Packet از کجا آمده؟
به کجا می‌رود؟
چه نوع داده‌ای دارد؟
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Payload چیست؟
</p>

<p dir='rtl'>
Payload داده اصلی است.
</p>

---

مثال:

اگر صفحه وب دانلود کنیم:

```html
<html>
Hello
</html>
```

---

این محتوا داخل Payload قرار می‌گیرد.

---

بنابراین:

```text
Header = اطلاعات کنترلی
```

---

و

```text
Payload = داده واقعی
```

---

# مثال تصویری

```text
+----------------------+
|       Header         |
+----------------------+
|       Payload        |
+----------------------+
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Protocol چیست؟
</p>

<p dir='rtl'>
Protocol یعنی:
</p>

```text
قانون ارتباط
```

---

همان‌طور که انسان‌ها برای صحبت کردن قواعد دارند:

---

شبکه نیز قوانین خودش را دارد.

---

به این قوانین می‌گوییم:

```text
Protocol
```

---

# مثال واقعی

فرض کن من فارسی صحبت کنم.

و شخص مقابل فقط ژاپنی بلد باشد.

---

ارتباط تقریباً غیرممکن می‌شود.

---

در شبکه نیز اگر دو سیستم از Protocol مشترک استفاده نکنند:

```text
ارتباط برقرار نمی‌شود
```

---

# نمونه پروتکل‌ها

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
HTTP
</p>

برای وب‌سایت‌ها

```text
http://example.com
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
HTTPS
</p>

نسخه امن HTTP

```text
https://example.com
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
DNS
</p>

برای تبدیل Domain به IP

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
FTP
</p>

برای انتقال فایل

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
SSH
</p>

برای مدیریت از راه دور

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
SMTP
</p>

برای ارسال ایمیل

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
TCP و UDP هم Protocol هستند
</p>

بله.

---

<p dir='rtl'>
TCP یک Protocol است.
</p>

---

<p dir='rtl'>
UDP نیز یک Protocol است.
</p>

---

اما در لایه پایین‌تری از HTTP قرار دارند.

---

مثال:

```text
HTTP
  ↓
TCP
  ↓
IP
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Packet هنگام عبور از شبکه
</p>

فرض کن مرورگر درخواست زیر را ارسال کند:

```text
GET /
```

---

این داده به Packet تبدیل می‌شود.

---

هر Packet دارای Header و Payload خواهد بود.

---

سپس در شبکه حرکت می‌کند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Source و Destination
</p>

هر Packet معمولاً شامل:

```text
Source
```

و

```text
Destination
```

است.

---

مثال:

```text
Source:
192.168.1.10
```

---

```text
Destination:
142.250.190.78
```

---

این اطلاعات در Header قرار می‌گیرند.

---

# ارتباط Packet با Port

علاوه بر IP، پورت‌ها نیز داخل اطلاعات ارتباطی قرار دارند.

---

مثال:

```text
192.168.1.10:50000
```

↓

```text
142.250.190.78:443
```

---

یعنی:

```text
Source Port
```

و

```text
Destination Port
```

نیز وجود دارند.

---

# ارتباط Packet با Port Scanner

وقتی Port Scanner اجرا می‌شود:

---

مثلاً:

```python
socket.connect()
```

---

پشت صحنه Packet هایی ساخته می‌شوند.

---

این Packet ها به سمت هدف ارسال می‌شوند.

---

و پاسخ آن‌ها بررسی می‌شود.

---

# اگر پورت باز باشد

هدف پاسخ می‌دهد.

---

نتیجه:

```text
OPEN
```

---

# اگر پورت بسته باشد

هدف پاسخ مناسب اتصال را نمی‌دهد.

---

نتیجه:

```text
CLOSED
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Banner Grabbing و Packet
</p>

وقتی Banner دریافت می‌کنیم:

---

سرور Packet هایی ارسال می‌کند.

---

داخل Payload ممکن است چیزی شبیه این باشد:

```text
OpenSSH_9.7
```

---

یا:

```text
Apache/2.4.58
```

---

اسکنر آن را استخراج می‌کند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Service Detection و Packet
</p>

تشخیص سرویس نیز از روی اطلاعاتی انجام می‌شود که بین Packet ها رد و بدل می‌شوند.

---

در نسخه‌های حرفه‌ای‌تر Nmap حتی پاسخ‌های بسیار خاص سرویس‌ها بررسی می‌شوند.

---

تا نوع دقیق نرم‌افزار شناسایی شود.

---

# چرا این موضوع مهم است؟

چون اکنون متوجه می‌شویم:

---

پورت اسکنر:

```text
جادو نمی‌کند
```

---

بلکه:

```text
Packet ارسال می‌کند
```

و

```text
Packet دریافت می‌کند
```

---

و بر اساس آن‌ها تصمیم می‌گیرد.

---

# چیزی که امروز یاد گرفتیم

<p dir='rtl'>
✅ Packet چیست <br>
✅ Header چیست <br>
✅ Payload چیست <br>
✅ Protocol چیست <br>
✅ نمونه Protocol ها <br>
✅ ارتباط TCP و UDP با Protocol <br>
✅ ارتباط Packet با Port <br>
✅ ارتباط Packet با Port Scanner <br>
✅ ارتباط Packet با Banner Grabbing
</p>

---

# تمرین

فرض کن می‌خواهی وارد:

```text
https://github.com
```

بشوی.

مراحل زیر را روی کاغذ بنویس:

<p dir='rtl'>
1. DNS چه کاری انجام می‌دهد؟ <br>
2. IP چگونه پیدا می‌شود؟ <br>
3. ارتباط روی چه پورتی برقرار می‌شود؟ <br>
4. چه Protocol هایی درگیر هستند؟ <br>
5. Packet ها چه نقشی دارند؟
</p>

---

# جلسه بعد

فایل:

```text
08-osi-model.md
```

موضوع:

**مدل OSI**

در جلسه بعد یاد می‌گیریم:

<p dir='rtl'>
• OSI چیست <br>
• چرا ساخته شد <br>
• 7 لایه OSI چیست <br>
• TCP/IP با OSI چه تفاوتی دارد <br>
• Port Scanner در کدام لایه‌ها کار می‌کند <br>
• DNS ، TCP ، UDP ، HTTP در کجای این مدل قرار می‌گیرند
</p>

این جلسه یکی از مهم‌ترین جلسات کل بخش شبکه خواهد بود.

</div>