# درس ۵: ماژول‌ها (Modules) و Import در پایتون

## مقدمه

تا اینجا برنامه‌های ما کوچک بودند.

اما در پروژه‌های واقعی نمی‌توان همه چیز را داخل یک فایل نوشت.

فرض کنید تمام کدهای DNS Lookup را داخل یک فایل قرار می‌دادیم:

```python
validate_domain()
lookup_record()
build_dns_results()
format_dns_results()
main()
```

و صدها خط کد دیگر.

خیلی سریع پروژه:

<p dir='rtl'>
• سخت‌خوان <br>
• سخت‌توسعه <br>
• سخت‌تست <br>
• سخت‌نگهداری
</p>

می‌شد.

به همین دلیل پروژه‌های حرفه‌ای به چندین فایل تقسیم می‌شوند.

---

# ماژول چیست؟

در پایتون هر فایل <span dir='ltr'>`.py`</span> یک ماژول (Module) محسوب می‌شود.

مثال:

```text
validator.py
```

یک ماژول است.

همچنین:

```text
resolver.py
```

نیز یک ماژول است.

---

# چرا از ماژول استفاده می‌کنیم؟

مزایا:

<p dir='rtl'>
• جداسازی مسئولیت‌ها <br>
• خوانایی بیشتر <br>
• تست‌نویسی ساده‌تر <br>
• توسعه راحت‌تر <br>
• استفاده مجدد از کد
</p>

---

<div align='right'>

# <span dir='rtl'>Import چیست؟</span>

</div>

برای استفاده از کد یک ماژول در ماژول دیگر از Import استفاده می‌کنیم.

مثال:

فایل:

```python
math_utils.py
```

```python
def add(a, b):
    return a + b
```

فایل دوم:

```python
from math_utils import add

print(add(10, 20))
```

خروجی:

```text
30
```

---

<div align='right'>

# <span dir='rtl'>Import کامل</span>

</div>

مثال:

```python
import math
```

استفاده:

```python
math.sqrt(25)
```

خروجی:

```text
5.0
```

---

<div align='right'>

# <span dir='rtl'>Import بخشی از ماژول</span>

</div>

مثال:

```python
from math import sqrt
```

استفاده:

```python
sqrt(25)
```

---

<div align='right'>

# <span dir='rtl'>Import چند عضو</span>

</div>

مثال:

```python
from math import sqrt, pi
```

---

<div align='right'>

# Alias

</div>

گاهی نام ماژول طولانی است.

مثال:

```python
import dns.resolver as resolver
```

استفاده:

```python
resolver.resolve(...)
```

---

# ساختار پروژه DNS Lookup

پروژه ما شامل چندین ماژول است:

```text
src/

├── validator.py
├── resolver.py
├── models.py
├── results.py
├── formatter.py
├── exporter.py
├── csv_exporter.py
├── logger.py
├── cli.py
└── __init__.py
```

هر فایل یک وظیفه مشخص دارد.

---

<div align='right'>

# validator.py

</div>

مسئول:

```text
Input Validation
```

مثال:

```python
validate_domain()
```

```python
validate_record_type()
```

---

<div align='right'>

# resolver.py

</div>

مسئول:

```text
DNS Resolution
```

مثال:

```python
lookup_record()
```

---

<div align='right'>

# models.py

</div>

مسئول:

```text
Data Models
```

مثال:

```python
DNSRecord
```

---

<div align='right'>

# results.py

</div>

مسئول:

```text
Result Processing
```

مثال:

```python
build_dns_results()
```

---

<div align='right'>

# formatter.py

</div>

مسئول:

```text
Terminal Output
```

مثال:

```python
format_dns_results()
```

---

<div align='right'>

# cli.py

</div>

مسئول:

```text
Application Entry Point
```

یعنی نقطه شروع برنامه.

---

<div align='right'>

# Import در پروژه

</div>

در فایل:

```python
results.py
```

داریم:

```python
from src import (
    DNSRecord,
    lookup_record,
)
```

این یعنی:

<p dir='rtl'>
• از مدل داده استفاده کن <br>
• از ماژول DNS Resolver استفاده کن
</p>

---

# جریان اجرای پروژه

