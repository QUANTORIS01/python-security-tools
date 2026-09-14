<div dir="rtl">

# جلسه ۸: کار با فایل‌ها، JSON و CSV

# چرا باید کار با فایل‌ها را یاد بگیریم؟

فرض کن پورت اسکنر را اجرا کرده‌ایم.

خروجی:

```text
53
135
445
```

نمایش داده شده است.

اما بعد از بستن برنامه:

همه اطلاعات از بین می‌رود.

---

راه حل چیست؟

ذخیره کردن اطلاعات در فایل.

---

# باز کردن فایل

برای باز کردن فایل از تابع:

```python
open()
```

استفاده می‌کنیم.

---

مثال:

```python
file = open("test.txt")
```

---

# خواندن فایل

فرض کن فایل:

```text
test.txt
```

دارای محتویات زیر باشد:

```text
Hello World
```

---

کد:

```python
file = open("test.txt")

content = file.read()

print(content)
```

خروجی:

```text
Hello World
```

---

# بستن فایل

بعد از پایان کار باید فایل بسته شود.

---

مثال:

```python
file = open("test.txt")

content = file.read()

file.close()
```

---

# روش حرفه‌ای‌تر

در دنیای واقعی تقریباً همیشه از:

```python
with
```

استفاده می‌شود.

---

مثال:

```python
with open("test.txt") as file:
    content = file.read()

print(content)
```

---

مزیت:

حتی اگر خطا رخ دهد فایل به‌صورت خودکار بسته می‌شود.

---

# نوشتن در فایل

حالت نوشتن:

```python
w
```

---

مثال:

```python
with open("result.txt", "w") as file:
    file.write("Hello")
```

---

خروجی:

```text
result.txt
```

مقدار:

```text
Hello
```

---

# اضافه کردن به فایل

اگر نخواهیم محتویات قبلی حذف شود:

```python
a
```

---

مثال:

```python
with open("log.txt", "a") as file:
    file.write("New Log\n")
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
JSON چیست؟
</p>

<p dir='rtl'>
JSON مخفف:
</p>

```text
JavaScript Object Notation
```

است.

---

یکی از محبوب‌ترین فرمت‌های ذخیره داده در دنیاست.

---

نمونه JSON:

```json
{
  "ip": "127.0.0.1",
  "port": 80,
  "service": "http"
}
```

---

# ماژول JSON

پایتون به‌صورت پیش‌فرض دارای ماژول:

```python
json
```

است.

---

# تبدیل Dictionary به JSON

```python
import json

data = {
    "port": 80,
    "service": "http"
}

print(json.dumps(data))
```

خروجی:

```json
{"port": 80, "service": "http"}
```

---

# ذخیره JSON در فایل

```python
import json

data = {
    "port": 80,
    "service": "http"
}

with open("result.json", "w") as file:
    json.dump(data, file)
```

---

فایل تولید شده:

```json
{
  "port": 80,
  "service": "http"
}
```

---

# خواندن JSON

```python
import json

with open("result.json") as file:
    data = json.load(file)

print(data)
```

---

خروجی:

```python
{'port': 80, 'service': 'http'}
```

---

# ارتباط با پروژه ما

فایل:

```python
exporter.py
```

دقیقاً همین کار را انجام می‌دهد.

---

مثال خروجی:

```json
{
  "target": "127.0.0.1",
  "open_ports": [
    {
      "port": 80,
      "service": "http"
    }
  ]
}
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
CSV چیست؟
</p>

<p dir='rtl'>
CSV مخفف:
</p>

```text
Comma Separated Values
```

است.

---

نمونه:

```csv
port,service
80,http
443,https
```

---

این فرمت برای:

<p dir='rtl'>
• Excel <br>
• LibreOffice <br>
• Google Sheets
</p>

بسیار مناسب است.

---

# ماژول CSV

پایتون دارای ماژول داخلی:

```python
csv
```

است.

---

# نوشتن CSV

```python
import csv

with open("result.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["port", "service"])

    writer.writerow([80, "http"])

    writer.writerow([443, "https"])
```

---

فایل تولید شده:

```csv
port,service
80,http
443,https
```

---

# خواندن CSV

```python
import csv

with open("result.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

خروجی:

```python
['port', 'service']
['80', 'http']
['443', 'https']
```

---

# ارتباط با پروژه ما

فایل:

```python
csv_exporter.py
```

دقیقاً از همین مفاهیم استفاده می‌کند.

---

نمونه خروجی واقعی:

```csv
port,service,banner
80,http,Apache
443,https,nginx
```

---

# چیزی که امروز یاد گرفتیم

<p dir='rtl'>
✓ کار با فایل‌ها <br>
✓ open <br>
✓ read <br>
✓ write <br>
✓ with <br>
✓ JSON <br>
✓ json.dump <br>
✓ json.load <br>
✓ CSV <br>
✓ csv.writer <br>
✓ ارتباط مستقیم با exporter.py <br>
✓ ارتباط مستقیم با csv_exporter.py
</p>

---

# تمرین

فایلی به نام:

```text
ports.json
```

بساز که اطلاعات زیر را ذخیره کند:

```python
{
    "port": 22,
    "service": "ssh"
}
```

سپس فایل را بخوان و مقدار service را چاپ کن.

---

جلسه بعد:

<p align='right' dir='ltr' style='font-size:32px; font-wight:bold;'>
09-networking-with-python.md
</p>

در جلسه بعد وارد دنیای شبکه می‌شویم و یاد می‌گیریم Socket چیست؛ مهم‌ترین پیش‌نیاز ساخت Port Scanner.

</div>