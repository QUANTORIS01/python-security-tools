# ۱۸. تست‌نویسی برای خروجی CSV در پایتون

## هدف درس

در این درس، فایل `tests/test_csv_exporter.py` را بررسی می‌کنیم تا یاد بگیریم چگونه خروجی CSV را با `pytest` آزمایش کنیم.

موضوعات اصلی:

<div align='right' dir="rtl">

<span dir='rtl'>• استفاده از `tmp_path` برای ساخت فایل موقت</span> <br>
<span dir='rtl'>• بررسی ایجاد شدن فایل CSV</span> <br>
<span dir='rtl'>• خواندن فایل با <span dir='ltr'>`csv.reader()`</span></span> <br>
<span dir='rtl'>• تبدیل ردیف‌های CSV به لیست‌های پایتون</span> <br>
<span dir='rtl'>• بررسی عنوان ستون‌ها، مقادیر و ترتیب ردیف‌ها</span> <br>
<span dir='rtl'>• تفاوت تست خروجی CSV با تست خروجی JSON</span>

</div>

## کد کامل فایل تست

```python id="f9gjpz"
import csv

from src import export_csv


def test_export_csv_creates_file(tmp_path):
    output_file = (tmp_path / 'results.csv')
    data = {
        'records': [{
            'domain': 'google.com',
            'record_type': 'A',
            'value': '8.8.8.8',
        }]
    }
    export_csv(data, str(output_file))
    assert output_file.exists()


def test_export_csv_content(tmp_path):
    output_file = (tmp_path / 'results.csv')
    data = {
        'records': [{
            'domain': 'google.com',
            'record_type': 'A',
            'value': '8.8.8.8',
        }, {
            'domain': 'google.com',
            'record_type': 'MX',
            'value': 'smtp.google.com',
        }]
    }
    export_csv(data, str(output_file))
    with open(output_file, 'r', newline='', encoding='utf-8') as file:
        rows = list(csv.reader(file))
    assert rows == [[
        'domain',
        'record_type',
        'value',
    ], [
        'google.com',
        'A',
        '8.8.8.8',
    ], [
        'google.com',
        'MX',
        'smtp.google.com',
    ], ]
```

## ۱. وارد کردن کتابخانه‌ها

```python
import csv

from src import export_csv
```

در این فایل از دو جزء استفاده می‌شود:

<div align='right' dir="rtl">

<span dir='rtl'>• `csv`: کتابخانهٔ استاندارد پایتون برای خواندن و نوشتن فایل‌های CSV.</span> <br>
<span dir='rtl'>• `export_csv`: تابع پروژه که داده‌ها را در قالب CSV ذخیره می‌کند.</span>

</div>

تابع <span dir='ltr'>`export_csv()`</span> در فایل `src/csv_exporter.py` قرار دارد و برای نوشتن داده‌ها از <span dir='ltr'>`csv.writer()`</span> استفاده می‌کند.

## ۲. تست اول: بررسی ایجاد فایل

کد تست:

```python
def test_export_csv_creates_file(tmp_path):
    output_file = tmp_path / 'results.csv'

    data = {
        'records': [{
            'domain': 'google.com',
            'record_type': 'A',
            'value': '8.8.8.8',
        }]
    }

    export_csv(data, str(output_file))

    assert output_file.exists()
```

### مرحلهٔ اول: تعیین مسیر فایل

```python
output_file = tmp_path / 'results.csv'
```

<div align='right' dir="rtl">

<span dir='rtl'>`tmp_path` یک fixture آماده در `pytest` است که مسیر پوشه‌ای موقت را فراهم می‌کند.</span>

</div>

با ترکیب آن با نام `results.csv`، مسیر فایل آزمایشی ساخته می‌شود. تبدیل مسیر به رشته با `str(output_file)` نیز آن را برای ارسال به تابع exporter آماده می‌کند.

### مرحلهٔ دوم: ساخت دادهٔ ورودی

```python
data = {
    'records': [{
        'domain': 'google.com',
        'record_type': 'A',
        'value': '8.8.8.8',
    }]
}
```

ساختار ورودی شامل کلید `records` است که مقدار آن یک لیست از دیکشنری‌هاست.

هر دیکشنری اطلاعات یک رکورد DNS را نگه می‌دارد:

<div align='right' dir="rtl">

<span dir='rtl'>• `domain`: نام دامنه</span> <br>
<span dir='rtl'>• `record_type`: نوع رکورد</span> <br>
<span dir='rtl'>• `value`: مقدار رکورد</span>

</div>

این ساختار با نحوهٔ خواندن داده‌ها در <span dir='ltr'>`export_csv()`</span> هماهنگ است.

### مرحلهٔ سوم: اجرای تابع و بررسی فایل

```python
export_csv(data, str(output_file))

assert output_file.exists()
```

