<div align='right'>

# <span dir='rtl'>Exception Handling در پایتون</span>

## <span dir='rtl'>Exception چیست؟</span>

</div>

در زمان اجرای برنامه ممکن است خطاهایی رخ دهند که قابل پیش‌بینی هستند.

برای مثال:

<p dir='rtl'>
• فایل مورد نظر وجود نداشته باشد. <br>
• اتصال شبکه برقرار نشود. <br>
• کاربر مقدار نامعتبر وارد کند. <br>
• درخواست DNS با شکست مواجه شود.
</p>

به این نوع خطاهای زمان اجرا (Runtime Errors) در پایتون **Exception** گفته می‌شود.

---

## مشکل بدون Exception Handling

مثال:

```python
number = int(input("Enter a number: "))
print(number)
```

اگر کاربر بنویسد:

```text
abc
```

برنامه متوقف می‌شود:

```text
ValueError: invalid literal for int()
```

در این حالت برنامه کرش می‌کند و اجرای آن پایان می‌یابد.

---

## ساختار try / except

برای مدیریت خطاها از بلوک‌های `try` و `except` استفاده می‌کنیم.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number")
```

اگر ورودی معتبر باشد:

```text
10
```

خروجی:

```text
10
```

اگر ورودی نامعتبر باشد:

```text
abc
```

خروجی:

```text
Invalid number
```

برنامه بدون کرش کردن ادامه پیدا می‌کند.

---

## نحوه کار try

هر کدی که احتمال خطا دارد داخل بخش `try` قرار می‌گیرد.

```python
try:
    risky_operation()
```

اگر خطایی رخ ندهد:

```text
try
↓
ادامه برنامه
```

اگر خطا رخ دهد:

```text
try
↓
Exception
↓
except
↓
ادامه برنامه
```

---

## گرفتن نوع خاصی از خطا

مثال:

```python
try:
    value = int("abc")
except ValueError:
    print("Value Error")
```

خروجی:

```text
Value Error
```

فقط خطای `ValueError` گرفته می‌شود.

---

## چند except

می‌توان چند نوع خطا را جداگانه مدیریت کرد.

```python
try:
    number = int(input())
    result = 10 / number

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

ورودی:

```text
abc
```

خروجی:

```text
Invalid number
```

ورودی:

```text
0
```

خروجی:

```text
Cannot divide by zero
```

---

## گرفتن چند Exception در یک except

```python
try:
    operation()

except (ValueError, TypeError):
    print("Input error")
```

---

<div align='right'>

## <span dir='rtl'>Exception به صورت متغیر</span>

</div>

گاهی می‌خواهیم جزئیات خطا را ببینیم.

```python
try:
    value = int("abc")

except ValueError as error:
    print(error)
```

خروجی:

```text
invalid literal for int() with base 10: 'abc'
```

---

<div align='right'>

## <span dir='rtl'>except عمومی</span>

</div>

```python
try:
    operation()

except Exception as error:
    print(error)
```

این روش تقریباً تمام Exceptionهای معمول را می‌گیرد.

اما نباید همیشه از آن استفاده کرد.

بهتر است تا جای ممکن Exceptionهای مشخص را مدیریت کنیم.

---

## بلوک else

کد داخل `else` فقط زمانی اجرا می‌شود که هیچ خطایی رخ نداده باشد.

```python
try:
    number = int(input())

except ValueError:
    print("Invalid")

else:
    print("Valid number")
```

---

## بلوک finally

کد داخل `finally` همیشه اجرا می‌شود.

فرقی نمی‌کند Exception رخ داده باشد یا نه.

```python
try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found")

finally:
    print("Finished")
```

---

## مثال کاربردی فایل

```python
try:
    file = open("data.txt")

except FileNotFoundError:
    print("Missing file")

finally:
    print("Cleanup")
```

خروجی:

```text
Missing file
Cleanup
```

---

<div align='right'>

## Exception Raising

</div>

گاهی خودمان عمداً Exception ایجاد می‌کنیم.

```python
raise ValueError("Invalid input")
```

خروجی:

```text
ValueError: Invalid input
```

---

## مثال عملی

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

---

## ارتباط با پروژه DNS Lookup

در فایل `resolver.py` دقیقاً از Exception Handling استفاده کردیم.

نمونه:

```python
try:
    answers = dns.resolver.resolve(
        domain,
        record_type,
    )

except dns.resolver.NXDOMAIN:
    return []
```

---

## خطاهای مهمی که در پروژه مدیریت کردیم

<div align='right'>

### NXDOMAIN

</div>

دامنه وجود ندارد.

```python
dns.resolver.NXDOMAIN
```

مثال:

```text
does-not-exist-example.com
```

---

<div align='right'>

### NoAnswer

</div>

دامنه وجود دارد اما رکورد مورد نظر ندارد.

```python
dns.resolver.NoAnswer
```

مثال:

```text
google.com CNAME
```

---

<div align='right'>

### NoNameservers

</div>

سرور DNS پاسخ مناسبی ارائه نکرده است.

```python
dns.resolver.NoNameservers
```

---

<div align='right'>

### LifetimeTimeout

</div>

درخواست DNS به موقع پاسخ نگرفته است.

```python
dns.resolver.LifetimeTimeout
```

---

## نسخه نهایی پروژه

```python
try:
    answers = dns.resolver.resolve(
        domain,
        record_type,
    )

    return [str(answer) for answer in answers]

except (
    dns.resolver.NXDOMAIN,
    dns.resolver.NoAnswer,
    dns.resolver.NoNameservers,
    dns.resolver.LifetimeTimeout,
):
    return []
```

به جای کرش کردن برنامه:

```text
Traceback ...
```

کاربر نتیجه‌ای تمیز و قابل مدیریت دریافت می‌کند.

---

## بهترین روش‌ها (Best Practices)

<div align='right'>

<span dir='rtl'>✅ Exceptionهای مشخص را بگیرید.</span>

✅ پیام خطای مناسب به کاربر نمایش دهید.

✅ از `finally` برای آزادسازی منابع استفاده کنید.

✅ از `raise` برای اعتبارسنجی استفاده کنید.

❌ همه خطاها را بی‌دلیل با `except Exception` مخفی نکنید.

❌ خطاها را بدون لاگ یا پیام مناسب نادیده نگیرید.

</div>

---

## جمع‌بندی

در این درس یاد گرفتیم:

<div align='right'>

<span dir='rtl'>• Exception چیست.</span> <br>
<span dir='rtl'>• چرا برنامه‌ها کرش می‌کنند.</span> <br>
<span dir='rtl'>• نحوه استفاده از `try` و `except`.</span> <br>
<span dir='rtl'>• استفاده از `else` و `finally`.</span> <br>
<span dir='rtl'>• ساخت Exception با `raise`.</span> <br>
<span dir='rtl'>• مدیریت خطاهای DNS در پروژه DNS Lookup.</span> <br>
<span dir='rtl'>• اصول حرفه‌ای مدیریت خطا در برنامه‌های واقعی.</span>

</div>

<p dir='rtl'>
Exception Handling یکی از مهم‌ترین ابزارهای ساخت نرم‌افزارهای پایدار و حرفه‌ای است و تقریباً در تمام پروژه‌های واقعی پایتون از آن استفاده می‌شود.
</p>
