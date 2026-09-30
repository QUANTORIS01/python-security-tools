<div dir='rtl'>

# بررسی کامل فایل `test_cli.py`

# مقدمه

تبریک 🎉

به مهم‌ترین فایل تست کل پروژه رسیدیم.

---

تا اینجا فایل‌هایی را تست کردیم که:

```text
یک تابع
↓
یک ورودی
↓
یک خروجی
```

داشتند.

---

مثلاً:

```python
validate_ip()
```

---

یا:

```python
detect_service()
```

---

اما فایل:

```text
test_cli.py
```

متفاوت است.

---

چرا؟

---

چون این بار داریم:

```text
کل برنامه
```

را تست می‌کنیم.

---

یعنی دقیقاً همان چیزی که کاربر اجرا می‌کند:

```bash
python cli.py ...
```

---

در واقع این فایل نزدیک‌ترین تست به تجربه واقعی کاربر است.

---

# هدف فایل

بررسی:

```python
create_parser()
```

و

```python
main()
```

---

یعنی مطمئن شویم:

✅ پارامترها درست خوانده می‌شوند

✅ اعتبارسنجی درست کار می‌کند

✅ خطاها نمایش داده می‌شوند

✅ خروجی ترمینال صحیح است

✅ فایل JSON ساخته می‌شود

✅ فایل CSV ساخته می‌شود

✅ لاگ ثبت می‌شود

---

# محتوای فایل

```python
import pytest

from src.cli import create_parser, main
from src import ScanResult


def test_create_parser():
    parser = create_parser()
    args = parser.parse_args(["127.0.0.1", "1", "1000"])
    assert args.ip == "127.0.0.1"
    assert args.start_port == 1
    assert args.end_port == 1000
    assert args.timeout == 0.5
    assert args.workers == 100


def test_main_with_valid_arguments(monkeypatch, capsys):
    def fake_scan_range(ip, start_port, end_port, timeout, workers):
        return [22, 80, 443]

    monkeypatch.setattr("src.cli.scan_range", fake_scan_range)
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "1000"])
    main()
    captured = capsys.readouterr()
    assert "ssh" in captured.out
    assert "http" in captured.out
    assert "https" in captured.out

    assert "22" in captured.out
    assert "80" in captured.out
    assert "443" in captured.out


def test_main_with_invalid_ip(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["cli.py", "999.999.999.999", "1", "1000"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Invalid IP address" in captured.out


def test_main_with_invalid_port_range(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "5000", "1000"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Invalid port range" in captured.out


def test_main_with_invalid_timeout(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "1000", "--timeout", "0"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Timeout must be greater than 0" in captured.out


def test_main_with_invalid_workers(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "1000", "--workers", "0"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Workers must be greater than 0" in captured.out


def test_main_shows_service_names(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["port_scanner", "127.0.0.1", "1", "1000"])
    monkeypatch.setattr("src.cli.scan_range", lambda *args, **kwargs: [80, 443])
    monkeypatch.setattr("src.cli.build_scan_results", lambda *args, **kwargs: [
        ScanResult(
            port=80,
            service="http",
            banner=None,
        ),
        ScanResult(
            port=443,
            service="https",
            banner=None,
        ),
    ])
    main()
    captured = capsys.readouterr()
    assert "http" in captured.out
    assert "https" in captured.out


def test_main_exports_json(monkeypatch, capsys):
    exported = {}

    def fake_scan_range(*args, **kwargs):
        return [80, 443]

    def fake_export_json(data, filename):
        exported["data"] = data
        exported["filename"] = filename

    monkeypatch.setattr("src.cli.scan_range", fake_scan_range)
    monkeypatch.setattr("src.cli.export_json", fake_export_json)
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "1000", "--json", "result.json"])
    main()
    assert exported["filename"] == "result.json"


def test_main_exports_csv(monkeypatch):
    exported = {}

    def fake_scan_range(*args, **kwargs):
        return [80, 443]

    def fake_export_csv(data, filename):
        exported["data"] = data
        exported["filename"] = filename

    monkeypatch.setattr("src.cli.scan_range", fake_scan_range)
    monkeypatch.setattr("src.cli.export_csv", fake_export_csv)
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "1000", "--csv", "result.csv"])
    main()
    assert exported["filename"] == "result.csv"
    assert exported["data"]["target"] == "127.0.0.1"
    assert exported["data"]["open_ports"] == [
        {
            "port": 80,
            "service": "http",
            "banner": None,
        },
        {
            "port": 443,
            "service": "https",
            "banner": None,
        },
    ]


def test_main_creates_log_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "10"])
    monkeypatch.setattr("src.cli.scan_range", lambda *args, **kwargs: [3, 5])
    main()
    log_file = tmp_path / "scan.log"
    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert "Scan started" in content
    assert "target=127.0.0.1" in content
    assert "ports=1-10" in content
    assert "Scan completed" in content
    assert "open_ports=2" in content
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Import ها
</p>

```python
import pytest
```

---

برای:

```python
pytest.raises()
```

---

که کمی جلوتر بررسی می‌کنیم.

---

```python
from src.cli import (
    create_parser,
    main
)
```

---

توابع مورد تست.

---

```python
from src import ScanResult
```

---

برای ساخت داده تستی.

---

# تست اول

```python
def test_create_parser():
```

---

هدف:

```text
بررسی Argument Parser
```

---

# ساخت Parser

```python
parser = create_parser()
```

---

همان تابعی که در:

```text
cli.py
```

نوشتیم.

---

# شبیه‌سازی ورودی

```python
args =
    parser.parse_args(
        [
            "127.0.0.1",
            "1",
            "1000"
        ]
    )
