# درس ۲۰: تست رابط خط فرمان (CLI) با Pytest

## ۱. هدف درس

در این درس یاد می‌گیریم چگونه رابط خط فرمان یک برنامه پایتون را آزمایش کنیم؛ بدون اینکه برای هر تست به سرور DNS واقعی متصل شویم یا فایل‌های جانبی پروژه را به‌طور ناخواسته تحت تأثیر قرار دهیم.

در پایان این درس می‌توانیم:

<div align='right' dir="rtl">

<span dir='rtl'>• آرگومان‌های خط فرمان را آزمایش کنیم.</span> <br>
<span dir='rtl'>• ورودی‌های نامعتبر را بررسی کنیم.</span> <br>
<span dir='rtl'>• وابستگی‌های برنامه را با `monkeypatch` جایگزین کنیم.</span> <br>
<span dir='rtl'>• مدیریت خطا و کد خروج برنامه را تست کنیم.</span> <br>
<span dir='rtl'>• تفاوت میان تست موفقیت و تست خطا را تشخیص دهیم.</span>

</div>

## کد کامل فایل تست

```python id="f9gjpz"
import pytest

from src.cli import create_parser, main
from src import DNSRecord
from src.exception import DNSTimeoutError


class FakeLogger:
    def info(self, *args, **kwargs):
        pass


def test_create_parser():
    parser = create_parser()

    args = parser.parse_args(['google.com', 'A'])
    assert args.domain == 'google.com'
    assert args.record_type == 'A'


def test_main_invalid_domain(monkeypatch):
    monkeypatch.setattr('src.cli.setup_logger', lambda *args, **kwargs: FakeLogger())
    monkeypatch.setattr('sys.argv', ['cli.py', '!!!', 'A'])
    with pytest.raises(SystemExit):
        main()


def test_main_invalid_record_type(monkeypatch):
    monkeypatch.setattr('src.cli.setup_logger', lambda *args, **kwargs: FakeLogger())
    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'BAD'])
    with pytest.raises(SystemExit):
        main()


def test_main_valid_arguments(monkeypatch):
    monkeypatch.setattr('src.cli.setup_logger', lambda *args, **kwargs: FakeLogger())
    monkeypatch.setattr('src.cli.build_dns_results', lambda *args, **kwargs: [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        )
    ])

    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'A'])
    main()


def test_main_handles_timeout(monkeypatch):
    monkeypatch.setattr('src.cli.setup_logger', lambda *args, **kwargs: FakeLogger())
    monkeypatch.setattr('src.cli.build_dns_results', lambda *args, **kwargs: (_ for _ in ()).throw(DNSTimeoutError()))
    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'MX'])
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 1
```

## ۲. وارد کردن وابستگی‌ها

```python
import pytest

from src.cli import create_parser, main
from src import DNSRecord
from src.exception import DNSTimeoutError
```

هر واردسازی نقش مشخصی دارد:

<div align='right' dir="rtl">

<span dir='rtl'>• `pytest`: ابزار اجرای تست‌ها و بررسی رفتار مورد انتظار.</span> <br>
<span dir='rtl'>• `create_parser`: تابع ساخت پارسر آرگومان‌های خط فرمان.</span> <br>
<span dir='rtl'>• `main`: تابع اصلی اجرای ابزار DNS Lookup.</span> <br>
<span dir='rtl'>• `DNSRecord`: مدل داده‌ای که برای شبیه‌سازی نتیجهٔ جست‌وجوی DNS استفاده می‌شود.</span> <br>
<span dir='rtl'>• `DNSTimeoutError`: استثنای اختصاصی پروژه برای پایان مهلت درخواست DNS.</span>

</div>

نکتهٔ معماری: این تست‌ها مستقیماً سراغ تابع اصلی CLI می‌روند؛ بنابراین می‌توانند تعامل میان اعتبارسنجی ورودی، اجرای عملیات، ثبت گزارش و مدیریت خطا را بررسی کنند.

## ۳. ساخت Logger آزمایشی

```python
class FakeLogger:
    def info(self, *args, **kwargs):
        pass
```

در پیاده‌سازی اصلی، تابع `setup_logger` یک Logger واقعی برمی‌گرداند که پیام‌ها را در فایل ثبت می‌کند. اما بیشتر تست‌های CLI به بررسی محتوای فایل گزارش نیاز ندارند.

به همین دلیل، یک Logger سادهٔ آزمایشی ساخته‌ایم.

### چرا از `FakeLogger` استفاده می‌کنیم؟

متد `info` در کد اصلی برای ثبت پیام‌هایی مانند شروع و پایان جست‌وجو فراخوانی می‌شود. کلاس `FakeLogger` همان متد را دارد، اما کاری انجام نمی‌دهد.

این جایگزینی چند مزیت دارد:

<p dir='rtl'>
• تست‌ها به ساخت فایل گزارش وابسته نمی‌شوند. <br>
• رفتار CLI را می‌توان مستقل‌تر بررسی کرد. <br>
• تمرکز تست روی موضوع اصلی باقی می‌ماند.
</p>

متد `pass` یعنی اجرای تابع عمداً هیچ عملی انجام نمی‌دهد.

## ۴. آزمایش ساخت پارسر

```python
def test_create_parser():
    parser = create_parser()

    args = parser.parse_args(['google.com', 'A'])
    assert args.domain == 'google.com'
    assert args.record_type == 'A'
```

این تست بررسی می‌کند که `create_parser` آرگومان‌های موقعیتی را درست دریافت و تفسیر می‌کند.

دستور زیر را در نظر بگیرید:

```bash
python -m src.cli google.com A
```

در این دستور:

<div align='right' dir="rtl">

<span dir='rtl'>• `google.com` دامنهٔ هدف است.</span> <br>
<span dir='rtl'>• `A` نوع رکورد DNS است.</span>

</div>

در تست، به‌جای اجرای فرمان واقعی در ترمینال، این دو مقدار مستقیماً به `parse_args` داده می‌شوند.

سپس با `assert` بررسی می‌کنیم که مقادیر استخراج‌شده درست باشند.

**نکته:** این تست پارسر را به‌صورت مستقیم بررسی می‌کند؛ هنوز تابع `main` را اجرا نکرده‌ایم.

## ۵. آزمایش دامنهٔ نامعتبر

```python
def test_main_invalid_domain(monkeypatch):
    monkeypatch.setattr(
        'src.cli.setup_logger',
        lambda *args, **kwargs: FakeLogger()
    )
    monkeypatch.setattr('sys.argv', ['cli.py', '!!!', 'A'])

    with pytest.raises(SystemExit):
        main()
```

این تست بررسی می‌کند که برنامه در صورت دریافت دامنهٔ نامعتبر از ادامهٔ اجرای عادی جلوگیری کند.

### تغییر موقت `sys.argv`

در اجرای واقعی، `argparse` آرگومان‌ها را از `sys.argv` دریافت می‌کند. در تست، این مقدار را تغییر می‌دهیم:

```python
monkeypatch.setattr('sys.argv', ['cli.py', '!!!', 'A'])
```

فهرست بالا به این معناست که نام برنامه `cli.py` است و آرگومان‌های کاربر شامل `!!!` و `A` هستند.

چون `!!!` یک دامنهٔ معتبر نیست، تابع `main` باید مسیر خطا را اجرا کند.

### چرا `pytest.raises(SystemExit)`؟

در کد CLI، ورودی نامعتبر با `sys.exit(1)` خاتمه پیدا می‌کند. پایتون این عملیات را با ایجاد استثنای `SystemExit` پیاده‌سازی می‌کند.

بنابراین:

```python
with pytest.raises(SystemExit):
    main()
```

یعنی انتظار داریم اجرای <span dir='ltr'>`main()`</span> به `SystemExit` منجر شود.

اگر چنین استثنایی ایجاد نشود، تست شکست می‌خورد.

### چرا Logger را هم جایگزین می‌کنیم؟

در مسیر دامنهٔ نامعتبر، برنامه قبل از ساخت Logger از ورودی عبور نمی‌کند. بااین‌حال، جایگزینی `setup_logger` در این تست یکسان‌سازی محیط تست‌ها را حفظ می‌کند و از ساخت Logger واقعی در صورت تغییرات آینده در ترتیب اجرای کد جلوگیری می‌کند.

## ۶. آزمایش نوع رکورد نامعتبر

```python
def test_main_invalid_record_type(monkeypatch):
    monkeypatch.setattr(
        'src.cli.setup_logger',
        lambda *args, **kwargs: FakeLogger()
    )
    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'BAD'])

    with pytest.raises(SystemExit):
        main()
```

این تست شبیه تست قبلی است، اما این بار دامنه معتبر و نوع رکورد نامعتبر است.

مقدار `BAD` در مجموعهٔ نوع رکوردهای پشتیبانی‌شده قرار ندارد؛ بنابراین تابع `validate_record_type` باید آن را رد کند.

این تست به‌طور مشخص بررسی می‌کند که:

<p dir='rtl'>
1. برنامه ورودی را از خط فرمان دریافت می‌کند. <br>
2. نوع رکورد را اعتبارسنجی می‌کند. <br>
3. در صورت نامعتبر بودن نوع رکورد، اجرای عادی را متوقف می‌کند.
</p>

این موضوع مهم است؛ چون اعتبارسنجی دامنه به‌تنهایی کافی نیست. همهٔ ورودی‌های مورد استفاده در عملیات DNS باید مطابق قواعد برنامه بررسی شوند.

