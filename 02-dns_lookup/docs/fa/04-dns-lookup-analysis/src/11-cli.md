<div align='right'>

[🇬🇧 English](/02-dns_lookup/docs/en/04-dns-lookup-analysis/src/11-cli.md)

</div>

# درس یازدهم: طراحی رابط خط فرمان با argparse

**فایل مورد بررسی:** `src/cli.py`

## ۱. هدف درس

در این درس یاد می‌گیریم چگونه با استفاده از `argparse` یک رابط خط فرمان بسازیم و اجزای مختلف یک برنامه را از طریق تابع اصلی به یکدیگر متصل کنیم.

فایل `cli.py` نقطه‌ی هماهنگ‌کننده‌ی اجرای ابزار DNS Lookup است. وظایف اصلی آن عبارت‌اند از:

<p dir='rtl'>
• دریافت دامنه و نوع رکورد از خط فرمان <br>
• اعتبارسنجی ورودی‌ها <br>
• راه‌اندازی logger <br>
• اجرای جست‌وجوی DNS <br>
• مدیریت خطای timeout <br>
• نمایش نتایج در ترمینال <br>
• آماده‌سازی داده‌ها برای خروجی JSON و CSV <br>
• اعلام موفقیت ذخیره‌سازی خروجی‌ها
</p>

در معماری این پروژه، هر بخش وظیفه‌ی مشخصی دارد و `cli.py` اجرای آن‌ها را هماهنگ می‌کند.

## ۲. کد کامل فایل

```python
import argparse
import sys

from src import (
    validate_domain,
    validate_record_type,
    build_dns_results,
    format_dns_results,
    export_json,
    export_csv,
    setup_logger,
)

from .exception import DNSTimeoutError


def create_parser() -> argparse.ArgumentParser:
    """
    Create command-line argument parser.
    """
    parser = argparse.ArgumentParser(description='DNS Lookup Tool')
    parser.add_argument('domain', type=str, help='Target domain name')
    parser.add_argument('record_type', type=str, help='DNS record type')
    parser.add_argument('--json', dest='json_file', type=str, help='Export results to JSON')
    parser.add_argument('--csv', dest='csv_file', type=str, help='Export results to CSV')
    return parser


def main() -> None:
    """
    Run DNS lookup CLI.
    """
    parser = create_parser()
    args = parser.parse_args()
    if not validate_domain(args.domain):
        print(f'❌ Invalid domain: {args.domain}')
        sys.exit(1)
    if not validate_record_type(args.record_type):
        print(f'❌ Invalid record type: {args.record_type}')
        sys.exit(1)
    logger = setup_logger('dns.log')
    logger.info('Lookup started domain=%s type=%s', args.domain, args.record_type)
    try:
        results = build_dns_results(args.domain, args.record_type)
    except DNSTimeoutError:
        print('❌ DNS query timed out.')
        sys.exit(1)
    logger.info('Lookup completed records=%s', len(results))
    print(format_dns_results(results))
    export_data = {
        'domain': args.domain,
        'record_type': args.record_type,
        'records': [{
            'domain': result.domain,
            'record_type': result.record_type,
            'value': result.value,
        } for result in results]
    }
    if args.json_file:
        export_json(export_data, args.json_file)
        print(f'Results exported to {args.json_file}')
    if args.csv_file:
        export_csv(export_data, args.csv_file)
        print(f'Results exported to {args.csv_file}')


if __name__ == '__main__':
    main()
```

## ۳. وارد کردن ماژول‌ها

```python
import argparse
import sys
```

### ماژول `argparse`

ماژول `argparse` از کتابخانه‌ی استاندارد پایتون است و برای ساخت رابط خط فرمان به کار می‌رود. با آن می‌توان ورودی‌های اجباری، گزینه‌های اختیاری، توضیحات و راهنمای اجرای برنامه را تعریف کرد.

### ماژول `sys`

