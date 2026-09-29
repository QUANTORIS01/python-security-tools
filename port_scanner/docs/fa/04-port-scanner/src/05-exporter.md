<div align='right' dir='rtl'>

# بررسی کامل فایل `exporter.py`


## مقدمه

در جلسه قبل فایل:

```text
src/services.py
```

را بررسی کردیم.

یاد گرفتیم:

<p dir='rtl'>
• Service Detection چیست <br>
• IANA چیست <br>
• getservbyport چگونه کار می‌کند <br>
• تفاوت Service Detection و Banner Grabbing چیست
</p>

تا اینجا پورت اسکنر ما می‌تواند:

✅ پورت‌ها را اسکن کند

✅ سرویس‌ها را تشخیص دهد

اما یک مشکل وجود دارد.

---

فرض کن اسکن 1000 پورت انجام شده است.

نتیجه فقط روی صفحه نمایش داده می‌شود:

```text
80
443
22
53
```

اگر ترمینال را ببندیم:

```text
تمام نتایج از بین می‌روند.
```

---

برای حل این مشکل باید نتایج را ذخیره کنیم.

به همین دلیل فایل:

```text
src/exporter.py
```

ایجاد شده است.

---

# محتوای فایل

```python
import json


def export_json(data: dict, filename: str) -> None:
    """
    Export scan results to a JSON file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
```

---

# هدف این فایل چیست؟

وظیفه این فایل:

```text
ذخیره نتایج اسکن در قالب JSON
```

است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
JSON چیست؟
</p>

<p dir='rtl'>
JSON مخفف:
</p>

```text
JavaScript Object Notation
```

است.

---

<p dir='rtl'>
JSON یکی از محبوب‌ترین فرمت‌های ذخیره و انتقال داده در دنیا است.
</p>

---

تقریباً همه تکنولوژی‌های مدرن از آن استفاده می‌کنند:

<p dir='rtl'>
• Python <br>
• JavaScript <br>
• Node.js <br>
• Go <br>
• Java <br>
• PHP <br>
• APIs <br>
• Cloud Services
</p>

---

# نمونه JSON

```json
{
    "ip": "127.0.0.1",
    "open_ports": [
        80,
        443
    ]
}
```

---

# چرا JSON محبوب است؟

چون:

✅ انسان می‌تواند آن را بخواند

✅ ماشین می‌تواند آن را پردازش کند

✅ سبک است

✅ استاندارد جهانی است

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import
</p>

```python
import json
```

---

## این ماژول چیست؟

یکی از ماژول‌های استاندارد پایتون.

---

وظیفه:

```text
تبدیل داده‌های پایتون به JSON
```

و برعکس.

---

# تعریف تابع

```python
def export_json(
    data: dict,
    filename: str
) -> None:
```

---

## ورودی اول

```python
data: dict
```

---

یعنی:

```python
{
    "ip": "127.0.0.1",
    "ports": [80, 443]
}
```

---

دیکشنری پایتون.

---

## ورودی دوم

```python
filename: str
```

---

مثال:

```python
"result.json"
```

---

یا:

```python
"scan_report.json"
```

---

## خروجی

```python
None
```

---

یعنی تابع چیزی برنمی‌گرداند.

---

فقط فایل ایجاد می‌کند.

---

# داک استرینگ

```python
"""
Export scan results to a JSON file.
"""
```

---

معنی:

```text
خروجی اسکن را در فایل JSON ذخیره کن.
```

---

# مهم‌ترین بخش فایل

```python
with open(
    filename,
    "w",
    encoding="utf-8"
) as file:
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
open چیست؟
</p>

برای کار با فایل‌ها استفاده می‌شود.

---

مثال:

```python
open("result.json")
```

---

# پارامتر اول

```python
filename
```

---

نام فایل.

---

مثال:

```python
result.json
```

---

# پارامتر دوم

```python
"w"
```

---

یعنی:

```text
Write Mode
```

---

در این حالت:

<p dir='rtl'>
• فایل ایجاد می‌شود <br>
• اگر فایل وجود داشته باشد بازنویسی می‌شود
</p>

---

مثال:

```python
open("data.json", "w")
```

---

# پارامتر سوم

```python
encoding="utf-8"
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
Encoding چیست؟
</p>

روشی برای ذخیره متن.

---

<p dir='rtl'>
UTF-8 استاندارد جهانی ذخیره متن است.
</p>

