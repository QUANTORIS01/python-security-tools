# فصل چهارم: تحلیل کد پروژه DNS Lookup

## درس ۶: ساخت نتایج ساخت‌یافته با پایتون

### ۱. هدف درس

در این درس، فایل `src/results.py` را بررسی می‌کنیم؛ بخشی از ابزار DNS Lookup که پاسخ‌های خام دریافت‌شده از resolver را به ساختاری منظم و قابل استفاده در ادامه برنامه تبدیل می‌کند.

در پایان این درس، با این مفاهیم آشنا خواهید شد:

<div align='right' dir='rtl'>

<span dir='rtl'>• استفاده از تابع برای ترکیب منطق چند بخش پروژه</span> <br>
<span dir='rtl'>• تبدیل رشته‌های پاسخ DNS به اشیای مدل `DNSRecord`</span> <br>
<span dir='rtl'>• کاربرد List Comprehension</span> <br>
<span dir='rtl'>• اهمیت یکپارچگی ساختار داده‌ها در معماری نرم‌افزار</span>

</div>

### ۲. کد فایل `results.py`

```python
from src import DNSRecord, lookup_record


def build_dns_results(domain: str, record_type: str) -> list[DNSRecord]:
    """
    Build structured DNS results.
    """
    values = lookup_record(domain, record_type)
    return [
        DNSRecord(
            domain=domain,
            record_type=record_type,
            value=value,
        )
        for value in values
    ]
```

این فایل دو نام را از بسته `src` وارد می‌کند:

<div align='right' dir='rtl'>

<span dir='rtl'>• `DNSRecord`: مدل داده‌ای که در فایل `models.py` تعریف کرده‌ایم.</span> <br>
<span dir='rtl'>• `lookup_record`: تابعی که در فایل `resolver.py` درخواست DNS را اجرا می‌کند و پاسخ‌ها را به شکل رشته برمی‌گرداند.</span>

</div>

به این ترتیب، `results.py` بین اجرای درخواست DNS و ساخت خروجی ساخت‌یافته قرار می‌گیرد.

### ۳. اجرای درخواست و دریافت مقادیر

در ابتدای تابع:

```python
values = lookup_record(domain, record_type)
```

تابع <span dir='ltr'>`lookup_record()`</span> با استفاده از دامنه و نوع رکورد، درخواست DNS را اجرا می‌کند.

بر اساس پیاده‌سازی resolver، پاسخ‌های موفق به شکل `list[str]` برگردانده می‌شوند. در وضعیت‌هایی مانند نبودن دامنه، نبودن پاسخ یا در دسترس نبودن پاسخ‌دهنده‌های نام، resolver می‌تواند فهرست خالی برگرداند. خطای پایان مهلت درخواست نیز به شکل `DNSTimeoutError` منتقل می‌شود.

بنابراین، <span dir='ltr'>`build_dns_results()`</span> لازم نیست خودش جزئیات اجرای درخواست DNS را مدیریت کند؛ این مسئولیت در resolver قرار دارد.

### ۴. تبدیل پاسخ‌ها به اشیای `DNSRecord`

بخش اصلی تابع:

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

این عبارت از **List Comprehension** برای ساخت فهرست استفاده می‌کند.

برای هر مقدار موجود در `values`، یک شیء `DNSRecord` ساخته می‌شود. هر شیء سه فیلد دارد:

<div align='right' dir='rtl'>

<span dir='rtl'>• `domain`: دامنه‌ای که درخواست برای آن انجام شده است.</span> <br>
<span dir='rtl'>• `record_type`: نوع رکورد درخواست‌شده.</span> <br>
<span dir='rtl'>• `value`: یکی از مقادیر دریافت‌شده از resolver.</span>

</div>

برای مثال، فرض کنید resolver دو مقدار زیر را برگرداند:

```python
values = ["192.0.2.10", "192.0.2.11"]
```

تابع نتیجه‌ای معادل این فهرست می‌سازد:

```python
[
    DNSRecord(
        domain="example.com",
        record_type="A",
        value="192.0.2.10",
    ),
    DNSRecord(
        domain="example.com",
        record_type="A",
        value="192.0.2.11",
    ),
]
```

این مقادیر صرفاً نمونه آموزشی هستند؛ هدف، نمایش شکل خروجی است.

### ۵. چرا از مدل داده استفاده می‌کنیم؟

اگر پاسخ‌ها فقط به‌صورت رشته منتقل شوند، برای فهمیدن اینکه هر مقدار به کدام دامنه و نوع رکورد تعلق دارد، باید اطلاعات دیگری نیز در دسترس باشد.

مدل `DNSRecord` این اطلاعات را کنار مقدار رکورد نگه می‌دارد. در نتیجه، هر نتیجه به‌صورت یک شیء مشخص نمایش داده می‌شود.

