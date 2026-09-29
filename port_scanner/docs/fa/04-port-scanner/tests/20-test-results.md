# بررسی کامل فایل `test_results.py`

# مقدمه

تا اینجا تقریباً تمام اجزای پروژه را بررسی کرده‌ایم:

<p dir='rtl'>
✅ Validator <br>
✅ Scanner <br>
✅ Services <br>
✅ Exporter <br>
✅ Logger <br>
✅ Banner <br>
✅ Models <br>
✅ CLI
</p>

---

اما اکنون به یکی از مهم‌ترین فایل‌های پروژه رسیده‌ایم:

```text
results.py
```

---

اگر یادت باشد این فایل وظیفه داشت:

```text
خروجی خام اسکن
```

را تبدیل کند به:

```text
نتایج ساختاریافته
```

---

یعنی از این:

```python
[22, 80]
```

---

به این:

```python
[
    ScanResult(
        port=22,
        service="ssh",
        banner="SSH-2.0-TestServer"
    ),
    ScanResult(
        port=80,
        service="http",
        banner="HTTP/1.1 200 OK"
    )
]
```

---

تبدیل کند.

---

در واقع:

```python
build_scan_results()
```

پل ارتباطی بین:

```text
اسکنر
```

و

```text
خروجی نهایی
```

است.

---

# محتوای فایل

```python
from src import ScanResult, build_scan_results


def test_build_scan_results(monkeypatch):
    def fake_detect_service(port):
        return "ssh"

    def fake_grab_banner(ip, port, timeout):
        return "SSH-2.0-TestServer"

    monkeypatch.setattr("src.results.detect_service", fake_detect_service)
    monkeypatch.setattr("src.results.grab_banner", fake_grab_banner)
    results = build_scan_results("127.0.0.1", [22], timeout=2.0)
    assert results == [
        ScanResult(
            port=22,
            service="ssh",
            banner="SSH-2.0-TestServer",
        )
    ]


def test_build_scan_results_with_multiple_ports(monkeypatch):
    def fake_detect_service(port):
        services = {22: "ssh", 80: "http"}
        return services[port]

    def fake_grab_banner(ip, port, timeout):
        banners = {22: "SSH-2.0-TestServer", 80: "HTTP/1.1 200 OK"}
        return banners[port]

    monkeypatch.setattr("src.results.detect_service", fake_detect_service)
    monkeypatch.setattr("src.results.grab_banner", fake_grab_banner)
    results = build_scan_results("127.0.0.1", [22, 80])
    assert results == [
        ScanResult(
            port=22,
            service="ssh",
            banner="SSH-2.0-TestServer",
        ),
        ScanResult(
            port=80,
            service="http",
            banner="HTTP/1.1 200 OK",
        ),
    ]


def test_build_scan_results_handles_missing_banner(monkeypatch):
    monkeypatch.setattr("src.results.detect_service", lambda port: "http")
    monkeypatch.setattr("src.results.grab_banner", lambda ip, port, timeout: None)
    results = build_scan_results("127.0.0.1", [80])
    assert results == [
        ScanResult(
            port=80,
            service="http",
            banner=None,
        )
    ]
```

---

# هدف فایل چیست؟

بررسی اینکه:

```python
build_scan_results()
```

در شرایط مختلف:

<p dir='rtl'>
✅ سرویس را درست تشخیص دهد <br>
✅ Banner را درست دریافت کند <br>
✅ ScanResult را درست بسازد <br>
✅ چند پورت را درست پردازش کند <br>
✅ نبود Banner را درست مدیریت کند
</p>

---

# تست اول

```python
def test_build_scan_results(
    monkeypatch
):
```

---

هدف:

```text
بررسی ساخت نتیجه برای یک پورت
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Fake Detect Service
</p>

```python
def fake_detect_service(
    port
):
    return "ssh"
```

---

هر پورتی دریافت شود:

```python
"ssh"
```

برمی‌گرداند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Fake Banner
</p>

```python
def fake_grab_banner(
    ip,
    port,
    timeout
):
    return "SSH-2.0-TestServer"
```

---

همیشه یک Banner مشخص برمی‌گرداند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Monkeypatch
</p>

```python
monkeypatch.setattr(
    "src.results.detect_service",
    fake_detect_service
)
```

---

از این لحظه:

```python
detect_service()
```

واقعی اجرا نمی‌شود.

---

بلکه:

```python
fake_detect_service()
```

اجرا می‌شود.

---

همین اتفاق برای:

```python
grab_banner()
```

نیز می‌افتد.

---

# اجرای تابع

```python
results =
    build_scan_results(
        "127.0.0.1",
        [22],
        timeout=2.0
    )
