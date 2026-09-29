# بررسی کامل فایل `csv_exporter.py`

# مقدمه

در جلسه قبل فایل:

```text
src/exporter.py
```

را بررسی کردیم.

در آن یاد گرفتیم:

<p dir='rtl'>
• JSON چیست <br>
• چگونه خروجی اسکن را ذخیره کنیم <br>
• json.dump چگونه کار می‌کند <br>
• UTF-8 چیست <br>
• چرا ابزارهای امنیتی از JSON استفاده می‌کنند
</p>

---

اما یک سؤال مهم مطرح می‌شود:

اگر بخواهیم خروجی را داخل:

<p dir='rtl'>
• Excel <br>
• LibreOffice Calc <br>
• Google Sheets
</p>

باز کنیم چه؟

---

<p dir='rtl'>
JSON برای ماشین‌ها فوق‌العاده است.
</p>

اما برای کار با جدول‌ها همیشه بهترین گزینه نیست.

به همین دلیل فایل:

```text
src/csv_exporter.py
```

را ایجاد کردیم.

---

# محتوای فایل

```python
import csv


def export_csv(data: dict, filename: str) -> None:
    """
    Export scan results to a CSV file.
    """
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["port", "service", "banner"])

        for item in data["open_ports"]:
            writer.writerow(
                [
                    item["port"],
                    item["service"],
                    item.get("banner")
                ]
            )
```

---

# هدف این فایل چیست؟

هدف:

```text
ذخیره نتایج اسکن در قالب جدول
```

است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
CSV چیست؟
</p>

<p dir='rtl'>
CSV مخفف:
</p>

```text
Comma Separated Values
```

است.

---

معنی:

```text
مقادیر جدا شده با ویرگول
```

---

نمونه:

```csv
port,service,banner
80,http,Apache
443,https,Nginx
22,ssh,OpenSSH
```

---

هر خط:

```text
یک رکورد
```

است.

---

هر ستون:

```text
یک فیلد
```

است.

---

# چرا CSV مهم است؟

زیرا تقریباً همه نرم‌افزارهای جدولی دنیا از آن پشتیبانی می‌کنند.

---

مثال:

<p dir='rtl'>
• Microsoft Excel <br>
• Google Sheets <br>
• LibreOffice Calc <br>
• Apple Numbers
</p>

---

همچنین بسیاری از ابزارهای تحلیل داده:

<p dir='rtl'>
• Pandas <br>
• NumPy <br>
• Power BI <br>
• Tableau
</p>

از CSV پشتیبانی می‌کنند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import
</p>

```python
import csv
```

---

این ماژول یکی از کتابخانه‌های استاندارد پایتون است.

---

وظیفه:

```text
ساخت و خواندن فایل‌های CSV
```

---

# تعریف تابع

```python
def export_csv(
    data: dict,
    filename: str
) -> None:
```

---

## پارامتر اول

```python
data
```

---

اطلاعات اسکن.

مثال:

```python
{
    "open_ports": [
        {
            "port": 80,
            "service": "http",
            "banner": "Apache"
        }
    ]
}
```

---

## پارامتر دوم

```python
filename
```

---

نام فایل خروجی.

مثال:

```python
"result.csv"
```

---

# خروجی

```python
None
```

---

تابع چیزی برنمی‌گرداند.

---

فقط فایل ایجاد می‌کند.

---

# داک استرینگ

```python
"""
Export scan results to a CSV file.
"""
```

---

معنی:

```text
نتایج اسکن را در قالب CSV ذخیره کن.
```

---

# باز کردن فایل

```python
with open(
    filename,
    "w",
    newline="",
    encoding="utf-8"
) as file:
```

---

در اینجا تقریباً همان چیزی را می‌بینیم که در فایل JSON داشتیم.

---

اما یک پارامتر جدید اضافه شده است:

```python
newline=""
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
newline چیست؟
</p>

این قسمت یکی از مهم‌ترین نکات کار با CSV است.

---

در ویندوز اگر این پارامتر را ننویسیم:

```python
open(file, "w")
```

ممکن است فایل خروجی این شکلی شود:

```text
row1

row2

