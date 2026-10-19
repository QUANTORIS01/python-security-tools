[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/src/09-models.md)

# A Complete Review of the `models.py` File

# Introduction

So far in the project, we have reviewed almost all the practical parts of the port scanner:

✅ Input validation

✅ Port scanning

✅ Service detection

✅ Banner retrieval

✅ JSON output

✅ CSV output

✅ Logging

---

But there is an important question.

---

Suppose the scan result of one port is:

```python
80
```

---

The number 80 alone is not enough.

---

We usually have several pieces of information:

```python
80
http
Apache
```

---

Or:

```python
22
ssh
OpenSSH
```

---

The question:

How do we keep this information together?

---

One way:

```python
tuple
```

---

Example:

```python
(
    80,
    "http",
    "Apache"
)
```

---

But the problem is:

```python
result[0]
```

---

What is this?

---

Port?
Service?
Banner?

---

It is not clear.

---

To solve this problem, we use:

```text
Data Model
```

---

The file:

```text
src/models.py
```

was created for exactly this.

---

# File Content

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class ScanResult:
    """
    Represent the result of a scanned open port.
    """

    port: int
    service: str
    banner: str | None = None
```

---

# What Is the Goal of This File?

Goal:

```text
Building a standard model for storing scan results
```

---

# What Is a Data Model?

A Data Model means:

```text
Defining a data structure
```

---

Example:

If we want to represent a user:

```python
name
email
age
```

---

We can build a model.

---

If we want to represent a scan result:

```python
port
service
banner
```

---

We can also build a model.

---

# Import

```python
from dataclasses import dataclass
```

---

# What Is a Dataclass?

One of the best features of modern Python.

---

Before Dataclass, to build a simple class, we had to do this:

```python
class ScanResult:

    def __init__(
        self,
        port,
        service,
        banner
    ):
        self.port = port
        self.service = service
        self.banner = banner
```

---

Too much code.

---

Repetitive.

---

Tedious.

---

But Dataclass does these things automatically.

---

# Decorator

```python
@dataclass(
    frozen=True
)
```

---

It runs before entering the class.

---

This kind of structure is called:

```python
Decorator
```

---

In the Python course, we said:

```text
A Decorator adds behavior to code.
```

---

Here, Dataclass adds many features.

---

# What Does Dataclass Build?

Automatically:

---

# `__init__`

```python
__init__()
```

---

Meaning:

```python
ScanResult(
    80,
    "http",
    "Apache"
)
```

---

Without us writing `__init__` ourselves.

---

# `__repr__`

---

For displaying the object.

---

Example:

```python
print(result)
```

---

Output:

```python
ScanResult(
    port=80,
    service='http',
    banner='Apache'
)
```

---

# `__eq__`

---

For comparing two objects.

---

Example:

```python
a == b
```

---

# What Is `frozen=True`?

This part is very important.

---

```python
@dataclass(
    frozen=True
)
```

---

Meaning:

```text
The object should be unchangeable.
```

---

In the programming world:

```text
Immutable Object
```

is what it is called.

---

# What Is Immutable?

Meaning:

```text
After the object is created, we cannot change its values.
```

---

Example:

```python
result = ScanResult(
    80,
    "http",
    "Apache"
)
```

---

If we write:

```python
result.port = 443
```

---

We get an error.

---

Why?

---

Because:

```python
frozen=True
```

is set.

---

# Why Is Immutable Good?

Because:

```text
Scan results should not change.
```

---

Suppose:

```python
Port 80 Open
```

---

Later someone writes:

```python
result.port = 22
```

---

All the data is corrupted.

---

Immutable prevents this from happening.

---

# The Class Definition

```python
class ScanResult:
```

---

This class represents:

```text
One open port
```

---

Pay attention:

```text
One port
```

not the whole scan.

---

Example:

```python
80
http
Apache
```

---

One object.

---

The next port:

```python
443
https
Nginx
```

---

Another object.

---

# The Docstring

```python
"""
Represent the result of a scanned open port.
"""
```

---

Meaning:

```text
Represents the result of one scanned open port.
```

---

# The First Field

```python
port: int
```

---

Type:

```python
int
```

---

Example:

```python
80
```

---

Or:

```python
443
```

---

Or:

```python
22
```

---

# The Second Field

```python
service: str
```

---

Type:

```python
str
```

---

Example:

```python
"http"
```

---

Or:

```python
"https"
```

---

Or:

```python
"ssh"
```

---

# The Third Field

```python
banner: str | None = None
```

---

This part is the most interesting.

---

Type:

```python
str | None
```

---

Meaning:

```python
"Apache"
```

---

Or:

```python
None
```

---

# Default Value

```python
= None
```

---

Meaning:

If we did not have a Banner:

```python
banner
```

automatically equals:

```python
None
```

---

Example:

```python
ScanResult(
    port=53,
    service="domain"
)
```

---

In this case:

```python
banner
```

is automatically:

```python
None
```

---

# Creating a Real Object

```python
result = ScanResult(
    port=80,
    service="http",
    banner="Apache"
)
```

---

Contents:

```python
result.port
```

↓

```python
80
```

---

```python
result.service
```

↓

```python
"http"
```

---

```python
result.banner
```

↓

```python
"Apache"
```

---

# A Second Example

```python
result = ScanResult(
    port=53,
    service="domain"
)
```

---

Result:

```python
result.port
```

↓

```python
53
```

---

```python
result.service
```

↓

```python
"domain"
```

---

```python
result.banner
```

↓

```python
None
```

---

# Why Is This Design Professional?

Instead of:

```python
{
    "port": 80,
    "service": "http",
    "banner": "Apache"
}
```

---

Or:

```python
(
    80,
    "http",
    "Apache"
)
```

---

We have a clear model:

```python
ScanResult
```

---

Advantages:

✅ Better readability

✅ Better typing

✅ Easier testing

✅ Fewer errors

✅ Better extensibility

---

That is why almost all professional projects use Data Models.

---

# Summary

In this session, we learned:

✅ What a Data Model is

✅ What a Dataclass is

✅ What a Decorator is

✅ How `__init__` is built automatically

✅ What `__repr__` is

✅ What `__eq__` is

✅ What Immutable is

✅ What `frozen=True` is

✅ Why `ScanResult` was created

✅ Why using a Model is more professional than a Dictionary

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
src/results.py
```

There we will learn:

- Why `ScanResult` was created
- How we convert Open Ports into `ScanResult`
- How we combine Service Detection and Banner Grabbing
- What List Comprehension is
- How the data design pipeline works in the project

