<div dir="rtl">

# جلسه ۱۰: جمع‌بندی پایتون برای ساخت Port Scanner

## هدف این جلسه

تا اینجا تقریباً تمام ابزارهای پایتونی که برای ساخت پروژه Port Scanner نیاز داشتیم را یاد گرفتیم.

در این جلسه می‌خواهیم ببینیم هر بخش از پروژه واقعی ما دقیقاً از کدام مفاهیم پایتون استفاده می‌کند.

بعد از پایان این جلسه آماده ورود به فصل شبکه خواهیم بود.

---

# تصویری کلی از پروژه

پورت اسکنر ما در ظاهر ساده است:

<p dir='rtl'>
1. دریافت IP <br>
2. دریافت بازه پورت <br>
3. بررسی باز بودن پورت‌ها <br>
4. تشخیص سرویس <br>
5. دریافت Banner <br>
6. نمایش نتیجه <br>
7. ذخیره خروجی
</p>

اما پشت صحنه تقریباً تمام مفاهیم مهم پایتون را استفاده کرده‌ایم.

---

# دریافت اطلاعات از کاربر

فایل:

```python
cli.py
```

نمونه:

```python
parser.add_argument("ip")
parser.add_argument("start_port")
parser.add_argument("end_port")
```

اینجا از موارد زیر استفاده کرده‌ایم:

<p dir='rtl'>
• متغیرها <br>
• توابع <br>
• ماژول‌ها <br>
• کتابخانه argparse
</p>

---

# اعتبارسنجی ورودی‌ها

فایل:

```python
validator.py
```

مثال:

```python
if port < 1 or port > 65535:
    raise ValueError()
```

اینجا از:

<p dir='rtl'>
• شرط‌ها <br>
• عملگرها <br>
• Exception ها
</p>

استفاده شده است.

---

# اسکن پورت‌ها

فایل:

```python
scanner.py
```

مثال:

```python
for port in range(start_port, end_port + 1):
```

اینجا از:

<p dir='rtl'>
• حلقه‌ها <br>
• توابع <br>
• ThreadPoolExecutor
<?p>

استفاده شده است.

---

# کار با Socket

مثال:

```python
with socket.socket() as sock:
    ...
```

اینجا از:

<p dir='rtl'>
• Context Manager <br>
• ماژول socket <br>
• مدیریت منابع
</p>

استفاده کرده‌ایم.

---

# تشخیص سرویس‌ها

فایل:

```python
services.py
```

مثال:

```python
COMMON_PORTS = {
    80: "http",
    443: "https",
}
```

اینجا از:

<p dir='rtl'>
• Dictionary <br>
• Lookup سریع
</p>

استفاده شده است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Banner Grabbing
</p>

فایل:

```python
banner.py
```

مثال:

```python
banner = sock.recv(1024)
```

اینجا از:

<p dir='rtl'>
• بایت‌ها (Bytes) <br>
• Decode <br>
• مدیریت خطا
</p>

استفاده شده است.

---

# ساخت مدل داده

فایل:

```python
models.py
```

مثال:

```python
@dataclass(frozen=True)
class ScanResult:
```

اینجا از:

<p dir='rtl'>
• Class <br>
• Dataclass <br>
• Object
</p>

استفاده کرده‌ایم.

---

# ذخیره خروجی JSON

فایل:

```python
exporter.py
```

مثال:

```python
json.dump(data, file)
```

مفاهیم:

<p dir='rtl'>
• فایل‌ها <br>
• JSON <br>
• Dictionary
</p>

---

# ذخیره خروجی CSV

فایل:

```python
csv_exporter.py
```

مثال:

```python
writer.writerow(row)
```

مفاهیم:

<p dir='rtl'>
• CSV <br>
• File Handling
</p>

---

# نمایش نتایج

فایل:

```python
formatter.py
```

مثال:

```python
f"{result.port:<8}"
```

مفاهیم:

<p dir='rtl'>
• String Formatting <br>
• f-string
</p>

---

# لاگ‌گیری

فایل:

```python
logger.py
```

مثال:

```python
logger.info("Scan started")
```

مفاهیم:

<p dir='rtl'>
• Logging <br>
• File Writing
</p>

---

# تست‌نویسی

فایل:

```python
tests/
```

مثال:

```python
def test_scan_open_port():
```

مفاهیم:

<p dir='rtl'>
• Unit Testing <br>
• Pytest <br>
• Mocking
</p>

---

# چیزی که تا الان یاد گرفتیم

تا این لحظه شما با مفاهیم زیر آشنا شده‌اید:

<p dir='rtl'>
✓ متغیرها <br>
✓ انواع داده <br>
✓ شرط‌ها <br>
✓ حلقه‌ها <br>
✓ توابع <br>
✓ ماژول‌ها <br>
✓ فایل‌ها <br>
✓ JSON <br>
✓ CSV <br>
✓ Exception <br>
✓ Socket <br>
✓ Logging <br>
✓ Dataclass <br>
✓ Testing
</p>

---

# آیا الان می‌توانیم Port Scanner بسازیم؟

بله.

در واقع پروژه‌ای که تا الان ساخته‌ایم دقیقاً با همین دانش نوشته شده است.

اما هنوز یک قطعه مهم کم است:

«دانستن شبکه»

ما تا الان یاد گرفتیم چگونه کدنویسی کنیم.

اما هنوز نمی‌دانیم:

<p dir='rtl'>
• IP چیست؟ <br>
• Port چیست؟ <br>
• TCP چیست؟ <br>
• UDP چیست؟ <br>
• DNS چیست؟ <br>
• Router چیست؟ <br>
• Packet چیست؟
</p>

بدون دانستن این مفاهیم درک Port Scanner ناقص خواهد بود.

---

# پایان فصل اول

تبریک 🎉

شما فصل پایتون را تمام کردید.

اکنون آماده ورود به فصل دوم هستید:

<p align='right' dir='ltr' style='font-size:32px; font-wight:bold'>
02-networking
</p>

و در آنجا از صفر تا سطح موردنیاز برای درک کامل Port Scanner با شبکه آشنا خواهیم شد.

</div>