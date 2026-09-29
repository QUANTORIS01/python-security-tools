<div dir='rtl'>

# بررسی کامل فایل `test_banner.py`

# مقدمه

تا اینجا تقریباً تمام بخش‌های اصلی پروژه را تست کرده‌ایم:

<p dir='rtl'>
✅ Validator <br>
✅ Scanner <br>
✅ Services <br>
✅ Exporter <br>
✅ CLI
</p>

---

اما هنوز یکی از جذاب‌ترین قابلیت‌های پورت اسکنر باقی مانده است:

```text
Banner Grabbing
```

---

اگر یادت باشد در فصل شبکه و امنیت گفتیم:

```text
بعضی سرویس‌ها بعد از اتصال
خودشان اطلاعاتی ارسال می‌کنند.
```

---

مثلاً:

```text
SSH-2.0-OpenSSH_9.3
```

---

یا:

```text
220 FTP Server Ready
```

---

یا:

```text
Apache/2.4.58
```

---

به این اطلاعات:

```text
Banner
```

گفته می‌شود.

---

و تابع:

```python
grab_banner()
```

وظیفه دریافت آن را بر عهده داشت.

---

اکنون باید مطمئن شویم:

```python
grab_banner()
```

در شرایط مختلف درست کار می‌کند.

---

# محتوای فایل

```python
import socket

from src import grab_banner


def test_grab_banner_returns_banner(monkeypatch):
    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass

        def settimeout(self, timeout):
            self.timeout = timeout

        def connect(self, address):
            self.address = address

        def recv(self, size):
            return b"SSH-2.0-TestServer\r\n"

    monkeypatch.setattr(socket, "socket", lambda *args, **kwargs: FakeSocket())
    result = grab_banner("127.0.0.1", 22)
    assert result == "SSH-2.0-TestServer"


def test_grab_banner_returns_none_on_connection_error(monkeypatch):
    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass

        def settimeout(self, timeout):
            pass

        def connect(self, address):
            raise socket.error("Connection failed")

    monkeypatch.setattr(socket, "socket", lambda *args, **kwargs: FakeSocket())
    result = grab_banner("127.0.0.1", 9999)
    assert result is None


def test_grab_banner_returns_none_for_empty_response(monkeypatch):
    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass

        def settimeout(self, timeout):
            pass

        def connect(self, address):
            pass

        def recv(self, size):
            return b""

    monkeypatch.setattr(socket, "socket", lambda *args, **kwargs: FakeSocket())
    result = grab_banner("127.0.0.1", 80)
    assert result is None


def test_grab_banner_sets_timeout(monkeypatch):
    captured = {}

    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass

        def settimeout(self, timeout):
            captured["timeout"] = timeout

        def connect(self, address):
            pass

        def recv(self, size):
            return b"Test Banner"

    monkeypatch.setattr(socket, "socket", lambda *args, **kwargs: FakeSocket())
    grab_banner("127.0.0.1", 80, timeout=2.5)
    assert captured["timeout"] == 2.5
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import اول
</p>

```python
import socket
```

---

برای Mock کردن Socket.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import دوم
</p>

```python
from src import grab_banner
```

---

تابعی که قرار است تست شود.

---

# چرا در این فایل از Mock استفاده شده؟

اگر بخواهیم:

```python
grab_banner()
```

را واقعاً اجرا کنیم:

---

باید:

```text
یک سرور واقعی
```

داشته باشیم.

---

و آن سرور:

```text
واقعاً Banner ارسال کند.
```

---

این کار تست را:

❌ کند

❌ پیچیده

❌ وابسته به شبکه

می‌کند.

---

برای همین:

```python
FakeSocket
```

می‌سازیم.

---

# تست اول

```python
test_grab_banner_returns_banner()
```

---

هدف:

```text
بررسی دریافت موفق Banner
```

---

# کلاس FakeSocket

```python
class FakeSocket:
```

---

این کلاس:

```text
جایگزین Socket واقعی
```

است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
متد __enter__
</p>

```python
def __enter__(self):
    return self
```

---

اگر یادت باشد در:

```python
grab_banner()
```

داشتیم:

```python
with socket.socket(...) as sock:
```

---

برای کار کردن:

```python
with
```

باید:

```python
__enter__
```

وجود داشته باشد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
متد __exit__
</p>

```python
def __exit__(...)
```

---

برای خروج از:

```python
with
```

است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
settimeout
</p>

```python
def settimeout(...)
```

---

فقط مقدار را ذخیره می‌کند.

---

هیچ کار واقعی انجام نمی‌دهد.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
connect
</p>

```python
def connect(...)
```

---

اتصال موفق را شبیه‌سازی می‌کند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
recv
</p>

مهم‌ترین قسمت تست.

---

```python
def recv(self, size):
```

---

برمی‌گرداند:

```python
b"SSH-2.0-TestServer\r\n"
```

---

دقت کن:

```python
b"..."
```

---

یعنی:

```text
Bytes
```

---

دقیقاً همان چیزی که Socket واقعی برمی‌گرداند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Monkeypatch
</p>

```python
monkeypatch.setattr(
    socket,
    "socket",
    ...
)
```

---

از این لحظه:

```python
socket.socket()
```

واقعی اجرا نمی‌شود.

---

بلکه:

```python
FakeSocket()
```

ساخته می‌شود.

---

# اجرای تابع

```python
result =
    grab_banner(
        "127.0.0.1",
        22
    )