در این فایل، از `sys.exit(1)` برای پایان‌دادن به اجرای برنامه با کد خروج غیرصفر استفاده می‌شود. معمولاً کد خروج `0` نشان‌دهنده‌ی پایان موفق و کد غیرصفر نشان‌دهنده‌ی خطا یا پایان غیرموفق است.

## ۴. وارد کردن اجزای داخلی پروژه

```python
from src import (
    validate_domain,
    validate_record_type,
    build_dns_results,
    format_dns_results,
    export_json,
    export_csv,
    setup_logger,
)

from .exception import DNSTimeoutError
```

این importها نشان می‌دهند که `cli.py` خودش منطق اصلی هر عملیات را پیاده‌سازی نمی‌کند؛ بلکه از توابع و کلاس‌هایی استفاده می‌کند که قبلاً در بخش‌های مختلف پروژه تعریف شده‌اند.

<div align='center' dir="rtl">

| نام | مسئولیت |
|---|---|
| `validate_domain` | بررسی قالب دامنه |
| `validate_record_type` | بررسی پشتیبانی از نوع رکورد |
| `build_dns_results` | اجرای جست‌وجو و ساخت نتایج ساختاریافته |
| `format_dns_results` | آماده‌سازی متن جدولی برای ترمینال |
| `export_json` |<span dir='rtl'> ذخیره‌ی داده‌ها در JSON</span> |
| `export_csv` |<span dir='rtl'> ذخیره‌ی داده‌ها در CSV</span> |
| `setup_logger` |<span dir='rtl'> آماده‌سازی logger</span> |
| `DNSTimeoutError` |<span dir='rtl'> شناسایی خطای timeout اختصاصی پروژه</span> |

</div>

این جداسازی باعث می‌شود رابط خط فرمان، مسئول هماهنگی عملیات باشد و جزئیات هر وظیفه در بخش مربوط به خودش باقی بماند.

## ۵. ساخت parser با <span dir='ltr'>`create_parser()`</span>

```python
def create_parser() -> argparse.ArgumentParser:
    """
    Create command-line argument parser.
    """
    parser = argparse.ArgumentParser(description='DNS Lookup Tool')
```

تابع <span dir='ltr'>`create_parser()`</span> شیء parser را می‌سازد و تنظیم می‌کند.

<div align='right' dir="rtl">

<span dir='rtl'>`ArgumentParser` مسئول تفسیر آرگومان‌هایی است که هنگام اجرای برنامه وارد می‌شوند.</span>

</div>

پارامتر `description` توضیح کوتاهی برای برنامه تعیین می‌کند. این توضیح در راهنمایی که با گزینه‌ی <span dir='ltr'>`--help`</span> نمایش داده می‌شود، قابل مشاهده است.

جداکردن ساخت parser در یک تابع مستقل، کد را منظم‌تر می‌کند و امکان آزمایش تنظیمات آرگومان‌ها را نیز فراهم می‌سازد.

## ۶. تعریف آرگومان‌های اجباری

```python
parser.add_argument(
    'domain',
    type=str,
    help='Target domain name'
)
parser.add_argument(
    'record_type',
    type=str,
    help='DNS record type'
)
```

در `argparse`، آرگومان‌هایی که بدون پیشوند گزینه تعریف می‌شوند، به‌صورت پیش‌فرض اجباری هستند.

بنابراین، کاربر باید دامنه و نوع رکورد را در زمان اجرای برنامه مشخص کند.

برای مثال:

```bash
python -m src.cli example.com A
```

در این فرمان:

<div align='right' dir="rtl">

<span dir='rtl'>• `example.com` مقدار آرگومان `domain` است.</span> <br>
<span dir='rtl'>• `A` مقدار آرگومان `record_type` است.</span>

</div>

پارامتر `type=str` مشخص می‌کند که مقدار آرگومان به رشته تبدیل شود. از آنجا که آرگومان‌های خط فرمان معمولاً به‌صورت رشته دریافت می‌شوند، اینجا بیشتر نقش مستندسازی صریح نوع مورد انتظار را دارد.

پارامتر `help` نیز توضیح آرگومان را برای راهنمای خط فرمان تعیین می‌کند.