## ۷. آزمایش اجرای موفق با ورودی معتبر

```python
def test_main_valid_arguments(monkeypatch):
    monkeypatch.setattr(
        'src.cli.setup_logger',
        lambda *args, **kwargs: FakeLogger()
    )
    monkeypatch.setattr(
        'src.cli.build_dns_results',
        lambda *args, **kwargs: [
            DNSRecord(
                domain='google.com',
                record_type='A',
                value='8.8.8.8',
            )
        ]
    )

    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'A'])
    main()
```

این تست مسیر اجرای موفق برنامه را بررسی می‌کند.

### جایگزینی تابع جست‌وجوی DNS

بخش مهم تست این است:

```python
monkeypatch.setattr(
    'src.cli.build_dns_results',
    lambda *args, **kwargs: [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        )
    ]
)
```

در کد اصلی، `build_dns_results` عملیات جست‌وجوی DNS را انجام می‌دهد و نتایج را به اشیای `DNSRecord` تبدیل می‌کند.

اما در تست، این تابع با یک تابع جایگزین می‌شود که همیشه یک نتیجهٔ مشخص برمی‌گرداند.

در نتیجه، تست برای اجرا شدن به پاسخ واقعی DNS وابسته نیست.

### چرا از `DNSRecord` استفاده می‌کنیم؟

چون تابع اصلی CLI انتظار دارد نتایج را با ساختار مدل پروژه دریافت کند. شیء آزمایشی نیز همان ساختار مورد انتظار را دارد:

<div align='right' dir="rtl">

<span dir='rtl'>• `domain`: دامنهٔ هدف</span> <br>
<span dir='rtl'>• `record_type`: نوع رکورد</span> <br>
<span dir='rtl'>• `value`: مقدار رکورد</span>

</div>

به این ترتیب، ادامهٔ اجرای `main` می‌تواند نتایج را قالب‌بندی و برای خروجی یا صادرکردن آماده کند.

### آیا این تست خروجی چاپ‌شده را بررسی می‌کند؟

خیر. این تست فقط <span dir='ltr'>`main()`</span> را اجرا می‌کند و انتظار دارد اجرای موفق بدون استثنای پیش‌بینی‌نشده به پایان برسد.

در این تست از `capsys` برای بررسی متن چاپ‌شده استفاده نشده و خروجی ترمینال مستقیماً مقایسه نمی‌شود. بنابراین نباید نتیجه بگیریم که متن خروجی نیز در همین تست به‌طور کامل اعتبارسنجی شده است.

## ۸. آزمایش مدیریت Timeout

```python
def test_main_handles_timeout(monkeypatch):
    monkeypatch.setattr(
        'src.cli.setup_logger',
        lambda *args, **kwargs: FakeLogger()
    )
    monkeypatch.setattr(
        'src.cli.build_dns_results',
        lambda *args, **kwargs: (
            _ for _ in ()
        ).throw(DNSTimeoutError())
    )
    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'MX'])

    with pytest.raises(SystemExit) as exc:
        main()

    assert exc.value.code == 1
```

این تست یکی از مهم‌ترین مسیرهای خطای CLI را بررسی می‌کند: زمانی که درخواست DNS با Timeout مواجه می‌شود.

### شبیه‌سازی Timeout

تابع جایگزین `build_dns_results` به‌جای برگرداندن نتیجه، استثنای `DNSTimeoutError` ایجاد می‌کند.

عبارت زیر شاید در نگاه اول غیرمعمول به نظر برسد:

```python
(_ for _ in ()).throw(DNSTimeoutError())
```

این عبارت از یک generator خالی استفاده می‌کند و با `throw` استثنا را ایجاد می‌کند. هدف آن این است که یک تابع جایگزین کوتاه برای `monkeypatch` بسازیم که هنگام فراخوانی، به‌جای بازگرداندن مقدار، استثنا پرتاب کند.

این روش معتبر است، هرچند برای خوانایی بیشتر می‌توان تابعی مستقل تعریف کرد:

```python
def raise_timeout(*args, **kwargs):
    raise DNSTimeoutError()
```

سپس آن را جایگزین کرد:

```python
monkeypatch.setattr(
    'src.cli.build_dns_results',
    raise_timeout
)
```

هر دو روش در این سناریو یک هدف دارند.

### بررسی کد خروج

در کد CLI، هنگام دریافت `DNSTimeoutError`، پیام خطا چاپ می‌شود و برنامه با `sys.exit(1)` خاتمه پیدا می‌کند.

در تست:

```python
with pytest.raises(SystemExit) as exc:
    main()
```

شیء `exc` اطلاعات استثنای رخ‌داده را نگه می‌دارد.

سپس:

```python
assert exc.value.code == 1
```