```

---

جریان:

```python
recv()
```

↓

```python
b"SSH-2.0-TestServer\r\n"
```

↓

```python
decode()
```

↓

```python
"SSH-2.0-TestServer"
```

---

# بررسی خروجی

```python
assert result ==
    "SSH-2.0-TestServer"
```

---

اگر مقدار دقیقاً همین باشد:

```text
PASS
```

---

# تست دوم

```python
test_grab_banner_returns_none_on_connection_error()
```

---

هدف:

```text
بررسی خطای اتصال
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
FakeSocket
</p>

این بار:

```python
connect()
```

تغییر کرده است.

---

```python
raise socket.error(
    "Connection failed"
)
```

---

یعنی:

```text
اتصال شکست بخورد.
```

---

# اجرای تابع

```python
grab_banner(...)
```

---

در:

```python
banner.py
```

داشتیم:

```python
except (
    socket.timeout,
    socket.error
):
    return None
```

---

پس انتظار داریم:

```python
None
```

برگردد.

---

# بررسی

```python
assert result is None
```

---

این تست بررسی می‌کند:

```text
مدیریت خطا درست کار می‌کند.
```

---

# تست سوم

```python
test_grab_banner_returns_none_for_empty_response()
```

---

هدف:

```text
بررسی Banner خالی
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
recv
</p>

این بار:

```python
return b""
```

---

یعنی:

```text
هیچ داده‌ای دریافت نشده.
```

---

# جریان اجرا

در:

```python
grab_banner()
```

داشتیم:

```python
banner.decode(...)
```

↓

```python
""
```

↓

```python
strip()
```

↓

```python
""
```

---

سپس:

```python
"" or None
```

↓

```python
None
```

---

# بررسی

```python
assert result is None
```

---

این تست ثابت می‌کند:

```text
Banner خالی
به عنوان Banner معتبر پذیرفته نمی‌شود.
```

---

# تست چهارم

```python
test_grab_banner_sets_timeout()
```

---

هدف:

```text
بررسی ارسال صحیح Timeout
```

---

این تست از نظر طراحی بسیار حرفه‌ای است.

---

چرا؟

---

چون:

```text
خروجی تابع را بررسی نمی‌کند.
```

---

بلکه:

```text
رفتار داخلی تابع
```

را بررسی می‌کند.

---

# دیکشنری کمکی

```python
captured = {}
```

---

برای ذخیره اطلاعات.

---

# متد settimeout

```python
def settimeout(
    self,
    timeout
):
```

---

به جای انجام عملیات واقعی:

```python
captured["timeout"] =
    timeout
```

---

ذخیره می‌شود.

---

# اجرای تابع

```python
grab_banner(
    "127.0.0.1",
    80,
    timeout=2.5
)
```

---

در داخل تابع:

```python
sock.settimeout(
    2.5
)
```

اجرا می‌شود.

---

# بررسی

```python
assert captured["timeout"] == 2.5
```

---

اگر مقدار:

```python
2.5
```

ثبت شده باشد:

```text
PASS
```

---

# این نوع تست چه نامی دارد؟

به این نوع تست می‌گویند:

```text
Behavior Verification
```

---

یعنی:

```text
بررسی رفتار داخلی
```

---

نه صرفاً خروجی نهایی.

---

# نکته بسیار مهم

این فایل تقریباً تمام مفاهیم حرفه‌ای Mocking را دارد:

<p dir='rtl'>
✅ Fake Class <br>
✅ Fake Socket <br>
✅ Monkeypatch <br>
✅ Error Simulation <br>
✅ Empty Response Simulation <br>
✅ Behavior Verification
</p>

---

به همین دلیل یکی از آموزشی‌ترین فایل‌های تست پروژه است.

---

# خروجی pytest

اگر همه چیز درست باشد:

```bash
pytest
```

---

خروجی:

```text
==== 4 passed ====
```

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ چگونه Socket را Mock کنیم <br>
✅ چگونه Banner جعلی بسازیم <br>
✅ چگونه خطای اتصال را شبیه‌سازی کنیم <br>
✅ چگونه پاسخ خالی را تست کنیم <br>
✅ چگونه Timeout را اعتبارسنجی کنیم <br>
✅ Behavior Verification چیست <br>
✅ Fake Objects چیست <br>
✅ Mocking در تست‌های شبکه‌ای چگونه انجام می‌شود
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
tests/test_models.py
```

می‌شویم.

---

در آن یاد می‌گیریم:

<p dir='rtl'>
✅ تست Dataclass ها <br>
✅ ویژگی frozen=True چیست <br>
✅ Immutable Object چیست <br>
✅ چگونه مدل‌های داده‌ای را تست کنیم <br>
✅ Equality در Dataclass ها چگونه کار می‌کند
</p>

</div>