# ۱۷. تست‌نویسی برای خروجی JSON در پایتون

## هدف درس

در این درس، فایل `tests/test_exporter.py` را بررسی می‌کنیم تا یاد بگیریم چگونه عملیات فایل‌نویسی را با `pytest` آزمایش کنیم.

موضوعات اصلی:

<div align='right' dir="rtl">

<span dir='rtl'>• کار با فایل‌های موقت در تست‌ها</span> <br>
<span dir='rtl'>• آشنایی با fixture به نام `tmp_path`</span> <br>
<span dir='rtl'>• بررسی ایجاد شدن فایل</span> <br>
<span dir='rtl'>• خواندن JSON با <span dir='ltr'>`json.load()`</span></span> <br>
<span dir='rtl'>• مقایسهٔ دادهٔ اصلی با دادهٔ ذخیره‌شده</span> <br>
<span dir='rtl'>• نوشتن تست‌هایی که به فایل‌های واقعی پروژه وابسته نیستند</span>

</div>

## کد کامل فایل تست

```python id="f9gjpz"
import json

from src import export_json


def test_export_json_creates_file(tmp_path):
    output_file = (tmp_path / 'results.json')
    data = {
        'domain': 'google.com',
        'records': ['8.8.8.8'],
    }
    export_json(data, str(output_file))
    assert output_file.exists()


def test_export_json_content(tmp_path):
    output_file = (tmp_path / 'results.json')
    data = {
        'domain': 'google.com',
        'records': ['8.8.8.8', '8.8.4.4'],
    }
    export_json(data, str(output_file))
    with open(output_file, 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)
    assert loaded_data == data
```

## ۱. وارد کردن کتابخانه‌ها

```python id="p0f8y3"
import json

from src import export_json
```

در این فایل دو مورد استفاده می‌شوند:

<div align='right' dir="rtl">

<span dir='rtl'>• `json`: برای خواندن داده‌های JSON از فایل.</span> <br>
<span dir='rtl'>• `export_json`: تابع پروژه که داده‌ها را در یک فایل JSON ذخیره می‌کند.</span>

</div>

تابع <span dir='ltr'>`export_json()`</span> در فایل `src/exporter.py` تعریف شده است و از <span dir='ltr'>`json.dump()`</span> برای نوشتن داده‌ها استفاده می‌کند.

## ۲. آشنایی با `tmp_path`

هر دو تست این فایل، آرگومان `tmp_path` را دریافت می‌کنند:

```python id="m0eq2p"
def test_export_json_creates_file(tmp_path):
    ...
```

<div align='right' dir="rtl">

<span dir='rtl'>`tmp_path` یک fixture آماده در `pytest` است که مسیر یک پوشهٔ موقت و اختصاصی برای هر تست را فراهم می‌کند.</span>

</div>

با استفاده از این مسیر می‌توان فایل آزمایشی ساخت، بدون اینکه فایل‌های پروژه یا پوشهٔ کاری اصلی تغییر کنند.

برای مثال:

```python id="p4a7q9"
output_file = tmp_path / 'results.json'
```

عملگر `/` در اینجا برای ترکیب مسیر پوشه و نام فایل استفاده می‌شود. نتیجه یک شیء مسیر از نوع `pathlib.Path` است.

در ادامه:

```python id="k6f2s8"
str(output_file)
```

مسیر به رشته تبدیل می‌شود تا به تابع <span dir='ltr'>`export_json()`</span> داده شود.

این روش باعث می‌شود تست‌ها فایل‌های موقت خود را در اختیار داشته باشند و به مسیرهای ثابت روی سیستم وابسته نباشند.

## ۳. تست اول: بررسی ایجاد فایل

کد تست:

```python id="n3r7w1"
def test_export_json_creates_file(tmp_path):
    output_file = tmp_path / 'results.json'

    data = {
        'domain': 'google.com',
        'records': ['8.8.8.8'],
    }

    export_json(data, str(output_file))

    assert output_file.exists()
```

### مرحلهٔ اول: تعیین مسیر خروجی