تابع داده‌ها را در فایل ذخیره می‌کند و سپس <span dir='ltr'>`exists()`</span> بررسی می‌کند که فایل ایجاد شده باشد.

این تست فقط وجود فایل را بررسی می‌کند؛ برای اطمینان از صحت محتوای CSV به تست دوم نیاز داریم.

## ۳. تست دوم: بررسی محتوای CSV

کد تست:

```python
def test_export_csv_content(tmp_path):
    output_file = tmp_path / 'results.csv'

    data = {
        'records': [
            {
                'domain': 'google.com',
                'record_type': 'A',
                'value': '8.8.8.8',
            },
            {
                'domain': 'google.com',
                'record_type': 'MX',
                'value': 'smtp.google.com',
            },
        ]
    }

    export_csv(data, str(output_file))

    with open(
        output_file,
        'r',
        newline='',
        encoding='utf-8'
    ) as file:
        rows = list(csv.reader(file))

    assert rows == [
        ['domain', 'record_type', 'value'],
        ['google.com', 'A', '8.8.8.8'],
        ['google.com', 'MX', 'smtp.google.com'],
    ]
```

این تست فایل را ایجاد می‌کند، سپس آن را دوباره می‌خواند و تمام ردیف‌ها را با مقدار مورد انتظار مقایسه می‌کند.

### مرحلهٔ اول: نوشتن دو رکورد

در این تست، دو رکورد متفاوت وجود دارند:

<div align='right' dir="rtl">

<span dir='rtl'>• رکورد `A` با مقدار `8.8.8.8`</span> <br>
<span dir='rtl'>• رکورد `MX` با مقدار `smtp.google.com`</span>

</div>

وجود دو رکورد کمک می‌کند بررسی کنیم که exporter همهٔ رکوردها را ذخیره می‌کند، نه فقط اولین مورد را.

### مرحلهٔ دوم: باز کردن فایل

```python
with open(
    output_file,
    'r',
    newline='',
    encoding='utf-8'
) as file:
    rows = list(csv.reader(file))
```

در این قسمت:

<div align='right' dir="rtl">

<span dir='rtl'>• `'r'` فایل را برای خواندن باز می‌کند.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`newline=''`</span> روش توصیه‌شده برای باز کردن فایل CSV با ماژول `csv` است تا مدیریت خط‌های جدید به‌درستی انجام شود.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`encoding='utf-8'`</span> کدگذاری متن را مشخص می‌کند.</span> <br>
<span dir='rtl'>• `csv.reader(file)` ردیف‌های CSV را می‌خواند.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`list(...)`</span> تمام ردیف‌های خوانده‌شده را در یک لیست قرار می‌دهد.</span>

</div>

برای این دادهٔ نمونه، مقدار `rows` باید از سه لیست تشکیل شود:

<div align='right' dir="rtl">

<span dir='rtl'>1. عنوان ستون‌ها</span> <br>
<span dir='rtl'>2. ردیف رکورد `A`</span> <br>
<span dir='rtl'>3. ردیف رکورد `MX`</span>

</div>

### مرحلهٔ سوم: بررسی تمام ردیف‌ها

```python
assert rows == [
    ['domain', 'record_type', 'value'],
    ['google.com', 'A', '8.8.8.8'],
    ['google.com', 'MX', 'smtp.google.com'],
]
```

این assertion کل ساختار خوانده‌شده را با ساختار مورد انتظار مقایسه می‌کند.

در نتیجه، موارد زیر هم‌زمان بررسی می‌شوند:

<p dir='rtl'>
• عنوان ستون‌ها درست است. <br>
• مقادیر هر رکورد درست نوشته شده‌اند. <br>
• ترتیب ستون‌ها حفظ شده است. <br>
• هر دو رکورد در فایل وجود دارند. <br>
• ترتیب ردیف‌ها مطابق انتظار است.
</p>

این روش از بررسی وجود چند رشته در فایل دقیق‌تر است؛ زیرا ساختار CSV را به‌صورت ردیف و ستون بررسی می‌کند.

## ۴. ارتباط تست‌ها با `src/csv_exporter.py`

پیاده‌سازی exporter در پروژه به این شکل است:

```python
import csv


def export_csv(data: dict, filename: str) -> None:
    with open(
        filename,
        'w',
        newline='',
        encoding='utf-8'
    ) as file:
        writer = csv.writer(file)
        writer.writerow(['domain', 'record_type', 'value'])

        for item in data['records']:
            writer.writerow([
                item['domain'],
                item['record_type'],
                item['value'],
            ])
```

این تابع چند مرحله دارد:

<div align='right' dir="rtl">