## ۷. تعریف گزینه‌های اختیاری JSON و CSV

```python
parser.add_argument(
    '--json',
    dest='json_file',
    type=str,
    help='Export results to JSON'
)
parser.add_argument(
    '--csv',
    dest='csv_file',
    type=str,
    help='Export results to CSV'
)
```

این دو گزینه به کاربر اجازه می‌دهند مشخص کند که نتایج در چه قالبی ذخیره شوند.

### گزینه‌ی <span dir='ltr'>`--json`</span>

نمونه‌ی استفاده:

```bash
python -m src.cli example.com A --json results.json
```

نام فایل `results.json` به‌عنوان مقدار گزینه‌ی <span dir='ltr'>`--json`</span> دریافت می‌شود.

### گزینه‌ی <span dir='ltr'>`--csv`</span>

نمونه‌ی استفاده:

```bash
python -m src.cli example.com A --csv results.csv
```

در این حالت، فایل `results.csv` به‌عنوان مقصد خروجی CSV تعیین می‌شود.

### نقش `dest`

پارامتر `dest` نام ویژگی‌ای را مشخص می‌کند که مقدار آرگومان در آن ذخیره خواهد شد.

در نتیجه:

<div align='right' dir="rtl">

<span dir='rtl'>• مقدار <span dir='ltr'>`--json`</span> در `args.json_file` قرار می‌گیرد.</span> <br>
<span dir='rtl'>• مقدار <span dir='ltr'>`--csv`</span> در `args.csv_file` قرار می‌گیرد.</span>

</div>

اگر کاربر یکی از این گزینه‌ها را وارد نکند، مقدار متناظر معمولاً `None` خواهد بود.

این طراحی باعث می‌شود ذخیره‌سازی خروجی اختیاری باشد و کاربر بتواند فقط خروجی ترمینال را دریافت کند یا یک یا هر دو قالب را انتخاب کند.

## ۸. برگرداندن parser

```python
return parser
```

تابع <span dir='ltr'>`create_parser()`</span> پس از تعریف تمام آرگومان‌ها، parser را برمی‌گرداند.

در ادامه، تابع <span dir='ltr'>`main()`</span> از همین شیء برای پردازش ورودی واقعی خط فرمان استفاده می‌کند.

## ۹. نقطه‌ی ورود اجرای برنامه: تابع <span dir='ltr'>`main()`</span>

```python
def main() -> None:
    """
    Run DNS lookup CLI.
    """
    parser = create_parser()
    args = parser.parse_args()
```

در این قسمت، اجرای اصلی رابط خط فرمان آغاز می‌شود.

ابتدا parser ساخته می‌شود؛ سپس <span dir='ltr'>`parse_args()`</span> آرگومان‌های واردشده را می‌خواند و نتیجه را در شیء `args` قرار می‌دهد.

پس از پردازش، مقادیر با دسترسی به ویژگی‌های شیء قابل استفاده‌اند:

```python
args.domain
args.record_type
args.json_file
args.csv_file
```

برای نمونه، اگر فرمان چنین باشد:

```bash
python -m src.cli example.com A --json results.json
```

مقادیر اصلی `args` به این شکل خواهند بود:

<div align='center' dir="rtl">

| ویژگی | مقدار |
|---|---|
| `args.domain` | `example.com` |
| `args.record_type` | `A` |
| `args.json_file` | `results.json` |
| `args.csv_file` | `None` |

</div>

نکته‌ی مهم این است که `argparse` ساختار ورودی خط فرمان را بررسی می‌کند؛ اما اعتبارسنجی معنایی دامنه و نوع رکورد همچنان به توابع اختصاصی پروژه سپرده شده است.

## ۱۰. اعتبارسنجی دامنه

```python
if not validate_domain(args.domain):
    print(f'❌ Invalid domain: {args.domain}')
    sys.exit(1)
```

در این قسمت، مقدار دامنه به تابع <span dir='ltr'>`validate_domain()`</span> داده می‌شود.

