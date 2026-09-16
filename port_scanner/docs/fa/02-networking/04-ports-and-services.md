<div dir="rtl">

# جلسه ۴: پورت (Port) چیست؟

# مقدمه

تا اینجا یاد گرفتیم:

<p dir='rtl'>
✅ شبکه چیست <br>
✅ IP چیست <br>
✅ TCP چیست <br>
✅ UDP چیست
</p>

اما هنوز یک سؤال مهم باقی مانده است:

---

اگر یک کامپیوتر فقط یک IP داشته باشد، چطور می‌تواند همزمان:

<p dir='rtl'>
• وب‌سایت اجرا کند <br>
• ایمیل دریافت کند <br>
• DNS داشته باشد <br>
• FTP داشته باشد <br>
• SSH داشته باشد
</p>

؟

---

پاسخ:

```text
Port
```

---

# پورت چیست؟

پورت را می‌توان مانند:

```text
درِ یک ساختمان
```

تصور کرد.

---

فرض کن آدرس ساختمان:

```text
192.168.1.10
```

باشد.

---

این ساختمان فقط یک آدرس دارد.

اما چندین اتاق دارد.

---

مثلاً:

```text
اتاق 1
```

---

```text
اتاق 2
```

---

```text
اتاق 3
```

---

هر اتاق کار متفاوتی انجام می‌دهد.

---

در شبکه نیز:

```text
IP = ساختمان
```

و

```text
Port = اتاق
```

---

# مثال واقعی

فرض کن:

```text
192.168.1.10
```

یک سرور باشد.

---

روی همین سرور:

<p dir='rtl'>
• وب‌سایت اجرا می‌شود <br>
• SSH اجرا می‌شود <br>
• DNS اجرا می‌شود
</p>

---

همه روی یک IP هستند.

---

اما روی پورت‌های مختلف.

---

مثال:

```text
192.168.1.10:80
```

وب‌سایت

---

```text
192.168.1.10:22
```

<p dir='rtl'>
SSH
</p>

---

```text
192.168.1.10:53
```

<p dir='rtl'>
DNS
</p>

---

# فرمت نمایش IP و Port

معمولاً به این شکل نوشته می‌شود:

```text
IP:PORT
```

---

مثال:

```text
192.168.1.10:80
```

---

یا:

```text
8.8.8.8:53
```

---

# تعداد پورت‌ها چقدر است؟

پورت‌ها از:

```text
0
```

تا:

```text
65535
```

هستند.

---

یعنی:

```text
65536
```

پورت مختلف.

---

# چرا اسکن کامل زمان‌بر است؟

وقتی Nmap یا Port Scanner اجرا می‌شود:

---

ممکن است بخواهیم:

```text
1 تا 65535
```

را بررسی کنیم.

---

یعنی:

```text
65535 اتصال مختلف
```

---

برای همین اسکن کامل می‌تواند زمان‌بر باشد.

---

# دسته‌بندی پورت‌ها

<p dir='rtl' style='font-size:24px; font-wight:bold'>
Well Known Ports
</p>

از:

```text
0 - 1023
```

---

سرویس‌های معروف اینترنت.

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
Registered Ports
</p>

از:

```text
1024 - 49151
```

---

برای نرم‌افزارها و سرویس‌های مختلف.

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
Dynamic Ports
</p>

از:

```text
49152 - 65535
```

---

معمولاً موقت هستند.

---

# معروف‌ترین پورت‌های دنیا

<p dir='rtl' style='font-size:24px; font-wight:bold'>
SSH
</p>

```text
22
```

---

اتصال امن به سرور

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
FTP
</p>

```text
21
```

---

انتقال فایل

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
SMTP
</p>

```text
25
```

---

ارسال ایمیل

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
DNS
</p>

```text
53
```

---

تبدیل دامنه به IP

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
HTTP
</p>

```text
80
```

---

وب‌سایت

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
POP3
</p>

```text
110
```

---

دریافت ایمیل

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
HTTPS
</p>

```text
443
```

---

وب امن

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
SMB
</p>

```text
445
```

---

اشتراک فایل ویندوز

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
RDP
</p>

```text
3389
```

---

ریموت دسکتاپ ویندوز

---

# چرا پورت‌ها برای هکرها مهم هستند؟

فرض کن سروری داریم.

---

اگر فقط IP را بدانیم:

```text
192.168.1.50
```

---

هنوز نمی‌دانیم:

<p dir='rtl'>
• وب‌سرور دارد؟ <br>
• SSH دارد؟ <br>
• دیتابیس دارد؟
</p>

---

اما اگر پورت‌ها را پیدا کنیم:

