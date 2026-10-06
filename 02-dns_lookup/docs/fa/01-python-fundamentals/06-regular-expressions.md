# درس ۶: عبارات باقاعده (Regular Expressions یا Regex)

## مقدمه

در پروژه DNS Lookup اولین جایی که از یک ابزار نسبتاً پیشرفته پایتون استفاده کردیم فایل:

```text
validator.py
```

بود.

در این فایل تابع:

```python
validate_domain()
```

برای بررسی معتبر بودن نام دامنه از Regex استفاده می‌کند.

اگر Regex وجود نداشت مجبور بودیم ده‌ها شرط مختلف بنویسیم.

به همین دلیل Regex یکی از مهم‌ترین ابزارهای اعتبارسنجی داده در برنامه‌نویسی محسوب می‌شود.

---

<div align='right'>

# <span dir='rtl'>Regex چیست؟</span>

</div>

<p dir='rtl'>
Regex مخفف:
</p>

```text
Regular Expression
```

است.

<p dir='rtl'>
Regex یک زبان کوچک برای جستجو و تطبیق الگوها در متن است.
</p>

مثلاً:

<p dir='rtl'>
• بررسی ایمیل <br>
• بررسی شماره تلفن <br>
• بررسی IP <br>
• بررسی دامنه <br>
• استخراج داده از متن
</p>

همگی کاربردهای رایج Regex هستند.

---

# اولین مثال

فرض کنید بخواهیم بررسی کنیم آیا رشته فقط شامل عدد است یا خیر.

```python
import re

pattern = r"\d+"

print(bool(re.fullmatch(pattern, "12345")))
```

خروجی:

```text
True
```

اما:

```python
print(bool(re.fullmatch(pattern, "123abc")))
```

خروجی:

```text
False
```

---

# ماژول re

در پایتون Regex توسط ماژول:

```python
import re
```

پیاده‌سازی شده است.

تقریباً تمام عملیات Regex از طریق همین ماژول انجام می‌شود.

---

# تابع fullmatch

در پروژه از:

```python
re.fullmatch()
```

استفاده کرده‌ایم.

مثال:

```python
re.fullmatch(r"\d+", "123")
```

نتیجه:

```text
Match
```

اما:

```python
re.fullmatch(r"\d+", "123abc")
```

نتیجه:

```text
None
```

---

# چرا fullmatch؟

زیرا می‌خواهیم کل رشته بررسی شود.

نه فقط بخشی از آن.

مثال:

```python
re.search(r"\d+", "abc123xyz")
```

موفق است.

اما:

```python
re.fullmatch(r"\d+", "abc123xyz")
```

ناموفق است.

---

<div align='right'>

# Raw String

</div>

در Regex معمولاً می‌نویسیم:

```python
r"\d+"
```

حرف:

```text
r
```

قبل از رشته یعنی:

```text
Raw String
```

تا بک‌اسلش‌ها به درستی تفسیر شوند.

---

# کاراکترهای مهم Regex

## نقطه

```python
.
```

یعنی:

```text
هر کاراکتر
```

مثال:

```python
re.fullmatch(r"a.c", "abc")
```

موفق است.

---

## ستاره

```python
*
```

یعنی:

```text
صفر یا بیشتر
```

مثال:

```python
ab*
```

موارد زیر را می‌پذیرد:

```text
a
ab
abb
abbb
```

---

## علامت +

```python
+
```

یعنی:

```text
یک یا بیشتر
```

مثال:

```python
ab+
```

می‌پذیرد:

```text
ab
abb
abbb
```

اما:

```text
a
```

را نمی‌پذیرد.

---

## علامت سؤال

```python
?
```

یعنی:

```text
صفر یا یک بار
```

مثال:

```python
colou?r
```

می‌پذیرد:

```text
color
colour
```

---

# کلاس‌های کاراکتری

## اعداد

```python
\d
```

معادل:

```text
0-9
```

---

## حروف و اعداد

```python
\w
```

---

## فاصله

```python
\s
```

---

# براکت‌ها

مثال:

```python
[A-Z]
```

یعنی:

تمام حروف بزرگ انگلیسی.

---

مثال:

```python
[a-z]
```

تمام حروف کوچک.

---

مثال:

```python
[0-9]
```

تمام اعداد.

---

# بازه‌ها

مثال:

```python
[A-Za-z]
```

یعنی:

تمام حروف انگلیسی.

---

مثال:

```python
[A-Za-z0-9]
```

یعنی:

تمام حروف و اعداد.

---

# بررسی Regex پروژه

در فایل:

```python
validator.py
```

داریم:

```python
pattern = (
    r"^(?!-)"
    r"(?:[A-Za-z0-9-]{1,63}\.)+"
    r"[A-Za-z]{2,63}$"
)
```

اکنون آن را بخش به بخش بررسی می‌کنیم.

---

# بخش اول

```python
^
```

یعنی:

```text
ابتدای رشته
```

<p dir='rtl'>
Regex باید از ابتدای متن شروع شود.
</p>

---

# بخش دوم

```python
(?!-)
```

این یک:

```text
Negative Lookahead
```

است.

معنی:

```text
دامنه نباید با - شروع شود
```

---

مثال معتبر:

```text
google.com
```

---

مثال نامعتبر:

```text
-google.com
```

---

# بخش سوم

```python
[A-Za-z0-9-]
```

اجازه می‌دهد:

<p dir='rtl'>
• حروف <br>
• اعداد <br>
• خط تیره
</p>

در دامنه وجود داشته باشند.

---

# بخش چهارم

```python
{1,63}
```

یعنی:

```text
حداقل 1 و حداکثر 63 کاراکتر
```

زیرا هر Label در DNS حداکثر 63 کاراکتر دارد.

---

مثال:

```text
google
```

معتبر است.

---

# بخش پنجم

```python
\.
```

نقطه واقعی دامنه را نشان می‌دهد.

مثال:

```text
google.com
```

---

# بخش ششم

```python
(?: ... )+
```

این بخش می‌گوید:

<div align='right'>

```text
یک یا چند Label
```

</div>

وجود داشته باشد.

---

مثال:

```text
google.com
```

---

مثال:

```text
mail.google.com
```

---

مثال:

```text
docs.mail.google.com
```

همگی معتبر هستند.

---

# بخش آخر

```python
[A-Za-z]{2,63}
```

برای TLD است.

مثال:

```text
com
net
org
io
dev
academy
```

---

# انتهای رشته

```python
$
```

یعنی:

```text
پایان رشته
```

بنابراین چیزی بعد از TLD مجاز نیست.

---

# مثال‌های معتبر

```text
google.com
```

```text
openai.com
```

```text
mail.google.com
```

```text
example.org
```

---

# مثال‌های نامعتبر

```text
-google.com
```

---

```text
google
```

---

```text
google.
```

---

```text
google..com
```

---

```text
@google.com
```

---

# تست‌های پروژه

در فایل:

```text
test_validator.py
```

تعداد زیادی تست برای همین Regex نوشتیم.

مثال:

```python
assert validate_domain("google.com")
```

---

مثال:

```python
assert not validate_domain("google")
```

---

مثال:

```python
assert not validate_domain("-google.com")
```

---

# چرا Regex مهم است؟

در ابزارهای امنیتی دائماً با اعتبارسنجی داده سروکار داریم.

مثال‌ها:

<p dir='rtl'>
• Domain Validation <br>
• Email Validation <br>
• URL Validation <br>
• IP Validation <br>
• Log Parsing <br>
• IOC Extraction
</p>

بنابراین Regex یکی از مهم‌ترین مهارت‌های مورد نیاز در ابزارهای امنیتی است.

---

# محدودیت Regex فعلی

<p dir='rtl'>
Regex ما ساده و آموزشی است.
</p>

تمام قوانین RFC دامنه‌ها را پوشش نمی‌دهد.

اما برای این پروژه:

```text
Learning-Oriented
```

کاملاً کافی و مناسب است.

---

# تمرین

<p dir='rtl'>
۱. Regex بنویسید که فقط اعداد را بپذیرد.
</p>

---

<p dir='rtl'>
۲. Regex بنویسید که فقط حروف انگلیسی را بپذیرد.
</p>

---

<p dir='rtl'>
۳. Regex بنویسید که دامنه‌های زیر را بپذیرد:
</p>

```text
google.com
openai.com
example.org
```

---

۴. بررسی کنید:

```python
re.search()
```

و

```python
re.fullmatch()
```

چه تفاوتی دارند.

---

<p dir='rtl'>
۵. Regex فعلی پروژه را خط به خط توضیح دهید.
</p>

---

# خلاصه درس

در این درس یاد گرفتیم:

<p dir='rtl'>
• Regex چیست <br>
• ماژول re <br>
• fullmatch <br>
• Raw String <br>
• کلاس‌های کاراکتری <br>
• Quantifierها <br>
• Lookahead <br>
• اعتبارسنجی دامنه با Regex
</p>

این اولین مفهومی بود که مستقیماً از کد واقعی پروژه DNS Lookup استخراج و تحلیل شد.

در درس بعدی وارد **Dataclass** می‌شویم؛ مفهومی که در فایل `models.py` برای ساخت مدل `DNSRecord` استفاده کرده‌ایم.
