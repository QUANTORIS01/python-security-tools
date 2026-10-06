# درس ۱۳: CSV Handling در Python

## مقدمه

<p dir='rtl'>
CSV مخفف عبارت:
</p>

```text
Comma-Separated Values
```

است.

<p dir='rtl'>
CSV یکی از رایج‌ترین فرمت‌های ذخیره و تبادل داده در جهان محسوب می‌شود.
</p>

بسیاری از ابزارها و نرم‌افزارها از CSV پشتیبانی می‌کنند:

<p dir='rtl'>
• Microsoft Excel <br>
• Google Sheets <br>
• LibreOffice Calc <br>
• ابزارهای مانیتورینگ <br>
• سیستم‌های گزارش‌گیری <br>
• ابزارهای امنیتی <br>
• برنامه‌های تحلیل داده
</p>

در پروژه‌های امنیتی نیز معمولاً نتایج اسکن، لاگ‌ها و گزارش‌ها در قالب CSV ذخیره می‌شوند.

---

# فایل CSV چیست؟

نمونه یک فایل CSV:

```csv
port,service,banner
22,ssh,OpenSSH
80,http,Apache
443,https,Nginx
```

هر سطر یک رکورد است.

هر ستون با کاما از ستون بعدی جدا می‌شود.

---

# ارتباط CSV و Python

در Python برای کار با CSV از ماژول داخلی:

```python
import csv
```

استفاده می‌کنیم.

این ماژول بخشی از Standard Library است و نیازی به نصب ندارد.

---

# نوشتن فایل CSV

مثال:

```python
import csv

with open(
    "ports.csv",
    "w",
    newline="",
    encoding="utf-8",
) as file:

    writer = csv.writer(file)

    writer.writerow(
        ["port", "service"]
    )

    writer.writerow(
        [22, "ssh"]
    )

    writer.writerow(
        [80, "http"]
    )
```

فایل ایجاد شده:

```csv
port,service
22,ssh
80,http
```

---

# خواندن فایل CSV

مثال:

```python
import csv

with open(
    "ports.csv",
    encoding="utf-8",
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

خروجی:

```python
['port', 'service']
['22', 'ssh']
['80', 'http']
```

---

# هر سطر یک لیست است

مثال:

```python
row = ['22', 'ssh']
```

دسترسی:

```python
print(row[0])
```

خروجی:

```text
22
```

---

# رد کردن Header

معمولاً اولین سطر شامل نام ستون‌ها است.

مثال:

```python
import csv

with open(
    "ports.csv",
    encoding="utf-8",
) as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row)
```

خروجی:

```python
['22', 'ssh']
['80', 'http']
```

---

# استفاده از DictReader

گاهی بهتر است داده‌ها به شکل Dictionary خوانده شوند.

مثال:

```python
import csv