---

مزیت:

```text
پشتیبانی از فارسی
```

---

مثال:

```json
{
    "message": "سلام دنیا"
}
```

---

بدون UTF-8 ممکن است کاراکترهای فارسی خراب شوند.

---

# چرا از with استفاده کرده‌ایم؟

```python
with open(...) as file:
```

---

وقتی کار تمام شود:

```python
file.close()
```

خودکار اجرا می‌شود.

---

مزایا:

✅ تمیزتر

✅ امن‌تر

✅ جلوگیری از نشت منابع

---

# مهم‌ترین خط کل فایل

```python
json.dump(
    data,
    file,
    indent=4
)
```

---

<p dir='rtl' style='font-size:24px; font-wight:bold;'>
dump چیست؟
</p>

تابعی که داده‌های پایتون را به JSON تبدیل می‌کند.

---

مثال:

```python
data = {
    "port": 80,
    "service": "http"
}
```

---

بعد از:

```python
json.dump(...)
```

فایل:

```json
{
    "port": 80,
    "service": "http"
}
```

ایجاد می‌شود.

---

# پارامتر اول

```python
data
```

---

اطلاعاتی که می‌خواهیم ذخیره کنیم.

---

مثال:

```python
{
    "ip": "127.0.0.1",
    "open_ports": [80, 443]
}
```

---

# پارامتر دوم

```python
file
```

---

فایل باز شده.

---

یعنی:

```text
این داده‌ها را داخل این فایل بنویس.
```

---

# پارامتر سوم

```python
indent=4
```

---

این پارامتر ظاهر JSON را زیباتر می‌کند.

---

بدون indent:

```json
{"ip":"127.0.0.1","ports":[80,443]}
```

---

خواندنش سخت است.

---

با:

```python
indent=4
```

خروجی:

```json
{
    "ip": "127.0.0.1",
    "ports": [
        80,
        443
    ]
}
```

---

بسیار خواناتر است.

---

# چرا JSON برای ابزارهای امنیتی مهم است؟

فرض کن بخواهیم:

```text
100 سرور
```

را اسکن کنیم.

---

خروجی ترمینال کافی نیست.

---

اما JSON را می‌توان:

<p dir='rtl'>
• ذخیره کرد <br>
• پردازش کرد <br>
• ارسال کرد <br>
• تحلیل کرد <br>
• وارد دیتابیس کرد
</p>

---

به همین دلیل تقریباً تمام ابزارهای امنیتی مدرن خروجی JSON دارند.

---

نمونه‌ها:

<p dir='rtl'>
• Nmap <br>
• Nessus <br>
• Burp Suite <br>
• OpenVAS <br>
• Security Dashboards
</p>

---

# مثال واقعی در پروژه ما

فرض کن خروجی اسکن:

```python
{
    "ip": "127.0.0.1",
    "open_ports": [
        53,
        135,
        445
    ]
}
```

باشد.

---

فراخوانی:

```python
export_json(
    data,
    "result.json"
)
```

---

فایل زیر را تولید می‌کند:

```json
{
    "ip": "127.0.0.1",
    "open_ports": [
        53,
        135,
        445
    ]
}
```

---

# نکته طراحی

این فایل فقط یک وظیفه دارد:

```text
Export JSON
```

---

وظایف زیر را انجام نمی‌دهد:

❌ اسکن پورت

❌ تشخیص سرویس

❌ گرفتن بنر

❌ چاپ خروجی

❌ لاگ‌گیری

---

این همان اصل:

```text
Single Responsibility Principle
```

است.

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ JSON چیست <br>
✅ چرا JSON مهم است <br>
✅ ماژول json چیست <br>
✅ تابع export_json چگونه کار می‌کند <br>
✅ open چیست <br>
✅ UTF-8 چیست <br>
✅ dump چیست <br>
✅ indent=4 چیست <br>
✅ چرا ابزارهای امنیتی خروجی JSON دارند
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
src/csv_exporter.py
```

می‌شویم.

در آن یاد می‌گیریم:

<p dir='rtl'>
• CSV چیست <br>
• تفاوت CSV و JSON چیست <br>
• چرا هر دو فرمت را پشتیبانی می‌کنیم <br>
• فایل‌های جدولی چگونه ساخته می‌شوند <br>
• چگونه خروجی اسکن را وارد Excel کنیم
</p>

</div>