```

---

در واقع معادل:

```bash
python cli.py 127.0.0.1 1 1000
```

است.

---

# بررسی IP

```python
assert args.ip == "127.0.0.1"
```

---

# بررسی Start Port

```python
assert args.start_port == 1
```

---

# بررسی End Port

```python
assert args.end_port == 1000
```

---

# بررسی Default Timeout

```python
assert args.timeout == 0.5
```

---

اگر کاربر مقدار ندهد:

```python
0.5
```

قرار می‌گیرد.

---

# بررسی Default Workers

```python
assert args.workers == 100
```

---

این تست مطمئن می‌شود:

```text
Parser دقیقاً مطابق طراحی ما عمل می‌کند.
```

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
Monkeypatch چیست؟
</p>

قبل از ادامه باید با مهم‌ترین ابزار فایل آشنا شویم.

---

```python
monkeypatch
```

---

یکی از امکانات فوق‌العاده pytest.

---

وظیفه:

```text
جایگزین کردن موقت اشیاء
```

---

مثلاً:

```python
scan_range()
```

---

را با نسخه تقلبی عوض کنیم.

---

# چرا Monkeypatch مهم است؟

فرض کن در هر تست:

```python
scan_range()
```

واقعاً اجرا شود.

---

مشکلات:

❌ تست کند می‌شود

❌ شبکه لازم داریم

❌ نتایج متغیر می‌شوند

---

برای همین:

```python
Fake Functions
```

می‌سازیم.

---

# تست دوم

```python
test_main_with_valid_arguments()
```

---

یکی از مهم‌ترین تست‌های پروژه.

---

# تابع تقلبی

```python
def fake_scan_range(...):
```

---

به جای اسکن واقعی:

```python
return [22, 80, 443]
```

---

برمی‌گرداند.

---

# جایگزینی

```python
monkeypatch.setattr(
    "src.cli.scan_range",
    fake_scan_range
)
```

---

از این لحظه:

```python
scan_range()
```

واقعی اجرا نمی‌شود.

---

بلکه:

```python
fake_scan_range()
```

اجرا می‌شود.

---

# شبیه‌سازی خط فرمان

```python
monkeypatch.setattr(
    "sys.argv",
    [...]
)
```

---

این فوق‌العاده مهم است.

---

در واقع داریم وانمود می‌کنیم کاربر اجرا کرده:

```bash
python cli.py 127.0.0.1 1 1000
```

---

# اجرای برنامه

```python
main()
```

---

برنامه اجرا می‌شود.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
capsys چیست؟
</p>

یکی دیگر از قابلیت‌های pytest.

---

```python
capsys
```

---

تمام خروجی:

```python
print()
```

ها را ذخیره می‌کند.

---

# گرفتن خروجی

```python
captured =
    capsys.readouterr()
