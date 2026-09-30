<div dir="rtl">

# جلسه ۱۰: جمع‌بندی کامل شبکه برای ورود به امنیت سایبری

# مقدمه

تا اینجا تقریباً تمام مفاهیم شبکه‌ای که برای ساخت و درک پروژه Port Scanner لازم هستند را یاد گرفته‌ایم.

---

در این جلسه قرار نیست موضوع جدیدی یاد بگیریم.

---

هدف این جلسه این است که:

```text
تمام قطعات پازل را کنار هم قرار دهیم
```

تا دقیقاً متوجه شویم هنگام اسکن یک پورت در پشت صحنه چه اتفاقی می‌افتد.

---

# از لحظه وارد کردن آدرس تا رسیدن به سرور

فرض کن کاربر در مرورگر می‌نویسد:

```text
https://github.com
```

---

در ظاهر فقط یک آدرس نوشته شده است.

---

اما در پشت صحنه ده‌ها اتفاق رخ می‌دهد.

---

# مرحله اول: DNS

مرورگر نمی‌تواند با:

```text
github.com
```

ارتباط برقرار کند.

---

کامپیوترها با IP کار می‌کنند.

---

بنابراین ابتدا:

```text
DNS Query
```

ارسال می‌شود.

---

مثلاً:

```text
github.com
↓
140.82.121.3
```

---

# مرحله دوم: ساخت Packet

حالا IP مقصد مشخص شده است.

---

سیستم عامل یک Packet می‌سازد.

---

داخل این Packet اطلاعات مختلفی قرار می‌گیرد:

```text
Source IP
Destination IP
Source Port
Destination Port
Payload
```

---

# مرحله سوم: TCP Connection

اگر از TCP استفاده شود:

---

ابتدا:

```text
Three Way Handshake
```

انجام می‌شود.

---

یعنی:

```text
SYN
SYN-ACK
ACK
```

---

پس از آن ارتباط برقرار می‌شود.

---

# مرحله چهارم: انتقال داده

اکنون مرورگر می‌تواند درخواست ارسال کند.

---

مثلاً:

```http
GET /
```

---

و سرور پاسخ می‌دهد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Packet چیست؟
</p>

تمام داده‌هایی که در شبکه جابه‌جا می‌شوند در قالب Packet حرکت می‌کنند.

---

می‌توان Packet را مانند یک پاکت نامه در نظر گرفت.

---

روی پاکت نوشته شده است:

```text
از کجا آمده؟
به کجا می‌رود؟
```

---

داخل پاکت نیز داده قرار دارد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Port دقیقاً چه کاری انجام می‌دهد؟
</p>

<p dir='rtl'>
IP مشخص می‌کند:
</p>

```text
کدام دستگاه
```

---

<p dir='rtl'>
Port مشخص می‌کند:
</p>

```text
کدام برنامه
```

---

مثال:

```text
192.168.1.10
```

---

این فقط دستگاه را مشخص می‌کند.

---

اما:

```text
192.168.1.10:80
```

---

مشخص می‌کند:

```text
Web Server
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
TCP و UDP
</p>

دو پروتکل مهم لایه انتقال.

---

<p dir='rtl'>
TCP:
</p>

```text
Reliable
Connection Oriented
```

---

<p dir='rtl'>
UDP:
</p>

```text
Fast
Connectionless
```

---

پروژه فعلی ما:

```text
TCP Scanner
```

است.

---

# چرا Port Scanner می‌تواند سرویس‌ها را پیدا کند؟

زیرا هر سرویس معمولاً روی یک Port مشخص اجرا می‌شود.

---

مثال:

```text
22   SSH
53   DNS
80   HTTP
443  HTTPS
3306 MySQL
```

---

بنابراین وقتی پورت باز باشد:

---

احتمالاً آن سرویس فعال است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Open Port یعنی چه؟
</p>

یعنی برنامه‌ای روی آن پورت در حال گوش دادن است.

---

در دنیای شبکه اصطلاح:

```text
Listening
```

استفاده می‌شود.

---

مثال:

```text
Apache
```

روی:

```text
Port 80
```

گوش می‌دهد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Closed Port یعنی چه؟
</p>

هیچ برنامه‌ای منتظر اتصال نیست.

---

در نتیجه سیستم پاسخ می‌دهد:

```text
Connection Refused
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Filtered Port یعنی چه؟
</p>

معمولاً فایروال اجازه پاسخ نمی‌دهد.

---

در نتیجه:

```text
Timeout
```

اتفاق می‌افتد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Firewall چیست؟
</p>

فایروال نگهبان شبکه است.

---

وظیفه:

```text
اجازه دادن
یا
مسدود کردن
```

ارتباطات.

---

مثال:

```text
Allow: 80
Allow: 443
Block: 22
```

---

# نقش سیستم عامل چیست؟

وقتی اسکنر اجرا می‌شود:

---

در حقیقت:

```python
socket
```

با سیستم عامل صحبت می‌کند.

---

و سیستم عامل:

```text
Packetها را ارسال می‌کند
```

---

بنابراین بخش بزرگی از فرآیند اسکن توسط خود سیستم عامل انجام می‌شود.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Socket چیست؟
</p>

