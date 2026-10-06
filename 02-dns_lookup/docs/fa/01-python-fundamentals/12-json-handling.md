# درس ۱۲: JSON Handling در Python

## مقدمه

<p dir='rtl'>
JSON مخفف عبارت:
</p>

```text
JavaScript Object Notation
```

است.

<p dir='rtl'>
JSON یکی از رایج‌ترین فرمت‌های تبادل داده در جهان محسوب می‌شود و تقریباً در تمام حوزه‌های نرم‌افزار از آن استفاده می‌شود:
</p>

<p dir='rtl'>
• API ها <br>
• سرویس‌های وب <br>
• برنامه‌های تحت وب <br>
• برنامه‌های موبایل <br>
• فایل‌های تنظیمات <br>
• ابزارهای امنیتی <br>
• سیستم‌های مانیتورینگ <br>
• پردازش لاگ‌ها
</p>

در پروژه DNS Lookup نیز خروجی نتایج را در قالب JSON ذخیره می‌کنیم.

---

# نمونه JSON

مثال:

```json
{
    "domain": "google.com",
    "record_type": "A",
    "records": [
        {
            "value": "8.8.8.8"
        }
    ]
}
```

---

# ساختار JSON

<p dir='rtl'>
JSON از دو ساختار اصلی تشکیل شده است:
</p>

<div align='right'>

## Object

</div>

مشابه Dictionary در Python

```json
{
    "name": "Ali",
    "age": 25
}
```

---

<div align='right'>

## Array

</div>

مشابه List در Python

```json
[
    "A",
    "MX",
    "TXT"
]
```

---

# ارتباط JSON و Python

<p dir='rtl'>
Python:
</p>

```python
data = {
    "domain": "google.com",
    "record_type": "A",
}
```

<p dir='rtl'>
JSON:
</p>

```json
{
    "domain": "google.com",
    "record_type": "A"
}
```

---

# ماژول json

برای کار با JSON از ماژول داخلی Python استفاده می‌کنیم:

```python
import json
```

این ماژول بخشی از Standard Library است و نیازی به نصب ندارد.

---

# تبدیل Python به JSON

متد:

```python
json.dumps()
```

مثال:

```python
import json

data = {
    "domain": "google.com",
    "record_type": "A",
}

result = json.dumps(data)

print(result)
```

خروجی:

```json
{"domain": "google.com", "record_type": "A"}
```

---

# زیباسازی JSON

برای خوانایی بیشتر:

```python
import json

data = {
    "domain": "google.com",
    "record_type": "A",
}

print(
    json.dumps(
        data,
        indent=4
    )
)
```

خروجی:

```json
{
    "domain": "google.com",
    "record_type": "A"
}
```

---

# تبدیل JSON به Python

متد:

```python
json.loads()
```

مثال:

```python
import json

raw = '''
{
    "domain": "google.com",
    "record_type": "A"
}
'''

data = json.loads(raw)

print(data)
```

خروجی:

```python
{
    'domain': 'google.com',
    'record_type': 'A'
}
```

---

# نوع داده خروجی

```python
type(data)
```

خروجی:

```python
dict
```

---

# ذخیره JSON در فایل

متد:

```python
json.dump()
```

مثال:

```python
import json

data = {
    "domain": "google.com",
    "record_type": "A",
}

with open(
    "result.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        data,
        file,
        indent=4
    )
```

---

# خواندن JSON از فایل

متد:

```python
json.load()
```

مثال:

```python
import json

with open(
    "result.json",
    encoding="utf-8"
) as file:
    data = json.load(file)

print(data)
```

---

<div align='right'>

# <span dir='rtl'>JSON شامل List</span>

</div>

مثال:

```python
data = {
    "records": [
        "8.8.8.8",
        "1.1.1.1"
    ]
}
```

خروجی:

```json
{
    "records": [
        "8.8.8.8",
        "1.1.1.1"
    ]
}
```

---

<div align='right'>

# <span dir='rtl'>JSON تو در تو</span>

</div>

مثال:

```python
data = {
    "domain": "google.com",
    "records": [
        {
            "type": "A",
            "value": "8.8.8.8"
        }
    ]
}
```

---

# دسترسی به داده‌ها

```python
print(
    data["records"][0]["value"]
)
```

خروجی:

```text
8.8.8.8
```

---

<div align='right'>

# <span dir='rtl'>JSON در پروژه DNS Lookup</span>

</div>

در فایل:

```text
exporter.py
```

نتایج Lookup به JSON تبدیل می‌شوند.

ساختار خروجی:

```json
{
    "domain": "google.com",
    "record_type": "A",
    "records": [
        {
            "domain": "google.com",
            "record_type": "A",
            "value": "8.8.8.8"
        }
    ]
}
```

---

# مزایای JSON

## قابل خواندن برای انسان

```json
{
    "name": "Ali"
}
```

---

## پشتیبانی گسترده

تقریباً تمام زبان‌های برنامه‌نویسی از JSON پشتیبانی می‌کنند.

---

## مناسب برای API

اکثر API های مدرن از JSON استفاده می‌کنند.

---

## مناسب برای ذخیره‌سازی

فایل‌های تنظیمات و گزارش‌ها معمولاً با JSON ذخیره می‌شوند.

---

# مدیریت خطاها

ممکن است JSON معتبر نباشد.

مثال:

```python
import json

try:
    json.loads("{")
except json.JSONDecodeError:
    print("Invalid JSON")
```

خروجی:

```text
Invalid JSON
```

---

# اشتباهات رایج

## استفاده از کوتیشن تکی

نامعتبر:

```json
{
    'name': 'Ali'
}
```

---

معتبر:

```json
{
    "name": "Ali"
}
```

---

## قرار دادن کامای اضافی

نامعتبر:

```json
{
    "name": "Ali",
}
```

---

معتبر:

```json
{
    "name": "Ali"
}
```

---

<div align='right'>

# <span dir='rtl'>JSON و امنیت</span>

</div>

هنگام پردازش JSON از منابع خارجی:

<p dir='rtl'>
• اعتبارسنجی داده‌ها را انجام دهید. <br>
• به نوع داده‌ها اعتماد نکنید. <br>
• خطاهای Parsing را مدیریت کنید. <br>
• داده‌های دریافتی را بررسی کنید.
</p>

---

# جمع‌بندی

در این درس یاد گرفتیم:

<div align='right'>

<span dir='rtl'>• JSON چیست</span> <br>
<span dir='rtl'>• ارتباط JSON و Python</span> <br>
<span dir='rtl'>• ماژول `json`</span> <br>
<span dir='rtl'>• متد <span dir='ltr'>`dumps()`</span></span> <br>
<span dir='rtl'>• متد <span dir='ltr'>`loads()`</span></span> <br>
<span dir='rtl'>• متد <span dir='ltr'>`dump()`</span></span> <br>
<span dir='rtl'>• متد <span dir='ltr'>`load()`</span></span> <br>
<span dir='rtl'>• ذخیره JSON در فایل</span> <br>
<span dir='rtl'>• خواندن JSON از فایل</span> <br>
<span dir='rtl'>• JSON های تو در تو</span> <br>
<span dir='rtl'>• مدیریت خطاها</span> <br>
<span dir='rtl'>• کاربرد JSON در پروژه DNS Lookup</span>

</div>

<p dir='rtl'>
JSON یکی از مهم‌ترین مهارت‌های توسعه نرم‌افزار مدرن است و تقریباً در تمام پروژه‌های شبکه، امنیت، اتوماسیون و API ها مورد استفاده قرار می‌گیرد.
</p>