```text
22
80
443
3306
```

---

متوجه می‌شویم:

<p dir='rtl'>
• SSH فعال است <br>
• HTTP فعال است <br>
• HTTPS فعال است <br>
• MySQL فعال است
</p>

---

به همین دلیل:

```text
Port Scanning
```

اولین مرحله بسیاری از تست‌های نفوذ است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Port Scanner ما دقیقاً چه کاری انجام می‌دهد؟
</p>

مثال:

```bash
python -m src.cli 127.0.0.1 1 1000
```

---

اسکنر:

پورت‌های:

```text
1 تا 1000
```

را بررسی می‌کند.

---

مثلاً:

```text
53
135
445
```

---

اگر پاسخ دریافت کند:

```text
OPEN
```

نمایش می‌دهد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Open Port چیست؟
</p>

یعنی:

سرویسی روی آن پورت در حال اجرا است.

---

مثال:

```text
80 OPEN
```

---

معمولاً یعنی:

```text
Web Server
```

در حال اجرا است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Closed Port چیست؟
</p>

یعنی:

هیچ سرویسی گوش نمی‌دهد.

---

مثال:

```text
8080 CLOSED
```

---

یعنی برنامه‌ای روی این پورت فعال نیست.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Listening چیست؟
</p>

وقتی یک برنامه آماده دریافت اتصال باشد می‌گوییم:

```text
Listening
```

---

مثال:

```text
Web Server Listening On Port 80
```

---

یعنی:

سرور منتظر اتصال کاربران است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Socket چیست؟
</p>

در برنامه‌نویسی شبکه:

اتصال به پورت‌ها با:

```python
socket
```

انجام می‌شود.

---

در پروژه ما:

```python
socket.connect()
```

---

تلاش می‌کند به:

```text
IP + Port
```

متصل شود.

---

# مثال واقعی

فرض کن:

```text
127.0.0.1:80
```

---

اسکنر سعی می‌کند متصل شود.

---

اگر موفق شود:

```text
OPEN
```

---

اگر موفق نشود:

```text
CLOSED
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Service Detection چیست؟
</p>

بعداً قابلیت زیر را اضافه کردیم:

```text
Service Detection
```

---

مثال:

به جای:

```text
80
```

نمایش می‌دهیم:

```text
http
```

---

و به جای:

```text
443
```

نمایش می‌دهیم:

```text
https
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Banner Grabbing چیست؟
</p>

بعد از پیدا کردن پورت:

گاهی می‌توانیم اطلاعات بیشتری بگیریم.

---

مثلاً:

```text
Apache/2.4.58
```

---

یا:

```text
OpenSSH_9.7
```

---

این اطلاعات:

```text
Banner
```

نام دارند.

---

ما این قابلیت را نیز به پروژه اضافه کرده‌ایم.

---

# خروجی واقعی پروژه

نمونه:

```text
PORT     STATUS   SERVICE       BANNER
--------------------------------------------------
53       OPEN     domain        -
135      OPEN     epmap         -
445      OPEN     microsoft-ds  -
```

---

همان چیزی که اخیراً از پروژه دریافت کردی.

---

# چرا Nmap معروف شد؟

چون فقط نمی‌گوید:

```text
Port Open
```

---

بلکه:

<p dir='rtl'>
• سرویس را تشخیص می‌دهد <br>
• نسخه سرویس را تشخیص می‌دهد <br>
• سیستم‌عامل را حدس می‌زند <br>
• اسکریپت اجرا می‌کند <br>
• آسیب‌پذیری پیدا می‌کند
</p>

---

اما همه این قابلیت‌ها از همین نقطه شروع می‌شوند:

```text
Port Scanning
```

---

# چیزی که امروز یاد گرفتیم

<p dir='rtl'>
✅ Port چیست <br>
✅ تفاوت IP و Port <br>
✅ Well Known Ports <br>
✅ Open Port <br>
✅ Closed Port <br>
✅ Listening <br>
✅ Socket <br>
✅ Service Detection <br>
✅ Banner Grabbing <br>
✅ ارتباط مستقیم Port با پروژه Port Scanner
</p>

---

# جلسه بعد

فایل:

```text
05-client-server-model.md
```

موضوع:

**مدل Client / Server**

در جلسه بعد یاد می‌گیریم:

<p dir='rtl'>
• کلاینت دقیقاً چیست <br>
• سرور دقیقاً چیست <br>
• مرورگر چگونه با وب‌سایت ارتباط برقرار می‌کند <br>
• Port Scanner در این مدل چه نقشی دارد <br>
• چرا پورت باز یعنی یک Server در حال Listening است
</p>

</div>