[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/src/05-models.md)

# Chapter Four: DNS Lookup Project Code Analysis

## Lesson 5: Data Modeling with `dataclass`

### 1. Lesson Goal

In this lesson, we will learn:

- How to organize related data in a class.
- What repeated code the `@dataclass` decorator removes.
- What effect the `frozen=True` option has on class instances.
- How a data model contributes to better readability and maintainability of the project.

### 2. Examining the Structure of the `models.py` File

The file code:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class DNSRecord:
    """
    Represent a DNS record.
    """
    domain: str
    record_type: str
    value: str
```

This file defines a class named `DNSRecord` that has three attributes:

| Attribute | Use |
|---|---|
| `domain` | The domain name related to the record |
| `record_type` | The DNS record type |
| `value` | The record value |

All three attributes are defined with a type hint of type `str`; that is, string is specified as their expected type.

Instead of holding the data in several separate variables, this class places the information related to one DNS record in a single object.

### 3. What Does `@dataclass` Do?

In Python, if a class is created only for holding data, writing methods like `__init__()` and `__repr__()` manually can create repetitive code.

The `@dataclass` decorator simplifies this part of the work. Based on the fields defined in `DNSRecord`, Python generates the common methods needed to work with instances.

For example:

```python
record = DNSRecord(
    domain="example.com",
    record_type="A",
    value="192.0.2.10",
)

print(record)
```

The output will be similar to:

```text
DNSRecord(domain='example.com', record_type='A', value='192.0.2.10')
```

This display is useful for examining data during development and debugging.

### 4. Creating an Instance of `DNSRecord`

To create a record, it is enough to specify the values of the three fields when creating the instance:

```python
record = DNSRecord(
    domain="example.com",
    record_type="MX",
    value="mail.example.com",
)
```

Then its fields can be accessed:

```python
print(record.domain)
print(record.record_type)
print(record.value)
```

This structure is more readable than holding information in several unrelated variables; because it specifies which value belongs to which record and which attribute.

Note that the above values are only educational samples and are not necessarily the actual response of a DNS request.

### 5. The Concept of `frozen=True`

In the class definition, the following is seen:

```python
@dataclass(frozen=True)
```

The `frozen=True` parameter makes assigning a new value to the instance's fields after creation not allowed.

For example:

```python
record = DNSRecord(
    domain="example.com",
    record_type="A",
    value="192.0.2.10",
)

record.value = "192.0.2.20"
```

Running the last assignment raises `FrozenInstanceError`.

This feature helps preserve data integrity; different parts of the program cannot easily change the value of a field after creating the instance.

This feature is usually referred to as an **immutable-style data object**. However, it should be noted that `frozen=True` does not mean absolute immutability of all objects inside an instance; in this class, all three fields are of the string type, which are themselves immutable.

### 6. Does `dataclass` Validate Data Types?

No. Defining the type with `str` alone is not a runtime type check.

For example, the current definition by itself does not prevent creating an instance with a non-string value:

```python
record = DNSRecord(
    domain=123,
    record_type="A",
    value="192.0.2.10",
)
```

In the usual case, this code does not automatically raise an error solely because `123` is incompatible with the type hint.

Therefore, `dataclass` in this file performs the data modeling task, not full validation of its contents. Validation can be implemented in a separate layer or with specific logic in the model itself, if the project needs such a thing.

### 7. The Role of the Data Model in the Project Architecture

`DNSRecord` provides a specific template for displaying a DNS record. Using such a model can have the following advantages:

- Clear naming of fields related to the record
- Easy access to each part of the data
- Appropriate display of the object during debugging
- Preventing accidental changes to fields after creation
- Transferring data between different parts of the program with a specific structure

However, to precisely determine which parts of the project use `DNSRecord`, the related files must also be examined. The class definition alone does not show that all execution paths of the program use this model.

### 8. Practice Exercises

**Exercise 1 — Creating a Record**

Create an instance of `DNSRecord` with arbitrary values and print all three of its fields.

**Exercise 2 — Testing `frozen=True`**

Try to change the value of `record_type` after creating the instance. Observe the error raised and explain its cause.

**Exercise 3 — Examining the Type Hint**

Create an instance with a number placed in one of its fields. Explain why the type hint alone does not prevent this.

**Exercise 4 — Designing a Model**

Suppose a data model is to be designed for the complete result of a DNS lookup. What is the difference between a `DNSRecord` and a result containing several records, the request status, and error information?

### 9. Summary

In this lesson, we examined the `DNSRecord` class:

- `@dataclass` simplifies the construction of a data class.
- The three fields `domain`, `record_type`, and `value` hold the main information of a record.
- `frozen=True` prevents reassignment to the instance's fields after creation.
- Type hints are expected-type documentation and do not by themselves guarantee runtime validation.

This simple model provides a suitable basis for orderly display of DNS record information.
