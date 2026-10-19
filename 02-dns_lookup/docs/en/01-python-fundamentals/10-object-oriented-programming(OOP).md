[🇮🇷 فارسی](/02-dns_lookup/docs/fa/01-python-fundamentals/10-object-oriented-programming(OOP).md)

# Lesson 10: Object-Oriented Programming (OOP)

## Introduction

So far, our programs have consisted of functions, variables, and modules.

But as projects grow larger, maintaining the code becomes more difficult. To solve this problem, we use **Object-Oriented Programming (OOP)**.

In OOP, we place related data and behaviors inside a structure called a **Class**.

---

# What Is a Class?

A class is a blueprint for creating objects.

Example:

Suppose we want to store the information of a server.

```python
class Server:
    pass
```

For now, this class has nothing.

---

# What Is an Object?

An object is an instance of a class.

```python
class Server:
    pass

server1 = Server()
server2 = Server()
```

Here:

```text
Server  -> Class

server1 -> Object

server2 -> Object
```

---

# The `__init__` Method

When an object is created, the `__init__` method runs.

```python
class Server:

    def __init__(self, ip):
        self.ip = ip
```

Usage:

```python
server = Server("192.168.1.10")

print(server.ip)
```

Output:

```text
192.168.1.10
```

---

# What Is `self`?

The `self` parameter refers to the current object.

```python
class Server:

    def __init__(self, ip):
        self.ip = ip
```

Here:

```python
self.ip
```

means:

```text
The ip variable belongs to this object
```

---

# Attribute

The properties of an object are called Attributes.

Example:

```python
class Server:

    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname
```

Creating an object:

```python
server = Server(
    "192.168.1.10",
    "web-server"
)
```

Accessing:

```python
print(server.ip)

print(server.hostname)
```

---

# Method

Functions defined inside a class are called Methods.

```python
class Server:

    def __init__(self, ip):
        self.ip = ip

    def show_ip(self):
        print(self.ip)
```

Usage:

```python
server = Server("10.0.0.1")

server.show_ip()
```

Output:

```text
10.0.0.1
```

---

# A Practical Example

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

Usage:

```python
record = DNSRecord(
    "google.com",
    "A"
)

record.display()
```

Output:

```text
google.com A
```

---

# Default Values

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

Usage:

```python
result = ScanResult(80)

print(result.service)
```

Output:

```text
unknown
```

---

# `__str__`

Used for a better representation of objects.

```python
class Server:

    def __init__(self, ip):
        self.ip = ip

    def __str__(self):
        return self.ip
```

Usage:

```python
server = Server("192.168.1.10")

print(server)
```

Output:

```text
192.168.1.10
```

---

# The Difference Between `Class` and `Dataclass`

We learned earlier:

```python
from dataclasses import dataclass

@dataclass
class DNSRecord:
    domain: str
    record_type: str
    value: str
```

This is equivalent to a longer piece of code:

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

A Dataclass is suitable when we only want to hold data.

---

# OOP in Security Projects

In security tools, classes such as the following usually exist:

```text
Scanner

PortScanner

DNSLookup

PacketAnalyzer

NetworkMonitor

Logger
```

Each class is responsible for one specific task.

This makes:

- The code cleaner
- Development easier
- Testing easier
- Project maintenance simpler

---

# Summary

In this lesson, we learned:

- What a Class is
- What an Object is
- What `self` is
- What an Attribute is
- What a Method is
- The `__init__` method
- The `__str__` method
- The difference between `Class` and `Dataclass`
- The use of OOP in security projects

These concepts are the foundation of most large Python projects, and we will use them many times in future security tools.
