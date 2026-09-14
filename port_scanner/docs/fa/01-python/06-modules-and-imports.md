<div dir="rtl">

# جلسه ۶: ماژول‌ها و Import

# چرا به ماژول نیاز داریم؟

فرض کن کل پروژه Port Scanner را داخل یک فایل بنویسیم.

```python
scanner.py
```

و این فایل کم‌کم به 1000 خط برسد.

آن وقت:

<p dir='rtl'>
• پیدا کردن باگ سخت می‌شود. <br>
• توسعه پروژه سخت می‌شود. <br>
• تست‌نویسی سخت می‌شود. <br>
• نگهداری پروژه سخت می‌شود.
</p>

برای همین برنامه‌نویسان پروژه را به چند فایل تقسیم می‌کنند.

به هر فایل پایتون:

> ماژول (Module)

گفته می‌شود.

---

# اولین ماژول

فایل اول:

```python
math_tools.py
```

```python
def add(a, b):
    return a + b
```

---

فایل دوم:

```python
main.py
```

```python
from math_tools import add

result = add(10, 20)

print(result)
```

خروجی:

```text
30
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
import چیست؟
</p>

کلمه import یعنی:

> کدهای فایل دیگری را وارد این فایل کن.

---

مثال:

```python
import math
```

اکنون می‌توانیم از امکانات ماژول math استفاده کنیم.

---

مثال:

```python
import math

print(math.sqrt(25))
```

خروجی:

```text
5.0
```

---

# استفاده از from

روش اول:

```python
import math

print(math.sqrt(25))
```

---

روش دوم:

```python
from math import sqrt

print(sqrt(25))
```

خروجی:

```text
5.0
```

---

# تفاوت این دو روش

روش اول:

```python
import math
```

باید نام ماژول را بنویسیم.

```python
math.sqrt()
```

---

روش دوم:

```python
from math import sqrt
```

مستقیماً تابع را صدا می‌زنیم.

```python
sqrt()
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Import چند تابع
</p>

```python
from math import sqrt, pow
```

---

استفاده:

```python
print(sqrt(16))
print(pow(2, 3))
```

خروجی:

```text
4.0
8.0
```

---

< dir='rtl' style='font-size:32px; font-wight:bold'>

<p dir='rtl' style='font-size:24px; font-wight:bold'>Import همه چیز
>
</p>

```python
from math import *
```

این کار ممکن است.

اما در پروژه‌های واقعی توصیه نمی‌شود.

چون مشخص نیست هر تابع از کجا آمده است.

---

# ساختار واقعی پروژه ما

پروژه Port Scanner:

```text
src/
│
├── scanner.py
├── validator.py
├── services.py
├── banner.py
├── results.py
├── formatter.py
├── exporter.py
├── csv_exporter.py
└── cli.py
```

---

هر فایل فقط مسئول یک کار است.

---

# مثال واقعی از پروژه

فایل:

```python
validator.py
```

```python
def validate_ip(ip):
    return True
```

---

فایل:

```python
cli.py
```

```python
from validator import validate_ip

validate_ip("127.0.0.1")
```

---

# مزیت بزرگ ماژول‌ها

اگر بخواهیم اعتبارسنجی IP را تغییر دهیم:

فقط فایل زیر را تغییر می‌دهیم:

```python
validator.py
```

بقیه پروژه دست نخورده باقی می‌ماند.

---

# ماژول‌های داخلی پایتون

پایتون صدها ماژول آماده دارد.

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
socket
</p>

برای شبکه

```python
import socket
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
json
</p>

برای فایل JSON

```python
import json
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
csv
</p>

برای فایل CSV

```python
import csv
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
time
</p>

برای زمان

```python
import time
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold'>
threading
</p>

برای چندریسمانی

```python
import threading
```

---

# مثال از socket

```python
import socket

print(socket.gethostname())
```

---

خروجی نمونه:

```text
DESKTOP-ABC123
```

---

# مفهوم Package

وقتی چند ماژول را داخل یک پوشه قرار می‌دهیم:

```text
src/
│
├── scanner.py
├── validator.py
├── services.py
└── __init__.py
```

به آن:

<p dir='rtl' style='background-color: #383838; color: #c3c1c1; padding:5px 10px 5px 0; border-left:4px solid #665d5d'>
Package
</p>

می‌گویند.

---

# فایل __init__.py چیست؟

وجود این فایل به پایتون می‌گوید:

> این پوشه یک Package است.

---

در پروژه ما:

```text
src/__init__.py
```

وجود دارد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold'>
Import در پروژه ما
</p>

نمونه واقعی:

```python
from src.scanner import scan_range
```

---

یا:

```python
from src.validator import validate_ip
```

---

یا:

```python
from src.results import build_scan_results
```

---

# یکی از مهم‌ترین مهارت‌های برنامه‌نویسی

برنامه‌نویس مبتدی:

```python
all_code.py
```

۵۰۰۰ خط کد در یک فایل.

---

برنامه‌نویس حرفه‌ای:

```text
project/
│
├── network.py
├── security.py
├── database.py
├── api.py
└── cli.py
```

هر فایل یک مسئولیت مشخص.

---

# چیزی که امروز یاد گرفتیم

<p dir='rtl'>
✓ مفهوم Module <br>
✓ مفهوم Import <br>
✓ import <br>
✓ <span dir='ltr' style='display:inlineblock'>from ... import ...</span> <br>
✓ ماژول‌های داخلی پایتون <br>
✓ Package <br>
✓ فایل <span dir='ltr' style='display:inlineblock'>__init__.py</span> <br>
✓ معماری واقعی پروژه Port Scanner <br>
✓ دلیل شکستن پروژه به فایل‌های متعدد
</p>

---

# تمرین

دو فایل بساز:

فایل اول:

```python
calculator.py
```

```python
def multiply(a, b):
    return a * b
```

---

فایل دوم:

```python
main.py
```

تابع multiply را import کن و حاصل ضرب 5 و 8 را چاپ کن.

خروجی:

```text
40
```

---

جلسه بعد:

<p align='right' dir='ltr' style='font-size:32px; font-wight:bold;'>
07-exceptions-and-error-handling.md
</p>

در جلسه بعد یاد می‌گیریم چگونه خطاهای برنامه را مدیریت کنیم؛ دقیقاً همان چیزی که در Port Scanner برای مدیریت خطاهای شبکه استفاده کرده‌ایم.

</div>