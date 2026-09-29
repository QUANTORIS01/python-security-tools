<div align='right' dir='rtl'>

# بررسی کامل فایل `test_models.py`

# مقدمه

تا اینجا تقریباً تمام بخش‌های عملی پروژه را بررسی کردیم:

<p dir='rtl'>
✅ اعتبارسنجی ورودی‌ها <br>
✅ اسکن پورت‌ها <br>
✅ تشخیص سرویس‌ها <br>
✅ ذخیره‌سازی خروجی <br>
✅ CLI <br>
✅ Banner Grabbing
</p>

---

اما هنوز یک بخش مهم باقی مانده است.

---

بخشی که تقریباً همه اجزای پروژه به آن وابسته هستند:

```text
مدل داده (Data Model)
```

---

اگر یادت باشد در فایل:

```text
src/models.py
```

کلاس زیر را ساخته بودیم:

```python
@dataclass(frozen=True)
class ScanResult:
```

---

این کلاس وظیفه داشت:

```text
نتیجه هر پورت باز
```

را نگهداری کند.

---

مثلاً:

```python
ScanResult(
    port=22,
    service="ssh",
    banner="SSH-2.0-OpenSSH"
)
```

---

اکنون باید مطمئن شویم:

```python
ScanResult
```

درست ساخته می‌شود و همان رفتاری را دارد که انتظار داریم.

---

# محتوای فایل

```python
import pytest

from src import ScanResult


def test_scan_result_creation():
    result = ScanResult(port=22, service="ssh", banner="SSH-2.0-TestServer")
    assert result.port == 22
    assert result.service == "ssh"
    assert result.banner == "SSH-2.0-TestServer"


def test_scan_result_banner_defaults_to_none():
    result = ScanResult(port=80, service="http")
    assert result.banner is None


def test_scan_result_is_immutable():
    result = ScanResult(port=22, service="ssh")

    with pytest.raises(AttributeError):
        result.port = 80
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import اول
</p>

```python
import pytest
```

---

برای تست خطاها.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import دوم
</p>

```python
from src import ScanResult
```

---

مدلی که قرار است تست شود.

---

# هدف فایل چیست؟

بررسی سه موضوع مهم:

---

```text
ساخت صحیح شیء
```

---

```text
مقدار پیش‌فرض Banner
```

---

```text
Immutable بودن مدل
```

---

# تست اول

```python
def test_scan_result_creation():
```

---

هدف:

```text
بررسی ساخته شدن صحیح شیء
```

است.

---

# ساخت نمونه

```python
result = ScanResult(
    port=22,
    service="ssh",
    banner="SSH-2.0-TestServer"
)
```

---

در اینجا یک شیء از کلاس:

```python
ScanResult
```

می‌سازیم.

---

در حافظه چیزی شبیه این ایجاد می‌شود:

```python
{
    "port": 22,
    "service": "ssh",
    "banner": "SSH-2.0-TestServer"
}
```

---

البته این یک دیکشنری نیست.

---

اما برای درک ساختار می‌توانیم اینگونه تصورش کنیم.

---

# بررسی Port

```python
assert result.port == 22
```

---

بررسی می‌کنیم:

```python
port
```

درست ذخیره شده باشد.

---

# بررسی Service

```python
assert result.service == "ssh"
```

---

بررسی می‌کنیم:

```python
service
```

به درستی مقداردهی شده باشد.

---

# بررسی Banner

```python
assert (
    result.banner
    ==
    "SSH-2.0-TestServer"
)
```

---

بررسی می‌کنیم:

```python
banner
```

نیز به درستی ذخیره شده باشد.

---

# این تست چه چیزی را اثبات می‌کند؟

این تست ثابت می‌کند:

```text
Dataclass به درستی ساخته می‌شود.
```

---

و فیلدها به همان مقداری که داده‌ایم ذخیره می‌شوند.

---

# تست دوم

```python
def test_scan_result_banner_defaults_to_none():
```

---

هدف:

```text
بررسی مقدار پیش‌فرض Banner
```

است.

---

اگر یادت باشد در:

```python
models.py
```

داشتیم:

```python
banner: str | None = None
```

---

دقت کن:

```python
= None
```

---

یعنی:

```text
پارامتر اختیاری است.
```

---

# ساخت شیء

```python
result = ScanResult(
    port=80,
    service="http"
)
```

---

دقت کن:

```python
banner
```

را نفرستاده‌ایم.

---

# چه اتفاقی می‌افتد؟

پایتون مقدار پیش‌فرض را قرار می‌دهد:

```python
banner = None
```

---

# بررسی

```python
assert result.banner is None
```

---

این تست بررسی می‌کند:

```text
مقدار پیش‌فرض
درست تعریف شده باشد.
```

---

# چرا این تست مهم است؟

چون در پروژه ما:

```text
همه سرویس‌ها Banner ندارند.
```

---

مثلاً:

```python
80
```

ممکن است Banner برگرداند.

---

اما:

```python
53
```

معمولاً Banner ندارد.

---

برای همین:

```python
None
```

یک مقدار کاملاً معتبر است.

---

# تست سوم

```python
def test_scan_result_is_immutable():
```

---

مهم‌ترین تست فایل.

---

چرا؟

---

چون به ویژگی:

```python
frozen=True
```

مربوط است.

---

# ساخت شیء

```python
result = ScanResult(
    port=22,
    service="ssh"
)
```

---

تا اینجا همه چیز عادی است.

---

# بخش مهم تست

```python
with pytest.raises(
    AttributeError
):
```

---

هدف:

```text
انتظار خطا داریم.
```

---

# تلاش برای تغییر مقدار

```python
result.port = 80
```

---

اگر این یک کلاس معمولی بود:

```python
class Example:
```

---

هیچ مشکلی نداشت.

---

اما:

```python
ScanResult
```

اینطور تعریف شده:

```python
@dataclass(
    frozen=True
)
```

---

یعنی:

```text
بعد از ساخته شدن
قابل تغییر نیست.
```

---

به این ویژگی می‌گویند:

```text
Immutability
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Immutable چیست؟
</p>