<span dir='rtl'>1. فایل را برای نوشتن باز می‌کند.</span> <br>
<span dir='rtl'>2. یک شیء `csv.writer` می‌سازد.</span> <br>
<span dir='rtl'>3. عنوان ستون‌ها را با <span dir='ltr'>`writer.writerow()`</span> می‌نویسد.</span> <br>
<span dir='rtl'>4. روی رکوردهای موجود در `data['records']` پیمایش می‌کند.</span> <br>
<span dir='rtl'>5. برای هر رکورد، یک ردیف CSV می‌نویسد.</span>

</div>

تست دوم بررسی می‌کند که خروجی این مراحل، پس از خواندن مجدد فایل، با دادهٔ مورد انتظار برابر باشد.

## ۵. چرا <span dir='ltr'>`csv.reader()`</span> بهتر از بررسی متن خام است؟

<p dir='rtl'>
CSV یک قالب متنی برای نمایش داده‌های جدولی است. اگر فایل را به‌صورت متن خام بخوانیم، باید خودمان جداکننده‌ها، خط‌های جدید و موارد خاص را مدیریت کنیم.
</p>

استفاده از <span dir='ltr'>`csv.reader()`</span> به پایتون اجازه می‌دهد ردیف‌ها و ستون‌ها را بر اساس قواعد CSV تجزیه کند.

برای مثال، این خروجی:

```text
domain,record_type,value
google.com,A,8.8.8.8
google.com,MX,smtp.google.com
```

به یک ساختار شبیه این تبدیل می‌شود:

```python
[
    ['domain', 'record_type', 'value'],
    ['google.com', 'A', '8.8.8.8'],
    ['google.com', 'MX', 'smtp.google.com'],
]
```

این ساختار را می‌توان به‌سادگی با `assert` مقایسه کرد.

## ۶. تفاوت تست CSV و JSON

در تست‌های JSON، فایل با <span dir='ltr'>`json.load()`</span> به دیکشنری‌ها و لیست‌های پایتون تبدیل می‌شود و سپس با دادهٔ اولیه مقایسه می‌شود.

در تست‌های CSV، فایل با <span dir='ltr'>`csv.reader()`</span> به لیستی از ردیف‌ها تبدیل می‌شود.

<div align='center' dir="rtl">

| ویژگی | JSON | CSV |
|---|---|---|
| روش خواندن در تست | <span dir='ltr'>`json.load()`</span> | <span dir='ltr'>`csv.reader()`</span> |
| ساختار معمول | دیکشنری‌ها و لیست‌ها | ردیف‌ها و ستون‌ها |
| تست فعلی محتوا | مقایسهٔ دیکشنری‌ها | مقایسهٔ لیست ردیف‌ها |
| عنوان ستون | وابسته به ساختار داده | ردیف اول فایل |

</div>

هر دو روش بررسی می‌کنند که داده‌ها بعد از ذخیره‌سازی قابل‌بازیابی و مطابق انتظار باشند، اما ساختار خروجی و ابزار خواندن آن‌ها متفاوت است.

## ۷. اجرای تست‌ها

برای اجرای تست‌های CSV exporter:

```powershell
pytest tests/test_csv_exporter.py
```

برای مشاهدهٔ نتیجهٔ هر تست:

```powershell
pytest -v tests/test_csv_exporter.py
```

برای اجرای تمام تست‌های پروژه:

```powershell
pytest
```

## ۸. تمرین‌های پیشنهادی

۱. تستی اضافه کنید که دو رکورد از دو دامنهٔ متفاوت داشته باشد و هر دو را در خروجی بررسی کند.

۲. یک تست بنویسید که فقط عنوان ستون‌های فایل CSV را بررسی کند.

۳. توضیح دهید چرا `list(csv.reader(file))` در این تست استفاده شده است.

۴. بررسی کنید اگر ترتیب ستون‌های خروجی تغییر کند، آیا تست فعلی شکست می‌خورد؟ دلیل خود را توضیح دهید.

۵. یک تست برای لیست خالی رکوردها طراحی کنید. بر اساس پیاده‌سازی فعلی، فایل باید شامل چه ردیفی باشد؟

## جمع‌بندی

در این درس یاد گرفتیم که:

<div align='right' dir="rtl">

<span dir='rtl'>• `tmp_path` برای ساخت فایل‌های موقت در تست‌ها کاربرد دارد.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`exists()`</span> ایجاد شدن فایل را بررسی می‌کند.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`csv.reader()`</span> محتوای CSV را به ردیف‌ها و ستون‌های قابل‌استفاده در پایتون تبدیل می‌کند.</span> <br>
<span dir='rtl'>• مقایسهٔ کامل `rows`، عنوان ستون‌ها، مقادیر و ترتیب ردیف‌ها را بررسی می‌کند.</span> <br>
<span dir='rtl'>• تست ایجاد فایل و تست محتوای آن دو مسئولیت متفاوت دارند.</span>

</div>
