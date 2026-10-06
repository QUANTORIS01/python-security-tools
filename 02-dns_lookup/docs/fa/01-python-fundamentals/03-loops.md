# درس ۳: حلقه‌ها (Loops) در پایتون

## مقدمه

تا اینجا یاد گرفتیم چگونه داده‌ها را در متغیرها ذخیره کنیم و چگونه با استفاده از شرط‌ها تصمیم بگیریم.

اما در برنامه‌های واقعی معمولاً با یک مقدار سروکار نداریم.

برای مثال در پروژه DNS Lookup ممکن است چندین رکورد DNS دریافت کنیم:

```python
[
    "1.1.1.1",
    "8.8.8.8",
    "9.9.9.9",
]
```

اگر بخواهیم همه این مقادیر را نمایش دهیم، نوشتن کد جداگانه برای هر مقدار منطقی نیست.

برای حل این مشکل از **حلقه‌ها (Loops)** استفاده می‌کنیم.

---

# حلقه چیست؟

حلقه ابزاری است که یک قطعه کد را چندین بار اجرا می‌کند.

مثال:

```python
for number in [1, 2, 3]:
    print(number)
```

خروجی:

```text
1
2
3
```

---

# حلقه for

رایج‌ترین حلقه در پایتون، `for` است.

ساختار کلی:

```python
for item in collection:
    # code
```

مثال:

```python
domains = [
    "google.com",
    "github.com",
    "python.org",
]

for domain in domains:
    print(domain)
```

خروجی:

```text
google.com
github.com
python.org
```

---

# پیمایش رشته‌ها

رشته نیز مجموعه‌ای از کاراکترهاست.

مثال:

```python
for char in "DNS":
    print(char)
```

خروجی:

```text
D
N
S
```

---

# تابع <span dir='ltr'>range()</span>

برای تولید دنباله‌ای از اعداد استفاده می‌شود.

مثال:

```python
for number in range(5):
    print(number)
```

خروجی:

```text
0
1
2
3
4
```

---

# تعیین نقطه شروع و پایان

مثال:

```python
for number in range(1, 6):
    print(number)
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

# تعیین گام (Step)

مثال:

```python
for number in range(0, 10, 2):
    print(number)
```

خروجی:

```text
0
2
4
6
8
```

---

# حلقه روی لیست‌ها

یکی از مهم‌ترین کاربردهای حلقه در پروژه DNS Lookup پردازش لیست رکوردها است.

مثال:

```python
records = [
    "1.1.1.1",
    "8.8.8.8",
]

for record in records:
    print(record)
```

---

# ساخت لیست با حلقه

مثال:

```python
results = []

for value in ["1.1.1.1", "8.8.8.8"]:
    results.append(value)
```

اکنون:

```python
print(results)
```

خروجی:

```text
['1.1.1.1', '8.8.8.8']
```

---

<div align='right'>

# List Comprehension

</div>

پایتون راه کوتاه‌تری نیز برای ساخت لیست دارد.

مثال:

```python
results = [
    value
    for value in ["1.1.1.1", "8.8.8.8"]
]
```

این دقیقاً معادل مثال قبلی است.

---

# ارتباط مستقیم با پروژه

در فایل:

```python
results.py
```

از List Comprehension استفاده کرده‌ایم:

```python
return [
    DNSRecord(
        domain=domain,
        record_type=record_type,
        value=value,
    )
    for value in values
]
```

این کد روی تمام مقادیر بازگشتی DNS حرکت می‌کند و برای هر مقدار یک شیء `DNSRecord` می‌سازد.

---

# حلقه در formatter.py

در فایل:

```python
formatter.py
```

نیز از حلقه استفاده کرده‌ایم:

```python
for result in results:
    lines.append(
        f"{result.domain:<30} "
        f"{result.record_type:<8} "
        f"{result.value}"
    )
```

این حلقه تمام رکوردهای DNS را پردازش می‌کند و به خروجی متنی اضافه می‌کند.

---

# دستور break

برای خروج فوری از حلقه استفاده می‌شود.

مثال:

```python
for number in range(10):
    if number == 5:
        break

    print(number)
```

خروجی:

```text
0
1
2
3
4
```

---

# دستور continue

برای رد شدن از یک تکرار استفاده می‌شود.

مثال:

```python
for number in range(5):
    if number == 2:
        continue

    print(number)
```

خروجی:

```text
0
1
3
4
```

---

# تابع <span dir='ltr'>enumerate()</span>

اگر همزمان به شماره و مقدار نیاز داشته باشیم:

```python
records = [
    "1.1.1.1",
    "8.8.8.8",
]

for index, value in enumerate(records):
    print(index, value)
```

خروجی:

```text
0 1.1.1.1
1 8.8.8.8
```

---

# حلقه while

نوع دیگری از حلقه است که تا برقرار بودن شرط ادامه پیدا می‌کند.

مثال:

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

خروجی:

```text
0
1
2
```

---

# چرا در پروژه از for استفاده کردیم؟

زیرا:

<div align='right'>

<span dir='rtl'>• تعداد رکوردها از قبل مشخص نیست. </span> <br>
<span dir='rtl'>• باید روی یک مجموعه از نتایج حرکت کنیم. </span> <br>
<span dir='rtl'>• `for` خواناتر و امن‌تر از `while` است. </span>

</div>

به همین دلیل در اکثر بخش‌های پروژه از `for` و List Comprehension استفاده شده است.

---

# تمرین

۱. لیستی شامل سه دامنه بسازید.

۲. با استفاده از `for` همه دامنه‌ها را چاپ کنید.

۳. با استفاده از `range()` اعداد ۱ تا ۱۰ را چاپ کنید.

۴. لیستی از IPها بسازید و با استفاده از List Comprehension نسخه جدیدی از همان لیست ایجاد کنید.

۵. برنامه‌ای بنویسید که هنگام رسیدن به عدد ۵ از حلقه خارج شود.

---

# خلاصه درس

در این درس یاد گرفتیم:

<p dir='rtl'>
• حلقه for <br>
• حلقه while <br>
• تابع range <br>
• پیمایش لیست‌ها <br>
• List Comprehension <br>
• break <br>
• continue <br>
• enumerate
</p>

این مفاهیم در پروژه DNS Lookup برای پردازش نتایج DNS، ساخت مدل‌های داده و تولید خروجی نهایی استفاده می‌شوند.

در درس بعدی با توابع (Functions) آشنا خواهیم شد؛ مفهومی که تقریباً تمام فایل‌های پروژه بر اساس آن ساخته شده‌اند.
