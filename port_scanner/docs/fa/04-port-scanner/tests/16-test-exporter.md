# بررسی کامل فایل `test_exporter.py`

# مقدمه

تا اینجای بخش تست‌ها یاد گرفتیم چگونه:

✅ توابع اعتبارسنجی را تست کنیم

✅ توابع اسکن شبکه را تست کنیم

✅ تشخیص سرویس را تست کنیم

---

اما اکنون وارد نوع دیگری از تست می‌شویم.

---

تا الان بیشتر خروجی توابع ما:

```python
True
False
list
str
```

بود.

---

اما این بار با چیزی متفاوت روبه‌رو هستیم:

```text
فایل
```

---

یعنی باید بررسی کنیم:

```text
آیا فایل واقعاً ساخته شده است؟
```

و

```text
آیا محتوای فایل درست ذخیره شده است؟
```

---

این دقیقاً کاری است که:

```text
test_exporter.py
```

انجام می‌دهد.

---

# هدف فایل

هدف:

```text
تست export_json()
```

است.

---

اگر یادت باشد در:

```text
src/exporter.py
```

داشتیم:

```python
def export_json(
    data: dict,
    filename: str
):
```

---

وظیفه:

```text
ذخیره داده‌ها در فایل JSON
```

بود.

---

اکنون باید مطمئن شویم:

```python
export_json()
```

واقعاً درست کار می‌کند.

---

# محتوای فایل

```python
import json

from src import export_json


def test_export_json_creates_file(tmp_path):
    output_file = tmp_path / "results.json"
    data = {
        "target": "127.0.0.1",
        "open_ports": [80, 443]
    }
    export_json(data, str(output_file))
    assert output_file.exists()


def test_export_json_content(tmp_path):
    output_file = tmp_path / "results.json"
    data = {
        "target": "127.0.0.1",
        "open_ports": [80, 443]
    }
    export_json(data, str(output_file))

    with open(output_file, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
    assert loaded_data == data
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import اول
</p>

```python
import json
```

---

چرا؟

---

چون بعداً می‌خواهیم فایل ساخته‌شده را بخوانیم.

---

برای خواندن JSON از:

```python
json.load()
```

استفاده می‌کنیم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import دوم
</p>

```python
from src import export_json
```

---

تابعی که قرار است تست شود.

---

# تست اول

```python
def test_export_json_creates_file(
    tmp_path
):
```

---

هدف:

```text
بررسی ساخت فایل
```

است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
tmp_path چیست؟
</p>

یکی از قابلیت‌های فوق‌العاده pytest.

---

<p dir='rtl'>
Pytest به صورت خودکار:
</p>

```python
tmp_path
```

را به تابع تزریق می‌کند.

---

این مسیر:

```text
یک دایرکتوری موقت
```

است.

---

مثال:

```text
C:\Temp\pytest-1234\
```

---

یا:

```text
/tmp/pytest/
```

---

بعد از پایان تست:

```text
خودکار حذف می‌شود.
```

---

# چرا از tmp_path استفاده می‌کنیم؟

فرض کن فایل واقعی بسازیم:

```python
results.json
```

---

مشکلات:

❌ فایل‌های اضافی روی سیستم می‌مانند

❌ تست‌ها روی هم اثر می‌گذارند

❌ پروژه کثیف می‌شود

---

برای همین:

```python
tmp_path
```

راه حرفه‌ای تست فایل‌ها است.

---

# ساخت مسیر فایل

```python
output_file =
    tmp_path / "results.json"
```

---

خروجی:

```text
/tmp/pytest/results.json
```

---

یا چیزی مشابه آن.

---

# ساخت داده تستی

```python
data = {
    "target": "127.0.0.1",
    "open_ports": [80, 443]
}
```

---

داده‌ای که قرار است ذخیره شود.

---

# اجرای تابع

```python
export_json(
    data,
    str(output_file)
)
```

---

جریان:

```python
data
```

↓

```python
export_json()
```

↓

```python
results.json
```

---

# بررسی وجود فایل

```python
assert output_file.exists()
```

---

متد:

```python
exists()
```

بررسی می‌کند:

```text
آیا فایل وجود دارد؟
```

---

اگر فایل ساخته شده باشد:

```python
True
```

---

اگر ساخته نشده باشد:

```python
False
```

---

در نتیجه:

```python
assert
```

تست را Fail می‌کند.

---

# هدف تست اول

فقط بررسی:

```text
ساخته شدن فایل
```

است.

---

نه محتوای آن.

---

# تست دوم

```python
def test_export_json_content(
    tmp_path
):
```

---

این تست مهم‌تر است.

---

چرا؟

---

زیرا فقط وجود فایل کافی نیست.

---

ممکن است فایل ساخته شود اما:

```text
داده اشتباه باشد.
```

---

# ساخت فایل

دقیقاً مثل تست قبلی:

```python
output_file =
    tmp_path / "results.json"
