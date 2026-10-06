# درس ۱۱: File Handling در Python

## مقدمه

بسیاری از برنامه‌ها فقط با داده‌های موجود در حافظه کار نمی‌کنند. در دنیای واقعی معمولاً لازم است اطلاعات را در فایل‌ها ذخیره کنیم یا از فایل‌ها بخوانیم.

برخی از کاربردهای رایج File Handling:

<p dir='rtl'>
• ذخیره گزارش‌ها (Logs) <br>
• ذخیره تنظیمات برنامه <br>
• خواندن فایل‌های متنی <br>
• تولید فایل‌های JSON <br>
• تولید فایل‌های CSV <br>
• ذخیره نتایج پردازش‌ها
</p>

در پروژه DNS Lookup نیز برای ذخیره لاگ‌ها و خروجی‌های JSON و CSV از File Handling استفاده کرده‌ایم.

---

# باز کردن فایل

تابع اصلی کار با فایل‌ها در پایتون:

```python
open()
```

مثال:

```python
file = open("data.txt")
```

---

# خواندن محتوای فایل

فرض کنید فایل `data.txt` شامل محتوای زیر باشد:

```text
Hello
World
Python
```

کد:

```python
file = open("data.txt")

content = file.read()

print(content)

file.close()
```

خروجی:

```text
Hello
World
Python
```

---

# بستن فایل

پس از اتمام کار باید فایل بسته شود:

```python
file.close()
```

اگر فایل بسته نشود ممکن است:

<p dir='rtl'>
• منابع سیستم آزاد نشوند <br>
• فایل قفل شود <br>
• داده‌ها به‌درستی ذخیره نشوند
</p>

---

# استفاده از with

روش استاندارد در پایتون:

```python
with open("data.txt") as file:
    content = file.read()

print(content)
```

مزیت:

<div align='right'>

```text
فایل به صورت خودکار بسته می‌شود.
```

</div>

---

# خواندن فایل به صورت خط‌به‌خط

```python
with open("data.txt") as file:
    for line in file:
        print(line)
```

---

# خواندن تمام خطوط

```python
with open("data.txt") as file:
    lines = file.readlines()

print(lines)
```

خروجی:

```python
[
    "Hello\n",
    "World\n",
    "Python\n"
]
```

---

# نوشتن در فایل

برای نوشتن از حالت `w` استفاده می‌کنیم:

```python
with open("output.txt", "w") as file:
    file.write("Hello")
```

---

# رفتار حالت w

اگر فایل وجود داشته باشد، محتوای قبلی حذف می‌شود.

فایل اولیه:

```text
Old Data
```

کد:

```python
with open("output.txt", "w") as file:
    file.write("New Data")
```

نتیجه:

```text
New Data
```

---

# اضافه کردن به فایل

برای اضافه کردن محتوا بدون حذف داده‌های قبلی از حالت `a` استفاده می‌شود.

```python
with open("log.txt", "a") as file:
    file.write("New Log\n")
```

---

# تفاوت w و a

حالت `w`

```text
Overwrite
```

حالت `a`

```text
Append
```

---

# نوشتن چند خط

```python
with open("notes.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
```

---

<div align='right'>

# Encoding

</div>

برای جلوگیری از مشکلات مربوط به کاراکترهای فارسی بهتر است همیشه Encoding را مشخص کنیم.

```python
with open(
    "data.txt",
    encoding="utf-8"
) as file:
    print(file.read())
```

---

# ذخیره متن فارسی

```python
with open(
    "data.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write("سلام دنیا")
```

---

# مدیریت خطاها

ممکن است فایل موردنظر وجود نداشته باشد.

```python
try:
    with open("missing.txt") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")
```

---

# مسیر فایل‌ها

مسیر نسبی:

```python
open("data.txt")
```

مسیر کامل:

```python
open("C:/Projects/data.txt")
```

---

# بررسی وجود فایل

کتابخانه `pathlib` روش مدرن کار با مسیرها را فراهم می‌کند.

```python
from pathlib import Path

path = Path("data.txt")

print(path.exists())
```

خروجی:

```python
True
```

یا:

```python
False
```

---

<div align='right'>

# <span dir='rtl'>File Handling در پروژه DNS Lookup</span>

</div>

در پروژه DNS Lookup از File Handling در چند بخش استفاده شده است.

<div align='right'>

## Logger

</div>

فایل:

```text
dns.log
```

برای ذخیره رخدادهای برنامه.

---

<div align='right'>

## JSON Export

</div>

فایل:

```text
results.json
```

برای ذخیره خروجی ساختاریافته.

---

<div align='right'>

## CSV Export

</div>

فایل:

```text
results.csv
```

برای ذخیره نتایج در قالب CSV.

---

# مثال واقعی از پروژه

```python
with open(
    filename,
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

# اشتباهات رایج

## فراموش کردن close

نامناسب:

```python
file = open("data.txt")
```

مناسب:

```python
with open("data.txt") as file:
    ...
```

---

## استفاده اشتباه از w

نامناسب:

```python
open("log.txt", "w")
```

ممکن است کل فایل لاگ را حذف کند.

---

## مشخص نکردن Encoding

نامناسب:

```python
open("data.txt")
```

مناسب:

```python
open(
    "data.txt",
    encoding="utf-8"
)
```

---

# جمع‌بندی

در این درس یاد گرفتیم:

<div align='right'>

<span dir='rtl'>• تابع <span dir='ltr'>`open()`</span></span> <br>
<span dir='rtl'>• متد <span dir='ltr'>`read()`</span></span> <br>
<span dir='rtl'>• متد <span dir='ltr'>`readlines()`</span></span> <br>
<span dir='rtl'>• متد <span dir='ltr'>`write()`</span></span> <br>
<span dir='rtl'>• حالت‌های `r`، `w` و `a`</span> <br>
<span dir='rtl'>• استفاده از `with`</span> <br>
<span dir='rtl'>• مدیریت Encoding</span> <br>
<span dir='rtl'>• مدیریت خطاهای فایل</span> <br>
<span dir='rtl'>• استفاده از `pathlib`</span> <br>
<span dir='rtl'>• کاربرد File Handling در پروژه DNS Lookup</span>

</div>

<p dir='rtl'>
File Handling یکی از مهارت‌های پایه‌ای برای توسعه ابزارهای واقعی است و در تقریباً تمام پروژه‌های عملی از آن استفاده می‌شود.
</p>