اگر تابع `False` برگرداند، شرط `not` برقرار می‌شود؛ پیام خطا نمایش داده شده و برنامه با کد خروج `1` خاتمه پیدا می‌کند.

این کنترل قبل از آغاز عملیات DNS انجام می‌شود. در نتیجه، ورودی‌ای که با قواعد اعتبارسنجی فعلی پروژه سازگار نیست، به مرحله‌ی جست‌وجو نمی‌رسد.

عبارت زیر نیز از یک f-string استفاده می‌کند:

```python
f'❌ Invalid domain: {args.domain}'
```

به کمک f-string، مقدار واردشده‌ی کاربر در پیام خطا قرار می‌گیرد.

## ۱۱. اعتبارسنجی نوع رکورد

```python
if not validate_record_type(args.record_type):
    print(f'❌ Invalid record type: {args.record_type}')
    sys.exit(1)
```

این شرط، نوع رکورد واردشده را بررسی می‌کند.

در پروژه، تابع <span dir='ltr'>`validate_record_type()`</span> نوع رکورد را با مجموعه‌ی انواع پشتیبانی‌شده مقایسه می‌کند. اگر نوع ورودی پذیرفته نشود، برنامه قبل از اجرای جست‌وجو خاتمه می‌یابد.

نکته‌ی مهم این است که دامنه و نوع رکورد دو بررسی مستقل‌اند. معتبر بودن یکی، معتبر بودن دیگری را تضمین نمی‌کند.

## ۱۲. آماده‌سازی logger و ثبت شروع عملیات

```python
logger = setup_logger('dns.log')
logger.info(
    'Lookup started domain=%s type=%s',
    args.domain,
    args.record_type
)
```

ابتدا logger با استفاده از تابع <span dir='ltr'>`setup_logger()`</span> که در درس قبل بررسی کردیم، آماده می‌شود.

سپس یک پیام `INFO` ثبت می‌شود که دامنه و نوع رکورد درخواست‌شده را مشخص می‌کند.

در این فراخوانی، <span dir='ltr'>`%s`</span>ها جایگاه مقادیر رشته‌ای هستند. ماژول `logging` مقادیر بعدی را هنگام آماده‌سازی پیام در این جایگاه‌ها قرار می‌دهد.

این روش برای ثبت پیام‌ها متداول است و از ساختن دستی رشته با f-string پیش از فراخوانی logger جلوگیری می‌کند.

با ثبت این پیام، فایل لاگ می‌تواند نشان دهد که درخواست جست‌وجو برای چه دامنه و چه نوع رکوردی آغاز شده است.

## ۱۳. اجرای جست‌وجوی DNS و مدیریت timeout

```python
try:
    results = build_dns_results(
        args.domain,
        args.record_type
    )
except DNSTimeoutError:
    print('❌ DNS query timed out.')
    sys.exit(1)
```

در این بخش، تابع <span dir='ltr'>`build_dns_results()`</span> فراخوانی می‌شود؛ همان تابعی که مسئول تبدیل مقادیر دریافت‌شده به نتایج ساختاریافته‌ی `DNSRecord` است.

چون عملیات DNS ممکن است به دلیل timeout با شکست مواجه شود، فراخوانی داخل یک بلوک `try` قرار گرفته است.

اگر `DNSTimeoutError` رخ دهد، اجرای عادی این بخش ادامه پیدا نمی‌کند؛ پیام خطا نمایش داده می‌شود و برنامه با کد خروج `1` پایان می‌یابد.

### چرا خطای اختصاصی استفاده شده است؟

در فایل `exception.py`، کلاس `DNSTimeoutError` به‌عنوان زیرکلاس `DNSLookupError` تعریف شده است. در فایل `resolver.py` نیز timeout کتابخانه‌ی DNS به این خطای اختصاصی تبدیل می‌شود.

بنابراین، رابط خط فرمان می‌تواند به‌جای وابستگی مستقیم به جزئیات خطای کتابخانه‌ی DNS، خطایی مشخص از دامنه‌ی مسئله‌ی خود پروژه را مدیریت کند.

