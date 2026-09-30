<div dir="rtl">

# جلسه ۰۴ - شرط‌ها و حلقه‌ها

# مقدمه

فرض کنید یک پورت را اسکن کرده‌ایم.

اگر پورت باز بود:

```text
OPEN
```

نمایش دهیم.

و اگر بسته بود:

```text
CLOSED
```

نمایش دهیم.

یا فرض کنید بخواهیم پورت‌های ۱ تا ۱۰۰۰ را یکی یکی بررسی کنیم.

برای انجام چنین کارهایی به دو مفهوم بسیار مهم نیاز داریم:

<p dir='rtl'>
• شرط‌ها (Conditions) <br>
• حلقه‌ها (Loops)
</p>

تقریباً تمام برنامه‌های واقعی از این دو مفهوم استفاده می‌کنند.

---

# شرط چیست؟

شرط به برنامه اجازه می‌دهد تصمیم بگیرد.

مثال:

```python
port_is_open = True

if port_is_open:
    print("Port is open")
```

خروجی:

```text
Port is open
```

---

در زبان ساده:

```text
اگر این شرط برقرار بود،
این کد را اجرا کن.
```

---

# ساختار if

شکل کلی:

```python
if condition:
    code
```

مثال:

```python
port = 80

if port == 80:
    print("HTTP Port")
```

خروجی:

```text
HTTP Port
```

---

# عملگر ==

خیلی از افراد مبتدی این قسمت را اشتباه می‌گیرند.

این:

```python
=
```

برای ذخیره مقدار است.

مثال:

```python
port = 80
```

اما این:

```python
==
```

برای مقایسه است.

مثال:

```python
port == 80
```

یعنی:

```text
آیا مقدار port برابر 80 است؟
```

---

# استفاده از else

گاهی می‌خواهیم اگر شرط برقرار نبود کار دیگری انجام شود.

مثال:

```python
port = 443

if port == 80:
    print("HTTP")
else:
    print("Not HTTP")
```

خروجی:

```text
Not HTTP
```

---

# استفاده از elif

گاهی بیش از دو حالت داریم.

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

# عملگرهای مقایسه

برابر:

```python
==
```

---

نامساوی:

```python
!=
```

مثال:

```python
port != 80
```

---

بزرگ‌تر:

```python
>
```

---

کوچک‌تر:

```python
<
```

---

بزرگ‌تر یا مساوی:

```python
>=
```

---

کوچک‌تر یا مساوی:

```python
<=
```

---

# مثال واقعی

بررسی شماره پورت:

```python
port = 8080

if port > 1024:
    print("User Port")
```

---

# حلقه چیست؟

گاهی لازم است یک کار را بارها تکرار کنیم.

فرض کنید بخواهیم:

```text
Scanning Port 1
Scanning Port 2
Scanning Port 3
...
Scanning Port 1000
```

را نمایش دهیم.

نوشتن هزار خط کد منطقی نیست.

برای همین از حلقه استفاده می‌کنیم.

---

# حلقه for

مثال:

```python
for port in range(1, 6):
    print(port)
```

خروجی:

```text
1
2
3
4
5
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
range چیست؟
</p>

تابع:

```python
range()
```

دنباله‌ای از اعداد تولید می‌کند.

مثال:

```python
range(1, 6)
```

اعداد:

```text
1
2
3
4
5
```

را تولید می‌کند.

توجه کنید:

```text
عدد آخر شامل نمی‌شود.
```

---

# مثال واقعی Port Scanner

فرض کنید بخواهیم پورت‌های ۱ تا ۱۰ را بررسی کنیم:

```python
for port in range(1, 11):
    print(f"Scanning Port {port}")
```

خروجی:

```text
Scanning Port 1
Scanning Port 2
Scanning Port 3
...
Scanning Port 10
```

---

# استفاده از if داخل for

این دقیقاً شبیه چیزی است که در پورت اسکنر اتفاق می‌افتد.

مثال:

```python
for port in range(1, 6):

    if port == 3:
        print("Open")

    else:
        print("Closed")
```

خروجی:

```text
Closed
Closed
Open
Closed
Closed
```

---

# حلقه while

نوع دیگری از حلقه:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

خروجی:

```text
1
2
3
4
5
```

---

# چرا در Port Scanner بیشتر از for استفاده می‌کنیم؟

زیرا معمولاً بازه مشخصی از پورت‌ها داریم:

```python
1 - 1000
```

یا:

```python
1 - 65535
```

برای همین:

```python
for port in range(...)
```

بسیار مناسب‌تر است.

---

# مثال نزدیک به پروژه واقعی

کدی شبیه آنچه در اسکنر انجام می‌دهیم:

```python
open_ports = [80, 443]

for port in range(1, 6):

    if port in open_ports:
        print(f"{port} OPEN")

    else:
        print(f"{port} CLOSED")
```

خروجی:

```text
1 CLOSED
2 CLOSED
3 CLOSED
4 CLOSED
5 CLOSED
```

اگر پورت ۸۰ در بازه بود:

```text
80 OPEN
```

نمایش داده می‌شد.

---

# ارتباط این درس با پروژه

در پروژه Port Scanner:

از شرط‌ها استفاده می‌کنیم برای:

<p dir='rtl'>
• تشخیص باز بودن پورت <br>
• تشخیص بسته بودن پورت <br>
• تشخیص سرویس‌ها <br>
• بررسی خطاها
</p>

---

از حلقه‌ها استفاده می‌کنیم برای:

<p dir='rtl'>
• پیمایش پورت‌ها <br>
• پردازش نتایج <br>
• ساخت خروجی‌ها <br>
• نمایش اطلاعات
</p>

---

# خلاصه

✅ شرط‌ها باعث تصمیم‌گیری برنامه می‌شوند.

✅ از `if` برای بررسی شرط استفاده می‌کنیم.

✅ از `else` برای حالت جایگزین استفاده می‌کنیم.

✅ از `elif` برای چندین شرط استفاده می‌کنیم.

✅ حلقه‌ها برای تکرار عملیات هستند.

✅ حلقه `for` پرکاربردترین حلقه در پروژه Port Scanner است.

---

# تمرین

برنامه‌ای بنویسید که:

<p dir='rtl'>
• پورت‌های ۱ تا ۱۰ را بررسی کند. <br>
• اگر شماره پورت زوج بود:
</p>

```text
Even Port
```

نمایش دهد.

<p dir='rtl'>
• اگر فرد بود:
</p>

```text
Odd Port
```

نمایش دهد.

</div>