```

---

ورودی:

```python
[22]
```

---

جریان اجرا:

```python
22
```

↓

```python
detect_service()
```

↓

```python
"ssh"
```

↓

```python
grab_banner()
```

↓

```python
"SSH-2.0-TestServer"
```

↓

```python
ScanResult(...)
```

---

# خروجی مورد انتظار

```python
[
    ScanResult(
        port=22,
        service="ssh",
        banner="SSH-2.0-TestServer"
    )
]
```

---

# بررسی

```python
assert results == [...]
```

---

نکته جالب:

```python
Dataclass
```

ها قابلیت مقایسه خودکار دارند.

---

یعنی:

```python
ScanResult(...)
==
ScanResult(...)
```

---

فیلد به فیلد مقایسه می‌شود.

---

# تست دوم

```python
test_build_scan_results_with_multiple_ports()
```

---

هدف:

```text
بررسی پردازش چند پورت
```

است.

---

این تست به واقعیت پروژه نزدیک‌تر است.

---

چون معمولاً:

```python
scan_range()
```

چند پورت برمی‌گرداند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Fake Service
</p>

```python
services = {
    22: "ssh",
    80: "http"
}
```

---

سپس:

```python
return services[port]
```

---

نتیجه:

```python
22 → ssh
80 → http
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Fake Banner
</p>

```python
banners = {
    22: "SSH-2.0-TestServer",
    80: "HTTP/1.1 200 OK"
}
```

---

نتیجه:

```python
22
```

↓

```python
SSH Banner
```

---

و:

```python
80
```

↓

```python
HTTP Banner
```

---

# اجرای تابع

```python
results =
    build_scan_results(
        "127.0.0.1",
        [22, 80]
    )
```

---

# انتظار

```python
[
    ScanResult(...),
    ScanResult(...)
]
```

---

یعنی:

```text
دو شیء مستقل
```

---

باید ساخته شود.

---

# چرا این تست مهم است؟

چون بررسی می‌کند:

```python
for port in open_ports:
```

---

در:

```python
results.py
```

درست کار می‌کند.

---

اگر حلقه مشکل داشته باشد:

```text
این تست Fail می‌شود.
```

---

# تست سوم

```python
test_build_scan_results_handles_missing_banner()
```

---

یکی از مهم‌ترین تست‌های فایل.

---

هدف:

```text
بررسی نبود Banner
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Fake Service
</p>

```python
lambda port: "http"
```

---

همیشه:

```python
"http"
```

برمی‌گرداند.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Fake Banner
</p>

```python
lambda ip, port, timeout: None
```

---

همیشه:

```python
None
```

برمی‌گرداند.

---

یعنی:

```text
هیچ Banner وجود ندارد.
```

---

# اجرای تابع

```python
results =
    build_scan_results(
        "127.0.0.1",
        [80]
    )
```

---

# انتظار

```python
[
    ScanResult(
        port=80,
        service="http",
        banner=None
    )
]
```

---

# چرا این تست مهم است؟

چون در دنیای واقعی:

```text
همه سرویس‌ها Banner ندارند.
```

---

بعضی سرویس‌ها:

```python
recv()
```

را خالی برمی‌گردانند.

---

یا اصلاً داده‌ای ارسال نمی‌کنند.

---

در این حالت:

```python
grab_banner()
```

↓

```python
None
```

---

و برنامه باید بدون خطا ادامه پیدا کند.

---

این تست همین رفتار را تضمین می‌کند.

---

# مفهوم مهم: Dependency Isolation

این فایل یکی از بهترین نمونه‌های:

```text
Dependency Isolation
```

است.

---

یعنی:

```python
build_scan_results()
```

را تست می‌کنیم.

---

بدون اینکه:

```python
detect_service()
```

واقعی اجرا شود.

---

و بدون اینکه:

```python
grab_banner()
```

واقعی اجرا شود.

---

چرا؟

---

چون ما فقط می‌خواهیم:

```python
build_scan_results()
```

را بررسی کنیم.

---

نه وابستگی‌هایش را.

---

این یکی از مهم‌ترین اصول تست حرفه‌ای است.

---

# مسیر اجرای واقعی

در برنامه اصلی:

```python
scan_range()
```

↓

```python
open_ports
```

↓

```python
build_scan_results()
```

↓

```python
detect_service()
```

↓

```python
grab_banner()
```

↓

```python
ScanResult
```

↓

```python
results
```

---

این فایل دقیقاً بخش وسط این زنجیره را تست می‌کند.

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
✅ تست <span dir='ltr'>build_scan_results()</span> <br>
✅ Mock کردن <span dir='ltr'>detect_service()</span> <br>
✅ Mock کردن <span dir='ltr'>grab_banner()</span> <br>
✅ ساخت ScanResult ها <br>
✅ تست چند پورت همزمان <br>
✅ مدیریت Banner خالی <br>
✅ Dependency Isolation چیست <br>
✅ مقایسه Dataclass ها چگونه انجام می‌شود <br>
✅ اهمیت تست پردازش نتایج
</p>

---

# وضعیت فعلی پروژه

فایل‌های تست بررسی‌شده:

```text
test_validator.py
test_scanner.py
test_services.py
test_exporter.py
test_cli.py
test_banner.py
test_models.py
test_results.py
```

---

یعنی تقریباً به انتهای بخش تست‌ها نزدیک شده‌ایم.

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
tests/test_formatter.py
```

می‌شویم.

---

در آن یاد می‌گیریم:

<p dir='rtl'>
✅ تست خروجی ترمینال <br>
✅ تست قالب‌بندی جدول <br>
✅ تست Banner های طولانی <br>
✅ تست Empty Results <br>
✅ تست رشته‌های چندخطی <br>
✅ چگونه خروجی CLI را اعتبارسنجی کنیم
</p>
