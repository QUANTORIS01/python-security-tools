# درس ۷: Dataclass در پایتون

## مقدمه

در پروژه DNS Lookup یک فایل بسیار کوچک اما بسیار مهم داریم:

```text
models.py
```

داخل این فایل مدل اصلی پروژه قرار دارد:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class DNSRecord:
    domain: str
    record_type: str
    value: str
```

شاید در نگاه اول این فایل بسیار ساده به نظر برسد.

اما در واقع یکی از مهم‌ترین مفاهیم برنامه‌نویسی مدرن پایتون را معرفی می‌کند:

```text
Dataclass
```

در این درس یاد می‌گیریم Dataclass چیست، چه مشکلی را حل می‌کند و چرا در پروژه DNS Lookup از آن استفاده کرده‌ایم.

---

# قبل از Dataclass

فرض کنید بخواهیم اطلاعات یک رکورد DNS را ذخیره کنیم.

روش قدیمی:

```python
class DNSRecord:
    def __init__(
        self,
        domain,
        record_type,
        value,
    ):
        self.domain = domain
        self.record_type = record_type
        self.value = value
```

استفاده:

```python
record = DNSRecord(
    "google.com",
    "A",
    "8.8.8.8",
)
```

این روش کار می‌کند.

اما برای کلاس‌های ساده، مقدار زیادی کد تکراری تولید می‌شود.

---

# مشکل روش قدیمی

معمولاً نیاز داریم:

<div align='right'>

• سازنده (`__init__`) <br>
• نمایش مناسب (`__repr__`) <br>
• مقایسه (`__eq__`) <br>
• هش (`__hash__`)

</div>

را پیاده‌سازی کنیم.

در کلاس‌های داده‌ای این کار خسته‌کننده است.

---

# راه‌حل: Dataclass

پایتون از نسخه 3.7 ماژولی معرفی کرد:

```python
from dataclasses import dataclass
```

که بخش زیادی از این کدها را به صورت خودکار تولید می‌کند.

---

# اولین Dataclass

مثال:

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
```

استفاده:

```python
user = User(
    name="Ali",
    age=25,
)

print(user)
```

خروجی:

```text
User(name='Ali', age=25)
```

بدون اینکه خودمان `__repr__` نوشته باشیم.

---

# سازنده خودکار

<p dir='rtl'>
Dataclass به صورت خودکار:
</p>

```python
__init__()
```

را تولید می‌کند.

بنابراین می‌توانیم مستقیماً بنویسیم:

```python
user = User(
    "Ali",
    25,
)
```

---

# مقایسه خودکار

مثال:

```python
user1 = User(
    "Ali",
    25,
)

user2 = User(
    "Ali",
    25,
)
```

اکنون:

```python
print(user1 == user2)
```

خروجی:

```text
True
```

زیرا Dataclass متد:

```python
__eq__()
```

را تولید کرده است.

---

# ارتباط با تست‌ها

در پروژه این قابلیت بسیار مهم بود.

مثال:

```python
assert DNSRecord(
    domain="google.com",
    record_type="A",
    value="8.8.8.8",
) == DNSRecord(
    domain="google.com",
    record_type="A",
    value="8.8.8.8",
)
```

بدون Dataclass این تست بسیار سخت‌تر می‌شد.

---

<div align='right'>

# Type Hint در Dataclass

</div>

مثال:

```python
@dataclass
class User:
    name: str
    age: int
```

هر فیلد دارای نوع مشخص است.

این موضوع:

<p dir='rtl'>
• خوانایی را افزایش می‌دهد. <br>
• ابزارهای تحلیل کد را کمک می‌کند. <br>
• خطاها را کاهش می‌دهد.
</p>

---

<div align='right'>

# Dataclass در پروژه

</div>

مدل اصلی ما:

```python
@dataclass(frozen=True)
class DNSRecord:
    domain: str
    record_type: str
    value: str
```

دارای سه فیلد است:

---

<div align='right'>

## domain

</div>

```python
domain: str
```

نام دامنه

مثال:

```text
google.com
```

---

<div align='right'>

## record_type

</div>

```python
record_type: str
```

نوع رکورد

مثال:

```text
A
MX
TXT
AAAA
```

---

<div align='right'>

## value

</div>

```python
value: str
```

مقدار واقعی رکورد

مثال:

```text
8.8.8.8
```

یا:

```text
mail.google.com.
```

---

<div align='right'>

# <span dir='rtl'>frozen=True چیست؟</span>

</div>

در پروژه نوشته‌ایم:

```python
@dataclass(frozen=True)
```

این گزینه کلاس را:

```text
Immutable
```

می‌کند.

یعنی پس از ساخت شیء دیگر قابل تغییر نیست.

---

# مثال

```python
record = DNSRecord(
    domain="google.com",
    record_type="A",
    value="8.8.8.8",
)
```

اکنون:

```python
record.domain = "github.com"
```

خطا تولید می‌کند.

---

# چرا Immutable؟

زیرا نتیجه DNS Query نباید بعداً به صورت تصادفی تغییر کند.

پس از ساخته شدن رکورد، داده باید ثابت بماند.

این دقیقاً همان کاری است که در پروژه Port Scanner نیز برای:

```python
ScanResult
```

انجام داده بودیم.

---

# مزایای Immutable Objects

<p dir='rtl'>
• کاهش باگ‌ها <br>
• امنیت بیشتر داده‌ها <br>
• قابلیت پیش‌بینی بالاتر <br>
• مناسب برای تست‌نویسی
</p>

---

# ساخت نمونه

مثال:

```python
record = DNSRecord(
    domain="google.com",
    record_type="A",
    value="8.8.8.8",
)
```

نمایش:

```python
print(record)
```

خروجی:

```text
DNSRecord(
    domain='google.com',
    record_type='A',
    value='8.8.8.8'
)
```

---

# ارتباط با results.py

در فایل:

```text
results.py
```

داریم:

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

برای هر پاسخ DNS یک شیء جدید ساخته می‌شود.

---

# چرا از Dictionary استفاده نکردیم؟

می‌توانستیم بنویسیم:

```python
{
    "domain": "google.com",
    "record_type": "A",
    "value": "8.8.8.8",
}
```

اما Dataclass مزایای بیشتری دارد:

<p dir='rtl'>
• Type Hint <br>
• خوانایی بهتر <br>
• تست آسان‌تر <br>
• ساختار مشخص‌تر <br>
• پشتیبانی بهتر IDEها
</p>

---

# تست‌های پروژه

در فایل:

```text
test_models.py
```

چند ویژگی مهم بررسی می‌شود.

مثال:

```python
record = DNSRecord(
    domain="google.com",
    record_type="A",
    value="8.8.8.8",
)

assert record.domain == "google.com"
```

---

همچنین:

```python
with pytest.raises(AttributeError):
    record.domain = "github.com"
```

برای بررسی Immutable بودن مدل.

---

# چه زمانی از Dataclass استفاده کنیم؟

وقتی کلاس شما:

<p dir='rtl'>
• داده نگهداری می‌کند <br>
• منطق پیچیده ندارد <br>
• بیشتر شبیه یک مدل است
</p>

<p dir='rtl'>
Dataclass گزینه بسیار خوبی است.
</p>

---

# چه زمانی Dataclass مناسب نیست؟

اگر کلاس:

<p dir='rtl'>
• رفتارهای پیچیده دارد <br>
• چندین متد تخصصی دارد <br>
• منطق تجاری سنگین دارد
</p>

ممکن است کلاس معمولی مناسب‌تر باشد.

---

# تمرین

۱. یک Dataclass به نام:

```python
Server
```

بسازید.

---

۲. فیلدهای زیر را اضافه کنید:

```python
host: str
port: int
```

---

۳. یک شیء از آن بسازید.

---

۴. آن را چاپ کنید.

---

۵. کلاس را Immutable کنید و بررسی کنید تغییر فیلدها خطا ایجاد می‌کند.

---

# خلاصه درس

در این درس یاد گرفتیم:

<p dir='rtl'>
• Dataclass چیست <br>
• مزایای Dataclass <br>
• سازنده خودکار <br>
• مقایسه خودکار <br>
• Type Hint <br>
• Immutable Objects <br>
• frozen=True <br>
• مدل DNSRecord پروژه
</p>

<p dir='rtl'>
Dataclass باعث شد مدل داده‌ای پروژه بسیار تمیز، کوتاه و قابل تست باشد.
</p>

در درس بعدی وارد مبحث **Exception Handling** می‌شویم؛ مفهومی که مستقیماً در `resolver.py` برای مدیریت خطاهای DNS استفاده کرده‌ایم.
