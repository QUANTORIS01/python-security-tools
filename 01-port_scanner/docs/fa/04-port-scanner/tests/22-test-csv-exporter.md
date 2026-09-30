<div dir='rtl'>

# بررسی کامل فایل `test_csv_exporter.py`

# مقدمه

تا اینجا تقریباً تمام بخش‌های پروژه را بررسی کرده‌ایم.

---

اگر یادت باشد در فصل پایتون گفتیم:

```text
CSV یکی از رایج‌ترین فرمت‌های ذخیره‌سازی داده است.
```

---

بسیاری از ابزارها می‌توانند فایل CSV را باز کنند:

<p dir='rtl'>
✅ Excel <br>
✅ LibreOffice Calc <br>
✅ Google Sheets <br>
✅ Pandas <br>
✅ Power BI
</p>

---

برای همین در پروژه پورت اسکنر قابلیت:

```text
Export CSV
```

را پیاده‌سازی کردیم.

---

اگر یادت باشد در فایل:

```text
src/csv_exporter.py
```

تابع زیر را داشتیم:

```python
export_csv()
```

---

وظیفه:

```text
تبدیل نتایج اسکن
به فایل CSV
```

را بر عهده داشت.

---

اکنون باید مطمئن شویم:

<p dir='rtl'>
✅ فایل ساخته می‌شود <br>
✅ محتوای فایل درست است <br>
✅ Header ها درست هستند <br>
✅ داده‌ها به ترتیب صحیح ذخیره می‌شوند
</p>

---

محتوای فایل:

```python
import csv

from src import export_csv


def test_export_csv_creates_file(tmp_path):
    output_file = tmp_path / "results.csv"
    data = {
        "target": "127.0.0.1",
        "open_ports": [
            {
                "port": 80,
                "service": "http",
            },
            {
                "port": 443,
                "service": "https",
            },
        ],
    }
    export_csv(data, str(output_file))
    assert output_file.exists()


def test_export_csv_content(tmp_path):
    output_file = tmp_path / "results.csv"
    data = {
        "target": "127.0.0.1",
        "open_ports": [
            {
                "port": 80,
                "service": "http",
                "banner": "HTTP/1.1 200 OK",
            },
            {
                "port": 443,
                "service": "https",
                "banner": "HTTPS Server",
            },
        ],
    }
    export_csv(data, str(output_file))

    with open(output_file, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
    assert rows == [
        ["port", "service", "banner"],
        ["80", "http", "HTTP/1.1 200 OK"],
        ["443", "https", "HTTPS Server"],
    ]
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import ها
</p>

```python
import csv

from src import export_csv
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import اول
</p>

```python
import csv
```

---

برای خواندن فایل CSV تولیدشده.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import دوم
</p>

```python
from src import export_csv
```

---

تابعی که قرار است تست شود.

---

# هدف فایل چیست؟

بررسی دو موضوع مهم:

```text
ساخته شدن فایل
```

---

و

```text
درستی محتوای فایل
```

---

# تست اول

```python
def test_export_csv_creates_file(
    tmp_path
):
```

---

هدف:

```text
بررسی ساخته شدن فایل CSV
```

است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
tmp_path چیست؟
</p>

یکی از قابلیت‌های فوق‌العاده pytest.

---

```python
tmp_path
```

---

یک پوشه موقت ایجاد می‌کند.

---

مثلاً چیزی شبیه:

```text
/tmp/pytest-12345/
```

---

یا در ویندوز:

```text
C:\Temp\pytest-xxxxx\
```

---

مزیت:

✅ فایل‌های تستی پروژه را کثیف نمی‌کنند

✅ بعد از پایان تست حذف می‌شوند

✅ هر تست محیط مستقل دارد

---

# ساخت مسیر فایل

```python
output_file =
    tmp_path / "results.csv"
```

---

نتیجه:

```text
/tmp/.../results.csv
```

---

# ساخت داده تستی

```python
data = {
    ...
}
```

---

ساختار داده:

```python
{
    "target": "127.0.0.1",
    "open_ports": [...]
}
```

---

دو پورت باز داریم:

```python
80
```

و

```python
443
```

---

# اجرای تابع

```python
export_csv(
    data,
    str(output_file)
)
```

---

تابع:

```python
export_csv()
```

اجرا می‌شود.

---

و باید:

```text
results.csv
```

را بسازد.

---

# بررسی وجود فایل

```python
assert output_file.exists()
```

---

اگر فایل ساخته شده باشد:

```text
PASS
```

---

اگر فایل وجود نداشته باشد:

```text
FAIL
```

---

# اهمیت این تست

این تست بررسی می‌کند:

```text
عملیات نوشتن فایل
واقعاً انجام شده است.
```

---

نه فقط اینکه تابع اجرا شده باشد.

---

# تست دوم

```python
def test_export_csv_content(
    tmp_path
):
```

---

هدف:

```text
بررسی محتوای فایل CSV
```

است.

---

این تست از تست قبلی مهم‌تر است.

---

چرا؟

---

چون:

```text
ساخته شدن فایل کافی نیست.
```

---

ممکن است فایل ساخته شود اما:

<p dir='rtl'>
❌ داده‌ها اشتباه باشند <br>
❌ ترتیب ستون‌ها اشتباه باشد <br>
❌ Header خراب باشد
</p>

---

این تست همه این موارد را بررسی می‌کند.

---

# مسیر فایل

```python
output_file =
    tmp_path / "results.csv"
```

---

همان پوشه موقت.

---

# داده تستی

```python
data = {
    ...
}
```

---

این بار علاوه بر:

```python
port
```

و

```python
service
```

---

داریم:

```python
banner
```

را نیز ذخیره می‌کنیم.

---

پورت اول:

```python
80
```

↓

```python
http
```

↓

```python
HTTP/1.1 200 OK
```

---

پورت دوم:

```python
443
```

↓

```python
https
```

↓

```python
HTTPS Server
```

---

# اجرای تابع

```python
export_csv(
    data,
    str(output_file)
)
```

---

فایل ساخته می‌شود.

---

# باز کردن فایل

```python
with open(
    output_file,
    "r",
    newline="",
    encoding="utf-8"
) as file:
```

---

در حالت خواندن.

---

# خواندن فایل

```python
rows =
    list(
        csv.reader(file)
    )
```

---

اگر فایل چنین باشد:

```csv
port,service,banner
80,http,HTTP/1.1 200 OK
443,https,HTTPS Server
```

---

خروجی:

```python
[
    ["port","service","banner"],
    ["80","http","HTTP/1.1 200 OK"],
    ["443","https","HTTPS Server"]
]
```

---

خواهد بود.

---

# بررسی Header

اولین ردیف:

```python
["port", "service", "banner"]
```

---

دقیقاً همان چیزی است که در:

```python
writer.writerow(...)
```

نوشتیم.

---

# بررسی ردیف اول

```python
[
    "80",
    "http",
    "HTTP/1.1 200 OK"
]
```

---

بررسی می‌کند:

```text
اطلاعات پورت 80
درست ذخیره شده‌اند.
```

---

# بررسی ردیف دوم

```python
[
    "443",
    "https",
    "HTTPS Server"
]
```

---

بررسی می‌کند:

```text
اطلاعات پورت 443
درست ذخیره شده‌اند.
```

---

# نکته جالب

دقت کن:

در داده اولیه:

```python
80
```

---

عدد بود.

---

اما در خروجی:

```python
"80"
```

---

رشته است.

---

چرا؟

---

چون:

```python
csv.reader()
```

همه داده‌ها را به صورت:

```python
str
```

برمی‌گرداند.

---

برای همین تست نیز:

```python
"80"
```

نوشته شده است.

---

نه:

```python
80
```

---

# ارتباط این تست با csv_exporter.py

اگر یادت باشد:

```python
writer.writerow(
    ["port", "service", "banner"]
)
```

---

این تست دقیقاً آن را بررسی می‌کند.

---

همچنین:

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

نیز توسط این تست اعتبارسنجی می‌شود.

---

# اگر ترتیب ستون‌ها عوض شود چه می‌شود؟

فرض کن کسی بنویسد:

```python
["service", "port", "banner"]
```

---

خروجی:

```csv
service,port,banner
```

---

تست فوراً:

```text
FAIL
```

می‌شود.

---

# اگر Banner ذخیره نشود؟

مثلاً:

```python
writer.writerow([
    item["port"],
    item["service"]
])
```

---

تست:

```text
FAIL
```

می‌شود.

---

# اگر ردیف‌ها اشتباه ذخیره شوند؟

مثلاً:

```python
443
```

قبل از:

```python
80
```

قرار گیرد.

---

باز هم:

```text
FAIL
```

می‌شود.

---

# خروجی pytest

اگر همه چیز درست باشد:

```bash
pytest
```

---

خروجی:

```text
==== 2 passed ====
```

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

✅ تست فایل‌های CSV

✅ استفاده از tmp_path

✅ خواندن CSV با csv.reader

✅ تست Header ها

✅ تست ردیف‌های داده

✅ اعتبارسنجی ترتیب ستون‌ها

✅ اعتبارسنجی محتوای فایل

✅ تفاوت عدد و رشته در CSV

✅ اهمیت تست خروجی فایل‌ها

---

# وضعیت فعلی پروژه

فایل‌های تست بررسی‌شده:

```text
test_validator.py
test_scanner.py
test_services.py
test_exporter.py
test_cli.py
test_banner.py
test_models.py
test_results.py
test_formatter.py
test_csv_exporter.py
```

---

تنها چند فایل تست دیگر باقی مانده‌اند و سپس:

```text
کل پروژه
از ابتدا تا انتها
تشریح شده خواهد بود.
```

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
tests/test_logger.py
```

می‌شویم.

---

در آن یاد می‌گیریم:

✅ تست Logging

✅ تست FileHandler

✅ بررسی محتوای Log

✅ جلوگیری از Handler تکراری

✅ تست سیستم ثبت رویدادها

</div>