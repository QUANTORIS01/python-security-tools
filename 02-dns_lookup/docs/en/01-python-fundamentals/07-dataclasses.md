[🇮🇷 فارسی](/02-dns_lookup/docs/fa/01-python-fundamentals/07-dataclasses.md)

# Lesson 7: Dataclass in Python

## Introduction

In the DNS Lookup project, we have a very small but very important file:

```text
models.py
```

Inside this file is the project's main model:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class DNSRecord:
    domain: str
    record_type: str
    value: str
```

At first glance, this file might seem very simple.

But in reality, it introduces one of the most important concepts of modern Python programming:

```text
Dataclass
```

In this lesson, we will learn what a Dataclass is, what problem it solves, and why we used it in the DNS Lookup project.

---

# Before Dataclass

Suppose we want to store the information of a DNS record.

The old way:

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

Usage:

```python
record = DNSRecord(
    "google.com",
    "A",
    "8.8.8.8",
)
```

This approach works.

But for simple classes, it produces a lot of repetitive code.

---

# The Problem with the Old Way

Usually, we need to implement:

- A constructor (`__init__`)
- A proper representation (`__repr__`)
- Comparison (`__eq__`)
- Hash (`__hash__`)

For data classes, this is tedious.

---

# The Solution: Dataclass

From version 3.7, Python introduced a module:

```python
from dataclasses import dataclass
```

which automatically generates a large part of this code.

---

# The First Dataclass

Example:

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
```

Usage:

```python
user = User(
    name="Ali",
    age=25,
)

print(user)
```

Output:

```text
User(name='Ali', age=25)
```

Without us writing `__repr__` ourselves.

---

# Automatic Constructor

A Dataclass automatically generates:

```python
__init__()
```

Therefore, we can directly write:

```python
user = User(
    "Ali",
    25,
)
```

---

# Automatic Comparison

Example:

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

Now:

```python
print(user1 == user2)
```

Output:

```text
True
```

Because the Dataclass has generated the method:

```python
__eq__()
```

---

# Connection to the Tests

In the project, this feature was very important.

Example:

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

Without a Dataclass, this test would have been much harder.

---

# Type Hints in Dataclass

Example:

```python
@dataclass
class User:
    name: str
    age: int
```

Each field has a specific type.

This:

- Increases readability
- Helps code-analysis tools
- Reduces errors

---

# Dataclass in the Project

Our main model:

```python
@dataclass(frozen=True)
class DNSRecord:
    domain: str
    record_type: str
    value: str
```

has three fields:

---

## `domain`

```python
domain: str
```

The domain name

Example:

```text
google.com
```

---

## `record_type`

```python
record_type: str
```

The record type

Example:

```text
A
MX
TXT
AAAA
```

---

## `value`

```python
value: str
```

The actual record value

Example:

```text
8.8.8.8
```

Or:

```text
mail.google.com.
```

---

# What Is `frozen=True`?

In the project, we wrote:

```python
@dataclass(frozen=True)
```

This option makes the class:

```text
Immutable
```

Meaning, after the object is created, it can no longer be changed.

---

# Example

```python
record = DNSRecord(
    domain="google.com",
    record_type="A",
    value="8.8.8.8",
)
```

Now:

```python
record.domain = "github.com"
```

raises an error.

---

# Why Immutable?

Because the result of a DNS query should not be accidentally changed later.

Once the record is created, the data should remain constant.

This is exactly what we did in the Port Scanner project for:

```python
ScanResult
```

---

# Advantages of Immutable Objects

- Fewer bugs
- Better data security
- Higher predictability
- Suitable for testing

---

# Creating an Instance

Example:

```python
record = DNSRecord(
    domain="google.com",
    record_type="A",
    value="8.8.8.8",
)
```

Display:

```python
print(record)
```

Output:

```text
DNSRecord(
    domain='google.com',
    record_type='A',
    value='8.8.8.8'
)
```

---

# Connection to `results.py`

In the file:

```text
results.py
```

we have:

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

For each DNS response, a new object is created.

---

# Why Did We Not Use a Dictionary?

We could have written:

```python
{
    "domain": "google.com",
    "record_type": "A",
    "value": "8.8.8.8",
}
```

But a Dataclass has more advantages:

- Type Hints
- Better readability
- Easier testing
- Clearer structure
- Better IDE support

---

# The Project's Tests

In the file:

```text
test_models.py
```

several important properties are checked.

Example:

```python
record = DNSRecord(
    domain="google.com",
    record_type="A",
    value="8.8.8.8",
)

assert record.domain == "google.com"
```

---

Also:

```python
with pytest.raises(AttributeError):
    record.domain = "github.com"
```

to verify the model's immutability.

---

# When Should We Use Dataclass?

When your class:

- Holds data
- Has no complex logic
- Is more like a model

Dataclass is a very good option.

---

# When Is Dataclass Not Suitable?

If the class:

- Has complex behaviors
- Has several specialized methods
- Has heavy business logic

a regular class may be more suitable.

---

# Exercise

1. Create a Dataclass named:

```python
Server
```

---

2. Add the following fields:

```python
host: str
port: int
```

---

3. Create an object from it.

---

4. Print it.

---

5. Make the class immutable and verify that changing fields raises an error.

---

# Lesson Summary

In this lesson, we learned:

- What a Dataclass is
- The advantages of Dataclass
- Automatic constructor
- Automatic comparison
- Type Hints
- Immutable Objects
- `frozen=True`
- The project's `DNSRecord` model

Dataclass made the project's data model very clean, short, and testable.

In the next lesson, we enter **Exception Handling**; a concept used directly in `resolver.py` for handling DNS errors.
