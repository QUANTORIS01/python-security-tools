<div dir='rtl'>

# 🎉 پایان پروژه Port Scanner

# تبریک!

اگر تا اینجای دوره همراه بوده‌ای، اکنون دیگر فقط یک کاربر پایتون نیستی.

---

تو:

<p dir='rtl'>
✅ یک پروژه واقعی طراحی کرده‌ای <br>
✅ آن را ماژولار پیاده‌سازی کرده‌ای <br>
✅ برای آن تست نوشته‌ای <br>
✅ خروجی JSON ساخته‌ای <br>
✅ خروجی CSV ساخته‌ای <br>
✅ سیستم Logging پیاده‌سازی کرده‌ای <br>
✅ Banner Grabbing اضافه کرده‌ای <br>
✅ CLI حرفه‌ای ساخته‌ای <br>
✅ کل پروژه را خط به خط تحلیل کرده‌ای
</p>

---

و مهم‌تر از همه:

```text
فقط کدنویسی نکرده‌ای،
بلکه معماری نرم‌افزار را یاد گرفته‌ای.
```

---

# از کجا شروع کردیم؟

در ابتدای دوره هدف ما این بود:

```text
ساخت یک Port Scanner واقعی
```

---

اما خیلی زود متوجه شدیم برای فهمیدن یک Port Scanner باید سه دانش مهم را یاد بگیریم:

```text
Python
Networking
Cybersecurity
```

---

برای همین دوره را به چهار فصل تقسیم کردیم.

---

# فصل اول

```text
01-python
```

---

در این فصل یاد گرفتیم:

<p dir='rtl'>
✅ متغیرها <br>
✅ انواع داده <br>
✅ شرط‌ها <br>
✅ حلقه‌ها <br>
✅ توابع <br>
✅ List و Dictionary <br>
✅ مدیریت فایل‌ها <br>
✅ JSON <br>
✅ CSV <br>
✅ Exception Handling <br>
✅ مفاهیم موردنیاز پروژه
</p>

---

هدف:

```text
یادگیری پایتون به اندازه ساخت پروژه
```

بود.

---

نه تبدیل شدن به یک Python Developer حرفه‌ای.

---

# فصل دوم

```text
02-networking
```

---

در این فصل یاد گرفتیم:

<p dir='rtl'>
✅ شبکه چیست <br>
✅ IP چیست <br>
✅ IPv4 <br>
✅ Port چیست <br>
✅ TCP <br>
✅ UDP <br>
✅ Socket چیست <br>
✅ Three Way Handshake <br>
✅ Client / Server <br>
✅ DNS <br>
✅ Service Detection
</p>

---

و مهم‌تر از همه فهمیدیم:

```text
Port Scanner
در واقع با TCP کار می‌کند.
```

---

# فصل سوم

```text
03-cybersecurity
```

---

در این فصل یاد گرفتیم:

<p dir='rtl'>
✅ CIA Triad <br>
✅ Threat <br>
✅ Vulnerability <br>
✅ Risk <br>
✅ Attack Surface <br>
✅ Security Lifecycle <br>
✅ Defense in Depth <br>
✅ Authentication <br>
✅ Authorization <br>
✅ Logging <br>
✅ Monitoring
</p>

---

و فهمیدیم:

```text
Port Scanner
یک ابزار دفاعی و شناسایی است.
```

---

# فصل چهارم

```text
04-port-scanner
```

---

در این فصل:

```text
کل پروژه
خط به خط
تشریح شد.
```

---

# ساختار نهایی پروژه

```text
port-scanner/
│
├── src/
│
├── tests/
│
├── README.md
│
└── requirements.txt
```

---

# پوشه src

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
validator.py
</p>

بررسی ورودی‌ها

```text
IP
Port Range
Timeout
Workers
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
scanner.py
</p>

هسته اصلی اسکن

```text
TCP Connect Scan
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
services.py
</p>

تشخیص سرویس‌ها

