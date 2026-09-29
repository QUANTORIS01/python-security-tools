<div align='right' dir='rtl'>

# بررسی کامل فایل `cli.py`

# مقدمه

به مهم‌ترین جلسه کل دوره رسیدیم.

---

تا اینجا تمام قطعات پورت اسکنر را جداگانه یاد گرفتیم:

<p dir='rtl'>
✅ validator.py <br>
✅ scanner.py <br>
✅ services.py <br>
✅ exporter.py <br>
✅ csv_exporter.py <br>
✅ logger.py <br>
✅ banner.py <br>
✅ models.py <br>
✅ results.py <br>
✅ formatter.py
</p>

---

اما هنوز یک سؤال بزرگ باقی مانده است.

---

این همه فایل چگونه با یکدیگر ارتباط برقرار می‌کنند؟

---

وقتی کاربر این دستور را اجرا می‌کند:

```bash
python cli.py 127.0.0.1 1 100
```

---

چه اتفاقی پشت صحنه رخ می‌دهد؟

---

کدام فایل اول اجرا می‌شود؟

---

کدام تابع فراخوانی می‌شود؟

---

داده‌ها چگونه بین فایل‌ها جابه‌جا می‌شوند؟

---

پاسخ تمام این سؤالات داخل:

```text
src/cli.py
```

قرار دارد.

---

# نقش فایل cli.py

این فایل:

```text
Entry Point
```

پروژه است.

---

یعنی:

```text
نقطه شروع اجرای برنامه
```

---

در واقع:

```text
مغز اصلی پروژه
```

است.

---

تمام فایل‌هایی که قبلاً ساختیم:

```text
ابزار هستند
```

---

اما:

```text
cli.py
```

رهبر این ابزارها است.

---

# محتوای فایل

این فایل را می‌توان به چند بخش تقسیم کرد:

---

## بخش اول

<p dir='rtl'>
Importها
</p>

---

## بخش دوم

ساخت Parser

---

## بخش سوم

خواندن آرگومان‌ها

---

## بخش چهارم

اعتبارسنجی ورودی

---

## بخش پنجم

اجرای اسکن

---

## بخش ششم

ساخت نتایج

---

## بخش هفتم

نمایش خروجی

---

## بخش هشتم

<p dir='rtl'>
Export
</p>

---

## بخش نهم

<p dir='rtl'>
Entry Point
</p>

---

# محتوای فایل

```python
import argparse
import sys
import time

from src import (
    scan_range,
    validate_ip,
    validate_port_range,
    validate_timeout,
    validate_workers,
    export_json,
    export_csv,
    setup_logger,
    build_scan_results,
    format_scan_results
)


def create_parser() -> argparse.ArgumentParser:
    """
    Create the command-line argument parser.
    """
    parser = argparse.ArgumentParser(description="TCP Port Scanner")
    parser.add_argument("ip", type=str, help="Target IPv4 address")
    parser.add_argument("start_port", type=int, help="Starting port number")
    parser.add_argument("end_port", type=int, help="Ending port number")
    parser.add_argument("-t", "--timeout", type=float, default=0.5, help="Connection timeout in seconds (default: 0.5)")
    parser.add_argument("-w", "--workers", type=int, default=100, help="Number of concurrent workers (default: 100)")
    parser.add_argument("--json", dest="json_file", type=str, help="Export results to a JSON file")
    parser.add_argument("--csv", dest="csv_file", type=str, help="Export results to a CSV file")
    return parser


def main() -> None:
    """
    Run the port scanner CLI.
    """
    parser = create_parser()
    args = parser.parse_args()
    if not validate_ip(args.ip):
        print(f"❌ Invalid IP address: {args.ip}")
        sys.exit(1)
    if not validate_port_range(args.start_port, args.end_port):
        print("❌ Invalid port range.")
        sys.exit(1)
    if not validate_timeout(args.timeout):
        print("❌ Timeout must be greater than 0.")
        sys.exit(1)

    if not validate_workers(args.workers):
        print("❌ Workers must be greater than 0.")
        sys.exit(1)
    logger = setup_logger("scan.log")
    print()
    print(f"🔍 Scanning {args.ip}")
    print(f"Port range: {args.start_port}-{args.end_port}")
    print(f"Timeout: {args.timeout}s")
    print(f"Workers: {args.workers}")
    print()
    start_time = time.perf_counter()
    logger.info("Scan started target=%s ports=%s-%s", args.ip, args.start_port, args.end_port)
    open_ports = scan_range(args.ip, args.start_port, args.end_port, timeout=args.timeout, workers=args.workers)
    results = build_scan_results(args.ip, open_ports, timeout=args.timeout)
    logger.info("Scan completed open_ports=%s", len(open_ports))
    elapsed_time = time.perf_counter() - start_time
    print("-" * 70)
    print(format_scan_results(results))
    print("-" * 70)
    print(f"Scan completed in {elapsed_time:.2f}s")
    print(f"Open ports found: {len(open_ports)}")
    export_data = {"target": args.ip, "start_port": args.start_port, "end_port": args.end_port, "open_ports": [
        {
            "port": result.port,
            "service": result.service,
            "banner": result.banner,
        } for result in results
    ]}
    if args.json_file:
        export_json(export_data, args.json_file)
        print(f"Results exported to {args.json_file}")

    if args.csv_file:
        export_csv(export_data, args.csv_file)
        print(f"Results exported to {args.csv_file}")


if __name__ == "__main__":
    main()

```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Importها
</p>

