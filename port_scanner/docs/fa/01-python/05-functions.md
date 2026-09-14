<div dir="rtl">

# جلسه ۵: توابع (Functions)

# چرا به توابع نیاز داریم؟

فرض کن قرار است یک پورت اسکنر بنویسیم.

اگر بخواهیم هر بار برای اسکن کردن یک پورت، تمام کدها را دوباره بنویسیم، برنامه خیلی بزرگ و غیرقابل مدیریت می‌شود.

به همین دلیل از **توابع (Functions)** استفاده می‌کنیم.

تابع یعنی:

> یک قطعه کد که یک کار مشخص را انجام می‌دهد و هر زمان بخواهیم می‌توانیم آن را صدا بزنیم.

---

# اولین تابع

```python
def say_hello():
    print("Hello")
```

---

# معنی کد

```python
def
```

کلمه کلیدی ساخت تابع است.

---

```python
say_hello
```

نام تابع است.

---

```python
()
```

محل قرار گرفتن ورودی‌های تابع است.

---

```python
:
```

شروع بدنه تابع را مشخص می‌کند.

---

```python
print("Hello")
```

کدی که هنگام اجرای تابع اجرا خواهد شد.

---

# اجرای تابع

```python
def say_hello():
    print("Hello")

say_hello()
```

خروجی:

```text
Hello
```

---

# اگر تابع را صدا نزنیم چه می‌شود؟

```python
def say_hello():
    print("Hello")
```

هیچ خروجی تولید نمی‌شود.

چون تابع فقط تعریف شده است.

اجرا نشده است.

---

# ورودی (Parameter)

اغلب لازم است تابع اطلاعاتی دریافت کند.

مثال:

```python
def greet(name):
    print(f"Hello {name}")
```

---

استفاده:

```python
greet("Ali")
greet("Sara")
```

خروجی:

```text
Hello Ali
Hello Sara
```

---

# چند ورودی

```python
def add(a, b):
    print(a + b)
```

---

استفاده:

```python
add(5, 10)
```

خروجی:

```text
15
```

---

# بازگرداندن مقدار

بسیاری از افراد تازه‌کار فکر می‌کنند print و return یکی هستند.

اما کاملاً متفاوت‌اند.

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
print
</p>

فقط نمایش می‌دهد.

```python
def add(a, b):
    print(a + b)
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
return
</p>

مقدار را برمی‌گرداند.

```python
def add(a, b):
    return a + b
```

---

استفاده:

```python
result = add(5, 10)

print(result)
```

خروجی:

```text
15
```

---

# چرا return مهم است؟

در پروژه Port Scanner تقریباً همه جا از آن استفاده می‌کنیم.

مثال:

```python
def validate_ip(ip):
    return True
```

---

یا:

```python
def scan_port(ip, port):
    return True
```

---

یا:

```python
def detect_service(port):
    return "http"
```

---

تمام این توابع باید نتیجه را برگردانند.

---

# مقدار پیش‌فرض

```python
def greet(name="Guest"):
    print(f"Hello {name}")
```

---

استفاده:

```python
greet()
```

خروجی:

```text
Hello Guest
```

---

و:

```python
greet("Ali")
```

خروجی:

```text
Hello Ali
```

---

# توابع کوچک بهترند

اشتباه:

```python
def scanner():
    # 200 خط کد
```

---

درست:

```python
def validate_ip():
    pass

def scan_port():
    pass

def detect_service():
    pass

def export_json():
    pass
```

---

دقیقاً به همین دلیل پروژه ما فایل‌های جداگانه دارد.

---

# مثال واقعی از پورت اسکنر

```python
def is_open(port):
    if port == 80:
        return True

    return False
```

---

استفاده:

```python
if is_open(80):
    print("Port is open")
```

خروجی:

```text
Port is open
```

---

# چیزی که امروز یاد گرفتیم

<p dir='rtl'>
✓ ساخت تابع با def <br>
✓ صدا زدن تابع <br>
✓ ورودی گرفتن <br>
✓ چند ورودی <br>
✓ return <br>
✓ تفاوت return و print <br>
✓ مقدار پیش‌فرض <br>
✓ طراحی ماژولار <br>
✓ کاربرد توابع در Port Scanner
</p>

---

# تمرین

تابعی بنویس که:

<p dir='rtl'>
1. یک شماره پورت دریافت کند. <br>
2. اگر پورت 80 بود عبارت HTTP را برگرداند. <br>
3. اگر پورت 443 بود عبارت HTTPS را برگرداند. <br>
4. در غیر این صورت Unknown را برگرداند.
</p>

نمونه:

```python
print(detect_service(80))
```

خروجی:

```text
HTTP
```

---

جلسه بعد:

<p align='right' dir='ltr' style='font-size:32px; font-wight:bold;'>
06-modules-and-imports.md
</p>

در جلسه بعد یاد می‌گیریم چگونه پروژه‌های بزرگ را به چند فایل تقسیم کنیم؛ دقیقاً همان کاری که در Port Scanner انجام داده‌ایم.

</div>