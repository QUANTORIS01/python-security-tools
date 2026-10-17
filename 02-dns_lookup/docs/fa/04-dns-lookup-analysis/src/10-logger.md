# درس دهم: ثبت رویدادها و مدیریت لاگ در پایتون

**فایل مورد بررسی:** `src/logger.py`

## ۱. هدف درس

در این درس یاد می‌گیریم چگونه با ماژول استاندارد `logging` در پایتون، یک سیستم ثبت رویداد برای برنامه ایجاد کنیم.

لاگ‌ها می‌توانند برای ثبت اتفاق‌های مهم برنامه، بررسی خطاها و عیب‌یابی رفتار ابزار مفید باشند. در یک ابزار شبکه مانند DNS Lookup، ثبت مناسب رویدادها به بررسی مشکلاتی مانند خطاهای عملیاتی یا شکست درخواست‌ها کمک می‌کند؛ البته این تابع به‌تنهایی رویدادها را ثبت نمی‌کند، بلکه logger را برای استفاده در بخش‌های دیگر برنامه آماده می‌سازد.

## ۲. کد کامل فایل

```python
import logging


def setup_logger(filename: str) -> logging.Logger:
    """
    Configure and return a file logger.
    """
    logger = logging.getLogger('dns_lookup')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            if handler.baseFilename == filename:
                return logger
    handler = logging.FileHandler(filename, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
```

## ۳. وارد کردن ماژول `logging`

```python
import logging
```

ماژول `logging` بخشی از کتابخانه‌ی استاندارد پایتون است و برای ثبت پیام‌های برنامه استفاده می‌شود.

پیام‌های لاگ می‌توانند سطح‌های مختلفی داشته باشند؛ برای مثال:

<div align='center' dir="rtl">

| سطح | کاربرد |
|---|---|
| `DEBUG` | اطلاعات جزئی برای عیب‌یابی |
| `INFO` | رویدادهای عادی و مهم برنامه |
| `WARNING` | شرایط غیرعادی که لزوماً اجرای برنامه را متوقف نمی‌کنند |
| `ERROR` | خطاهایی که باعث شکست یک عملیات شده‌اند |
| `CRITICAL` | مشکلات بسیار جدی |

</div>

انتخاب سطح مناسب باعث می‌شود پیام‌های ثبت‌شده متناسب با نیاز برنامه باشند.

## ۴. تعریف تابع `setup_logger`

```python
def setup_logger(filename: str) -> logging.Logger:
```

این تابع نام یا مسیر فایل لاگ را دریافت می‌کند و یک شیء از نوع `logging.Logger` برمی‌گرداند.

<div align='right' dir="rtl">

<span dir='rtl'>• `filename: str` مشخص می‌کند که ورودی مورد انتظار یک رشته است.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`-> logging.Logger`</span> نوع شیء خروجی را نشان می‌دهد.</span>

</div>

این تابع برای تنظیم logger طراحی شده است؛ ثبت پیام‌ها معمولاً پس از دریافت logger و با متدهایی مانند <span dir='ltr'>`logger.info()`</span> یا <span dir='ltr'>`logger.error()`</span> انجام می‌شود.

## ۵. دریافت logger با نام مشخص

```python
logger = logging.getLogger('dns_lookup')
```

تابع <span dir='ltr'>`logging.getLogger()`</span> یک logger با نام مشخص دریافت می‌کند.

در این پروژه، نام logger برابر با `dns_lookup` است. فراخوانی دوباره‌ی <span dir='ltr'>`getLogger()`</span> با همین نام، در همان محیط اجرای پایتون معمولاً همان شیء logger را برمی‌گرداند؛ یعنی هر بار logger کاملاً جدیدی ساخته نمی‌شود.

این ویژگی برای برنامه‌ای که چند بخش آن از یک logger مشترک استفاده می‌کنند مفید است.

## ۶. تعیین سطح ثبت پیام‌ها

```python
logger.setLevel(logging.INFO)
```

