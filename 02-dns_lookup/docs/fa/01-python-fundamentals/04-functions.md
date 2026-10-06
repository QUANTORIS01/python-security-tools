# درس ۴: توابع (Functions) در پایتون

## مقدمه

اگر بخواهیم یک برنامه حرفه‌ای، قابل نگهداری و قابل تست بنویسیم، نمی‌توانیم تمام کدها را پشت سر هم در یک فایل قرار دهیم.

به جای آن، کد را به بخش‌های کوچک‌تر تقسیم می‌کنیم که هر بخش یک وظیفه مشخص دارد.

این بخش‌های کوچک در پایتون **تابع (Function)** نام دارند.

در واقع تقریباً تمام پروژه DNS Lookup بر پایه توابع ساخته شده است.

برای مثال:

```python
validate_domain()
```

```python
validate_record_type()
```

```python
lookup_record()
```

```python
build_dns_results()
```

```python
format_dns_results()
```

همگی تابع هستند.

---

# تابع چیست؟

تابع مجموعه‌ای از دستورات است که برای انجام یک کار مشخص نوشته می‌شود.

مثال:

```python
def greet():
    print("Hello")
```

اجرای تابع:

```python
greet()
```

خروجی:

```text
Hello
```

---

# ساختار تابع

یک تابع معمولاً از بخش‌های زیر تشکیل می‌شود:

```python
def function_name():
    pass
```

اجزای آن:

```python
def
```

کلمه کلیدی تعریف تابع

```python
function_name
```

نام تابع

```python
()
```

پارامترها

```python
:
```

شروع بدنه تابع

---

# پارامترها (Parameters)

تابع می‌تواند ورودی دریافت کند.

مثال:

```python
def greet(name):
    print(f"Hello {name}")
```

استفاده:

```python
greet("Ali")
```

خروجی:

```text
Hello Ali
```

---

# چند پارامتر

مثال:

```python
def add(a, b):
    print(a + b)
```

استفاده:

```python
add(10, 20)
```

خروجی:

```text
30
```

---

# مقدار بازگشتی (Return Value)

اکثر توابع فقط چیزی چاپ نمی‌کنند.

بلکه نتیجه را برمی‌گردانند.

مثال:

```python
def add(a, b):
    return a + b
```

استفاده:

```python
result = add(10, 20)
print(result)
```

خروجی:

```text
30
```

---

# تفاوت print و return

اشتباه رایج:

```python
def add(a, b):
    print(a + b)
```

در این حالت:

```python
result = add(10, 20)
```

مقدار:

```python
result
```

برابر خواهد بود با:

```python
None
```

زیرا تابع چیزی باز نگردانده است.

---

<div align='right'>

# Type Hint

</div>

در پروژه از Type Hint استفاده کرده‌ایم.

مثال:

```python
def add(a: int, b: int) -> int:
    return a + b
```

معنی:

<p dir='rtl'>
• a عدد صحیح است. <br>
• b عدد صحیح است. <br>
• خروجی عدد صحیح است.
</p>

---

# مثال از پروژه

در فایل:

```python
validator.py
```

داریم:

```python
def validate_timeout(
    timeout: float
) -> bool:
    return timeout > 0
```

معنی:

ورودی:

```python
float
```

خروجی:

```python
bool
```

---

# چند مقدار بازگشتی

پایتون می‌تواند چند مقدار را همزمان برگرداند.

مثال:

```python
def get_user():
    return "Ali", 25
```

استفاده:

```python
name, age = get_user()
```

---

# توابع بدون پارامتر

مثال:

```python
def show_banner():
    print("DNS Lookup")
```

استفاده:

```python
show_banner()
```

---

# توابع با مقدار پیش‌فرض

مثال:

```python
def greet(name="User"):
    print(f"Hello {name}")
```

استفاده:

```python
greet()
```

خروجی:

```text
Hello User
```

---

<div align='right'>

# <span dir='rtl'>Scope یا محدوده متغیرها</span>

