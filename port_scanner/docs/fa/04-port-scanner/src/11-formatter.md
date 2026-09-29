<div dir='rtl'>

# بررسی کامل فایل `formatter.py`

# مقدمه

تا اینجای پروژه تقریباً تمام داده‌های موردنیاز را جمع‌آوری کرده‌ایم.

---

ما می‌توانیم:

<p dir='rtl'>
✅ پورت‌ها را اسکن کنیم <br>
✅ سرویس را تشخیص دهیم <br>
✅ Banner را دریافت کنیم <br>
✅ نتایج را داخل Model ذخیره کنیم
</p>

---

مثلاً اکنون خروجی ما ممکن است چیزی شبیه این باشد:

```python
[
    ScanResult(
        port=22,
        service="ssh",
        banner="OpenSSH_9.5"
    ),

    ScanResult(
        port=80,
        service="http",
        banner="Apache/2.4.58"
    )
]
```

---

اما یک مشکل وجود دارد.

---

اگر این خروجی را مستقیماً چاپ کنیم:

```python
print(results)
```

---

کاربر چیزی شبیه این می‌بیند:

```python
[
    ScanResult(port=22, service='ssh', banner='OpenSSH_9.5'),
    ScanResult(port=80, service='http', banner='Apache/2.4.58')
]
```

---

این خروجی برای برنامه‌نویس قابل فهم است.

---

اما برای کاربر نهایی:

```text
چندان زیبا نیست.
```

---

به همین دلیل فایل:

```text
src/formatter.py
```

ساخته شده است.

---

وظیفه این فایل:

```text
تبدیل داده‌های خام
به
خروجی خوانا برای انسان
```

است.

---

# محتوای فایل

```python
from src import ScanResult


def format_scan_results(
    results: list[ScanResult],
    max_banner_length: int = 40
) -> str:
    """
    Format scan results for terminal output.
    """

    if not results:
        return "No open ports found."

    lines = [
        f"{'PORT':<8} {'STATUS':<8} {'SERVICE':<16} {'BANNER'}",
        "-" * 70
    ]

    for result in results:

        banner = result.banner or "-"

        if len(banner) > max_banner_length:
            banner = (
                banner[: max_banner_length - 3]
                + "..."
            )

        lines.append(
            f"{result.port:<8} "
            f"{'OPEN':<8} "
            f"{result.service:<16} "
            f"{banner}"
        )

    return "\n".join(lines)
```

---

# هدف این فایل چیست؟

هدف:

```text
نمایش حرفه‌ای نتایج در ترمینال
```

است.

---

قبل:

```python
[
    ScanResult(...),
    ScanResult(...)
]
```

---

بعد:

