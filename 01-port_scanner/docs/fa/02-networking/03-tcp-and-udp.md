<div dir="rtl">

# جلسه ۳: TCP و UDP چیستند؟


# مقدمه

تا اینجای کار یاد گرفتیم:

<p dir='rtl'>
✅ شبکه چیست <br>
✅ IP چیست
</p>

اما هنوز یک سؤال بسیار مهم باقی مانده است:

وقتی دو کامپیوتر به یکدیگر متصل می‌شوند، اطلاعات چگونه جابه‌جا می‌شوند؟

---

پاسخ این سؤال:

```text
Protocol
```

یا

```text
پروتکل
```

---

# پروتکل چیست؟

پروتکل یعنی:

```text
مجموعه قوانین ارتباطی
```

---

مثال دنیای واقعی:

اگر دو نفر بخواهند با تلفن صحبت کنند باید قوانینی را رعایت کنند.

مثلاً:

<p dir='rtl'>
• یکی صحبت کند <br>
• دیگری گوش کند <br>
• صدا قابل فهم باشد <br>
• تماس قطع نشود
</p>

---

کامپیوترها نیز برای ارتباط نیاز به قوانین دارند.

---

به این قوانین می‌گوییم:

```text
Protocol
```

---

# مهم‌ترین پروتکل‌های اینترنت

<p dir='rtl' style='font-size:24px; font-wight:bold'>
HTTP
</p>

برای وب‌سایت‌ها

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
HTTPS
</p>

نسخه امن HTTP

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
FTP
</p>

انتقال فایل

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
DNS
</p>

تبدیل دامنه به IP

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
TCP
</p>

انتقال مطمئن اطلاعات

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
UDP
</p>

انتقال سریع اطلاعات

---

در این جلسه روی TCP و UDP تمرکز می‌کنیم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
TCP چیست؟
</p>

<p dir='rtl'>
TCP مخفف:
</p>

```text
Transmission Control Protocol
```

است.

---

هدف TCP:

```text
ارسال مطمئن اطلاعات
```

---

<p dir='rtl'>
TCP می‌خواهد مطمئن شود که:
</p>

<p dir='rtl'>
• داده گم نشده <br>
• داده خراب نشده <br>
• ترتیب داده‌ها حفظ شده
</p>

---

# مثال واقعی

فرض کن می‌خواهی یک کتاب ۱۰۰ صفحه‌ای را برای دوستت ارسال کنی.

---

<p dir='rtl'>
TCP شبیه پستی است که:
</p>

<p dir='rtl'>
• هر صفحه را شماره‌گذاری می‌کند <br>
• رسید تحویل می‌گیرد <br>
• اگر صفحه‌ای گم شود دوباره ارسال می‌کند
</p>

---

در نتیجه:

تمام کتاب سالم می‌رسد.

---

اما کمی زمان بیشتری صرف می‌شود.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Handshake چیست؟
</p>

قبل از انتقال داده در TCP:

ارتباط باید برقرار شود.

---

به این فرآیند می‌گویند:

```text
Three-Way Handshake
```

---

# مرحله اول

کلاینت می‌گوید:

```text
SYN
```

یعنی:

```text
می‌خواهم ارتباط برقرار کنم
```

---

# مرحله دوم

سرور پاسخ می‌دهد:

```text
SYN + ACK
```

یعنی:

```text
درخواستت را دریافت کردم
```

---

# مرحله سوم

کلاینت می‌گوید:

```text
ACK
```

یعنی:

```text
پاسخ تو را دریافت کردم
```

---

اکنون ارتباط برقرار شده است.

---

# شکل ساده Handshake

```text
Client -------- SYN --------> Server

Client <---- SYN/ACK -------- Server

Client -------- ACK --------> Server
```

---

بعد از این مرحله انتقال داده شروع می‌شود.

---

# چرا TCP برای Port Scanner مهم است؟

پورت اسکنر فعلی ما از همین ویژگی استفاده می‌کند.

---

وقتی این کد اجرا می‌شود:

```python
socket.connect()
```

در پشت صحنه:

```text
TCP Handshake
```

انجام می‌شود.

---

اگر پاسخ دریافت شود:

```text
Port Open
```

---

اگر پاسخ دریافت نشود:

```text
Port Closed
```

---

به همین سادگی.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
UDP چیست؟
</p>

<p dir='rtl'>
UDP مخفف:
</p>

```text
User Datagram Protocol
```

است.

---

هدف UDP:

```text
سرعت بالا
```

---

<p dir='rtl'>
UDP برعکس TCP:
</p>

<p dir='rtl'>
• رسید نمی‌گیرد <br>
• بررسی نمی‌کند داده رسیده یا نه <br>
• دوباره ارسال نمی‌کند
</p>

---

فقط داده را ارسال می‌کند.

---

# مثال واقعی