<p dir='rtl'>
Socket رابط بین برنامه و شبکه است.
</p>

---

مثال:

```python
socket.connect()
```

---

یعنی:

```text
به این آدرس متصل شو
```

---

# پروژه ما چگونه کار می‌کند؟

گام به گام:

---

<p dir='rtl'>
۱)
</p>

کاربر اجرا می‌کند:

```bash
python -m src.cli 127.0.0.1 1 1000
```

---

<p dir='rtl'>
۲)
</p>

ورودی‌ها اعتبارسنجی می‌شوند.

---

<p dir='rtl'>
۳)
</p>

پورت‌ها ساخته می‌شوند:

```python
range(1, 1001)
```

---

<p dir='rtl'>
۴)
</p>

<p dir='rtl'>
ThreadPoolExecutor اجرا می‌شود.
</p>

---

<p dir='rtl'>
۵)
</p>

چندین پورت همزمان اسکن می‌شوند.

---

<p dir='rtl'>
۶)
</p>

برای هر پورت:

```python
connect_ex()
```

اجرا می‌شود.

---

<p dir='rtl'>
۷)
</p>

پورت‌های باز ذخیره می‌شوند.

---

<p dir='rtl'>
۸)
</p>

<p dir='rtl'>
Banner Grab انجام می‌شود.
</p>

---

<p dir='rtl'>
۹)
</p>

<p dir='rtl'>
Service Detection انجام می‌شود.
</p>

---

<p dir='rtl'>
۱۰)
</p>

نتایج نمایش داده می‌شوند.

---

# ارتباط تمام درس‌های شبکه با پروژه

<p dir='rtl' style='font-size:18px; font-wight:bold'>
DNS
</p>

برای تبدیل Domain به IP

---

<p dir='rtl' style='font-size:18px; font-wight:bold'>
IP
</p>

برای شناسایی سیستم هدف

---

<p dir='rtl' style='font-size:18px; font-wight:bold'>
Port
</p>

برای شناسایی سرویس هدف

---

<p dir='rtl' style='font-size:18px; font-wight:bold'>
TCP
</p>

برای برقراری ارتباط

---

<p dir='rtl' style='font-size:18px; font-wight:bold'>
Packet
</p>

برای انتقال اطلاعات

---

<p dir='rtl' style='font-size:18px; font-wight:bold'>
Protocol
</p>

برای تعریف قوانین ارتباط

---

<p dir='rtl' style='font-size:18px; font-wight:bold'>
OSI
</p>

برای درک محل فعالیت Port Scanner

---

<p dir='rtl' style='font-size:18px; font-wight:bold'>
Firewall
</p>

برای فهم Filtered Port

---

<p dir='rtl' style='font-size:18px; font-wight:bold'>
Socket
</p>

برای پیاده‌سازی اسکنر

---

# اکنون چه چیزهایی را درک می‌کنیم؟

اگر خروجی زیر را ببینیم:

```text
22   OPEN   ssh
80   OPEN   http
443  OPEN   https
```

---

می‌دانیم:

---

روی سیستم مقصد:

```text
SSH Server
Web Server
HTTPS Server
```

فعال هستند.

---

و می‌دانیم:

---

اسکنر چگونه این اطلاعات را پیدا کرده است.

---

# اگر بخواهیم Nmap بسازیم چه چیزهایی کم داریم؟

فعلاً نداریم:

```text
UDP Scan
SYN Scan
OS Detection
Version Detection
Host Discovery
Traceroute
Script Engine
```

---

اما پایه‌ای که ساخته‌ایم کاملاً مشابه چیزی است که Nmap نیز روی آن بنا شده است.

---

# جمع‌بندی کل فصل شبکه

در این فصل یاد گرفتیم:

<p dir='rtl'>
✅ Network چیست <br>
✅ IP چیست <br>
✅ Public IP چیست <br>
✅ Private IP چیست <br>
✅ DNS چیست <br>
✅ Port چیست <br>
✅ TCP چیست <br>
✅ UDP چیست <br>
✅ Packet چیست <br>
✅ Protocol چیست <br>
✅ OSI چیست <br>
✅ Firewall چیست <br>
✅ Socket چیست <br>
✅ Port Scanner چگونه کار می‌کند <br>
✅ Nmap چگونه کار می‌کند
</p>

---

# پایان فصل دوم

```text
02-networking
```

---

# فصل بعد

```text
03-cybersecurity
```

---

فصل امنیت سایبری.

---

در این فصل یاد خواهیم گرفت:

<p dir='rtl'>
• Cybersecurity چیست <br>
• Hacker چیست <br>
• انواع هکرها <br>
• Vulnerability چیست <br>
• Exploit چیست <br>
• Reconnaissance چیست <br>
• Enumeration چیست <br>
• Penetration Testing چیست <br>
• Port Scanning در چرخه حمله چه نقشی دارد
</p>

و در نهایت متوجه می‌شویم پروژه‌ای که ساخته‌ایم دقیقاً در کجای دنیای امنیت سایبری قرار می‌گیرد.

</div>