```python id="c8m4v2"
output_file = tmp_path / 'results.json'
```

مسیر فایل خروجی با نام `results.json` در پوشهٔ موقت ساخته می‌شود.

### مرحلهٔ دوم: آماده‌سازی داده‌ها

```python id="r5t1j6"
data = {
    'domain': 'google.com',
    'records': ['8.8.8.8'],
}
```

یک دیکشنری ساده برای آزمایش آماده می‌شود. این داده شامل نام دامنه و یک لیست از مقادیر رکوردهاست.

این ساختار صرفاً دادهٔ آزمایشی همین تست است؛ تست بررسی نمی‌کند که این دیکشنری حتماً تمام فیلدهای موردنیاز خروجی نهایی برنامه را داشته باشد.

### مرحلهٔ سوم: اجرای تابع ذخیره‌سازی

```python id="h2k9x4"
export_json(data, str(output_file))
```

تابع، داده‌ها و مسیر مقصد را دریافت می‌کند و فایل را می‌نویسد.

### مرحلهٔ چهارم: بررسی وجود فایل

```python id="w7p3d5"
assert output_file.exists()
```

متد <span dir='ltr'>`exists()`</span> بررسی می‌کند که مسیر موردنظر وجود داشته باشد.

اگر فایل ایجاد نشده باشد، مقدار این عبارت `False` خواهد بود و تست شکست می‌خورد.

**نکته:** این تست فقط وجود فایل را بررسی می‌کند؛ به‌تنهایی ثابت نمی‌کند که محتوای فایل معتبر یا برابر با دادهٔ ورودی است. این مسئولیت تست دوم است.

## ۴. تست دوم: بررسی محتوای JSON

کد تست:

```python id="q4v8n2"
def test_export_json_content(tmp_path):
    output_file = tmp_path / 'results.json'

    data = {
        'domain': 'google.com',
        'records': ['8.8.8.8', '8.8.4.4'],
    }

    export_json(data, str(output_file))

    with open(output_file, 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)

    assert loaded_data == data
```

این تست علاوه بر ایجاد فایل، بررسی می‌کند که داده‌ها درست ذخیره و دوباره خوانده شوند.

### مرحلهٔ اول: ذخیره‌سازی داده‌ها

مانند تست اول، یک دیکشنری آماده می‌شود و با <span dir='ltr'>`export_json()`</sapn> در فایل نوشته می‌شود. این بار دو مقدار در لیست `records` وجود دارند.

### مرحلهٔ دوم: باز کردن فایل برای خواندن

```python id="t5c9m1"
with open(output_file, 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)
```

در این بخش:

<div align='right' dir="rtl">

<span dir='rtl'>• <span dir='ltr'>`open()`</span> فایل را باز می‌کند.</span> <br>
<span dir='rtl'>• `'r'` یعنی فایل برای خواندن باز می‌شود.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`encoding='utf-8'`</span> کدگذاری متن را مشخص می‌کند.</span> <br>
<span dir='rtl'>• `with` تضمین می‌کند که فایل پس از پایان بلوک به‌درستی بسته شود.</span> <br>
<span dir='rtl'>• `json.load(file)` محتوای JSON را می‌خواند و آن را به ساختارهای داده‌ای پایتون تبدیل می‌کند.</span>

</div>

برای مثال، یک شیء JSON به دیکشنری پایتون تبدیل می‌شود و آرایهٔ JSON به لیست پایتون تبدیل خواهد شد.

### مرحلهٔ سوم: مقایسهٔ داده‌ها

```python id="e6b2k4"
assert loaded_data == data
```

این assertion بررسی می‌کند که دادهٔ خوانده‌شده از فایل با دیکشنری اولیه برابر باشد.

در نتیجه، تست مواردی مانند حفظ کلیدها، مقادیر و ترتیب عناصر لیست را در چارچوب مقایسهٔ ساختارهای پایتون بررسی می‌کند. ترتیب کلیدهای دیکشنری برای برابری دیکشنری‌ها تعیین‌کننده نیست، اما ترتیب عناصر لیست اهمیت دارد.

