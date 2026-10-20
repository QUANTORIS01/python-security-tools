[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/tests/12-test_validator.md)

# Lesson 12: Automated Testing of Input Validation with pytest

**Code under test:** `src/validator.py`

## 1. Lesson Goal

In this lesson, we become familiar with automated testing in Python and the method for examining the behavior of validation functions.

In the DNS Lookup project, we have three validation functions:

- `validate_domain()` for checking the domain format
- `validate_timeout()` for checking that timeout is positive
- `validate_record_type()` for checking support for a DNS record type

The `test_validator.py` file examines the behavior of these three functions with a set of different inputs.

## 2. The Complete Test File Code

```python
from src import (
    validate_domain,
    validate_timeout,
    validate_record_type,
)


def test_valid_domain():
    assert validate_domain('google.com')


def test_valid_subdomain():
    assert validate_domain('mail.google.com')


def test_invalid_domain_without_tld():
    assert not validate_domain('google')


def test_invalid_domain_with_protocol():
    assert not validate_domain('https://google.com')


def test_invalid_domain_with_space():
    assert not validate_domain('google .com')


def test_valid_timeout():
    assert validate_timeout(1.0)


def test_valid_timeout_boundary():
    assert validate_timeout(0.001)


def test_invalid_timeout():
    assert not validate_timeout(0)


def test_invalid_negative_timeout():
    assert not validate_timeout(-1)


def test_valid_record_type_a():
    assert validate_record_type('A')


def test_valid_record_type_lowercase():
    assert validate_record_type('mx')


def test_valid_record_type_aaaa():
    assert validate_record_type('AAAA')


def test_invalid_record_type():
    assert not validate_record_type('FTP')


def test_invalid_empty_record_type():
    assert not validate_record_type('')
```

## 3. Why Do We Write Automated Tests?

Suppose we change the domain validation function. The new change might reject a valid input or accept an invalid input.

By running the tests, we can check that the expected behaviors still hold.

Automated testing has several important advantages:

- It reveals possible errors sooner.
- It protects important program behaviors against unwanted changes.
- It enables repeated execution of the checks.
- It documents what behavior we expect from each function.

In this project, we use `pytest`.

## 4. Importing the Functions Under Test

```python
from src import (
    validate_domain,
    validate_timeout,
    validate_record_type,
)
```

This part imports three functions from the `src` package.

These functions are defined in the `validator.py` file and are also made available in the package through `src/__init__.py`.

In this way, the tests examine the behavior of functions that are accessible from the package's public interface.

## 5. The Structure of a Test with `assert`

The first test:

```python
def test_valid_domain():
    assert validate_domain('google.com')
```

This function is a test for a valid domain.

Test function names start with the `test_` prefix so that `pytest` can identify them automatically.

The `assert` statement checks a condition:

- If the condition is true, the test continues.
- If the condition is false, the test fails and pytest displays information about the failure.

In this example, we expect `validate_domain('google.com')` to return a true value.

Important note: This test only examines one specific input; its success alone does not prove that the function works correctly for all possible domains.

## 6. Testing Domains and Subdomains

```python
def test_valid_domain():
    assert validate_domain('google.com')


def test_valid_subdomain():
    assert validate_domain('mail.google.com')
```

The first test examines a regular domain.

The second test checks that the function also accepts a subdomain.

These two tests are useful for ensuring the basic validation behavior. They also show that tests can cover different samples of valid inputs.

## 7. Testing Invalid Domains

### Domain Without a TLD

```python
def test_invalid_domain_without_tld():
    assert not validate_domain('google')
```

In this test, `not` is used.

We expect the function to return `False` for the string `google`; because this input is not compatible with the expected domain pattern in the current implementation.

### Domain with Protocol

```python
def test_invalid_domain_with_protocol():
    assert not validate_domain('https://google.com')
```

Here the input includes `https://`.

The `validate_domain()` function is designed to validate the domain name format, not the full URL address; therefore, we expect this input to be rejected.

### Domain with a Space

```python
def test_invalid_domain_with_space():
    assert not validate_domain('google .com')
```

This test checks that the presence of a space within the string causes the input to be rejected.

These three tests show that validation is not limited to accepting valid samples; rejecting certain invalid inputs is also part of the expected behavior.

## 8. Testing the `validate_timeout()` Function

### A Regular Positive Value

```python
def test_valid_timeout():
    assert validate_timeout(1.0)
```