<p dir='rtl'>
TCP مثل:
</p>

```text
پست سفارشی
```

است.

---

<p dir='rtl'>
UDP مثل:
</p>

```text
بلندگو
```

است.

---

بلندگو فریاد می‌زند:

```text
اطلاعیه!
```

---

اگر کسی نشنود:

مهم نیست.

---

# مزیت UDP

بسیار سریع است.

---

# عیب UDP

اطمینان پایین‌تر دارد.

---

# چه سرویس‌هایی از UDP استفاده می‌کنند؟

<p dir='rtl' style='font-size:24px; font-wight:bold'>
DNS
</p>

پورت:

```text
53
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
DHCP
</p>

پورت:

```text
67
68
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
VoIP
</p>

تماس اینترنتی

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
Online Games
</p>

بازی‌های آنلاین

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
Streaming
</p>

پخش زنده

---

# چرا بازی‌های آنلاین UDP را دوست دارند؟

فرض کن در یک بازی:

موقعیت بازیکن هر ثانیه ۶۰ بار ارسال می‌شود.

---

اگر یکی از بسته‌ها گم شود:

اشکالی ندارد.

---

بسته بعدی بلافاصله می‌رسد.

---

اما اگر TCP استفاده شود:

باید بسته گمشده دوباره ارسال شود.

---

این باعث:

```text
Lag
```

می‌شود.

---

# مقایسه TCP و UDP

| TCP | UDP |
|------|------|
| مطمئن | سریع |
| دارای Handshake | بدون Handshake |
| دارای Error Checking | حداقل Error Checking |
| کندتر | سریع‌تر |
| مناسب وب | مناسب بازی |

---

# چرا اسکن UDP سخت‌تر است؟

این بخش بسیار مهم است.

---

در TCP:

اگر پورت باز باشد:

پاسخ دریافت می‌کنیم.

---

اما در UDP:

بسیاری از سرویس‌ها اصلاً پاسخ نمی‌دهند.

---

مثال:

```text
UDP Packet
```

ارسال می‌کنیم.

---

ممکن است:

```text
هیچ پاسخی
```

دریافت نکنیم.

---

اکنون نمی‌دانیم:

<p dir='rtl'>
• پورت باز است؟ <br>
• پورت بسته است؟ <br>
• فایروال بسته را حذف کرده؟
</p>

---

به همین دلیل:

```text
UDP Scanning
```

بسیار سخت‌تر است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Nmap چگونه UDP Scan انجام می‌دهد؟
</p>

<p dir='rtl'>
Nmap بسته UDP ارسال می‌کند.
</p>

---

اگر پیغام زیر را دریافت کند:

```text
ICMP Port Unreachable
```

متوجه می‌شود:

```text
Port Closed
```

---

اگر پاسخی دریافت نکند:

حدس می‌زند:

```text
Open | Filtered
```

---

به همین دلیل نتایج UDP Scan معمولاً قطعی نیستند.

---

# آیا Port Scanner ما UDP Scan انجام می‌دهد؟

فعلاً خیر.

---

اسکنر فعلی:

```text
TCP Scanner
```

است.

---

و این دقیقاً همان چیزی است که اکثر اسکنرهای ساده انجام می‌دهند.

---

# آیا بعداً UDP Scan اضافه می‌کنیم؟

بله.

---

در مسیر تبدیل پروژه به چیزی نزدیک‌تر به Nmap:

یکی از قابلیت‌های مهم:

```text
UDP Scanning
```

خواهد بود.

---

# ارتباط TCP با Banner Grabbing

وقتی بنر سرویس را دریافت می‌کنیم:

```python
socket.recv()
```

---

در حقیقت روی یک اتصال TCP کار می‌کنیم.

---

بنابراین:

<p dir='rtl'>
• Port Scan <br>
• Banner Grabbing
</p>

هر دو بر پایه TCP هستند.

---

# چیزی که امروز یاد گرفتیم

<p dir='rtl'>
✅ پروتکل چیست <br>
✅ TCP چیست <br>
✅ UDP چیست <br>
✅ Handshake چیست <br>
✅ تفاوت TCP و UDP <br>
✅ چرا Port Scanner ما TCP Scanner است <br>
✅ چرا UDP Scan سخت است <br>
✅ Nmap چگونه UDP Scan انجام می‌دهد <br>
✅ ارتباط TCP با Banner Grabbing
</p>

---

# جلسه بعد

فایل:

```text
04-ports-and-services.md
```

موضوع:

**پورت چیست؟**

در جلسه بعد یاد می‌گیریم:

<p dir='rtl'>
• Port چیست <br>
• چرا یک IP چندین سرویس دارد <br>
• Port Range چیست <br>
• Well Known Ports چیست <br>
• پورت‌های معروف امنیتی <br>
• ارتباط مستقیم Port با پروژه Port Scanner
</p>

</div>