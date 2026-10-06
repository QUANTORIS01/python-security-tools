# درس ۲: شرط‌ها و تصمیم‌گیری در پایتون

## مقدمه

تقریباً هیچ برنامه واقعی‌ای وجود ندارد که بدون تصمیم‌گیری کار کند.

برنامه‌ها دائماً باید شرایط مختلف را بررسی کنند و بر اساس نتیجه تصمیم بگیرند.

برای مثال در پروژه DNS Lookup:

<p dir='rtl'>
• آیا دامنه معتبر است؟ <br>
• آیا نوع رکورد DNS معتبر است؟ <br>
• آیا کاربر ورودی صحیح وارد کرده است؟ <br>
• آیا نتیجه‌ای از DNS دریافت شده است؟
</p>

همه این تصمیم‌ها با استفاده از ساختارهای شرطی انجام می‌شوند.

---

# دستور if

ساده‌ترین ساختار تصمیم‌گیری در پایتون `if` است.

مثال:

```python
age = 20

if age >= 18:
    print("Adult")
```

خروجی:

```text
Adult
```

---

# نحوه کار if

ابتدا شرط بررسی می‌شود.

اگر نتیجه شرط برابر با:

```python
True
```

باشد، کد داخل بلوک اجرا می‌شود.

اگر نتیجه:

```python
False
```

باشد، کد اجرا نمی‌شود.

مثال:

```python
number = 5

if number > 10:
    print("Greater")
```

خروجی:

```text
(هیچ خروجی تولید نمی‌شود)
```

---

# تورفتگی (Indentation)

پایتون به جای آکولاد از تورفتگی استفاده می‌کند.

درست:

```python
if True:
    print("Hello")
```

غلط:

```python
if True:
print("Hello")
```

---

# عملگرهای مقایسه‌ای

شرط‌ها معمولاً با عملگرهای مقایسه‌ای ساخته می‌شوند.

برابر:

```python
==
```

نامساوی:

```python
!=
```

بزرگ‌تر:

```python
>
```

کوچک‌تر:

```python
<
```

بزرگ‌تر یا مساوی:

```python
>=
```

کوچک‌تر یا مساوی:

```python
<=
```

مثال:

```python
port = 53

if port == 53:
    print("DNS")
```

---

# دستور else

گاهی می‌خواهیم زمانی که شرط برقرار نیست، عمل دیگری انجام شود.

مثال:

```python
port = 80

if port == 53:
    print("DNS")
else:
    print("Other Service")
```

خروجی:

```text
Other Service
```

---

# دستور elif

برای بررسی چندین حالت مختلف استفاده می‌شود.

مثال:

```python
port = 443

if port == 80:
    print("HTTP")

elif port == 443:
    print("HTTPS")

else:
    print("Unknown")
```

خروجی:

```text
HTTPS
```

---

# عملگر and

برای زمانی که چند شرط باید همزمان برقرار باشند.

مثال:

```python
age = 25
verified = True

if age >= 18 and verified:
    print("Access Granted")
```

---

# عملگر or

اگر فقط یکی از شرط‌ها برقرار باشد.

مثال:

```python
is_admin = False
is_owner = True

if is_admin or is_owner:
    print("Access Granted")
```

---

# عملگر not

معکوس کردن نتیجه شرط.

مثال:

```python
is_valid = False

if not is_valid:
    print("Invalid")
```

خروجی:

```text
Invalid
```

---

# بررسی رشته‌ها

در پروژه DNS Lookup زیاد با رشته‌ها کار می‌کنیم.

مثال:

```python
record_type = "A"

if record_type == "A":
    print("IPv4 Record")
```

---

# عضویت در مجموعه‌ها

یکی از الگوهای مهمی که در پروژه استفاده کرده‌ایم:

```python
SUPPORTED_RECORD_TYPES = {
    "A",
    "AAAA",
    "MX",
    "NS",
    "TXT",
    "CNAME",
}
```

بررسی عضویت:

```python
if record_type in SUPPORTED_RECORD_TYPES:
    print("Valid")
```

---

# ارتباط مستقیم با پروژه

در فایل:

```python
validator.py
```

تابع زیر را داریم:

```python
def validate_record_type(record_type: str) -> bool:
    return record_type.upper() in SUPPORTED_RECORD_TYPES
```

منطق آن:

۱. ورودی را بزرگ می‌کند.

```python
record_type.upper()
```

۲. بررسی می‌کند که آیا در لیست رکوردهای مجاز وجود دارد یا نه.

```python
in SUPPORTED_RECORD_TYPES
```

۳. نتیجه را به صورت:

```python
True
```

یا

```python
False
```

برمی‌گرداند.

---

# شرط‌های تو در تو

گاهی یک شرط داخل شرط دیگر قرار می‌گیرد.

مثال:

```python
domain = "google.com"

if domain:
    if "." in domain:
        print("Looks Valid")
```

---

# مقدارهای Truthy و Falsy

در پایتون بعضی مقادیر به صورت خودکار معادل False هستند.

مثال:

```python
""
0
[]
{}
None
```

نمونه:

```python
records = []

if records:
    print("Found")
else:
    print("No Records")
```

خروجی:

```text
No Records
```

---

# کاربرد در DNS Lookup

در فایل formatter.py داریم:

```python
if not results:
    return "No DNS records found."
```

اگر لیست نتایج خالی باشد:

```python
[]
```

پیغام مناسب نمایش داده می‌شود.

---

# تمرین

۱. متغیری به نام `record_type` بسازید و مقدار `"MX"` را در آن قرار دهید.

۲. بررسی کنید آیا مقدار آن برابر `"A"` است یا خیر.

۳. بررسی کنید آیا مقدار آن در مجموعه زیر وجود دارد یا خیر:

```python
{
    "A",
    "AAAA",
    "MX",
}
```

۴. برنامه‌ای بنویسید که اگر لیست خالی بود عبارت:

```text
No Records
```

را چاپ کند.

---

# خلاصه درس

در این درس یاد گرفتیم:

<p dir='rtl'>
• if <br>
• else <br>
• elif <br>
• عملگرهای مقایسه‌ای <br>
• and <br>
• or <br>
• not <br>
• بررسی عضویت با in <br>
• Truthy و Falsy Values
</p>

این مفاهیم در بخش اعتبارسنجی ورودی‌ها و پردازش نتایج پروژه DNS Lookup به‌صورت گسترده استفاده می‌شوند.

در درس بعدی با حلقه‌ها (Loops) آشنا می‌شویم؛ مفهومی که برای پردازش مجموعه‌ای از رکوردهای DNS ضروری است.