```text
22 → ssh
80 → http
443 → https
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
banner.py
</p>

دریافت Banner

```text
SSH Banner
HTTP Banner
...
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
models.py
</p>

مدل داده

```python
ScanResult
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
results.py
</p>

ساخت نتایج نهایی

```text
Port
Service
Banner
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
formatter.py
</p>

ساخت خروجی ترمینال

```text
PORT
STATUS
SERVICE
BANNER
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
exporter.py
</p>

خروجی JSON

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
csv_exporter.py
</p>

خروجی CSV

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
logger.py
</p>

ثبت رویدادها

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
cli.py
</p>

رابط خط فرمان

---

# پوشه tests

در این بخش برای تمام اجزای پروژه تست نوشتیم.

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
test_validator.py
</p>

اعتبارسنجی ورودی‌ها

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
test_scanner.py
</p>

اسکن پورت

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
test_services.py
</p>

تشخیص سرویس

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
test_exporter.py
</p>

خروجی JSON

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
test_csv_exporter.py
</p>

خروجی CSV

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
test_banner.py
</p>

<p dir='rtl'>
Banner Grabbing
</p>

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
test_models.py
</p>

مدل ScanResult

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
test_results.py
</p>

ساخت نتایج

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
test_formatter.py
</p>

خروجی ترمینال

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
test_logger.py
</p>

<p dir='rtl'>
Logging
</p>

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
test_cli.py
</p>

<p dir='rtl'>
CLI
</p>

---

# چه چیزی ساختیم؟

در ظاهر:

```text
یک Port Scanner
```

---

اما در واقع:

```text
یک پروژه واقعی Python
```

ساختیم.

---

پروژه‌ای که شامل:

```text
Networking
Concurrency
Testing
Logging
CLI
Serialization
Architecture
```

است.

---

# مهم‌ترین چیزی که یاد گرفتیم

مهم‌ترین درس این پروژه:

```text
کدنویسی فقط نوشتن کد نیست.
```

---

بلکه:

```text
طراحی
تست
مستندسازی
ساختاردهی
نگهداری
```

هم بخشی از برنامه‌نویسی هستند.

---

# اگر بخواهیم پروژه را حرفه‌ای‌تر کنیم

نسخه‌های بعدی می‌توانند شامل:

<p dir='rtl'>
✅ UDP Scan <br>
✅ SYN Scan <br>
✅ OS Detection <br>
✅ AsyncIO Scanner <br>
✅ HTML Report <br>
✅ XML Export <br>
✅ CIDR Scan <br>
✅ Subnet Scan <br>
✅ Progress Bar <br>
✅ Colorized Output <br>
✅ Plugin System <br>
✅ Multi Target Scan
</p>

باشند.

---

# اکنون در چه سطحی هستی؟

بعد از اتمام این پروژه:

<p dir='rtl'>
✅ مفاهیم پایه Python را بلدی <br>
✅ مفاهیم پایه Networking را بلدی <br>
✅ مفاهیم پایه Cybersecurity را بلدی <br>
✅ ساختار یک پروژه واقعی را بلدی <br>
✅ نوشتن Test را بلدی <br>
✅ Debug کردن را بلدی <br>
✅ طراحی ماژولار را بلدی
</p>

---

و مهم‌تر از همه:

```text
می‌توانی پروژه‌های مشابه را
خودت از صفر بسازی.
```

---

# پایان پروژه

```text
Project: TCP Port Scanner
Status: Completed Successfully ✅
```

---

# پایان دوره

```text
Python ✅
Networking ✅
Cybersecurity ✅
Port Scanner ✅
```

---

# سخن پایانی

این دوره قرار نبود فقط یاد بدهد:

```python
for
if
def
```

---

هدف این بود که نشان دهد:

```text
چگونه دانش برنامه‌نویسی،
شبکه و امنیت
در کنار هم
به یک ابزار واقعی تبدیل می‌شوند.
```

---

🎉 تبریک!

پروژه Port Scanner با موفقیت به پایان رسید.

</div>