این خط سطح logger را روی `INFO` تنظیم می‌کند.

در نتیجه، پیام‌هایی با سطح `INFO` و سطوح بالاتر مانند `WARNING`، `ERROR` و `CRITICAL` از فیلتر سطح logger عبور می‌کنند. پیام‌های `DEBUG` در این تنظیم معمولاً ثبت نمی‌شوند.

نکته‌ی مهم این است که سطح logger و سطح handler دو تنظیم جداگانه‌اند. در این کد سطح logger صریحاً تنظیم شده، اما برای handler سطح مستقلی تعیین نشده است؛ بنابراین سطح handler از تنظیم پیش‌فرض خودش پیروی می‌کند.

## ۷. جلوگیری از انتشار پیام به logger والد

```python
logger.propagate = False
```

به‌طور پیش‌فرض، پیام‌های یک logger نام‌دار می‌توانند پس از عبور از handlerهای خودش به loggerهای والد نیز منتقل شوند.

با تنظیم `propagate = False`، این انتقال متوقف می‌شود.

چرا این کار مفید است؟

اگر logger هم handler اختصاصی خودش را داشته باشد و هم پیام‌هایش به handlerهای والد منتقل شوند، ممکن است یک پیام بیش از یک بار نمایش داده یا ثبت شود.

این تنظیم به کنترل مسیر انتشار پیام‌ها کمک می‌کند؛ به‌خصوص وقتی برنامه می‌خواهد خروجی لاگ را در یک فایل مشخص نگه دارد.

## ۸. بررسی handlerهای موجود

```python
for handler in logger.handlers:
    if isinstance(handler, logging.FileHandler):
        if handler.baseFilename == filename:
            return logger
```

این بخش یکی از نکته‌های مهم پیاده‌سازی ماست.

<div align='right' dir="rtl">

### `logger.handlers`

</div>

هر logger می‌تواند یک یا چند handler داشته باشد. handler مشخص می‌کند پیام لاگ کجا ارسال شود؛ برای مثال، به فایل یا کنسول.

<div align='right' dir="rtl">

### <span dir='ltr'>`isinstance()`</span>

</div>

```python
isinstance(handler, logging.FileHandler)
```

این عبارت بررسی می‌کند که آیا handler فعلی از نوع `logging.FileHandler` است یا خیر.

<div align='right' dir="rtl">

<span dir='rtl'>`FileHandler` نوعی handler است که پیام‌های لاگ را در فایل می‌نویسد.</span>

</div>

<div align='right' dir="rtl">

### `handler.baseFilename`

</div>

این ویژگی مسیر فایل مرتبط با `FileHandler` را مشخص می‌کند.

کد ما مسیر handler موجود را با `filename` مقایسه می‌کند. اگر یک `FileHandler` برای همان مسیر از قبل وجود داشته باشد، تابع فوراً همان logger را برمی‌گرداند:

```python
return logger
```

در نتیجه، برای همان logger و همان مسیر فایل، یک handler تکراری اضافه نمی‌شود.

### چرا این بررسی اهمیت دارد؟

فرض کنیم تابع چند بار با نام یکسان فراخوانی شود:

```python
logger = setup_logger('dns_lookup.log')
logger = setup_logger('dns_lookup.log')
```

بدون بررسی handlerهای موجود، هر فراخوانی ممکن بود یک handler جدید اضافه کند. در چنین وضعیتی احتمال دارد یک پیام چند بار در یک فایل نوشته شود.

منطق فعلی ما این تکرار را برای handlerهای فایلی با مسیر یکسان کنترل می‌کند.

**نکته‌ی فنی:** مقایسه‌ی `baseFilename` با `filename` به شکل مستقیم انجام می‌شود. مسیرهای متفاوتی که به یک فایل اشاره می‌کنند، مانند مسیر نسبی و مسیر مطلق، ممکن است دقیقاً برابر نباشند. اگر برنامه در آینده با مسیرهای متنوع کار کند، می‌توان مقایسه‌ی مسیرهای نرمال‌شده را در نظر گرفت.

