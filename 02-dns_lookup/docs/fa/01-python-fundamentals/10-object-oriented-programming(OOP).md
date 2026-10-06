# درس 10: برنامه‌نویسی شی‌گرا (Object-Oriented Programming)

## مقدمه

تا اینجا برنامه‌های ما از توابع، متغیرها و ماژول‌ها تشکیل شده بودند.

اما وقتی پروژه‌ها بزرگ‌تر می‌شوند، نگهداری کد دشوارتر می‌شود. برای حل این مشکل از **برنامه‌نویسی شی‌گرا (OOP)** استفاده می‌کنیم.

در OOP داده‌ها و رفتارهای مرتبط را داخل یک ساختار به نام **Class** قرار می‌دهیم.

---

<div align='right'>

# <span dir='rtl'>Class چیست؟</span>

</div>

کلاس یک الگو (Blueprint) برای ساخت اشیاء است.

مثال:

فرض کنید می‌خواهیم اطلاعات یک سرور را نگهداری کنیم.

```python
class Server:
    pass
```

فعلاً این کلاس هیچ چیزی ندارد.

---

<div align='right'>

# <span dir='rtl'>Object چیست؟</span>

</div>

شیء (Object) نمونه‌ای از یک کلاس است.

```python
class Server:
    pass

server1 = Server()
server2 = Server()
```

در اینجا:

```text
Server  -> Class

server1 -> Object

server2 -> Object
```

---

# متد **init**

زمانی که یک شیء ساخته می‌شود، متد `__init__` اجرا می‌شود.

```python
class Server:

    def __init__(self, ip):
        self.ip = ip
```

استفاده:

```python
server = Server("192.168.1.10")

print(server.ip)
```

خروجی:

```text
192.168.1.10
```

---

<div align='right'>

# <span dir='rtl'>self چیست؟</span>

</div>

پارامتر `self` به همان شیء فعلی اشاره می‌کند.

```python
class Server:

    def __init__(self, ip):
        self.ip = ip
```

اینجا:

```python
self.ip
```

یعنی:

<div align='right'>

```text
متغیر ip متعلق به این شیء
```

</div>

---

<div align='right'>

# Attribute

ویژگی‌های یک شیء را Attribute می‌گویند.

</div>

مثال:

```python
class Server:

    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname
```

ساخت شیء:

```python
server = Server(
    "192.168.1.10",
    "web-server"
)
```

دسترسی:

```python
print(server.ip)

print(server.hostname)
```

---

<div align='right'>

# Method

</div>

توابعی که داخل کلاس تعریف می‌شوند Method نام دارند.

```python
class Server:

    def __init__(self, ip):
        self.ip = ip

    def show_ip(self):
        print(self.ip)
```

استفاده:

```python
server = Server("10.0.0.1")

server.show_ip()
```

خروجی:

```text
10.0.0.1
```

---

# مثال عملی

```python
class DNSRecord:

    def __init__(self, domain, record_type):
        self.domain = domain
        self.record_type = record_type

    def display(self):
        print(
            self.domain,
            self.record_type
        )
```

استفاده:

```python
record = DNSRecord(
    "google.com",
    "A"
)

record.display()
```

خروجی:

```text
google.com A
```

---

# مقداردهی پیش‌فرض

```python
class ScanResult:

    def __init__(
        self,
        port,
        service="unknown"
    ):
        self.port = port
        self.service = service
```

استفاده:

```python
result = ScanResult(80)

print(result.service)
```

خروجی:

```text
unknown
```

---

<div align='right'>

# **str**

</div>

برای نمایش بهتر اشیاء استفاده می‌شود.

```python
class Server:

    def __init__(self, ip):
        self.ip = ip

    def __str__(self):
        return self.ip
```

استفاده:

```python
server = Server("192.168.1.10")

print(server)
```

خروجی:

```text
192.168.1.10
```

---

# تفاوت Class و Dataclass

قبلاً یاد گرفتیم:

```python
from dataclasses import dataclass

@dataclass
class DNSRecord:
    domain: str
    record_type: str
    value: str
```

این معادل کد طولانی‌تری است:

```python
class DNSRecord:

    def __init__(
        self,
        domain,
        record_type,
        value
    ):
        self.domain = domain
        self.record_type = record_type
        self.value = value
```

<p dir='rtl'>
Dataclass زمانی مناسب است که فقط بخواهیم داده نگهداری کنیم.
</p>

---

<div align='right'>

# <span dir='rtl'>OOP در پروژه‌های امنیتی</span>

</div>

در ابزارهای امنیتی معمولاً کلاس‌هایی مانند موارد زیر وجود دارند:

```text
Scanner

PortScanner

DNSLookup

PacketAnalyzer

NetworkMonitor

Logger
```

هر کلاس مسئول انجام یک وظیفه مشخص است.

این باعث می‌شود:

<p dir='rtl'>
• کد تمیزتر شود <br>
• توسعه آسان‌تر شود <br>
• تست‌نویسی راحت‌تر شود <br>
• نگهداری پروژه ساده‌تر شود
</p>

---

# جمع‌بندی

در این درس یاد گرفتیم:

<div align='right'>

<span dir='rtl'>• Class چیست</span> <br>
<span dir='rtl'>• Object چیست</span> <br>
<span dir='rtl'>• self چیست</span> <br>
<span dir='rtl'>• Attribute چیست</span> <br>
<span dir='rtl'>• Method چیست</span> <br>
<span dir='rtl'>• متد **init**</span> <br>
<span dir='rtl'>• متد **str**</span> <br>
<span dir='rtl'>• تفاوت Class و Dataclass</span> <br>
<span dir='rtl'>• کاربرد OOP در پروژه‌های امنیتی</span>

</div>

این مفاهیم پایه اکثر پروژه‌های بزرگ پایتون هستند و در ابزارهای امنیتی آینده بارها از آن‌ها استفاده خواهیم کرد.