```

---

اکنون:

```python
captured.out
```

حاوی خروجی ترمینال است.

---

# بررسی خروجی

```python
assert "ssh" in captured.out
```

---

و:

```python
assert "http" in captured.out
```

---

و:

```python
assert "https" in captured.out
```

---

این تست مطمئن می‌شود:

```text
Service Detection
```

در خروجی دیده می‌شود.

---

# بررسی شماره پورت‌ها

```python
assert "22" in captured.out
```

---

```python
assert "80" in captured.out
```

---

```python
assert "443" in captured.out
```

---

پس خروجی جدول نیز بررسی شده است.

---

<p dir='rtl' style='font-size:32px; font-wight:bold;'>
pytest.raises چیست؟
</p>

در تست‌های بعدی چند بار این الگو را می‌بینیم:

```python
with pytest.raises(SystemExit):
```

---

هدف:

```text
بررسی خطاها
```

است.

---

# تست Invalid IP

```python
test_main_with_invalid_ip()
```

---

ورودی:

```python
999.999.999.999
```

---

برنامه باید:

```python
sys.exit(1)
```

اجرا کند.

---

در پایتون:

```python
sys.exit()
```

در واقع:

```python
SystemExit
```

پرتاب می‌کند.

---

برای همین:

```python
pytest.raises()
```

آن را شکار می‌کند.

---

# بررسی Exit Code

```python
assert exc_info.value.code == 1
```

---

یعنی:

```text
برنامه با خطا خارج شده است.
```

---

# بررسی پیام خطا

```python
assert "Invalid IP address"
```

---

این تست مطمئن می‌شود:

```text
کاربر پیام مناسب دریافت می‌کند.
```

---

# تست Invalid Port Range

همان منطق:

```python
5000
1000
```

---

و انتظار:

```python
SystemExit(1)
```

---

# تست Invalid Timeout

ورودی:

```python
--timeout 0
```

---

چون:

```python
timeout > 0
```

لازم بود.

---

باید خطا بگیریم.

---

# تست Invalid Workers

ورودی:

```python
--workers 0
```

---

باید:

```python
SystemExit(1)
```

اتفاق بیفتد.

---

# تست نمایش سرویس‌ها

```python
test_main_shows_service_names()
```

---

در این تست:

```python
scan_range()
```

و

```python
build_scan_results()
```

هر دو Mock شده‌اند.

---

# چرا؟

چون نمی‌خواهیم:

```text
واقعاً اسکن کنیم.
```

---

بلکه فقط می‌خواهیم:

```text
خروجی نمایش
```

را تست کنیم.

---

# داده ساختگی

```python
ScanResult(
    port=80,
    service="http"
)
```

---

و:

```python
ScanResult(
    port=443,
    service="https"
)
```

---

# بررسی خروجی

```python
assert "http"
```

---

و:

```python
assert "https"
```

---

# تست Export JSON

```python
test_main_exports_json()
```

---

اینجا:

```python
export_json()
```

<p dir='rtl'>
Mock شده است.
</p>

---

به جای ساخت فایل واقعی:

```python
exported = {}
```

---

پر می‌شود.

---

# تابع جعلی

```python
def fake_export_json(...)
```

---

داده‌ها را ذخیره می‌کند.

---

# بررسی

```python
assert exported["filename"]
```

---

این تست مطمئن می‌شود:

```text
نام فایل صحیح ارسال شده است.
```

---

# تست Export CSV

مشابه تست قبل.

---

اما این بار:

```python
export_csv()
```

بررسی می‌شود.

---

نکته مهم:

```python
assert exported["data"]
```

---

هم ساختار داده را بررسی می‌کند.

---

هم محتوا را.

---

# تست Log File

آخرین و حرفه‌ای‌ترین تست فایل.

---

```python
test_main_creates_log_file()
```

---

# تغییر پوشه کاری

```python
monkeypatch.chdir(
    tmp_path
)
```

---

یعنی:

```text
وارد پوشه موقت شو.
```

---

# اجرای برنامه

```python
main()
```

---

# بررسی فایل

```python
scan.log
```

---

باید ساخته شده باشد.

---

# بررسی وجود فایل

```python
assert log_file.exists()
```

---

# خواندن فایل

```python
content =
    log_file.read_text(...)
```

---

# بررسی محتوا

```python
assert "Scan started"
```

---

```python
assert "target=127.0.0.1"
```

---

```python
assert "ports=1-10"
```

---

```python
assert "Scan completed"
```

---

```python
assert "open_ports=2"
```

---

این تست ثابت می‌کند:

```text
سیستم لاگینگ پروژه
درست کار می‌کند.
```

---

# اهمیت این فایل

اگر بخواهم فقط یک فایل تست را در کل پروژه نگه دارم:

```text
test_cli.py
```

مهم‌ترین گزینه است.

---

چرا؟

---

چون تقریباً:

```text
تمام اجزای پروژه
```

را درگیر می‌کند.

---

# مفاهیم جدیدی که در این فایل یاد گرفتیم

<p dir='rtl'>
✅ Monkeypatch <br>
✅ Fake Functions <br>
✅ Mocking <br>
✅ capsys <br>
✅ sys.argv <br>
✅ pytest.raises <br>
✅ SystemExit <br>
✅ CLI Testing <br>
✅ Log Testing <br>
✅ Export Testing
</p>

---

# جمع‌بندی

در این جلسه یاد گرفتیم:

<p dir='rtl'>
✅ چگونه CLI را تست کنیم <br>
✅ چگونه ورودی خط فرمان را شبیه‌سازی کنیم <br>
✅ چگونه خروجی ترمینال را بررسی کنیم <br>
✅ چگونه خطاها را تست کنیم <br>
✅ چگونه فایل‌های Export را تست کنیم <br>
✅ چگونه سیستم Logging را تست کنیم <br>
✅ چگونه از Monkeypatch استفاده کنیم
</p>

---

# در جلسه بعد چه چیزی یاد می‌گیریم؟

در جلسه بعد وارد فایل:

```text
tests/test_banner.py
```

می‌شویم.

---

در آن یاد می‌گیریم:

<p dir='rtl'>
✅ تست Banner Grabbing <br>
✅ ساخت سرور آزمایشی برای ارسال Banner <br>
✅ تست داده‌های دریافتی از Socket <br>
✅ تست Timeout <br>
✅ تست Service Response
</p>

</div>