بررسی می‌کند که کد خروج دقیقاً `1` باشد؛ مقداری که معمولاً نشان‌دهندهٔ پایان برنامه به دلیل خطاست.

این تست فقط وجود `SystemExit` را بررسی نمی‌کند؛ بلکه کد خروج مورد انتظار را هم تأیید می‌کند.

## ۹. مفهوم مهم: `monkeypatch`

در این فایل، `monkeypatch` برای جایگزینی موقت وابستگی‌ها به کار رفته است.

<div align='center' dir="rtl">

| مورد جایگزین‌شده | هدف |
|---|---|
| `sys.argv` | شبیه‌سازی آرگومان‌های خط فرمان |
| `src.cli.setup_logger` |<span dir='rtl'> جلوگیری از وابستگی غیرضروری به Logger واقعی</span> |
| `src.cli.build_dns_results` |<span dir='rtl'> شبیه‌سازی نتیجهٔ موفق یا خطای DNS</span> |

</div>

تغییرهای ایجادشده با fixture استاندارد `monkeypatch` در پایان محدودهٔ تست بازگردانده می‌شوند. این موضوع به مستقل ماندن تست‌ها کمک می‌کند.

**قاعدهٔ کاربردی:** وقتی می‌خواهیم رفتار یک تابع را آزمایش کنیم، معمولاً بهتر است وابستگی‌های غیرمرتبط با همان رفتار را شبیه‌سازی کنیم تا تست سریع‌تر، قابل پیش‌بینی‌تر و مستقل‌تر باشد.

## ۱۰. جمع‌بندی تست‌های CLI

<div align='center' dir="rtl">

| نام تست | رفتار بررسی‌شده |
|---|---|
| `test_create_parser` | استخراج صحیح آرگومان‌های دامنه و نوع رکورد |
| `test_main_invalid_domain` | توقف اجرا در صورت نامعتبر بودن دامنه |
| `test_main_invalid_record_type` | توقف اجرا در صورت نامعتبر بودن نوع رکورد |
| `test_main_valid_arguments` | اجرای مسیر موفق با نتیجهٔ شبیه‌سازی‌شده |
| `test_main_handles_timeout` |<span dir='rtl'> مدیریت Timeout و خروج با کد `1`</span> |

</div>

این پنج تست، بخش‌های مهمی از رفتار رابط خط فرمان را پوشش می‌دهند: دریافت ورودی، اعتبارسنجی، اجرای موفق و مدیریت یک خطای مشخص.

البته این مجموعه همهٔ رفتارهای احتمالی CLI را بررسی نمی‌کند. برای نمونه، تست مستقلی برای متن دقیق خروجی، صادرکردن JSON یا CSV از طریق CLI، یا پیام خطای دقیق در همین فایل وجود ندارد. این موارد می‌توانند در صورت نیاز به پوشش بیشتر، به‌عنوان تمرین یا فرصت توسعه در نظر گرفته شوند.

## ۱۱. تمرین‌های پیشنهادی

۱. تابعی به نام `raise_timeout` بنویسید و از آن برای جایگزینی `build_dns_results` در تست Timeout استفاده کنید.

۲. با استفاده از `capsys`، بررسی کنید که اجرای موفق CLI نام دامنه و مقدار رکورد را در خروجی چاپ می‌کند.

۳. تستی اضافه کنید که بررسی کند اجرای CLI با دامنهٔ معتبر و نوع رکورد `BAD` با کد خروج `1` پایان می‌یابد.

۴. بررسی کنید آیا می‌توانید یک تست مستقل برای پیام `DNS query timed out` بنویسید؛ به‌طوری‌که هم پیام چاپ‌شده و هم کد خروج برنامه بررسی شوند.

## ۱۲. اجرای تست‌ها

برای اجرای همین فایل:

```bash
pytest tests/test_cli.py -v
```

برای اجرای تمام تست‌های پروژه:

```bash
pytest -v
```

اجرای کامل تست‌ها کمک می‌کند مطمئن شویم تغییر در یک بخش، رفتار بخش‌های دیگر را ناخواسته خراب نکرده است.

## نتیجهٔ درس

با این فایل دیدیم که تست رابط خط فرمان فقط به بررسی آرگومان‌ها محدود نیست؛ می‌توان با جایگزینی وابستگی‌ها، مسیر موفق و مسیرهای خطا را نیز بدون اجرای عملیات واقعی DNS بررسی کرد.

به این ترتیب، بررسی فایل‌های تست پروژهٔ DNS Lookup به پایان می‌رسد. گام بعدی، کنار هم گذاشتن آموخته‌ها و ترسیم معماری کلی پروژه است تا مشخص شود هر ماژول چه مسئولیتی دارد و داده‌ها چگونه از ورودی CLI تا نمایش و صادرکردن نتیجه حرکت می‌کنند.