در پیاده‌سازی فعلی، این بلوک به‌طور مشخص `DNSTimeoutError` را می‌گیرد. سایر خطاهای پیش‌بینی‌نشده در این بخش مدیریت نمی‌شوند و می‌توانند به فراخواننده منتقل شوند یا باعث پایان غیرعادی اجرا شوند.

## ۱۴. ثبت پایان عملیات

```python
logger.info('Lookup completed records=%s', len(results))
```

پس از بازگشت موفق تابع <span dir='ltr'>`build_dns_results()`</span>، تعداد نتایج ثبت می‌شود.

تابع <span dir='ltr'>`len()`</span> تعداد عناصر موجود در `results` را برمی‌گرداند.

اگر جست‌وجو نتیجه‌ای نداشته باشد و `results` یک فهرست خالی باشد، مقدار ثبت‌شده برابر با صفر خواهد بود. این وضعیت لزوماً به معنای خطای برنامه نیست؛ ممکن است جست‌وجو با موفقیت انجام شده باشد، اما رکوردی برای نمایش وجود نداشته باشد.

این پیام پایان عملیات موفق را ثبت می‌کند، نه صرفاً وجود یک یا چند رکورد را.

## ۱۵. نمایش نتایج در ترمینال

```python
print(format_dns_results(results))
```

در این قسمت، نتایج به تابع <span dir='ltr'>`format_dns_results()`</span> داده می‌شوند.

این تابع که در درس مربوط به `formatter.py` بررسی کردیم، فهرست `DNSRecord`ها را به یک رشته‌ی متنی با قالب جدولی تبدیل می‌کند.

سپس <span dir='ltr'>`print()`</span> آن رشته را در ترمینال نمایش می‌دهد.

با این طراحی، `cli.py` مسئول تصمیم‌گیری درباره‌ی زمان نمایش نتایج است؛ اما جزئیات چینش ستون‌ها در `formatter.py` قرار دارد.

## ۱۶. آماده‌سازی داده‌ها برای خروجی‌گیری

```python
export_data = {
    'domain': args.domain,
    'record_type': args.record_type,
    'records': [{
        'domain': result.domain,
        'record_type': result.record_type,
        'value': result.value,
    } for result in results]
}
```

این بخش، نتایج ساختاریافته را به یک دیکشنری تبدیل می‌کند تا توابع خروجی‌گیری بتوانند از آن استفاده کنند.

ساختار نهایی شامل سه کلید اصلی است:

<div align='right' dir="rtl">

<span dir='rtl'>• `domain`: دامنه‌ی درخواست‌شده</span> <br>
<span dir='rtl'>• `record_type`: نوع رکورد درخواست‌شده</span> <br>
<span dir='rtl'>• `records`: فهرستی از رکوردهای پیدا‌شده</span>

</div>

هر عنصر داخل `records` یک دیکشنری با کلیدهای `record_type`، `domain` و `value` است.

### درک list comprehension

قسمت زیر یک *list comprehension* است:

```python
[
    {
        'domain': result.domain,
        'record_type': result.record_type,
        'value': result.value,
    }
    for result in results
]
```

این عبارت برای هر شیء `DNSRecord` در `results` یک دیکشنری می‌سازد و دیکشنری‌ها را در فهرستی قرار می‌دهد.

برای مثال، یک شیء با مقادیر زیر:

```python
DNSRecord(
    domain='example.com',
    record_type='A',
    value='93.184.216.34'
)
```

به این دیکشنری تبدیل می‌شود:

```python
{
    'domain': 'example.com',
    'record_type': 'A',
    'value': '93.184.216.34'
}
```

این تبدیل، ساختار داده‌ای را برای exporterهای فعلی پروژه مناسب می‌کند؛ زیرا <span dir='ltr'>`export_json()`</span> و <span dir='ltr'>`export_csv()`</span> هر دو از دیکشنری `export_data` استفاده می‌کنند.

## ۱۷. ذخیره‌ی اختیاری در JSON