We expect a timeout of `1.0` to be accepted; because its value is positive.

### A Small Positive Value

```python
def test_valid_timeout_boundary():
    assert validate_timeout(0.001)
```

This test examines a small positive value.

The test name uses the word *boundary*, but technically this value is not the smallest possible positive value for the `float` type. This test examines a value close to zero to ensure that the function does not reject it merely because the value is small.

### Zero and Negative Values

```python
def test_invalid_timeout():
    assert not validate_timeout(0)


def test_invalid_negative_timeout():
    assert not validate_timeout(-1)
```

The `validate_timeout()` function in the current implementation checks this condition:

```python
return timeout > 0
```

Therefore:

| Input | Expected Result |
|---:|---|
| `1.0` | Accepted |
| `0.001` | Accepted |
| `0` | Rejected |
| `-1` | Rejected |

These tests examine the positivity behavior of the value.

An educational note: The current tests cover positive, zero, and negative values, but they do not examine the behavior of inputs like `float('inf')`, `float('nan')`, or a text string. If the function needs specific behavior for these inputs too, separate tests can be written for them.

## 9. Testing the `validate_record_type()` Function

### Record Type A

```python
def test_valid_record_type_a():
    assert validate_record_type('A')
```

This test checks that the record type `A` is accepted.

### Record Type with Lowercase Letters

```python
def test_valid_record_type_lowercase():
    assert validate_record_type('mx')
```

This test examines an important point: the function should also accept the record type `mx`, even though it is written with lowercase letters.

The reason for this behavior is in the implementation of `validate_record_type()`:

```python
return record_type.upper() in SUPPORTED_RECORD_TYPES
```

The `upper()` method converts the string to uppercase. Therefore, `mx` is converted to `MX` and compared with the set of supported types.

This test documents a specific and important behavior: record type validation is not case-sensitive.

### Record Type AAAA

```python
def test_valid_record_type_aaaa():
    assert validate_record_type('AAAA')
```

This test checks that the record type `AAAA` is also among the supported types.

### An Invalid Record Type

```python
def test_invalid_record_type():
    assert not validate_record_type('FTP')
```

In this test, we expect `FTP` to be rejected; because it is not in the project's set of supported types.

### An Empty String

```python
def test_invalid_empty_record_type():
    assert not validate_record_type('')
```

This test examines the empty input.

Since the empty string remains empty after conversion with `upper()` and is not in the set of supported types, we expect the function to return `False`.

## 10. What Do These Tests Cover?

This file has a total of 14 tests:

| Part | Number of Tests | Items Examined |
|---|---:|---|
| Domain | 5 | Regular domain, subdomain, and three invalid inputs |
| Timeout | 4 | Positive value, small positive value, zero, and negative value |
| Record Type | 5 | Valid types, lowercase, invalid type, and empty string |
| **Total** | **14** | **Three validation functions** |

This set covers important basic behaviors. Of course, the number of tests alone is not a complete measure of quality; it matters that the necessary important scenarios and boundary cases are also considered.

## 11. Running the Tests

To run just this file from the project root, you can use this command:

```powershell
python -m pytest tests/test_validator.py
```

To run all the project's tests:

```powershell
python -m pytest
```

In the pytest output, the result of each test and the number of successful or failed tests are usually displayed.

If a test fails, its information helps us determine which expectation was not met.

## 12. Opportunities for Extending the Tests

The current tests specify the basic behaviors well. To expand coverage, the following scenarios can be added in the future:

- Domains with very long lengths
- A domain label that ends with a hyphen
- Infinite timeouts like `float('inf')`
- A timeout of type `NaN`
- Non-string inputs for functions that expect strings
- Valid record types with different letter cases

These are suggestions for increasing test coverage. Adding each test should be done based on the function's expected contract; first, we must specify whether the intended input should be accepted or rejected, and then record that behavior with a test.

## 13. Summary

In this lesson, we learned that automated testing is not just running a function and seeing its output; rather, it is defining a clear expectation about the function's behavior.

Main concepts:

- Identifying tests with names starting with `test_`
- Using `assert` to examine the result
- Examining valid and invalid inputs
- Testing boundary values
- Documenting the expected behavior of functions
- Running tests with `pytest`

In the DNS Lookup project, this file helps make the behavior of the three validation functions verifiable and repeatable against a set of specific inputs.
