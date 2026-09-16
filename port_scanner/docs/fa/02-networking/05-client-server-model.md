<div dir="rtl">

# جلسه ۵: مدل Client و Server چیست؟

# مقدمه

تا اینجا یاد گرفتیم:

<p dir='rtl'>
✅ شبکه چیست <br>
✅ IP چیست <br>
✅ TCP چیست <br>
✅ UDP چیست <br>
✅ Port چیست
</p>

---

اکنون به مهم‌ترین مفهومی می‌رسیم که کل اینترنت روی آن ساخته شده است:

```text
Client / Server Model
```

---

تقریباً هر چیزی که در اینترنت انجام می‌دهی بر اساس همین مدل است.

---

مثلاً:

<p dir='rtl'>
• باز کردن یک وب‌سایت <br>
• تماشای ویدیو در یوتیوب <br>
• استفاده از اینستاگرام <br>
• ارسال ایمیل <br>
• دانلود فایل <br>
• اجرای Port Scanner
</p>

همه بر اساس مدل Client / Server هستند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Client چیست؟
</p>

<p dir='rtl'>
Client یعنی:
</p>

```text
درخواست‌کننده
```

---

سیستمی که درخواست ارسال می‌کند.

---

مثال:

وقتی مرورگر را باز می‌کنی:

```text
Google Chrome
```

یا

```text
Firefox
```

---

مرورگر نقش:

```text
Client
```

را دارد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Server چیست؟
</p>

<p dir='rtl'>
Server یعنی:
</p>

```text
پاسخ‌دهنده
```

---

سیستمی که منتظر درخواست‌هاست و به آن‌ها پاسخ می‌دهد.

---

مثال:

سرور گوگل.

---

وقتی وارد می‌شوی:

```text
https://google.com
```

---

سرور گوگل درخواست را دریافت می‌کند و پاسخ می‌دهد.

---

# مثال واقعی

فرض کن وارد یک رستوران شده‌ای.

---

تو می‌گویی:

```text
یک پیتزا لطفاً
```

---

آشپز پاسخ می‌دهد:

```text
پیتزا آماده است
```

---

در این مثال:

```text
تو = Client
```

---

```text
آشپز = Server
```

---

# شکل ساده ارتباط

```text
Client  ---------- Request ----------> Server

Client <--------- Response ---------- Server
```

---

در تمام اینترنت تقریباً همین اتفاق رخ می‌دهد.

---

# مثال وب‌سایت

وقتی آدرس زیر را باز می‌کنی:

```text
https://google.com
```

---

مرورگر درخواست می‌فرستد:

```text
GET /
```

---

سرور پاسخ می‌دهد:

```html
<html>
...
</html>
```

---

مرورگر صفحه را نمایش می‌دهد.

---

# درخواست و پاسخ

دو مفهوم بسیار مهم:

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
Request
</p>

درخواست

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
Response
</p>

پاسخ

---

مثال:

```text
Request:
Give Me Homepage
```

---

```text
Response:
Here Is Homepage
```

---

# آیا یک سرور همیشه روشن است؟

معمولاً بله.

---

سرور باید دائماً آماده باشد.

---

به همین دلیل:

```text
Listening
```

می‌کند.

---

یعنی منتظر اتصال‌های جدید است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Listening یعنی چه؟
</p>

فرض کن سرور روی پورت 80 اجرا شده است.

---

سرور می‌گوید:

```text
من روی Port 80 منتظر درخواست هستم
```

---

به این حالت می‌گوییم:

```text
Listening
```

---

# ارتباط Listening با Port Scanner

پورت اسکنر دقیقاً همین را بررسی می‌کند.

---

وقتی این دستور اجرا می‌شود:

```bash
python -m src.cli 127.0.0.1 1 1000
```

---

اسکنر می‌پرسد:

```text
آیا کسی روی این پورت Listening می‌کند؟
```

---

اگر پاسخ مثبت باشد:

```text
OPEN
```

---

اگر پاسخ منفی باشد:

```text
CLOSED
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Port Scanner در این مدل چه نقشی دارد؟
</p>

<p dir='rtl'>
Port Scanner یک Client است.
</p>

---

خیلی مهم:

پورت اسکنر:

```text
Server نیست
```

---

بلکه:

```text
Client است
```

---

زیرا درخواست اتصال ارسال می‌کند.

---

# مثال واقعی

فرض کن:

```text
192.168.1.100
```

سرور باشد.

---

و روی:

```text
80
```

گوش دهد.

---

پورت اسکنر تلاش می‌کند:

```text
Connect To 192.168.1.100:80
```

---

اگر موفق شود:

```text
OPEN
```

---

# پشت صحنه <span style='display=inline-block' dir='ltr'>connect()</span>

در پروژه ما:

```python
socket.connect()
```

---

نقش Client را بازی می‌کند.

---

و سعی می‌کند به Server متصل شود.

---

# چند Client می‌توانند به یک Server وصل شوند؟

بله.

---

مثال:

سرور گوگل.

---

ممکن است:

```text
میلیون‌ها Client
```

همزمان متصل باشند.

---

# چند Server روی یک سیستم می‌توانند باشند؟

بله.

---

مثال:

```text
Port 80
HTTP
```

---

```text
Port 22
SSH
```

---

```text
Port 443
HTTPS
```

---

همه روی یک IP.

---

اما روی پورت‌های مختلف.

---

# چرا Server ها پورت دارند؟

برای اینکه بتوانند تشخیص دهند:

درخواست مربوط به کدام سرویس است.

---

مثال:

```text
192.168.1.10:80
```

---

وب‌سایت

---

و

```text
192.168.1.10:22
```

---

<p dir='rtl'>
SSH
</p>

---

هر دو روی یک IP هستند.

---

اما روی پورت‌های متفاوت.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Banner Grabbing در مدل Client/Server
</p>

وقتی پورت اسکنر بنر دریافت می‌کند:

---

ابتدا:

```text
Client Connects
```

---

سپس:

```text
Server Sends Banner
```

---

مثال:

```text
OpenSSH_9.7
```

---

یا:

```text
Apache/2.4.58
```

---

این اطلاعات از سمت Server ارسال می‌شوند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Service Detection در این مدل
</p>

بعد از اتصال:

---

پورت:

```text
80
```

---

به سرویس:

```text
HTTP
```

نگاشت می‌شود.

---

و

```text
22
```

---

به:

```text
SSH
```

---

این همان قابلیت Service Detection است.

---

# مدل Client / Server در دنیای واقعی

تقریباً همه چیز:

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
مرورگر
</p>

<p dir='rtl'>
Client
</p>

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
وب‌سایت
</p>

<p dir='rtl'>
Server
</p>

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
ایمیل
</p>

<p dir='rtl'>
Client ↔ Server
</p>

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
FTP
</p>

<p dir='rtl'>
Client ↔ Server
</p>

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
SSH
</p>

<p dir='rtl'>
Client ↔ Server
</p>

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
Port Scanner
</p>

<p dir='rtl'>
Client ↔ Server
</p>

---

# چرا این جلسه مهم است؟

زیرا اکنون می‌فهمیم:

پورت اسکنر چه کاری انجام می‌دهد.

---

اسکنر:

```text
در حال هک کردن نیست
```

---

بلکه:

```text
در حال تلاش برای برقراری ارتباط
```

است.

---

و از پاسخ یا عدم پاسخ سرور نتیجه‌گیری می‌کند.

---

# چیزی که امروز یاد گرفتیم

<p dir='rtl'>
✅ Client چیست <br>
✅ Server چیست <br>
✅ Request چیست <br>
✅ Response چیست <br>
✅ Listening چیست <br>
✅ ارتباط Port Scanner با مدل Client/Server <br>
✅ نقش <span style='display:inline-block;' dir='ltr'>socket.connect()</span> <br>
✅ ارتباط Banner Grabbing با Server <br>
✅ ارتباط Service Detection با Server
</p>

---

# جلسه بعد

فایل:

```text
06-dns-and-domain-names.md
```

موضوع:

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
DNS و Domain Name
</p>

در جلسه بعد یاد می‌گیریم:

<p dir='rtl'>
• Domain چیست <br>
• DNS چیست <br>
• چرا به جای IP از نام دامنه استفاده می‌کنیم <br>
• google.com چگونه به IP تبدیل می‌شود <br>
• Port Scanner چگونه می‌تواند دامنه را اسکن کند
</p>

</div>