```python
if args.json_file:
    export_json(export_data, args.json_file)
    print(f'Results exported to {args.json_file}')
```

اگر کاربر گزینه‌ی <span dir='ltr'>`--json`</span> را وارد کرده باشد، `args.json_file` معمولاً یک رشته‌ی غیرخالی خواهد بود و شرط برقرار می‌شود.

سپس:

<div align='right' dir="rtl">

<span dir='rtl'>1. داده‌ها با تابع <span dir='ltr'>`export_json()`</span> در فایل مشخص‌شده ذخیره می‌شوند.</span> <br>
<span dir='rtl'>2. پیام مربوط به مسیر خروجی نمایش داده می‌شود.</span>

</div>

اگر گزینه‌ی <span dir='ltr'>`--json`</span> استفاده نشده باشد، این بلوک اجرا نمی‌شود و فایل JSON ساخته نخواهد شد.

نکته: پیام موفقیت پس از بازگشت تابع خروجی‌گیری چاپ می‌شود. اگر ذخیره‌سازی با خطایی مدیریت‌نشده شکست بخورد، اجرای برنامه به این پیام نمی‌رسد.

## ۱۸. ذخیره‌ی اختیاری در CSV

```python
if args.csv_file:
    export_csv(export_data, args.csv_file)
    print(f'Results exported to {args.csv_file}')
```

این بخش ساختاری مشابه خروجی JSON دارد؛ با این تفاوت که از تابع <span dir='ltr'>`export_csv()`</span> استفاده می‌کند.

کاربر می‌تواند فقط CSV، فقط JSON، هر دو یا هیچ‌کدام را انتخاب کند.

از آنجا که شرط‌های JSON و CSV مستقل‌اند، انتخاب هر دو گزینه باعث اجرای هر دو بلوک می‌شود.

## ۱۹. ترتیب کلی اجرای برنامه

جریان اجرای تابع <span dir='ltr'>`main()`</span> را می‌توان این‌گونه خلاصه کرد:

<div align='right' dir="rtl">

<span dir='rtl'>1. ساخت parser و دریافت آرگومان‌ها</span> <br>
<span dir='rtl'>2. اعتبارسنجی دامنه</span> <br>
<span dir='rtl'>3. اعتبارسنجی نوع رکورد</span> <br>
<span dir='rtl'>4. آماده‌سازی logger و ثبت شروع درخواست</span> <br>
<span dir='rtl'>5. اجرای جست‌وجوی DNS و مدیریت timeout</span> <br>
<span dir='rtl'>6. ثبت تعداد نتایج</span> <br>
<span dir='rtl'>7. نمایش نتایج در ترمینال</span> <br>
<span dir='rtl'>8. تبدیل نتایج به دیکشنری `export_data`</span> <br>
<span dir='rtl'>9. ذخیره‌ی اختیاری در JSON</span> <br>
<span dir='rtl'>10. ذخیره‌ی اختیاری در CSV</span>

</div>

این ترتیب اهمیت دارد؛ برای مثال، اگر اعتبارسنجی دامنه ناموفق باشد، برنامه پیش از ایجاد logger و اجرای جست‌وجوی DNS خاتمه پیدا می‌کند.

## ۲۰. نقطه‌ی ورود برنامه

```python
if __name__ == '__main__':
    main()
```

در پایتون، متغیر ویژه‌ی `__name__` مشخص می‌کند یک ماژول چگونه اجرا شده است.

وقتی فایل مستقیماً به‌عنوان برنامه‌ی اصلی اجرا شود، مقدار `__name__` برابر با `'__main__'` خواهد بود و تابع <span dir='ltr'>`main()`</span> فراخوانی می‌شود.

اما وقتی ماژول از بخش دیگری از برنامه import شود، این شرط معمولاً برقرار نخواهد بود؛ بنابراین اجرای خودکار رابط خط فرمان اتفاق نمی‌افتد.

این الگو اجازه می‌دهد یک فایل هم قابلیت اجرا داشته باشد و هم بتوان توابع آن را از ماژول‌های دیگر import کرد.