زمانی که کاربر دستور زیر را اجرا می‌کند:

```bash
python -m src.cli google.com A
```

اتفاقات زیر رخ می‌دهد:

```text
cli.py

    │

    ▼

validator.py

    │

    ▼

results.py

    │

    ▼

resolver.py

    │

    ▼

models.py

    │

    ▼

formatter.py

    │

    ▼

نمایش خروجی
```

---

<div align='right'>

# <span dir='rtl'>**init**.py چیست؟</span>

</div>

در پوشه:

```text
src/
```

فایلی داریم:

```text
__init__.py
```

این فایل پوشه را به یک Package پایتون تبدیل می‌کند.

---

<div align='right'>

# <span dir='rtl'>Package چیست؟</span>

</div>

وقتی چند ماژول مرتبط را کنار هم قرار دهیم:

```text
src/
```

یک Package ساخته‌ایم.

مثال:

```text
src/
    validator.py
    resolver.py
    results.py
```

همگی اعضای یک Package هستند.

---

<div align='right'>

# <span dir='rtl'>Export کردن اعضا</span>

</div>

معمولاً داخل:

```python
__init__.py
```

اعضای مهم پروژه را Export می‌کنیم.

مثال:

```python
from .validator import (
    validate_domain,
    validate_record_type,
)
```

اکنون می‌توان نوشت:

```python
from src import validate_domain
```

به جای:

```python
from src.validator import validate_domain
```

---

# مزیت این روش

کدها خواناتر می‌شوند.

مثال:

```python
from src import (
    validate_domain,
    lookup_record,
    DNSRecord,
)
```

بسیار تمیزتر از Importهای پراکنده است.

---

# اصل مهم معماری

هر ماژول باید یک مسئولیت مشخص داشته باشد.

مثال:

```text
validator.py
```

فقط اعتبارسنجی.

---

مثال:

```text
resolver.py
```

فقط DNS Query.

---

مثال:

```text
formatter.py
```

فقط نمایش خروجی.

---

این همان اصل:

```text
Separation of Concerns
```

است.

---

# چرا این معماری را انتخاب کردیم؟

اگر تمام پروژه داخل:

```python
main.py
```

قرار می‌گرفت:

<p dir='rtl'>
• تست‌نویسی سخت می‌شد. <br>
• توسعه سخت می‌شد. <br>
• خطاها بیشتر می‌شدند. <br>
• نگهداری پروژه دشوار می‌شد.
</p>

بنابراین پروژه را به چند ماژول کوچک تقسیم کردیم.

---

# ارتباط با تست‌ها

به خاطر ماژولار بودن پروژه توانستیم برای هر فایل تست جداگانه بنویسیم:

```text
test_validator.py
```

```text
test_resolver.py
```

```text
test_results.py
```

```text
test_formatter.py
```

و غیره.

---

# تمرین

۱. یک فایل به نام:

```text
math_utils.py
```

بسازید.

---

۲. تابع زیر را داخل آن قرار دهید:

```python
def add(a, b):
    return a + b
```

---

۳. فایل دیگری بسازید:

```text
main.py
```

---

۴. تابع را Import کنید.

---

۵. نتیجه اجرای:

```python
add(5, 10)
```

را چاپ کنید.

---

۶. بررسی کنید چگونه می‌توان از:

```python
import
```

و

```python
from ... import ...
```

استفاده کرد.

---

# خلاصه درس

در این درس یاد گرفتیم:

<div align='right'>

• ماژول چیست <br>
• <span dir='rtl'>Package چیست</span> <br>
• <span dir='rtl'>Import چیست</span> <br>
• انواع Import <br>
• فایل <span dir='ltr'>**init**.py</span> <br>
• معماری ماژولار <br>
• Separation of Concerns

</div>

این مفاهیم دقیقاً دلیل ساختار فعلی پروژه DNS Lookup هستند و پایه‌ای‌ترین مفاهیم برای ساخت پروژه‌های حرفه‌ای پایتون محسوب می‌شوند.

در درس بعدی وارد **Regular Expressions (Regex)** می‌شویم؛ مفهومی که مستقیماً در `validator.py` برای اعتبارسنجی دامنه‌ها استفاده شده است.