## ۹. ساختن FileHandler

```python
handler = logging.FileHandler(filename, encoding='utf-8')
```

اگر handler فایلی با مسیر موردنظر پیدا نشود، یک `FileHandler` جدید ساخته می‌شود.

دو آرگومان مهم این خط عبارت‌اند از:

<div align='right' dir="rtl">

<span dir='rtl'>• `filename`: مسیر فایل مقصد.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`encoding='utf-8'`</span>: رمزگذاری مورد استفاده برای نوشتن متن.</span>

</div>

با UTF-8 می‌توان پیام‌های متنی، از جمله متن‌های فارسی، را در فایل لاگ ذخیره کرد.

نکته: `FileHandler` به‌طور پیش‌فرض فایل را در حالت افزودن (`append`) باز می‌کند. بنابراین ایجاد handler جدید برای فایلی موجود، معمولاً محتوای قبلی آن را پاک نمی‌کند؛ پیام‌های جدید به انتهای فایل اضافه می‌شوند.

## ۱۰. تعریف قالب پیام‌های لاگ

```python
formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(message)s'
)
```

<div align='right' dir="rtl">

<span dir='rtl'>`logging.Formatter` قالب نمایش هر پیام لاگ را مشخص می‌کند.</span>

</div>

در این پروژه، قالب از سه بخش تشکیل شده است:

<div align='right' dir="rtl">

<span dir='rtl'>• <span dir='ltr'>`%(asctime)s`</span>: زمان ثبت پیام.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`%(levelname)s`</span>: سطح پیام، مانند `INFO` یا `ERROR`.</span> <br>
<span dir='rtl'>• <span dir='ltr'>`%(message)s`</span>: متن اصلی پیام.</span>

</div>

برای مثال، اگر پیامی با سطح `INFO` و متن `DNS lookup completed` ثبت شود، خروجی می‌تواند شبیه این باشد:

```text
2026-10-13 10:30:00,123 INFO DNS lookup completed
```

زمان و شکل دقیق آن به زمان اجرا و تنظیمات formatter بستگی دارد؛ این خط صرفاً یک نمونه‌ی فرضی از قالب خروجی است.

وجود زمان، سطح و متن پیام کمک می‌کند رویدادها هنگام بررسی فایل لاگ قابل تشخیص باشند.

## ۱۱. اتصال formatter به handler

```python
handler.setFormatter(formatter)
```

در این مرحله، قالبی که تعریف کرده‌ایم به handler متصل می‌شود.

در نتیجه، پیام‌هایی که handler دریافت می‌کند با همین قالب آماده‌ی ثبت خواهند شد.

تفکیک formatter از handler مزیت طراحی مشخصی دارد: مقصد پیام و نحوه‌ی قالب‌بندی آن دو مسئولیت جدا هستند.

## ۱۲. افزودن handler به logger

```python
logger.addHandler(handler)
```

ساختن handler به‌تنهایی کافی نیست؛ باید آن را به logger متصل کنیم.

با <span dir='ltr'>`addHandler()`</span> مشخص می‌کنیم که logger از این handler برای ارسال پیام‌ها استفاده کند.

پس از این مرحله، پیام‌هایی که از فیلتر سطح عبور کنند می‌توانند از طریق handler به فایل هدایت شوند.

## ۱۳. برگرداندن logger

```python
return logger
```

در پایان، تابع logger تنظیم‌شده را برمی‌گرداند.

بخش‌های دیگر برنامه می‌توانند این شیء را دریافت کرده و پیام‌های خود را ثبت کنند. برای مثال:

```python
logger = setup_logger('dns_lookup.log')

logger.info('DNS lookup started')
logger.warning('No DNS records returned')
logger.error('DNS lookup failed')
```

این قطعه نمونه‌ای از نحوه‌ی استفاده از تابع است؛ متن پیام‌ها صرفاً برای نمایش رفتار logger انتخاب شده‌اند.