```python
import argparse
import sys
import time
```

---

سه ماژول داخلی پایتون.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
argparse
</p>

```python
import argparse
```

---

مهم‌ترین ماژول CLI در پایتون.

---

وظیفه:

```text
خواندن آرگومان‌های خط فرمان
```

---

مثال:

```bash
python cli.py 127.0.0.1 1 100
```

---

اینجا:

```text
127.0.0.1
1
100
```

آرگومان هستند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
sys
</p>

```python
import sys
```

---

برای تعامل با سیستم عامل.

---

ما فقط از:

```python
sys.exit()
```

استفاده می‌کنیم.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
time
</p>

```python
import time
```

---

برای اندازه‌گیری زمان اجرای اسکن.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import از پروژه
</p>

```python
from src import (...)
```

---

دقت کن.

---

تمام فایل‌هایی که در طول این دوره ساختیم اینجا جمع شده‌اند.

---

```python
scan_range
```

↓

اسکن

---

```python
validate_ip
```

↓

اعتبارسنجی IP

---

```python
validate_port_range
```

↓

اعتبارسنجی پورت

---

```python
validate_timeout
```

↓

اعتبارسنجی Timeout

---

```python
validate_workers
```

↓

اعتبارسنجی Worker

---

```python
export_json
```

↓

خروجی JSON

---

```python
export_csv
```

↓

خروجی CSV

---

```python
setup_logger
```

↓

ثبت Log

---

```python
build_scan_results
```

↓

ساخت مدل‌ها

---

```python
format_scan_results
```

↓

نمایش خروجی

---

# تابع create_parser

```python
def create_parser():
```

---

هدف:

```text
ساخت CLI
```

---

# ساخت Parser

```python
parser = argparse.ArgumentParser(
    description="TCP Port Scanner"
)
```

---

این خط:

```text
برنامه خط فرمان را می‌سازد.
```

---

اگر کاربر بنویسد:

```bash
python cli.py --help
```

---

همین Description نمایش داده می‌شود.

---

# آرگومان اول

```python
parser.add_argument(
    "ip"
)
```

---

اجباری است.

---

مثال:

```bash
127.0.0.1
```

---

# آرگومان دوم

```python
start_port
```

---

مثال:

```bash
1
```

---

# آرگومان سوم

```python
end_port
```

---

مثال:

```bash
100
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Timeout
</p>

```python
-t
--timeout
```

---

مثال:

```bash
--timeout 1
```

---

یا:

```bash
-t 1
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Workers
</p>

```python
-w
--workers
```

---

مثال:

```bash
-w 500
```

---

# خروجی JSON

```python
--json
```

---

مثال:

```bash
--json result.json
```

---

# خروجی CSV

```python
--csv
```

---

مثال:

```bash
--csv result.csv
```

---

# ورود به main

```python
def main():
```

---

تمام اجرای برنامه از اینجا شروع می‌شود.

---

# ساخت Parser

```python
parser = create_parser()
```

---

# خواندن آرگومان‌ها

```python
args = parser.parse_args()
```

---

فرض کن اجرا کنیم:

```bash
python cli.py 127.0.0.1 1 100
```

---

خروجی:

```python
args.ip
```

↓

```python
127.0.0.1
```

---

```python
args.start_port
```

↓

```python
1
```

---

```python
args.end_port
```

↓

```python
100
```

---

# اعتبارسنجی IP

```python
if not validate_ip(args.ip):
```

---

اگر IP معتبر نباشد:

```python
print(...)
sys.exit(1)
```

---

برنامه متوقف می‌شود.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
sys.exit(1)
</p>

```python
sys.exit(1)
```

---

کد خروج:

```text
1
```

---

معمولاً یعنی:

```text
خطا
```

---

# اعتبارسنجی پورت

```python
validate_port_range(...)
```

---

بررسی:

```text
0-65535
```

---

# اعتبارسنجی Timeout

```python
validate_timeout(...)
```

---

بررسی:

```text
بزرگتر از صفر
```

---

# اعتبارسنجی Workers

```python
validate_workers(...)
```

---

بررسی:

```text
بزرگتر از صفر
```

---

# ساخت Logger

```python
logger = setup_logger(
    "scan.log"
)
```

---

فایل:

```text
scan.log
```

ساخته می‌شود.

---

# نمایش اطلاعات اولیه

```python
print(...)
```

---

نمونه خروجی:

```text
Scanning 127.0.0.1
Port range: 1-100
Timeout: 0.5s
Workers: 100
```

---

# شروع اندازه‌گیری زمان

