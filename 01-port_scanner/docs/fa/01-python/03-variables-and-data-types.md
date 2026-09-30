<div dir="rtl">

# جلسه ۰۳ - متغیرها و انواع داده

## مقدمه

فرض کنید می‌خواهیم یک آدرس IP را داخل برنامه ذخیره کنیم:

```python
127.0.0.1
```

یا یک شماره پورت:

```python
80
```

یا نام یک سرویس:

```python
http
```

کامپیوتر باید این اطلاعات را در جایی نگهداری کند تا بعداً بتوانیم از آن‌ها استفاده کنیم.

اینجاست که مفهوم **متغیر (Variable)** وارد می‌شود.

---

# متغیر چیست؟

متغیر محلی برای ذخیره اطلاعات در حافظه کامپیوتر است.

مثال:

```python
ip = "127.0.0.1"
```

در این مثال:

<p dir='rtl'>
• <mark style='background-color: #383838; color: #c3c1c1; padding:2px 4px'>ip</mark> نام متغیر است. <br>
• <mark style='background-color: #383838; color: #c3c1c1; padding:2px 4px'>=</mark> عملگر انتساب است. <br>
• <mark style='background-color: #383838; color: #c3c1c1; padding:2px 4px'>"127.0.0.1"</mark> مقداری است که ذخیره می‌شود.
</p>

---

## مثال واقعی

فرض کنید می‌خواهیم IP هدف را ذخیره کنیم:

```python
target_ip = "192.168.1.1"
```

بعداً می‌توانیم از آن استفاده کنیم:

```python
print(target_ip)
```

خروجی:

```text
192.168.1.1
```

---

# چرا به متغیر نیاز داریم؟

بدون متغیر باید همه چیز را بارها تکرار کنیم.

بد:

```python
print("192.168.1.1")
print("192.168.1.1")
print("192.168.1.1")
```

بهتر:

```python
ip = "192.168.1.1"

print(ip)
print(ip)
print(ip)
```

---

# قوانین نام‌گذاری متغیرها

نام متغیر باید:

✅ با حرف شروع شود

```python
ip = "127.0.0.1"
```

✅ می‌تواند شامل عدد باشد

```python
port80 = 80
```

✅ می‌تواند شامل `_` باشد

```python
target_ip = "127.0.0.1"
```

---

نمونه‌های اشتباه:

```python
1port = 80
```

```python
target-ip = "127.0.0.1"
```

```python
class = "python"
```

---

# انواع داده چیست؟

تمام اطلاعات یکسان نیستند.

عدد با متن فرق دارد.

متن با درست و غلط فرق دارد.

به همین دلیل پایتون انواع داده مختلفی دارد.

---

# رشته (String)

برای ذخیره متن استفاده می‌شود.

مثال:

```python
service = "http"
```

یا:

```python
banner = "Apache Server"
```

---

بررسی نوع داده:

```python
print(type(service))
```

خروجی:

```text
<class 'str'>
```

---

# عدد صحیح (Integer)

برای ذخیره اعداد بدون اعشار.

مثال:

```python
port = 80
```

```python
workers = 100
```

---

بررسی نوع داده:

```python
print(type(port))
```

خروجی:

```text
<class 'int'>
```

---

# عدد اعشاری (Float)

برای ذخیره اعداد اعشاری.

مثال:

```python
timeout = 0.5
```

---

بررسی نوع داده:

```python
print(type(timeout))
```

خروجی:

```text
<class 'float'>
```

---

# مقدار بولین (Boolean)

برای ذخیره درست یا غلط.

مقادیر:

```python
True
```

و

```python
False
```

مثال:

```python
is_open = True
```

---

در پروژه پورت اسکنر:

```python
is_port_open = True
```

یعنی:

```text
این پورت باز است.
```

---

بررسی نوع داده:

```python
print(type(is_open))
```

خروجی:

```text
<class 'bool'>
```

---

# تغییر مقدار متغیر

مقدار متغیر می‌تواند تغییر کند.

```python
port = 80
```

بعد:

```python
port = 443
```

اکنون مقدار متغیر:

```text
443
```

است.

---

# چاپ چند متغیر

```python
ip = "127.0.0.1"
port = 80

print(ip, port)
```

خروجی:

```text
127.0.0.1 80
```

---

# مثال واقعی از پروژه Port Scanner

نمونه‌ای شبیه چیزی که در پروژه استفاده می‌کنیم:

```python
target_ip = "127.0.0.1"
port = 80
service = "http"
timeout = 0.5
is_open = True
```

هر متغیر اطلاعات خاصی را نگهداری می‌کند.

---

# ارتباط این درس با پروژه

در پروژه Port Scanner دائماً با متغیرها سروکار داریم.

مثال:

```python
ip
```

برای IP هدف.

---

```python
port
```

برای شماره پورت.

---

```python
service
```

برای نام سرویس.

---

```python
timeout
```

برای زمان انتظار.

---

```python
banner
```

برای اطلاعات دریافتی از سرویس.

---

# خلاصه

✅ متغیر محلی برای ذخیره اطلاعات است.

✅ از `=` برای ذخیره مقدار استفاده می‌کنیم.

✅ مهم‌ترین انواع داده:

<p dir='rtl'>
• <mark style='background-color: #383838; color: #c3c1c1; padding:2px 4px;'>str</mark> <br>
• <mark style='background-color: #383838; color: #c3c1c1; padding:2px 4px;'>int</mark> <br>
• <mark style='background-color: #383838; color: #c3c1c1; padding:2px 4px;'>float</mark> <br>
• <mark style='background-color: #383838; color: #c3c1c1; padding:2px 4px;'>bool</mark>
</p>

✅ پروژه Port Scanner به شدت از متغیرها استفاده می‌کند.

---

# تمرین

متغیرهای زیر را ایجاد کنید:

```python
target_ip
port
service
timeout
```

سپس همه آن‌ها را با `print()` نمایش دهید.

</div>