## ۱۴. چند نکته درباره‌ی رفتار واقعی این پیاده‌سازی

برای درک دقیق کد، باید میان «آماده‌سازی logger» و «ثبت یک رویداد» تفاوت قائل شویم.

تابع <span dir='ltr'>`setup_logger()`</sapn>:

<p dir='rtl'>
1. logger نام‌دار را دریافت می‌کند. <br>
2. سطح ثبت پیام را تنظیم می‌کند. <br>
3. انتشار به logger والد را غیرفعال می‌کند. <br>
4. وجود handler فایلی برای مسیر داده‌شده را بررسی می‌کند. <br>
5. در صورت نیاز، handler و formatter را می‌سازد و به logger متصل می‌کند. <br>
6. logger را برمی‌گرداند.
</p>

خود تابع هیچ پیام لاگی تولید نمی‌کند؛ ثبت پیام به فراخوانی‌هایی مانند <span dir='ltr'>`logger.info()`</sapn> یا <span dir='ltr'>`logger.error()`</sapn> نیاز دارد.

همچنین، این تابع handlerهای فایلی با مسیرهای متفاوت را حذف نمی‌کند. اگر logger قبلاً handler فایلی برای مسیر دیگری داشته باشد، handler جدید نیز ممکن است به آن اضافه شود. این رفتار می‌تواند برای ثبت در چند فایل مفید باشد، اما هنگام طراحی سیاست لاگ‌گیری باید آگاهانه در نظر گرفته شود.

## ۱۵. تمرین‌های آموزشی

### تمرین اول: بررسی سطح لاگ

یک logger با این تابع بسازید و پیام‌هایی با سطوح `DEBUG`، `INFO` و `ERROR` ثبت کنید.

بررسی کنید کدام پیام‌ها با تنظیم فعلی از فیلتر سطح logger عبور می‌کنند.

### تمرین دوم: بررسی جلوگیری از handler تکراری

تابع را دو بار با یک نام فایل یکسان فراخوانی کنید.

<p dir='rtl'>
• آیا در فراخوانی دوم handler فایلی جدیدی اضافه می‌شود؟ <br>
• چه بخشی از کد از این اتفاق جلوگیری می‌کند؟
</p>

### تمرین سوم: بررسی مسیرهای متفاوت

تابع را با دو نام فایل متفاوت فراخوانی کنید و سپس یک پیام ثبت کنید.

بررسی کنید که با توجه به handlerهای متصل به logger مشترک، پیام در کدام فایل‌ها ثبت می‌شود.

### تمرین چهارم: تغییر قالب

قالب formatter را طوری تغییر دهید که سطح پیام و متن آن با یک جداکننده‌ی واضح نمایش داده شوند.

سپس یک پیام `INFO` ثبت کنید و تفاوت خروجی را بررسی کنید.

## ۱۶. جمع‌بندی

در این درس با اجزای مهم ماژول `logging` آشنا شدیم:

<div align='right' dir="rtl">

<span dir='rtl'>• <span dir='ltr'>`getLogger()`</span> برای دریافت logger نام‌دار</span> <br>
<span dir='rtl'>• <span dir='ltr'>`setLevel()`</span> برای تعیین حداقل سطح پیام</span> <br>
<span dir='rtl'>• `propagate` برای کنترل انتشار پیام به loggerهای والد</span> <br>
<span dir='rtl'>• `FileHandler` برای نوشتن پیام‌ها در فایل</span> <br>
<span dir='rtl'>• `Formatter` برای تعیین قالب خروجی</span> <br>
<span dir='rtl'>• <span dir='ltr'>`addHandler()`</span> برای اتصال مقصد ثبت پیام به logger</span>

</div>

در پروژه‌ی DNS Lookup، فایل `logger.py` مسئول آماده‌سازی زیرساخت ثبت رویدادهاست. بررسی handlerهای موجود نیز کمک می‌کند فراخوانی مکرر تابع با یک مسیر یکسان، handler فایلی تکراری ایجاد نکند.