```text
PORT     STATUS   SERVICE          BANNER
------------------------------------------------------
22       OPEN     ssh              OpenSSH_9.5
80       OPEN     http             Apache/2.4.58
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import
</p>

```python
from src import ScanResult
```

---

این مدل را قبلاً در:

```text
models.py
```

ساختیم.

---

تمام نتایج پروژه در قالب:

```python
ScanResult
```

ذخیره می‌شوند.

---

# تعریف تابع

```python
def format_scan_results(
```

---

نام تابع:

```python
format_scan_results
```

---

معنی:

```text
نتایج اسکن را قالب‌بندی کن.
```

---

# پارامتر اول

```python
results: list[ScanResult]
```

---

مثال:

```python
[
    ScanResult(...),
    ScanResult(...)
]
```

---

یعنی:

```text
لیستی از نتایج اسکن
```

---

# پارامتر دوم

```python
max_banner_length: int = 40
```

---

مقدار پیش‌فرض:

```python
40
```

---

هدف:

```text
محدود کردن طول Banner
```

است.

---

چرا؟

---

فرض کن Banner این باشد:

```text
Apache/2.4.58 Ubuntu OpenSSL/3.0.5 PHP/8.2.1 Very Long Text...
```

---

اگر کامل نمایش داده شود:

```text
جدول به هم می‌ریزد.
```

---

برای همین طول آن محدود می‌شود.

---

# خروجی تابع

```python
-> str
```

---

یعنی:

```text
یک رشته متنی آماده چاپ
```

---

# داک استرینگ

```python
"""
Format scan results for terminal output.
"""
```

---

معنی:

```text
نتایج اسکن را برای نمایش در ترمینال قالب‌بندی کن.
```

---

# بررسی حالت بدون نتیجه

```python
if not results:
```

---

یادمان باشد:

```python
[]
```

در پایتون:

```python
False
```

محسوب می‌شود.

---

پس:

```python
if not results:
```

یعنی:

```text
اگر لیست خالی است
```

---

# خروجی

```python
return "No open ports found."
```

---

مثال:

```python
[]
```

↓

```text
No open ports found.
```

---

این باعث می‌شود برنامه خروجی معنادار داشته باشد.

---

# ساخت خطوط اولیه جدول

```python
lines = [
```

---

یک لیست جدید می‌سازیم.

---

این لیست تمام خطوط خروجی را نگهداری می‌کند.

---

# خط Header

```python
f"{'PORT':<8} {'STATUS':<8} {'SERVICE':<16} {'BANNER'}"
```

---

خروجی:

```text
PORT     STATUS   SERVICE          BANNER
```

---

این سطر عنوان ستون‌ها است.

---

# آشنایی با Format Alignment

قسمت:

```python
:<8
```

بسیار مهم است.

---

مثال:

```python
f"{'PORT':<8}"
```

---

معنی:

```text
رشته را در فضای 8 کاراکتری
چپ‌چین کن.
```

---

مثال:

```text
PORT____
```

(زیرخط فقط برای نمایش فاصله است)

---

# ستون دوم

```python
{'STATUS':<8}
```

---

خروجی:

```text
STATUS
```

---

در فضایی به طول:

```text
8
```

---

# ستون سوم

```python
{'SERVICE':<16}
```

---

خروجی:

```text
SERVICE
```

---

در فضایی به طول:

```text
16
```

---

چرا 16؟

---

چون نام سرویس‌ها معمولاً بلندتر هستند.

---

# خط جداکننده

```python
"-" * 70
```

---

یادمان باشد:

```python
"-" * 5
```

↓

```text
-----
```

---

پس:

```python
"-" * 70
```

↓

```text
----------------------------------------------------------------------
```

---

# شروع پردازش نتایج

```python
for result in results:
```

---

مثال:

```python
ScanResult(
    port=22,
    service="ssh",
    banner="OpenSSH"
)
```

---

در هر دور:

```python
result
```

یک شیء ScanResult است.

---

# مدیریت Banner خالی

```python
banner = result.banner or "-"
```

---

اگر:

```python
result.banner
```

برابر:

```python
None
```

باشد

---

خروجی:

```python
"-"
```

خواهد بود.

---

مثال:

قبل:

```python
None
```

---

بعد:

```text
-
```

---

چرا؟

---

برای اینکه جدول تمیزتر شود.

---

# بررسی طول Banner

```python
if len(banner) > max_banner_length:
```

---

اگر طول Banner بیشتر از:

```python
40
```

باشد

---

وارد شرط می‌شود.

---

مثال:

```text
Apache Ubuntu OpenSSL PHP Version Very Long Banner...
```

---

# کوتاه کردن Banner

```python
banner[: max_banner_length - 3]
```

---

فرض کنیم:

```python
40
```

---

پس:

```python
37
```

کاراکتر اول گرفته می‌شود.

---

# اضافه کردن سه نقطه

```python
+ "..."
```

---

خروجی:

```text
Apache Ubuntu OpenSSL PHP Version...
```

---

این تکنیک:

```text
Text Truncation
```

نام دارد.

---

در تقریباً تمام نرم‌افزارهای حرفه‌ای استفاده می‌شود.

---

# ساخت سطر جدول

```python
lines.append(
```

---

یعنی:

```text
یک خط جدید به جدول اضافه کن.
```

---

# ستون Port

```python
{result.port:<8}
```

---

مثال:

```python
22
```

↓

```text
22
```

در فضای 8 کاراکتری.

---

# ستون Status

```python
{'OPEN':<8}
```

---

خروجی:

```text
OPEN
```

---

فعلاً چون فقط پورت‌های باز را نمایش می‌دهیم همیشه:

```text
OPEN
```

است.

---

# ستون Service

```python
{result.service:<16}
```

---

مثال:

```python
"http"
```

↓

```text
http
```

---

# ستون Banner

```python
{banner}
```

---

مثال:

```text
Apache
```

---

یا:

```text
OpenSSH
```

---

# نمونه خروجی نهایی

```text
22       OPEN     ssh              OpenSSH
80       OPEN     http             Apache
443      OPEN     https            Nginx
```

---

# ساخت رشته نهایی

```python
"\n".join(lines)
```

---

این قسمت بسیار مهم است.

---

فرض کن:

```python
[
    "line1",
    "line2",
    "line3"
]
```

---

اگر بنویسیم:

```python
"\n".join(lines)
```

---

خروجی:

```text
line1
line2
line3
```

---

خواهد شد.

---

یعنی:

```text
تمام خطوط به یک رشته چندخطی تبدیل می‌شوند.
```

---

# خروجی نهایی تابع

مثال:

```text
PORT     STATUS   SERVICE          BANNER
----------------------------------------------------------------------
22       OPEN     ssh              OpenSSH
80       OPEN     http             Apache
443      OPEN     https            Nginx
```

---

# چرا این فایل مهم است؟

ممکن است در نگاه اول ساده به نظر برسد.

---

اما در دنیای واقعی:

```text
User Experience
```

بسیار مهم است.

---

کاربر خروجی را می‌بیند.

---

اگر خروجی نامرتب باشد:

```text
کل برنامه غیرحرفه‌ای به نظر می‌رسد.
```

---

به همین دلیل تقریباً تمام ابزارهای حرفه‌ای:

<p dir='rtl'>
• Nmap <br>
• Wireshark <br>
• Metasploit <br>
• Docker
</p>

روی Formatting بسیار کار می‌کنند.

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ Formatter چیست <br>
✅ چرا Formatting مهم است <br>
✅ f-string چیست <br>
✅ Alignment چیست <br>
✅ <span dir='ltr'>:<8</span> چیست <br>
✅ <span dir='ltr'>:<16</span> چیست <br>
✅ Text Truncation چیست <br>
✅ join چیست <br>
✅ append چیست <br>
✅ چگونه خروجی جدولی ساخته می‌شود
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد آخرین فایل دایرکتوری:

```text
src
```

می‌شویم:

```text
src/cli.py
```

این مهم‌ترین فایل کل پروژه است.

---

در آن یاد می‌گیریم:

<p dir='rtl'>
• argparse چیست <br>
• CLI چیست <br>
• Program Entry Point چیست <br>
• چگونه تمام ماژول‌های پروژه به هم متصل می‌شوند <br>
• جریان کامل اجرای پورت اسکنر از ابتدا تا انتها چگونه است
</p>

</div>