برای ساختار فعلی پروژه، نمونه‌ی اجرای ماژول به این شکل است:

```bash
python -m src.cli example.com A
```

استفاده از <span dir='ltr'>`-m`</span> ماژول را در قالب ساختار پکیج اجرا می‌کند.

## ۲۱. تمرین‌های آموزشی

### تمرین اول: بررسی راهنما

فرمان زیر را اجرا کنید:

```bash
python -m src.cli --help
```

بررسی کنید که توضیحات `record_type`، `domain`، <span dir='ltr'>`--json`</span> و <span dir='ltr'>`--csv`</span> چگونه نمایش داده می‌شوند.

### تمرین دوم: ورودی نامعتبر

برنامه را با یک دامنه‌ی نامعتبر اجرا کنید.

<p dir='rtl'>
• آیا عملیات DNS انجام می‌شود؟ <br>
• چه پیامی نمایش داده می‌شود؟ <br>
• کد خروج برنامه چیست؟
</p>

### تمرین سوم: انتخاب قالب خروجی

برنامه را در سه حالت اجرا کنید:

<div align='right' dir="rtl">

<span dir='rtl'>1. بدون گزینه‌ی خروجی</span> <br>
<span dir='rtl'>2. فقط با <span dir='ltr'>`--json`</span></span> <br>
<span dir='rtl'>3. با هر دو گزینه‌ی <span dir='ltr'>`--json`</span> و <span dir='ltr'>`--csv`</span></span>

</div>

رفتار هر حالت را مقایسه کنید.

### تمرین چهارم: بررسی timeout

با توجه به ساختار `try/except`، توضیح دهید اگر <span dir='ltr'>`build_dns_results()`</span> خطای `DNSTimeoutError` ایجاد کند، کدام مراحل بعدی اجرا نمی‌شوند.

### تمرین پنجم: بررسی ساختار داده

دیکشنری `export_data` را بررسی کنید و توضیح دهید چرا برای هر شیء `DNSRecord` یک دیکشنری جدید ساخته می‌شود.

## ۲۲. جمع‌بندی

فایل `cli.py` نقطه‌ی اتصال اجزای اصلی DNS Lookup است. این فایل مسئول هماهنگ‌کردن دریافت ورودی، اعتبارسنجی، جست‌وجو، نمایش، لاگ‌گیری و خروجی‌گیری است.

مهم‌ترین مفاهیم این درس عبارت‌اند از:

<div align='right' dir="rtl">

<span dir='rtl'>• ساخت رابط خط فرمان با `argparse`</span> <br>
<span dir='rtl'>• تفاوت آرگومان‌های اجباری و گزینه‌های اختیاری</span> <br>
<span dir='rtl'>• دسترسی به مقادیر از طریق `args`</span> <br>
<span dir='rtl'>• استفاده از <span dir='ltr'>`sys.exit()`</span> برای پایان با کد خروج مشخص</span> <br>
<span dir='rtl'>• مدیریت خطای اختصاصی با `try/except`</span> <br>
<span dir='rtl'>• ثبت پیام‌ها با `logging`</span> <br>
<span dir='rtl'>• تبدیل اشیای مدل به دیکشنری با list comprehension</span> <br>
<span dir='rtl'>• اتصال اجزای مستقل از طریق تابع اصلی</span> <br>
<span dir='rtl'>• استفاده از <span dir='ltr'>`if __name__ == '__main__'`</span> برای کنترل نقطه‌ی ورود</span>

</div>

**نتیجه‌ی معماری:** منطق اعتبارسنجی، جست‌وجوی DNS، قالب‌بندی و ذخیره‌سازی در بخش‌های جداگانه قرار گرفته‌اند و `cli.py` اجرای آن‌ها را مدیریت می‌کند. این ساختار، خوانایی و قابلیت نگهداری ابزار را بهبود می‌دهد و امکان توسعه‌ی هر بخش را با کمترین وابستگی به سایر بخش‌ها فراهم می‌سازد.
