# درس 6: DNS Caching & TTL

## مقدمه

در درس قبل دیدیم که برای تبدیل یک دامنه به IP ممکن است چندین DNS Server درگیر شوند:

```text
Client
 ↓
Resolver
 ↓
Root Server
 ↓
TLD Server
 ↓
Authoritative DNS
 ↓
Answer
```

اگر این فرآیند برای هر درخواست تکرار شود:

<div align='right' dir='rtl'>

```text
DNS بسیار کند خواهد شد.
```

</div>

برای حل این مشکل از:

```text
DNS Cache
```

استفاده می‌شود.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>DNS Cache چیست؟</span>

</div>

<p dir='rtl'>
Cache محلی برای ذخیره موقت پاسخ‌های DNS است.
</p>

---

به جای اینکه هر بار:

```text
google.com
```

دوباره Resolve شود،

پاسخ قبلی ذخیره می‌شود.

---

مثال:

```text
google.com
→
216.239.38.120
```

---

این نتیجه در Cache قرار می‌گیرد.

---

در درخواست بعدی:

```text
google.com
```

سیستم مستقیماً از Cache استفاده می‌کند.

---

# مزایای DNS Cache

### سرعت بیشتر

بدون نیاز به Query جدید:

<div align='right' dir='rtl'>

```text
پاسخ فوری دریافت می‌شود.
```

</div>

---

### کاهش ترافیک DNS

تعداد درخواست‌های ارسالی کاهش پیدا می‌کند.

---

### کاهش بار روی DNS Serverها

<p dir='rtl'>
DNS Infrastructure فشار کمتری تحمل می‌کند.
</p>

---

### بهبود عملکرد برنامه‌ها

وب‌سایت‌ها سریع‌تر باز می‌شوند.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>Cache در چه جاهایی وجود دارد؟</span>

</div>

<p dir='rtl'>
Cache فقط در یک نقطه نیست.
</p>

---

ممکن است در:

<div align='right' dir='rtl'>

### Browser

</div>

```text
Chrome
Firefox
Edge
```

---

<div align='right' dir='rtl'>

### Operating System

</div>

```text
Windows
Linux
macOS
```

---

<div align='right' dir='rtl'>

### Local DNS Resolver

</div>

---

<div align='right' dir='rtl'>

### ISP DNS Server

</div>

---

<div align='right' dir='rtl'>

### Enterprise DNS Server

</div>

وجود داشته باشد.

---

# مثال واقعی

کاربر وارد می‌کند:

```text
google.com
```

---

برای اولین بار:

```text
DNS Query
```

ارسال می‌شود.

---

پاسخ:

```text
216.239.38.120
```

---

در Cache ذخیره می‌شود.

---

چند ثانیه بعد:

```text
google.com
```

دوباره درخواست می‌شود.

---

سیستم پاسخ را مستقیماً از Cache برمی‌گرداند.

---

بدون هیچ Query جدیدی.

---

# مشکل Cache چیست؟

اطلاعات DNS ممکن است تغییر کنند.

---

مثال:

```text
google.com
```

امروز:

```text
216.239.38.120
```

---

فردا:

```text
216.239.38.121
```

---

اگر Cache همیشه باقی بماند:

<div align='right' dir='rtl'>

```text
اطلاعات قدیمی استفاده می‌شوند.
```

</div>

---

برای حل این مشکل از:

```text
TTL
```

استفاده می‌شود.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>TTL چیست؟</span>

</div>

<p dir='rtl'>
TTL مخفف:
</p>


```text
Time To Live
```

است.

---

<p dir='rtl'>
TTL مشخص می‌کند:
</p>


<div align='right' dir='rtl'>

```text
یک رکورد DNS
چند ثانیه در Cache باقی بماند.
```

</div>

---

مثال:

```text
TTL = 300
```

---

یعنی:

<div align='right' dir='rtl'>

```text
5 دقیقه
```

</div>

---

بعد از 5 دقیقه:

<p dir='rtl'>
Cache حذف می‌شود.
</p>

---

و Query جدید ارسال خواهد شد.

---

# مثال TTL

فرض کنیم:

```text
google.com
```

دارای:

```text
TTL = 300
```

است.

---

اولین درخواست:

```text
12:00
```

---

رکورد در Cache ذخیره می‌شود.

---

تا:

```text
12:05
```

---

پاسخ از Cache استفاده می‌شود.

---

بعد از آن:

<div align='right' dir='rtl'>

```text
DNS Query جدید
```

</div>

ارسال خواهد شد.

---

<div align='right' dir='rtl'>

# <span dir='rtl'>TTL بالا</span>

</div>

مثال:

```text
86400
```

---

یعنی:

<div align='right' dir='rtl'>

```text
24 ساعت
```

</div>

---

مزایا:

<p dir='rtl'>
• سرعت بیشتر <br>
• کاهش Query <br>
• کاهش بار DNS
</p>

---

معایب:

• تغییرات DNS دیرتر اعمال می‌شوند

---

<div align='right' dir='rtl'>

# <span dir='rtl'>TTL پایین</span>

</div>

مثال:

```text
60
```

---

یعنی:

```text
1 دقیقه
```

---

مزایا:

• تغییرات سریع‌تر منتشر می‌شوند

---

معایب:

<p dir='rtl'>
• Query بیشتر <br>
• بار بیشتر روی DNS
</p>

---

# مشاهده TTL

در ابزارهای DNS معمولاً TTL نمایش داده می‌شود.

---

مثال:

```text
google.com

A Record

216.239.38.120

TTL: 300
```

---

# چرا TTL مهم است؟

فرض کنید مدیر یک وب‌سایت هستید.

---

می‌خواهید سرور را تغییر دهید.

---

قبل از تغییر:

<p dir='rtl'>
TTL را کاهش می‌دهید.
</p>

---

مثال:

```text
86400
↓
300
```

---

سپس IP جدید را ثبت می‌کنید.

---

به این صورت تغییرات سریع‌تر در اینترنت منتشر می‌شوند.

---

# ارتباط TTL با امنیت

<p dir='rtl'>
TTL فقط موضوع عملکرد نیست.
</p>

---

در برخی حملات:

```text
DNS Poisoning
```

یا:

```text
Cache Poisoning
```

<p dir='rtl'>
TTL اهمیت زیادی پیدا می‌کند.
</p>

---

چون پاسخ‌های مخرب ممکن است در Cache ذخیره شوند.

---

<p dir='rtl'>
TTL مشخص می‌کند:
</p>

<div align='right' dir='rtl'>

```text
این داده‌ها
چه مدت باقی بمانند.
```

</div>

---

<div align='right' dir='rtl'>

# <span dir='rtl'>DNS Cache Poisoning چیست؟</span>

</div>

مهاجم تلاش می‌کند:

<div align='right' dir='rtl'>

```text
پاسخ جعلی DNS
```

</div>

را وارد Cache کند.

---

مثال:

کاربر درخواست می‌کند:

```text
bank.com
```

---

اما Cache آلوده شده است.

---

در نتیجه:

<div align='right' dir='rtl'>

```text
IP جعلی
```

</div>

برگردانده می‌شود.

---

و کاربر وارد سایت تقلبی می‌شود.

---

# نقش TTL در Cache Poisoning

اگر TTL زیاد باشد:

<div align='right' dir='rtl'>

```text
داده مخرب
مدت بیشتری باقی می‌ماند.
```

</div>

---

اگر TTL کوتاه باشد:

<div align='right' dir='rtl'>

```text
سریع‌تر حذف می‌شود.
```

</div>

---

البته TTL به تنهایی جلوی حمله را نمی‌گیرد.

---

# ارتباط با پروژه DNS Lookup

در نسخه فعلی پروژه:

```python
dns.resolver.resolve()
```

فقط مقدار رکورد را دریافت می‌کنیم.

---

فعلاً:

<div align='right' dir='rtl'>

```text
TTL را نمایش نمی‌دهیم.
```

</div>

---

اما در نسخه‌های پیشرفته‌تر می‌توانیم:

<p dir='rtl'>
• TTL <br>
• Authority <br>
• Nameserver <br>
• Additional Records
</p>

را نیز استخراج کنیم.

---

# چرا این درس مهم است؟

چون در دنیای واقعی:

<div align='right' dir='rtl'>

```text
بخش بزرگی از سرعت DNS
به Cache وابسته است.
```

</div>

---

و بسیاری از مشکلات DNS نیز:

<div align='right' dir='rtl'>

```text
به Cache و TTL
مربوط می‌شوند.
```

</div>

---

# جمع‌بندی

در این درس یاد گرفتیم:

<p dir='rtl'>
• DNS Cache چیست <br>
• چرا Cache وجود دارد <br>
• TTL چیست <br>
• TTL چگونه کار می‌کند <br>
• تفاوت TTL بالا و پایین <br>
• نقش TTL در مدیریت DNS <br>
• ارتباط Cache با امنیت <br>
• DNS Cache Poisoning چیست <br>
• ارتباط این مفاهیم با پروژه DNS Lookup
</p>

---

# درس بعدی

در درس بعدی وارد یکی از مهم‌ترین بخش‌های فنی DNS می‌شویم:

```text
Recursive Resolver vs Authoritative Server
```


<p dir='rtl'>
• Recursive Resolver چیست <br>
• Authoritative Name Server چیست <br>
• درخواست DNS از چه مسیرهایی عبور می‌کند <br>
• Google DNS چیست <br>
• Cloudflare DNS چیست <br>
• ISP DNS چیست
</p>