برای مثال، دسترسی به مقدار رکورد به شکل زیر انجام می‌شود:

```python
record.value
```

و دامنه و نوع رکورد نیز در دسترس هستند:

```python
record.domain
record.record_type
```

این ساختار، مصرف داده‌ها را در بخش‌های دیگر ابزار ساده‌تر می‌کند؛ به‌ویژه زمانی که قرار است نتایج قالب‌بندی یا صادر شوند.

### ۶. اگر resolver نتیجه‌ای نداشته باشد چه می‌شود؟

اگر <span dir='ltr'>`lookup_record()`</span> یک فهرست خالی برگرداند، حلقه در List Comprehension هیچ بار اجرا نمی‌شود و <span dir='ltr'>`build_dns_results()`</span> نیز فهرست خالی برمی‌گرداند.

از نظر رفتاری:

```python
values = []
results = [
    DNSRecord(domain="example.com", record_type="A", value=value)
    for value in values
]

print(results)
```

خروجی:

```text
[]
```

این رفتار باعث می‌شود قرارداد خروجی تابع ثابت بماند: در حالت معمول، نتیجه یک فهرست از اشیای `DNSRecord` است؛ حتی اگر هیچ رکوردی پیدا نشده باشد.

در مقابل، اگر resolver خطایی مانند `DNSTimeoutError` ایجاد کند، این تابع آن را نمی‌گیرد؛ بنابراین خطا به فراخواننده بالاتر منتقل می‌شود تا در لایه مناسب مدیریت شود.

### ۷. جایگاه `results.py` در معماری ابزار

جریان داده‌ای که در این بخش از ابزار پیاده‌سازی کرده‌ایم، به‌صورت زیر است:

<div align='center' dir='rtl'>

```text
ورودی دامنه و نوع رکورد
          |
          v
lookup_record()
          |
          v
فهرست رشته‌های پاسخ DNS
          |
          v
build_dns_results()
          |
          v
فهرست اشیای DNSRecord
```

</div>

هر بخش مسئولیت مشخصی دارد:

<div align='right' dir='rtl'>

<span dir='rtl'>• `resolver.py` درخواست DNS را اجرا می‌کند.</span> <br>
<span dir='rtl'>• `models.py` ساختار هر رکورد را تعریف می‌کند.</span> <br>
<span dir='rtl'>• `results.py` پاسخ‌های resolver را در قالب مدل پروژه سازمان‌دهی می‌کند.</span>

</div>

این جداسازی مسئولیت‌ها باعث می‌شود هر بخش منطق ساده‌تری داشته باشد و تغییرات در یک لایه، لزوماً نیازمند بازنویسی تمام بخش‌های دیگر نباشد.

### ۸. تمرین‌های آموزشی

**تمرین اول — ساخت خروجی**

فرض کنید resolver سه مقدار رشته‌ای برگردانده است. چند شیء `DNSRecord` توسط <span dir='ltr'>`build_dns_results()`</span> ساخته می‌شود؟ دلیل خود را توضیح دهید.

**تمرین دوم — فهرست خالی**

اگر هیچ رکوردی برگردانده نشود، خروجی تابع چه خواهد بود؟ توضیح دهید چرا.

**تمرین سوم — بازنویسی با حلقه**

بخش List Comprehension را با یک حلقه `for` معمولی بازنویسی کنید و نتیجه را با نسخه اصلی مقایسه کنید.

**تمرین چهارم — مسئولیت لایه‌ها**

توضیح دهید چرا تبدیل پاسخ‌های رشته‌ای به اشیای `DNSRecord` در این تابع انجام شده است، نه در خود <span dir='ltr'>`lookup_record()`</span>.

### ۹. جمع‌بندی

فایل `results.py` نقش واسط میان پاسخ‌های resolver و مدل داده‌ای پروژه را بر عهده دارد.

در این درس دیدیم که تابع <span dir='ltr'>`build_dns_results()`</span>:

<div align='right' dir='rtl'>

<span dir='rtl'>• درخواست DNS را از طریق <span dir='ltr'>`lookup_record()`</span> اجرا می‌کند.</span> <br>
<span dir='rtl'>• مقادیر پاسخ را دریافت می‌کند.</span> <br>
<span dir='rtl'>• برای هر مقدار، یک شیء `DNSRecord` می‌سازد.</span> <br>
<span dir='rtl'>• در صورت دریافت فهرست خالی، فهرست خالی برمی‌گرداند.</span> <br>
<span dir='rtl'>• خطاهایی را که از resolver منتقل می‌شوند، در این لایه مدیریت نمی‌کند.</span>

</div>

این طراحی کمک می‌کند داده‌های حاصل از جست‌وجوی DNS با ساختاری منظم در اختیار بخش‌های بعدی ابزار قرار بگیرند.