</div>

متغیر داخل تابع فقط داخل همان تابع قابل دسترسی است.

مثال:

```python
def test():
    name = "Ali"
```

این کد خطا می‌دهد:

```python
print(name)
```

زیرا متغیر خارج از تابع وجود ندارد.

---

<div align='right'>

# Docstring

</div>

در پروژه برای تمام توابع از Docstring استفاده کرده‌ایم.

مثال:

```python
def lookup_record(
    domain: str,
    record_type: str,
) -> list[str]:
    """
    Lookup DNS records.
    """
```

مزایا:

<p dir='rtl'>
• مستندسازی بهتر <br>
• خوانایی بیشتر <br>
• تولید خودکار Documentation
</p>

---

# ارتباط مستقیم با validator.py

تابع:

```python
def validate_domain(
    domain: str
) -> bool:
```

وظیفه:

<p dir='rtl'>
• دریافت دامنه <br>
• بررسی اعتبار <br>
• بازگرداندن True یا False
</p>

---

# ارتباط مستقیم با resolver.py

تابع:

```python
def lookup_record(
    domain: str,
    record_type: str,
) -> list[str]:
```

وظیفه:

<p dir='rtl'>
• ارسال درخواست DNS <br>
• دریافت پاسخ <br>
• تبدیل پاسخ به لیست رشته‌ها
</p>

---

# ارتباط مستقیم با results.py

تابع:

```python
def build_dns_results(
    domain: str,
    record_type: str,
) -> list[DNSRecord]:
```

وظیفه:

<p dir='rtl'>
• دریافت داده خام DNS <br>
• تبدیل آن به مدل DNSRecord
</p>

---

# ارتباط مستقیم با formatter.py

تابع:

```python
def format_dns_results(
    results: list[DNSRecord],
) -> str:
```

وظیفه:

<p dir='rtl'>
• دریافت نتایج <br>
• تولید خروجی قابل نمایش در ترمینال
</p>

---

# اصل مهم طراحی

هر تابع باید فقط یک مسئولیت مشخص داشته باشد.

مثال خوب:

```python
validate_domain()
```

فقط اعتبار دامنه را بررسی می‌کند.

مثال خوب:

```python
lookup_record()
```

فقط DNS Query انجام می‌دهد.

این همان اصل معروف:

```text
Single Responsibility Principle
```

است.

---

# چرا پروژه را تابع‌محور طراحی کردیم؟

مزایا:

<p dir='rtl'>
• تست‌نویسی آسان <br>
• خوانایی بیشتر <br>
• نگهداری ساده‌تر <br>
• توسعه راحت‌تر <br>
• کاهش خطاها
</p>

برای همین تقریباً هر فایل پروژه مجموعه‌ای از توابع کوچک و مستقل است.

---

# تمرین

۱. تابعی بنویسید که نام یک دامنه را دریافت کند و آن را چاپ کند.

۲. تابعی بنویسید که دو عدد را دریافت کرده و مجموع آن‌ها را بازگرداند.

۳. تابعی بنویسید که مقدار Timeout را دریافت کند و اگر بزرگ‌تر از صفر بود True برگرداند.

۴. برای یکی از توابع بالا Docstring بنویسید.

۵. برای یکی از توابع Type Hint اضافه کنید.

---

# خلاصه درس

در این درس یاد گرفتیم:

<p dir='rtl'>
• تعریف تابع <br>
• پارامترها <br>
• مقدار بازگشتی <br>
• تفاوت print و return <br>
• Type Hint <br>
• Scope <br>
• Docstring <br>
• Single Responsibility Principle
</p>

این مفاهیم پایه اصلی معماری پروژه DNS Lookup هستند و تقریباً تمام فایل‌های پروژه بر اساس آن‌ها ساخته شده‌اند.

در درس بعدی با Module ها و Import ها آشنا می‌شویم؛ مفهومی که توضیح می‌دهد چرا پروژه را به چندین فایل مختلف تقسیم کرده‌ایم.
