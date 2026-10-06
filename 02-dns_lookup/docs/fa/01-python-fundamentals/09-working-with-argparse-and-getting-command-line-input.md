# درس ۹: کار با argparse و دریافت ورودی از خط فرمان

## هدف درس

در این درس یاد می‌گیریم چگونه برنامه‌های پایتون را از طریق خط فرمان کنترل کنیم و ورودی‌های کاربر را دریافت نماییم.

ابزار DNS Lookup ما از این قابلیت استفاده می‌کند تا کاربر بتواند دامنه و نوع رکورد DNS را هنگام اجرای برنامه مشخص کند.

---

# چرا argparse؟

فرض کنید برنامه زیر را اجرا می‌کنیم:

```bash
python app.py google.com A
```

در این حالت:

<p dir='rtl'>
• google.com دامنه هدف است <br>
• A نوع رکورد DNS است
</p>

پایتون این مقادیر را به صورت خودکار پردازش نمی‌کند.

برای مدیریت حرفه‌ای آرگومان‌های خط فرمان از ماژول استاندارد `argparse` استفاده می‌کنیم.

---

# اولین مثال

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")

args = parser.parse_args()

print(args.name)
```

اجرا:

```bash
python app.py Ali
```

خروجی:

```text
Ali
```

---

# چند آرگومان

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("domain")
parser.add_argument("record_type")

args = parser.parse_args()

print(args.domain)
print(args.record_type)
```

اجرا:

```bash
python app.py google.com MX
```

خروجی:

```text
google.com
MX
```

---

# آرگومان‌های اختیاری

گاهی می‌خواهیم برخی گزینه‌ها اختیاری باشند.

مثال:

```python
parser.add_argument(
    "--timeout",
    type=float,
)
```

اجرا:

```bash
python app.py --timeout 2
```

خروجی:

```text
2.0
```

---

# تعیین نوع داده

<p dir='rtl'>
argparse می‌تواند نوع داده را کنترل کند.
</p>

```python
parser.add_argument(
    "--workers",
    type=int,
)
```

اگر کاربر مقدار نامعتبر وارد کند:

```bash
python app.py --workers hello
```

<p dir='rtl'>
argparse خطا تولید می‌کند.
</p>

---

# نمایش راهنما

```python
parser = argparse.ArgumentParser(
    description="DNS Lookup Tool"
)
```

کاربر می‌تواند بنویسد:

```bash
python app.py --help
```

نمونه خروجی:

```text
usage: app.py domain record_type

DNS Lookup Tool

positional arguments:
  domain
  record_type
```

این قابلیت باعث می‌شود ابزارهای ما حرفه‌ای‌تر شوند.

---

# استفاده در پروژه DNS Lookup

در پروژه ما:

```python
parser.add_argument(
    "domain",
    type=str,
    help="Target domain name",
)

parser.add_argument(
    "record_type",
    type=str,
    help="DNS record type",
)
```

و همچنین:

```python
parser.add_argument(
    "--json",
    dest="json_file",
)

parser.add_argument(
    "--csv",
    dest="csv_file",
)
```

به همین دلیل می‌توانیم برنامه را به شکل زیر اجرا کنیم:

```bash
python -m src.cli google.com A
```

یا:

```bash
python -m src.cli google.com MX --json result.json
```

یا:

```bash
python -m src.cli google.com NS --csv result.csv
```

---

# مزایای argparse

<p dir='rtl'>
• خوانایی بالا <br>
• مدیریت خودکار خطاها <br>
• تولید خودکار help <br>
• پشتیبانی از آرگومان‌های اجباری و اختیاری <br>
• مناسب برای ابزارهای حرفه‌ای خط فرمان
</p>

---

# جمع‌بندی

در این درس یاد گرفتیم:

<p dir='rtl'>
• argparse چیست <br>
• چگونه آرگومان دریافت کنیم <br>
• تفاوت آرگومان اجباری و اختیاری <br>
• استفاده از type <br>
• استفاده از help <br>
• نحوه استفاده argparse در پروژه DNS Lookup
</p>

این ماژول پایه اصلی ساخت ابزارهای CLI حرفه‌ای در پایتون است و تقریباً در تمام پروژه‌های امنیتی و اتوماسیون کاربرد دارد.