اگر فایل معتبر نباشد و <span dir='ltr'>`json.load()`</span> نتواند آن را تجزیه کند، تست نیز با خطا متوقف می‌شود.

## ۵. ارتباط تست‌ها با `src/exporter.py`

پیاده‌سازی تابع پروژه چنین است:

```python id="u1d7h3"
import json


def export_json(data: dict, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
```

این تابع از دو عملیات اصلی استفاده می‌کند:

<div align='right' dir="rtl">

<span dir='rtl'>• `open(..., 'w')`: فایل را برای نوشتن باز می‌کند. اگر فایل از قبل وجود داشته باشد، محتوای قبلی آن جایگزین می‌شود.</span> <br>
<span dir='rtl'>• `json.dump(data, file, indent=4)`: داده‌ها را به قالب JSON تبدیل کرده و در فایل می‌نویسد. مقدار `indent=4` باعث می‌شود خروجی با تورفتگی چهار فاصله‌ای خواناتر باشد.</span>

</div>

تست‌های فعلی بررسی می‌کنند که فایل ساخته شود و داده‌های نوشته‌شده با داده‌های اولیه برابر باشند. آن‌ها به‌طور مستقل مقدار `indent` یا شیوهٔ دقیق فاصله‌گذاری JSON را بررسی نمی‌کنند.

## ۶. چرا فایل موقت بهتر از فایل ثابت است؟

اگر تست همیشه در مسیر ثابتی مانند `results.json` در پوشهٔ پروژه فایل بسازد، ممکن است:

<p dir='rtl'>
• فایل واقعی پروژه را بازنویسی کند. <br>
• با اجرای هم‌زمان تست‌ها تداخل ایجاد کند. <br>
• به وضعیت باقی‌مانده از اجرای قبلی وابسته شود.
</p>

استفاده از `tmp_path` این مشکلات را کاهش می‌دهد، زیرا هر تست مسیر موقت مخصوص خود را دریافت می‌کند.

## ۷. اجرای تست‌ها

برای اجرای تست‌های JSON exporter:

```powershell
pytest tests/test_exporter.py
```

برای مشاهدهٔ نتیجهٔ هر تست:

```powershell
pytest -v tests/test_exporter.py
```

برای اجرای کل مجموعهٔ تست‌ها:

```powershell
pytest
```

## ۸. تمرین‌های پیشنهادی

۱. تستی اضافه کنید که دیکشنری شامل چند کلید و چند لیست را ذخیره کند و سپس برابری دادهٔ خوانده‌شده را بررسی کند.

۲. تستی طراحی کنید که دو بار در یک مسیر فایل بنویسد و رفتار حالت `'w'` را بررسی کند.

۳. توضیح دهید چرا <span dir='ltr'>`json.load()`</span> برای خواندن از فایل استفاده می‌شود، اما <span dir='ltr'>`json.loads()`</span> برای دریافت یک رشتهٔ JSON کاربرد دارد.

۴. بررسی کنید اگر فایل خالی یا دارای JSON نامعتبر باشد، <span dir='ltr'>`json.load()`</span> چه رفتاری نشان می‌دهد.

۵. توضیح دهید چرا بررسی وجود فایل و بررسی محتوای فایل در دو تست جداگانه می‌توانند مفید باشند.

## جمع‌بندی

در این درس یاد گرفتیم که:

<div align='right' dir="rtl">

<span dir='rtl'>• `tmp_path` مسیر موقتی برای فایل‌های آزمایشی فراهم می‌کند.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`Path.exists()`</span> وجود فایل را بررسی می‌کند.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`json.load()`</span> محتوای JSON را از فایل به ساختارهای پایتون تبدیل می‌کند.</span> <br>
<span dir='rtl'>• مقایسهٔ دادهٔ خوانده‌شده با دادهٔ اولیه، صحت ذخیره‌سازی را بررسی می‌کند.</span> <br>
<span dir='rtl'>• تست‌های فایل‌نویسی بهتر است مستقل از فایل‌های واقعی پروژه باشند.</span>

</div>