row3
```

---

یعنی بین هر سطر یک خط خالی اضافی ایجاد شود.

---

برای جلوگیری از این مشکل:

```python
newline=""
```

قرار داده شده است.

---

این یکی از نکاتی است که بسیاری از برنامه‌نویسان مبتدی نمی‌دانند.

---

# ساخت Writer

```python
writer = csv.writer(file)
```

---

اینجا یک شیء جدید ساخته می‌شود.

---

این شیء وظیفه دارد:

```text
داده‌ها را به فرمت CSV تبدیل کند.
```

---

می‌توان تصور کرد:

```text
writer = ماشین تولید CSV
```

---

# ساخت هدر جدول

```python
writer.writerow(
    [
        "port",
        "service",
        "banner"
    ]
)
```

---

اولین سطر فایل را می‌سازد.

---

خروجی:

```csv
port,service,banner
```

---

این سطر:

```text
نام ستون‌ها
```

است.

---

اگر این سطر را ننویسیم:

```csv
80,http,Apache
443,https,Nginx
```

---

تشخیص اینکه هر ستون چه معنایی دارد سخت می‌شود.

---

به همین دلیل همیشه Header می‌نویسیم.

---

# حلقه اصلی

```python
for item in data["open_ports"]:
```

---

فرض کن داده ما این باشد:

```python
{
    "open_ports": [
        {
            "port": 80,
            "service": "http",
            "banner": "Apache"
        },
        {
            "port": 443,
            "service": "https",
            "banner": "Nginx"
        }
    ]
}
```

---

در هر دور حلقه:

```python
item
```

یکی از این دیکشنری‌ها می‌شود.

---

دور اول:

```python
{
    "port": 80,
    "service": "http",
    "banner": "Apache"
}
```

---

دور دوم:

```python
{
    "port": 443,
    "service": "https",
    "banner": "Nginx"
}
```

---

# نوشتن هر سطر

```python
writer.writerow(
    [
        item["port"],
        item["service"],
        item.get("banner")
    ]
)
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
item["port"]
</p>

مثال:

```python
80
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
item["service"]
</p>

مثال:

```python
"http"
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
item.get("banner")
</p>

مثال:

```python
"Apache"
```

---

# چرا get استفاده شده؟

سؤال مهم.

چرا ننوشته‌ایم:

```python
item["banner"]
```

؟

---

فرض کن بنر وجود نداشته باشد.

---

مثال:

```python
{
    "port": 53,
    "service": "domain"
}
```

---

اگر بنویسیم:

```python
item["banner"]
```

خطا رخ می‌دهد:

```python
KeyError
```

---

اما:

```python
item.get("banner")
```

در صورت نبودن مقدار:

```python
None
```

برمی‌گرداند.

---

و برنامه کرش نمی‌کند.

---

این یکی از تصمیم‌های طراحی خوب در پروژه است.

---

# خروجی نهایی

اگر داده:

```python
{
    "open_ports": [
        {
            "port": 80,
            "service": "http",
            "banner": "Apache"
        },
        {
            "port": 443,
            "service": "https",
            "banner": "Nginx"
        }
    ]
}
```

باشد.

---

فایل خروجی:

```csv
port,service,banner
80,http,Apache
443,https,Nginx
```

خواهد بود.

---

# تفاوت CSV و JSON

| CSV | JSON |
|-------|-------|
| جدولی | ساختاری |
| مناسب Excel | مناسب API |
| خواندن سریع | انعطاف بالا |
| سبک | توصیفی‌تر |
| ستون محور | شیء محور |

---

# چرا هر دو را پیاده‌سازی کردیم؟

چون کاربران متفاوت هستند.

---

برخی می‌خواهند:

```text
خروجی را در Excel باز کنند.
```

---

برخی می‌خواهند:

```text
خروجی را وارد برنامه دیگری کنند.
```

---

به همین دلیل:

```text
JSON + CSV
```

هر دو پشتیبانی شده‌اند.

---

این دقیقاً همان کاری است که ابزارهای حرفه‌ای انجام می‌دهند.

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ CSV چیست <br>
✅ تفاوت CSV و JSON چیست <br>
✅ csv.writer چیست <br>
✅ writerow چیست <br>
✅ Header چیست <br>
✅ newline="" چرا استفاده می‌شود <br>
✅ حلقه ذخیره رکوردها چگونه کار می‌کند <br>
✅ item.get چرا استفاده شده است <br>
✅ چگونه خروجی را وارد Excel کنیم
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
src/logger.py
```

می‌شویم.

در آن یاد می‌گیریم:

<p dir='rtl'>
• Logging چیست <br>
• تفاوت print و log چیست <br>
• چرا ابزارهای امنیتی لاگ تولید می‌کنند <br>
• Handler چیست <br>
• Formatter چیست <br>
• FileHandler چیست <br>
• چگونه رخدادهای اسکن را ذخیره کنیم
</p>