with open(
    "ports.csv",
    encoding="utf-8",
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

خروجی:

```python
{
    'port': '22',
    'service': 'ssh'
}

{
    'port': '80',
    'service': 'http'
}
```

---

# دسترسی به ستون‌ها

```python
print(row["service"])
```

خروجی:

```text
ssh
```

---

# نوشتن CSV با DictWriter

مثال:

```python
import csv

with open(
    "ports.csv",
    "w",
    newline="",
    encoding="utf-8",
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "port",
            "service",
        ]
    )

    writer.writeheader()

    writer.writerow(
        {
            "port": 22,
            "service": "ssh",
        }
    )
```

---

# چرا newline مهم است؟

در ویندوز اگر:

```python
newline=""
```

قرار ندهیم ممکن است سطرهای خالی اضافی ایجاد شوند.

همیشه هنگام نوشتن CSV از آن استفاده کنید.

---

<div align='right'>

# <span dir='rtl'>CSV در پروژه DNS Lookup</span>

</div>

در فایل:

```text
csv_exporter.py
```

نتایج Lookup به CSV تبدیل می‌شوند.

نمونه خروجی:

```csv
domain,record_type,value
google.com,A,8.8.8.8
google.com,A,8.8.4.4
```

---

<div align='right'>

# <span dir='rtl'>CSV در پروژه Port Scanner</span>

</div>

نمونه:

```csv
port,service,banner
22,ssh,OpenSSH
80,http,Apache
443,https,Nginx
```

این نوع خروجی برای:

<p dir='rtl'>
• Excel <br>
• Google Sheets <br>
• تحلیل داده <br>
• گزارش‌گیری
</p>

بسیار مناسب است.

---

<div align='right'>

# <span dir='rtl'>CSV و اتوماسیون</span>

</div>

یکی از رایج‌ترین کاربردهای CSV:

```text
Export → Analyze → Report
```

است.

مثال:

```text
Port Scanner
      ↓
CSV Export
      ↓
Excel
      ↓
Security Report
```

---

# مدیریت خطاها

ممکن است فایل وجود نداشته باشد.

مثال:

```python
import csv

try:
    with open(
        "missing.csv"
    ) as file:
        reader = csv.reader(file)

except FileNotFoundError:
    print("File not found")
```

---

# اعتبارسنجی داده‌ها

نباید فرض کنیم داده‌های CSV همیشه معتبر هستند.

مثال:

```python
for row in reader:

    if len(row) != 2:
        continue
```

---

# اشتباهات رایج

## فراموش کردن Header

نامناسب:

```csv
22,ssh
80,http
```

---

بهتر:

```csv
port,service
22,ssh
80,http
```

---

## فراموش کردن newline

نامناسب:

```python
open("file.csv", "w")
```

---

بهتر:

```python
open(
    "file.csv",
    "w",
    newline=""
)
```

---

## فرض کردن نوع داده

تمام داده‌های CSV به صورت رشته خوانده می‌شوند.

مثال:

```python
row["port"]
```

خروجی:

```python
"22"
```

تبدیل:

```python
port = int(
    row["port"]
)
```

---

# مزایای CSV

<p dir='rtl'>
• ساده <br>
• سبک <br>
• قابل حمل <br>
• قابل خواندن <br>
• پشتیبانی گسترده <br>
• مناسب گزارش‌گیری
</p>

---

# محدودیت‌های CSV

<p dir='rtl'>
• فاقد ساختار تو در تو <br>
• فاقد نوع داده <br>
• فاقد اعتبارسنجی داخلی <br>
• مناسب داده‌های پیچیده نیست
</p>

برای داده‌های پیچیده معمولاً از JSON استفاده می‌شود.

---

# مقایسه JSON و CSV

<div align='center'>

| ویژگی           | CSV        | JSON  |
| --------------- | ---------- | ----- |
| خوانایی         | بالا       | بالا  |
| سادگی           | بسیار بالا | بالا  |
| ساختار تو در تو | ندارد      | دارد  |
| حجم             | کمتر       | بیشتر |
| مناسب گزارش     | عالی       | خوب   |
| مناسب API       | ضعیف       | عالی  |

</div>

---

# جمع‌بندی

در این درس یاد گرفتیم:

<div align='right'>

<span dir='rtl'>• CSV چیست</span> <br>
<span dir='rtl'>• ماژول `csv`</span> <br>
<span dir='rtl'>• `csv.reader`</span> <br>
<span dir='rtl'>• `csv.writer`</span> <br>
<span dir='rtl'>• `DictReader`</span> <br>
<span dir='rtl'>• `DictWriter`</span> <br>
<span dir='rtl'>• خواندن فایل CSV</span> <br>
<span dir='rtl'>• نوشتن فایل CSV</span> <br>
<span dir='rtl'>• مدیریت خطاها</span> <br>
<span dir='rtl'>• اعتبارسنجی داده‌ها</span> <br>
<span dir='rtl'>• کاربرد CSV در پروژه‌های امنیتی</span>

</div>

<p dir='rtl'>
CSV یکی از مهم‌ترین فرمت‌های خروجی در ابزارهای امنیتی، شبکه و اتوماسیون است و تقریباً در تمام پروژه‌های عملی با آن مواجه خواهید شد.
</p>
