# درس 1: اینترنت واقعاً چگونه کار می‌کند؟

## مقدمه

قبل از اینکه DNS را یاد بگیریم باید بفهمیم وقتی در مرورگر می‌نویسیم:

```text
google.com
```

چه اتفاقی پشت صحنه رخ می‌دهد.

---

## اینترنت چیست؟

به زبان ساده:

```text
Internet = Network of Networks
```

یعنی:

<div align='right'>

```text
شبکه‌ای از شبکه‌ها
```

</div>

هزاران ISP، دیتاسنتر، دانشگاه، شرکت و سازمان مختلف به یکدیگر متصل شده‌اند و چیزی به نام اینترنت را تشکیل داده‌اند.

---

## هر دستگاه به یک آدرس نیاز دارد

همان‌طور که خانه شما آدرس پستی دارد، هر دستگاه متصل به اینترنت نیز باید آدرسی داشته باشد.

به این آدرس می‌گوییم:

```text
IP Address
```

نمونه:

```text
8.8.8.8
```

یا:

```text
142.250.186.14
```

---

## مشکل IP Address

کامپیوترها با IP کار می‌کنند اما انسان‌ها در به خاطر سپردن اعداد ضعیف هستند.

حفظ کردن آدرس‌هایی مانند:

```text
142.250.186.14
151.101.1.140
104.18.33.45
```

کار دشواری است.

---

## راه حل

به جای استفاده از IP از نام‌های قابل خواندن استفاده می‌کنیم:

```text
google.com
github.com
openai.com
```

اما کامپیوترها این نام‌ها را نمی‌فهمند.

آن‌ها فقط IP را می‌شناسند.

---

<div align='right'>

## <span dir='rtl'>DNS چیست؟</span>

</div>

<p dir='rtl'>
DNS مخفف:
</p>

```text
Domain Name System
```

است.

وظیفه DNS تبدیل نام دامنه به IP Address است.

مثال:

```text
google.com
      ↓
142.250.186.14
```

به این فرآیند می‌گوییم:

```text
DNS Lookup
```

یا:

```text
Name Resolution
```

---

## هنگام باز کردن یک وب‌سایت چه اتفاقی می‌افتد؟

زمانی که در مرورگر می‌نویسید:

```text
https://google.com
```

مراحل زیر رخ می‌دهد:

```text
Browser
   ↓
DNS Lookup
   ↓
IP Address
   ↓
TCP Connection
   ↓
HTTP Request
   ↓
Google Server
   ↓
HTTP Response
   ↓
Browser
```

---

## جایگاه پروژه DNS Lookup

ابزاری که در این پروژه ساخته‌ایم دقیقاً در بخش DNS فعالیت می‌کند:

```text
Browser
   ↓
DNS Lookup   ← DNS Lookup Tool
   ↓
IP Address
```

ما از DNS سؤال می‌کنیم:

<div align='right' dir='rtl'>

```text
IP مربوط به google.com چیست؟
```

</div>

و پاسخ را دریافت می‌کنیم.

---

## ارتباط با پروژه Port Scanner

در پروژه قبلی:

```text
Port Scanner
```

ما یک IP را دریافت می‌کردیم و پورت‌های آن را بررسی می‌کردیم.

مثال:

```text
142.250.186.14
```

اما برای رسیدن به این IP معمولاً ابتدا باید یک DNS Lookup انجام شود.

بنابراین DNS Lookup در عمل یکی از مراحل قبل از Port Scanning محسوب می‌شود.

---

## چرا یک دامنه ممکن است چند IP داشته باشد؟

پاسخ DNS همیشه ثابت نیست.

برای مثال:

```text
google.com
```

ممکن است در زمان‌های مختلف IPهای متفاوتی برگرداند.

دلایل این موضوع:

<p dir='rtl'>
• Load Balancing <br>
• Content Delivery Networks (CDN) <br>
• Geographic Routing <br>
• High Availability
</p>

است.

---

## اهمیت DNS در امنیت سایبری

<p dir='rtl'>
DNS یکی از مهم‌ترین اجزای امنیت شبکه است.
</p>

بسیاری از فعالیت‌های امنیتی وابسته به DNS هستند:

<p dir='rtl'>
• Subdomain Enumeration <br>
• Threat Intelligence <br>
• Malware Analysis <br>
• Phishing Detection <br>
• DNS Monitoring <br>
• DNS Tunneling Detection
</p>

به همین دلیل شناخت DNS برای هر متخصص امنیت ضروری است.

---

## جمع‌بندی

در این درس یاد گرفتیم:

<p dir='rtl'>
• اینترنت چیست <br>
• IP Address چیست <br>
• چرا DNS ایجاد شد <br>
• DNS Lookup چیست <br>
• DNS در کجای ارتباطات شبکه قرار می‌گیرد <br>
• ارتباط DNS با Port Scanner <br>
• اهمیت DNS در امنیت سایبری
</p>

---

## درس بعدی

در درس بعد با مفاهیم زیر آشنا می‌شویم:

<p dir='rtl'>
• IPv4 <br>
• Network Address <br>
• Host Address <br>
• Public IP <br>
• Private IP
</p>

این مفاهیم پایه‌ای‌ترین بخش شبکه هستند و برای درک عملکرد DNS ضروری‌اند.