```

---

و:

```python
data = {...}
```

---

و:

```python
export_json(...)
```

---

# باز کردن فایل

```python
with open(
    output_file,
    "r",
    encoding="utf-8"
) as file:
```

---

حالت:

```python
"r"
```

یعنی:

```text
Read Mode
```

---

# خواندن JSON

```python
loaded_data =
    json.load(file)
```

---

اگر داخل فایل باشد:

```json
{
    "target": "127.0.0.1",
    "open_ports": [80, 443]
}
```

---

خروجی:

```python
{
    "target": "127.0.0.1",
    "open_ports": [80, 443]
}
```

---

یعنی دوباره تبدیل به Dictionary می‌شود.

---

# مقایسه داده‌ها

```python
assert loaded_data == data
```

---

مهم‌ترین خط فایل.

---

اگر:

```python
loaded_data
```

برابر باشد با:

```python
data
```

---

تست:

```text
PASS
```

می‌شود.

---

اگر حتی یک مقدار متفاوت باشد:

```text
FAIL
```

خواهد شد.

---

# مثال

فرض کن تابع اشتباه ذخیره کند:

```json
{
    "target": "127.0.0.1"
}
```

---

و:

```python
open_ports
```

را فراموش کند.

---

در این حالت:

```python
loaded_data == data
```

---

برابر:

```python
False
```

خواهد شد.

---

و تست شکست می‌خورد.

---

# نوع تست چیست؟

این فایل نمونه‌ای از:

```text
File I/O Testing
```

است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
File I/O چیست؟
</p>

<p dir='rtl'>
I/O مخفف:
</p>

```text
Input / Output
```

است.

---

یعنی:

```text
خواندن و نوشتن داده
```

---

مثال‌ها:

```python
open()
```

---

```python
read()
```

---

```python
write()
```

---

همگی I/O هستند.

---

# نکته مهم

این فایل:

```text
فقط فایل را نمی‌سازد
```

---

بلکه:

```text
صحت محتوا را نیز بررسی می‌کند.
```

---

این دقیقاً همان چیزی است که در تست‌های حرفه‌ای انجام می‌شود.

---

# اگر تست دوم را نداشتیم چه می‌شد؟

فرض کن:

```python
export_json()
```

فایل خالی تولید کند.

---

تست اول:

```python
PASS
```

می‌شود.

---

چون فایل وجود دارد.

---

اما:

```python
محتوا اشتباه است.
```

---

برای همین وجود تست دوم ضروری است.

---

# خروجی pytest

اگر همه چیز درست باشد:

```bash
pytest
```

---

خروجی:

```text
===== 2 passed =====
```

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ تست فایل‌های JSON <br>
✅ tmp_path چیست <br>
✅ Temporary Directory چیست <br>
✅ exists() چیست <br>
✅ File I/O Testing چیست <br>
✅ json.load چیست <br>
✅ چگونه محتوای فایل را اعتبارسنجی کنیم <br>
✅ تفاوت تست وجود فایل و تست محتوای فایل
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
tests/test_cli.py
```

می‌شویم.

---

این یکی از مهم‌ترین تست‌های پروژه است.

---

در آن یاد می‌گیریم:

<p dir='rtl'>
✅ Monkeypatch چیست <br>
✅ چگونه ورودی‌های CLI را شبیه‌سازی کنیم <br>
✅ چگونه sys.argv را تست کنیم <br>
✅ چگونه خروجی ترمینال را بررسی کنیم <br>
✅ تست Entry Point چگونه انجام می‌شود
</p>