```python
start_time = time.perf_counter()
```

---

این تابع بسیار دقیق‌تر از:

```python
time.time()
```

است.

---

برای Benchmark مناسب است.

---

# ثبت شروع اسکن

```python
logger.info(...)
```

---

نمونه:

```text
Scan started
```

---

# اجرای اسکن

```python
open_ports = scan_range(...)
```

---

اینجا فایل:

```python
scanner.py
```

اجرا می‌شود.

---

خروجی:

```python
[22, 80, 443]
```

---

# ساخت نتایج

```python
results = build_scan_results(...)
```

---

اینجا:

```python
results.py
```

اجرا می‌شود.

---

خروجی:

```python
[
    ScanResult(...),
    ScanResult(...)
]
```

---

# ثبت پایان اسکن

```python
logger.info(...)
```

---

ثبت تعداد پورت‌های باز.

---

# محاسبه زمان

```python
elapsed_time =
    time.perf_counter()
    - start_time
```

---

مثال:

```python
2.35
```

ثانیه.

---

# نمایش جدول

```python
format_scan_results(
    results
)
```

---

اینجا:

```python
formatter.py
```

اجرا می‌شود.

---

خروجی:

```text
PORT
STATUS
SERVICE
BANNER
```

---

# نمایش آمار

```python
Open ports found
```

---

مثال:

```text
3
```

---

# ساخت داده Export

```python
export_data = {...}
```

---

این دیکشنری:

```python
ScanResult
```

ها را به ساختار مناسب فایل تبدیل می‌کند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
List Comprehension
</p>

اینجا:

```python
[
    {
        ...
    }
    for result in results
]
```

---

از:

```python
List Comprehension
```

استفاده شده است.

---

این بخش:

```python
ScanResult
```

ها را تبدیل می‌کند به:

```python
dict
```

---

مثال:

قبل:

```python
ScanResult(...)
```

---

بعد:

```python
{
    "port": 80,
    "service": "http",
    "banner": "Apache"
}
```

---

# خروجی JSON

```python
if args.json_file:
```

---

اگر کاربر:

```bash
--json result.json
```

را وارد کرده باشد.

---

فایل JSON ساخته می‌شود.

---

# خروجی CSV

```python
if args.csv_file:
```

---

اگر:

```bash
--csv result.csv
```

وجود داشته باشد.

---

فایل CSV ساخته می‌شود.

---

# مهم‌ترین بخش فایل

```python
if __name__ == "__main__":
    main()
```

---

این یکی از مهم‌ترین مفاهیم پایتون است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
__name__ چیست؟
</p>

هر فایل پایتون یک متغیر داخلی دارد:

```python
__name__
```

---

اگر فایل مستقیماً اجرا شود:

```python
__name__
```

↓

```python
"__main__"
```

---

اما اگر Import شود:

```python
import cli
```

---

آنگاه:

```python
__name__
```

↓

```python
"cli"
```

---

# چرا این شرط مهم است؟

باعث می‌شود:

```python
main()
```

فقط هنگام اجرای مستقیم فایل اجرا شود.

---

نه هنگام Import کردن.

---

# جریان کامل اجرای پروژه

```text
cli.py
    │
    ▼

validate_ip()

    │
    ▼

validate_port_range()

    │
    ▼

scan_range()

    │
    ▼

detect_service()

    │
    ▼

grab_banner()

    │
    ▼

ScanResult()

    │
    ▼

build_scan_results()

    │
    ▼

format_scan_results()

    │
    ▼

export_json()
export_csv()
```

---

این همان معماری کامل پورت اسکنری است که ساخته‌ایم.

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ CLI چیست <br>
✅ argparse چیست <br>
✅ Parser چیست <br>
✅ parse_args چیست <br>
✅ sys.exit چیست <br>
✅ perf_counter چیست <br>
✅ Entry Point چیست <br>
✅ __name__ چیست <br>
✅ __main__ چیست <br>
✅ List Comprehension چیست <br>
✅ جریان کامل اجرای پروژه چگونه است
</p>

---

# پایان دایرکتوری src

تبریک 🎉

---

ما اکنون تمام فایل‌های اصلی پروژه را:

```text
خط به خط
```

بررسی کردیم.

---

اکنون یک دانشجو باید بتواند:

<p dir='rtl'>
✅ ساختار پروژه را درک کند <br>
✅ یک پورت اسکنر مشابه بسازد <br>
✅ قابلیت‌های جدید اضافه کند <br>
✅ معماری پروژه را توسعه دهد
</p>

---

# در فصل بعد چه چیزی یاد می‌گیریم؟

اکنون وارد دایرکتوری:

```text
04-port-scanner/tests
```

می‌شویم.

---

در این بخش یاد می‌گیریم:

<p dir='rtl'>
✅ تست چیست <br>
✅ Unit Test چیست <br>
✅ pytest چیست <br>
✅ Mock چیست <br>
✅ Monkeypatch چیست <br>
✅ چگونه برای پروژه‌های واقعی تست حرفه‌ای بنویسیم
</p>

</div>