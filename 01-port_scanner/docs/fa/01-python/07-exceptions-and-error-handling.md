<div dir="rtl">

# جلسه ۶: مدیریت خطاها (Exceptions & Error Handling)

# چرا مدیریت خطا مهم است؟

هیچ برنامه‌ای در دنیا وجود ندارد که همیشه بدون خطا اجرا شود.

ممکن است:

<p dir='rtl'>
• کاربر ورودی اشتباه وارد کند. <br>
• فایل وجود نداشته باشد. <br>
• اینترنت قطع شود. <br>
• سرور پاسخ ندهد. <br>
• پورت موردنظر بسته باشد.
</p>

اگر خطاها را مدیریت نکنیم:

برنامه ناگهان متوقف می‌شود.

---

# یک خطای ساده

```python
number = int("hello")
```

خروجی:

```text
ValueError:
invalid literal for int()
```

برنامه متوقف می‌شود.

---

# راه حل: try و except

```python
try:
    number = int("hello")
except ValueError:
    print("Invalid number")
```

خروجی:

```text
Invalid number
```

برنامه متوقف نمی‌شود.

---

# معنی try

```python
try:
```

یعنی:

> این کد را اجرا کن.

---

# معنی except

```python
except:
```

یعنی:

> اگر خطایی رخ داد این قسمت را اجرا کن.

---

# مثال واقعی

```python
try:
    age = int(input("Age: "))
except:
    print("Please enter a number")
```

---

اگر کاربر بنویسد:

```text
abc
```

خروجی:

```text
Please enter a number
```

---

# گرفتن نوع خاصی از خطا

بهتر است نوع خطا را مشخص کنیم.

---

اشتباه:

```python
except:
```

---

بهتر:

```python
except ValueError:
```

---

مثال:

```python
try:
    age = int("hello")
except ValueError:
    print("Wrong value")
```

---

# چند نوع خطا

```python
try:
    ...
except ValueError:
    ...
except TypeError:
    ...
except FileNotFoundError:
    ...
```

---

هر خطا به بخش مخصوص خودش می‌رود.

---

# ذخیره خطا در متغیر

```python
try:
    age = int("hello")
except ValueError as error:
    print(error)
```

خروجی:

```text
invalid literal for int()
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
finally
</p>

بعضی کدها باید همیشه اجرا شوند.

حتی اگر خطا رخ دهد.

---

مثال:

```python
try:
    print("Start")
except:
    print("Error")
finally:
    print("Finished")
```

---

خروجی:

```text
Start
Finished
```

---

# مثال دیگر

```python
try:
    int("abc")
except:
    print("Error")
finally:
    print("Finished")
```

خروجی:

```text
Error
Finished
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
finally در دنیای واقعی
</p>

معمولاً برای:

<p dir='rtl'>
• بستن فایل <br>
• بستن اتصال شبکه <br>
• آزادسازی منابع
</p>

استفاده می‌شود.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
raise چیست؟
</p>

گاهی خودمان می‌خواهیم خطا ایجاد کنیم.

---

مثال:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

خروجی:

```text
ValueError:
Age cannot be negative
```

---

# مثال واقعی

```python
def validate_port(port):
    if port < 1 or port > 65535:
        raise ValueError("Invalid port")
```

---

این دقیقاً شبیه اعتبارسنجی‌هایی است که در Port Scanner انجام داده‌ایم.

---

# خطاهای معروف پایتون

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
ValueError
</p>

مقدار اشتباه

```python
int("abc")
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
TypeError
</p>

نوع داده اشتباه

```python
"5" + 5
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
FileNotFoundError
</p>

فایل وجود ندارد

```python
open("test.txt")
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
ZeroDivisionError
</p>

تقسیم بر صفر

```python
10 / 0
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
IndexError
</p>

اندیس نامعتبر

```python
items = [1, 2]

print(items[10])
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
KeyError
</p>

کلید وجود ندارد

```python
data = {}

print(data["name"])
```

---

# کاربرد در Port Scanner

یکی از مهم‌ترین بخش‌های پروژه ما:

---

اتصال به پورت

```python
socket.connect()
```

---

ممکن است:

<p dir='rtl'>
• Timeout رخ دهد. <br>
• سرور پاسخ ندهد. <br>
• پورت بسته باشد.
</p>

---

برای همین از ساختارهای مدیریت خطا استفاده می‌کنیم.

---

نمونه ساده:

```python
try:
    socket.connect(...)
except OSError:
    return False
```

---

اگر این مدیریت وجود نداشته باشد:

اولین پورت بسته کل برنامه را متوقف می‌کند.

---

# مثال واقعی‌تر

```python
def scan_port(ip, port):
    try:
        ...
        return True
    except OSError:
        return False
```

---

همین ایده در اکثر ابزارهای امنیتی دنیا وجود دارد.

---

# یک اشتباه رایج

اشتباه:

```python
try:
    ...
except:
    pass
```

---

این کار خطا را مخفی می‌کند.

بعداً پیدا کردن مشکل بسیار سخت می‌شود.

---

بهتر:

```python
except OSError as error:
    print(error)
```

یا:

```python
logger.error(str(error))
```

---

# ارتباط با پروژه ما

در پروژه Port Scanner تاکنون:

<p dir='rtl'>
✓ ورودی‌ها را اعتبارسنجی کرده‌ایم <br>
✓ خطاهای شبکه را مدیریت کرده‌ایم <br>
✓ Timeout را کنترل کرده‌ایم <br>
✓ Banner Grabbing را ایمن کرده‌ایم
</p>

---

همه این‌ها بر پایه مدیریت خطا ساخته شده‌اند.

---

# چیزی که امروز یاد گرفتیم

<p dir='rtl'>
✓ Exception چیست <br>
✓ try <br>
✓ except <br>
✓ finally <br>
✓ raise <br>
✓ خطاهای رایج پایتون <br>
✓ مدیریت خطاهای شبکه <br>
✓ ارتباط مستقیم با Port Scanner
</p>

---

# تمرین

تابعی بنویس:

```python
def divide(a, b):
```

اگر کاربر عدد صفر وارد کرد:

```python
divide(10, 0)
```

به جای کرش کردن برنامه:

```text
Cannot divide by zero
```

نمایش داده شود.

---

جلسه بعد:

<p align='right' dir='ltr' style='font-size:32px; font-wight:bold'>
08-files-json-csv.md
</p>

در جلسه بعد یاد می‌گیریم چگونه فایل‌ها را بخوانیم و ذخیره کنیم؛ دقیقاً همان چیزی که برای خروجی‌های JSON و CSV در پروژه Port Scanner استفاده کرده‌ایم.

</div>