<div dir="rtl">

# جلسه ۹: پورت اسکنرها واقعاً چگونه کار می‌کنند؟

# مقدمه

تا اینجا تقریباً تمام پیش‌نیازهای لازم را یاد گرفته‌ایم:

<p dir='rtl'>
✅ IP <br>
✅ Port <br>
✅ TCP <br>
✅ UDP <br>
✅ DNS <br>
✅ Packet <br>
✅ Protocol <br>
✅ OSI Model
</p>

---

اکنون وقت آن رسیده است که به سؤال اصلی پروژه پاسخ دهیم:

---

# پورت اسکنر چیست؟

<p dir='rtl'>
Port Scanner ابزاری است که بررسی می‌کند:
</p>

```text
چه پورت‌هایی روی یک سیستم باز هستند؟
```

---

مثال:

```text
192.168.1.10
```

---

پورت اسکنر تلاش می‌کند به پورت‌های مختلف متصل شود:

```text
21
22
25
53
80
110
443
3306
8080
...
```

---

و وضعیت هرکدام را مشخص می‌کند.

---

# هدف پورت اسکن چیست؟

شناسایی سرویس‌های فعال.

---

مثال:

اگر این پورت‌ها باز باشند:

```text
22
80
443
```

---

احتمالاً سرویس‌های زیر در حال اجرا هستند:

```text
SSH
HTTP
HTTPS
```

---

# چرا این موضوع مهم است؟

برای مدیر شبکه:

```text
مدیریت سرویس‌ها
```

---

برای متخصص امنیت:

```text
شناسایی سطح حمله
```

---

برای مهاجم:

```text
شناسایی اهداف احتمالی
```

---

به همین دلیل Port Scan اولین مرحله بسیاری از تست‌های نفوذ است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Open Port چیست؟
</p>

فرض کن روی سیستم مقصد یک Web Server فعال باشد.

---

مثلاً:

```text
Port 80
```

---

وقتی اسکنر به آن متصل شود:

```text
Connection Successful
```

---

نتیجه:

```text
OPEN
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Closed Port چیست؟
</p>

اگر هیچ سرویسی روی آن پورت اجرا نشود:

---

اتصال رد می‌شود.

---

نتیجه:

```text
CLOSED
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Filtered Port چیست؟
</p>

گاهی فایروال وسط راه قرار دارد.

---

فایروال ممکن است پاسخ را مخفی کند.

---

در این حالت:

```text
OPEN ?
CLOSED ?
```

---

مشخص نیست.

---

به این وضعیت می‌گوییم:

```text
FILTERED
```

---

# پروژه فعلی ما چه کار می‌کند؟

اسکنر ما از این دستور استفاده می‌کند:

```python
socket.connect_ex()
```

---

این تابع تلاش می‌کند اتصال TCP ایجاد کند.

---

اگر موفق شود:

```text
Port Open
```

---

اگر موفق نشود:

```text
Port Closed
```

---

# فرآیند واقعی پشت صحنه

فرض کن داریم:

```text
127.0.0.1:80
```

را اسکن می‌کنیم.

---

اسکنر:

```python
socket.connect()
```

را اجرا می‌کند.

---

سیستم عامل شروع به برقراری ارتباط TCP می‌کند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
TCP Three-Way Handshake
</p>

در TCP قبل از ارسال داده باید ارتباط ایجاد شود.

---

سه مرحله وجود دارد:

```text
SYN
SYN-ACK
ACK
```

---

# مرحله اول

اسکنر:

```text
SYN
```

ارسال می‌کند.

---

یعنی:

```text
سلام، می‌توانم وصل شوم؟
```

---

# مرحله دوم

اگر پورت باز باشد:

سرور پاسخ می‌دهد:

```text
SYN-ACK
```

---

یعنی:

```text
بله، می‌توانی وصل شوی.
```

---

# مرحله سوم

کلاینت:

```text
ACK
```

ارسال می‌کند.

---

یعنی:

```text
متشکرم، ارتباط برقرار شد.
```

---

# نمایش تصویری

```text
Scanner
   |
   | SYN
   |
Server
   |
   | SYN-ACK
   |
Scanner
   |
   | ACK
   |
Connection Established
```

---

# اگر پورت بسته باشد چه می‌شود؟

سرور پاسخ متفاوتی می‌دهد.

---

معمولاً:

```text
RST
```

---

یعنی:

```text
این پورت وجود ندارد
```

---

نتیجه:

```text
CLOSED
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Timeout چیست؟
</p>

گاهی هیچ پاسخی دریافت نمی‌کنیم.

---

مثال:

```text
Firewall
```

---

یا:

```text
Packet Loss
```

---

در این حالت اسکنر مدتی منتظر می‌ماند.

---

مثلاً:

```python
timeout = 0.5
```

---

یعنی:

```text
نیم ثانیه صبر کن
```

---

اگر پاسخی نرسید:

```text
Timeout
```

---

# چرا Timeout مهم است؟

فرض کن:

```text
1000 Port
```

اسکن می‌کنیم.

---

اگر Timeout برابر:

```text
5 Seconds
```

باشد:

---

اسکن بسیار کند خواهد شد.

---

برای همین در پروژه ما:

```text
0.5 Second
```

استفاده کردیم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Connect Scan چیست؟
</p>

اسکنر فعلی ما از:

```text
TCP Connect Scan
```

استفاده می‌کند.

---

این ساده‌ترین نوع Port Scan است.

---

مزایا:

✅ پیاده‌سازی آسان

✅ بدون دسترسی Administrator

✅ پایدار

---

معایب:

❌ نسبتاً کند

❌ قابل شناسایی

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
SYN Scan چیست؟
</p>

اسکن معروف Nmap.

---

به آن می‌گویند:

```text
Half Open Scan
```

---

یا:

```text
Stealth Scan
```

---

# تفاوت با Connect Scan

در Connect Scan:

```text
SYN
SYN-ACK
ACK
```

---

ارتباط کامل می‌شود.

---

اما در SYN Scan:

```text
SYN
SYN-ACK
RST
```

---

ارتباط کامل نمی‌شود.

---

در نتیجه:

```text
سریع‌تر
```

و

```text
مخفی‌تر
```

است.

---

# چرا پروژه ما SYN Scan نیست؟

زیرا SYN Scan نیاز دارد:

```text
Raw Socket
```

استفاده کند.

---

معمولاً نیز نیازمند دسترسی Administrator است.

---

برای آموزش اولیه مناسب نیست.

---

به همین دلیل فعلاً از:

```text
TCP Connect Scan
```

استفاده می‌کنیم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Banner Grabbing چگونه کار می‌کند؟
</p>

بعد از اتصال:

```python
recv()
```

اجرا می‌شود.

---

برخی سرویس‌ها اطلاعاتی ارسال می‌کنند.

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

ما این اطلاعات را ذخیره می‌کنیم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Service Detection چگونه کار می‌کند؟
</p>

گاهی از روی شماره پورت:

---

مثال:

```text
22 → SSH
80 → HTTP
443 → HTTPS
```

---

نوع سرویس حدس زده می‌شود.

---

در نسخه‌های پیشرفته‌تر:

<p dir='rtl'>
Banner نیز بررسی می‌شود.
</p>

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Parallel Scanning چیست؟
</p>

فرض کن:

```text
1000 Port
```

داریم.

---

اگر یکی یکی اسکن شوند:

```text
کند
```

خواهد بود.

---

برای همین پروژه ما از:

```python
ThreadPoolExecutor
```

استفاده می‌کند.

---

و چندین پورت را همزمان اسکن می‌کند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Nmap چه کارهای بیشتری انجام می‌دهد؟
</p>

<p dir='rtl'>
Nmap فقط پورت اسکنر نیست.
</p>

---

امکانات:

```text
TCP Scan
UDP Scan
SYN Scan
OS Detection
Version Detection
Traceroute
Script Engine
Service Enumeration
Host Discovery
```

---

به همین دلیل یکی از قدرتمندترین ابزارهای امنیتی جهان است.

---

# پروژه ما اکنون در چه سطحی است؟

در حال حاضر قابلیت‌های زیر را دارد:

<p dir='rtl'>
✅ TCP Connect Scan <br>
✅ Multi Threading <br>
✅ Validation <br>
✅ Banner Grabbing <br>
✅ Service Detection <br>
✅ JSON Export <br>
✅ CSV Export <br>
✅ Logging <br>
✅ Structured Output
</p>

---

برای یک پروژه رزومه‌ای سطح بسیار خوبی محسوب می‌شود.

---

# چیزی که امروز یاد گرفتیم

<p dir='rtl'>
✅ Port Scan چیست <br>
✅ Open Port چیست <br>
✅ Closed Port چیست <br>
✅ Filtered Port چیست <br>
✅ Timeout چیست <br>
✅ Connect Scan چیست <br>
✅ SYN Scan چیست <br>
✅ TCP Handshake چیست <br>
✅ Banner Grabbing چگونه کار می‌کند <br>
✅ Service Detection چگونه کار می‌کند <br>
✅ Nmap چه تفاوتی با پروژه ما دارد
</p>

---

# تمرین

فرض کن:

```text
192.168.1.15
```

دارای پورت‌های زیر است:

```text
22
80
443
```

---

مشخص کن:

<p dir='rtl'>
1. چه سرویس‌هایی احتمالاً فعال هستند؟ <br>
2. پورت اسکنر چگونه آن‌ها را پیدا می‌کند؟ <br>
3. در صورت وجود Firewall چه اتفاقی می‌افتد؟ <br>
4. تفاوت Connect Scan و SYN Scan چیست؟
</p>

---

# جلسه بعد

فایل:

```text
10-networking-summary.md
```

موضوع:

**جمع‌بندی کامل شبکه برای ورود به بخش امنیت سایبری**

در این جلسه تمام مباحث شبکه را کنار هم قرار می‌دهیم و یک تصویر کامل از نحوه کار اینترنت، سرویس‌ها، پورت‌ها و پروژه Port Scanner خواهیم داشت.

پس از آن وارد فصل سوم می‌شویم:

```text
03-cybersecurity
```

و آموزش امنیت سایبری را آغاز خواهیم کرد.

</div>