کلمه:

```text
Immutable
```

یعنی:

```text
تغییرناپذیر
```

---

مثال:

```python
result.port = 80
```

↓

```text
ممنوع
```

---

پایتون خطا می‌دهد.

---

# چه خطایی؟

```python
AttributeError
```

---

برای همین:

```python
pytest.raises(
    AttributeError
)
```

منتظر همین خطا است.

---

# اگر خطا رخ دهد

```text
PASS
```

---

# اگر خطا رخ ندهد

```text
FAIL
```

---

# چرا Immutable بودن مهم است؟

فرض کن نتیجه اسکن ساخته شده:

```python
ScanResult(
    port=22,
    service="ssh"
)
```

---

حالا در بخشی از برنامه:

```python
result.port = 9999
```

---

اگر چنین چیزی مجاز باشد:

```text
داده‌های اسکن خراب می‌شوند.
```

---

اما با:

```python
frozen=True
```

این اتفاق غیرممکن می‌شود.

---

# مزیت‌های Immutable Object

✅ امنیت بیشتر

✅ جلوگیری از تغییر ناخواسته داده‌ها

✅ اشکال‌زدایی آسان‌تر

✅ مناسب برای سیستم‌های چندنخی

✅ مناسب برای مدل‌های داده

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Dataclass دقیقاً چه چیزی ساخته است؟
</p>

در پشت صحنه:

```python
@dataclass
```

تقریباً چنین چیزی تولید می‌کند:

```python
class ScanResult:
    def __init__(
        self,
        port,
        service,
        banner=None
    ):
        self.port = port
        self.service = service
        self.banner = banner
```

---

اما:

```python
frozen=True
```

نیز اضافه می‌شود.

---

که مانع تغییر فیلدها بعد از ساخت شیء می‌شود.

---

# خروجی pytest

اگر همه چیز درست باشد:

```bash
pytest
```

---

خروجی:

```text
==== 3 passed ====
```

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ Dataclass چیست <br>
✅ چگونه Dataclass را تست کنیم <br>
✅ تست ساخت شیء <br>
✅ تست مقدار پیش‌فرض <br>
✅ Immutable چیست <br>
✅ frozen=True چه کاری انجام می‌دهد <br>
✅ AttributeError چرا رخ می‌دهد <br>
✅ pytest.raises چگونه کار می‌کند <br>
✅ مزایای مدل‌های داده‌ای تغییرناپذیر
</p>

---

# وضعیت فعلی پروژه

تا این لحظه فایل‌های زیر را به طور کامل بررسی کرده‌ایم:

```text
test_validator.py
test_scanner.py
test_services.py
test_exporter.py
test_cli.py
test_banner.py
test_models.py
```

---

یعنی بخش بزرگی از تست‌های پروژه را پشت سر گذاشته‌ایم.

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
tests/test_results.py
```

می‌شویم.

---

در آن یاد می‌گیریم:

<p dir='rtl'>
✅ تست ساخت ScanResult ها <br>
✅ تست <span dir='ltr'>build_scan_results()</span> <br>
✅ Mock کردن <span dir='ltr'>detect_service()</span> <br>
✅ Mock کردن <span dir='ltr'>grab_banner()</span> <br>
✅ تست پردازش نتایج اسکن <br>
✅ Dependency Isolation چیست
</p>

</div>