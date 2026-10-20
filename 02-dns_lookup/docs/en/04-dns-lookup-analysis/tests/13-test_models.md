[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/tests/13-test_models.md)

# Lesson 13: Testing Data Models and Immutability in Python

**Code under test:** `src/models.py`

## 1. Lesson Goal

In this lesson, we will learn how to test the behavior of a data model with automated testing.

In the DNS Lookup project, the `DNSRecord` class is defined using `dataclass` and has the `frozen=True` attribute. The tests of this lesson examine that:

- A DNS record is created with the expected values.
- The record's fields cannot be changed after creation.
- The model can also hold an instance with the `MX` record type.

## 2. The Complete Test File Code

```python
import pytest

from src import DNSRecord


def test_dns_record_creation():
    record = DNSRecord(domain='google.com', record_type='A', value='8.8.8.8')
    assert record.domain == 'google.com'
    assert record.record_type == 'A'
    assert record.value == '8.8.8.8'


def test_dns_record_is_immutable():
    record = DNSRecord(domain='google.com', record_type='A', value='8.8.8.8')

    with pytest.raises(AttributeError):
        record.value = '1.1.1.1'


def test_dns_record_with_mx_record():
    record = DNSRecord(domain='google.com', record_type='MX', value='smtp.google.com')
    assert record.record_type == 'MX'
```

## 3. Importing the Required Tools

```python
import pytest

from src import DNSRecord
```

### The `pytest` Module

`pytest` is the tool for executing tests and examining their results. In this file, in addition to running tests, the `pytest.raises()` capability is used to examine the occurrence of an exception.

### The `DNSRecord` Class

This class is imported from the `src` package. Its definition is in the `models.py` file:

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

This model has three fields:

- `domain`: the domain name
- `record_type`: the DNS record type
- `value`: the record value

The `frozen=True` attribute also causes assigning a new value to the instance's fields after creation to be not allowed.

## 4. Testing DNS Record Creation

```python
def test_dns_record_creation():
    record = DNSRecord(
        domain='google.com',
        record_type='A',
        value='8.8.8.8'
    )
    assert record.domain == 'google.com'
    assert record.record_type == 'A'
    assert record.value == '8.8.8.8'
```

This test first creates a `DNSRecord` object and then checks the value of each field.

### Creating an Instance

```python
record = DNSRecord(
    domain='google.com',
    record_type='A',
    value='8.8.8.8'
)
```

Due to the use of `dataclass`, we do not need to write the `__init__()` constructor ourselves. Python creates it automatically for the defined fields.

### Checking with `assert`

```python
assert record.domain == 'google.com'
```

This statement checks that the value of the `domain` field equals the expected value.

The next two `assert`s do the same for `record_type` and `value`.

If any of these conditions is not met, the test fails.

**Important note:** This test examines the values stored in the object; it does not by itself verify the actual validity of DNS information or the validation of inputs. These responsibilities are in other parts of the project.

## 5. Testing Record Immutability

```python
def test_dns_record_is_immutable():
    record = DNSRecord(
        domain='google.com',
        record_type='A',
        value='8.8.8.8'
    )

    with pytest.raises(AttributeError):
        record.value = '1.1.1.1'
```

This test examines the `frozen=True` attribute.

### Changing the Field Value

```python
record.value = '1.1.1.1'
```

If `DNSRecord` were a regular, mutable dataclass, this assignment could change the field's value.

But because the model is defined with `frozen=True`, an attempt to assign a new value to a field raises the `AttributeError` exception.

### The Role of `pytest.raises()`

```python
with pytest.raises(AttributeError):
    record.value = '1.1.1.1'
```

This structure tells pytest that the execution of the code inside the block must raise the specified exception.

Consider two cases:

- If `AttributeError` is raised, this part of the test is successful.
- If the assignment is performed without that exception, the test fails.

In this way, the test not only checks that creating the object is successful; it also examines its behavior against an unauthorized operation.

### Why Is Immutability Useful?

In the DNS Lookup tool's workflow, a record after being created can be passed between different parts of the program; for example, from the results-building part to the formatter or the export stage.

Immutability helps prevent a record's field values from being accidentally overwritten. This attribute can make understanding the data flow and troubleshooting simpler.

Technical note: `frozen=True` does not mean deep immutability of all related objects; rather, it restricts reassignment of the instance's fields. In the current model, all three fields are of type string, which is a suitable choice for such a record.

## 6. Testing a Record of Type MX

```python
def test_dns_record_with_mx_record():
    record = DNSRecord(
        domain='google.com',
        record_type='MX',
        value='smtp.google.com'
    )
    assert record.record_type == 'MX'
```

This test creates an instance of `DNSRecord` with the record type `MX` and checks the value of the `record_type` field.

In the previous test, the record type was `A`. Here we test another type to show that the model is not designed only for one specific value.

The `DNSRecord` class is responsible for holding the record's information; the list of supported types and their validation are in the `validate_record_type()` function.

Therefore, the current test checks that the model can store the value `MX`; not that this value is valid from a DNS perspective or that a real and accessible record exists.

## 7. What Do These Three Tests Cover?

| Test Name | Behavior Examined |
|---|---|
| `test_dns_record_creation` | Record creation and correct field values |
| `test_dns_record_is_immutable` | Preventing reassignment to a field |
| `test_dns_record_with_mx_record` | Holding the value of the `MX` record type |

This set covers three specific scenarios: correct object creation, restricting field changes, and using another record type.

## 8. Running the Tests

To run just this file from the project root:

```powershell
python -m pytest tests/test_models.py
```

To run all the project's tests:

```powershell
python -m pytest
```

If the immutability test fails, we must examine whether the model definition still has `frozen=True` or the expected behavior has changed.

## 9. Practice Exercises

### Exercise 1: Examining the Fields

Create an instance of `DNSRecord` with arbitrary values and write an `assert` for each of the three fields.

### Exercise 2: Changing the Domain

After creating a record, try to change the value of `record.domain`.

- What exception is raised?
- Why do we expect this operation to fail?

### Exercise 3: Examining Other Fields

Write the immutability test for `record_type` too.

### Exercise 4: Separation of Responsibilities

Explain the difference between the task of `DNSRecord` and `validate_record_type()`.

## 10. Summary

In this lesson, we learned that testing a data model is not just examining the creation of an object. We can also test the values of its fields and its behavioral restrictions.

Key concepts:

- Using `dataclass` to define a data model
- Examining field values with `assert`
- Using `pytest.raises()` to test exceptions
- Examining the `frozen=True` behavior
- Separating the data model's responsibility from input validation

In the DNS Lookup project, `DNSRecord` provides a simple and specific structure for holding record information. These tests help preserve the model's main behavior against future changes.
