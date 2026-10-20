[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/src/02-validator.md)

# Chapter Four: DNS Lookup Project Code Analysis

## Lesson 2: Input Validation in Python

### 1. Lesson Goal

In this lesson, we will learn:

- Why input validation matters in network tools.
- How to examine a domain's format with a Regular Expression.
- How to validate the `timeout` value.
- How to compare a DNS record type against a set of allowed values.
- Why an input being valid in terms of format does not necessarily mean it is valid in the real world.

### 2. File Structure

The `src/validator.py` file contains a set of supported record types and three validation functions:

```python
import re

SUPPORTED_RECORD_TYPES = {
    'A',
    'AAAA',
    'MX',
    'NS',
    'TXT',
    'CNAME',
}
```

The `re` module provides tools for working with regular expressions. In this file, it is used to examine the format of a domain name.

The variable `SUPPORTED_RECORD_TYPES` is of type `set` and holds six DNS record types. A set is suitable for holding unique values, and checking membership in it is also simple.

Note: The existence of a record type in this set tells us that its validation is supported in this file; it does not by itself prove that all record types are correctly resolved or processed in all parts of the program.

### 3. Validating the Domain Name

The first function:

```python
def validate_domain(domain: str) -> bool:
    """
    Validate a domain name.
    """
    pattern = (
        r'^(?!-)'
        r'(?:[A-Za-z0-9-]{1,63}\.)+'
        r'[A-Za-z]{2,63}$'
    )
    return bool(re.fullmatch(pattern, domain))
```

#### Understanding the Function Signature

```python
def validate_domain(domain: str) -> bool:
```

- `domain: str` is a type hint indicating that the expected input is a string.
- `-> bool` indicates that the function is intended to return a boolean value to declare the result.
- These type hints alone do not enforce the input type at runtime.

#### How Does the Regular Expression Work?

The defined pattern consists of several parts:

| Pattern Part | Concept |
|---|---|
| `^` | Beginning of the string |
| `(?!-)` | At the start of the string, there must be no hyphen |
| `[A-Za-z0-9-]{1,63}` | One to 63 characters of English letters, digits, or hyphens |
| `\.` | A literal dot |
| `(?: ... )+` | A group without separate capture that is repeated one or more times |
| `[A-Za-z]{2,63}` | At the final part, two to 63 English letters |
| `$` | End of the string |

The function `re.fullmatch()` checks that the entire string matches the pattern. Then `bool()` converts the match result into `True` or `False`.

For example:

```python
print(validate_domain("example.com"))
print(validate_domain("api.example.com"))
print(validate_domain("-example.com"))
print(validate_domain("example"))
```

Expected output:

```text
True
True
False
False
```

The first two examples are accepted according to the current pattern. The third example starts with a hyphen, and the fourth has no dot and a separate final part.

#### An Important Limitation of This Validation

This function performs a pattern-based check; it is not a complete implementation of the domain name standard.

For example, the current pattern might accept some invalid names:

```python
print(validate_domain("exa_mple.com"))
print(validate_domain("example-.com"))
```

In these two cases, the function's result is `True`; because the pattern does not prohibit a hyphen at the end of a label, and in the middle parts it does not apply the full constraints of domain name rules.

Also, because the final part only accepts English letters, some international domain names written in Unicode form are not directly accepted.

**Result:** This function is a format check with specific limitations; it should not be considered a guarantee of the domain's existence, DNS validity, or the reachability of the target server.

### 4. Validating the Timeout

The second function:

```python
def validate_timeout(timeout: float) -> bool:
    """
    Validate DNS query timeout.
    """
    return timeout > 0
```

This function checks that the `timeout` value is greater than zero.

```python
print(validate_timeout(3.0))
print(validate_timeout(0))
print(validate_timeout(-1))
```

Output:

```text
True
False
False
```

The timeout specifies how long an operation is allowed to wait for a response. A zero or negative value is usually not suitable for such a setting; this function checks exactly this condition.

But this function does not check other limitations. For example, if the input is `float('inf')`, the comparison `timeout > 0` yields `True`. Also, `NaN` does not yield a positive comparison result and therefore returns `False`.

Important note: The `float` type hint does not guarantee that the input is actually a float at runtime. In this function, the input type is not explicitly checked.

If a stricter validation is to be implemented, it must be specified whether infinite values, `NaN`, strings, and other types of input are allowed or not.

### 5. Validating the DNS Record Type

The third function:

```python
def validate_record_type(record_type: str) -> bool:
    """
    Validate DNS record type.
    """
    return record_type.upper() in SUPPORTED_RECORD_TYPES
```

This function first uses `upper()` to convert the input letters to uppercase, and then checks the value's membership in the `SUPPORTED_RECORD_TYPES` set.

```python
print(validate_record_type("A"))
print(validate_record_type("aaaa"))
print(validate_record_type("MX"))
print(validate_record_type("SOA"))
```

Output:

```text
True
True
True
False
```

Due to the use of `upper()`, inputs like `"aaaa"` are also accepted; of course, only when the converted value exists in the allowed set.

This approach prevents repeating separate comparisons and keeps the set of acceptable values in one place.

However, the function only checks membership in the set. For example, it does not check the input type before calling `upper()`; therefore, passing a value like `None` would cause an error.

### 6. How the Three Functions Relate to Software Security

Input validation is one of the important parts of secure development; because inappropriate input might cause errors, unexpected behavior, or inappropriate resource consumption.

In this file, we have three separate controls:

- **Domain name:** Format check with a regular expression
- **Timeout:** Checking that the value is positive
- **Record type:** Checking membership in the set of allowed values

These controls are useful, but they are not substitutes for error management, validation in other layers, or examination of the actual result of the DNS operation.

For example, a valid format for `example.com` does not guarantee that the domain exists. Similarly, accepting the `A` record type does not guarantee that the domain in question has an `A` record.

### 7. Practice Exercises

**Exercise 1 — Domain Examination**

Using `validate_domain()`, predict the result of the following inputs and then verify by running the code:

```python
domains = [
    "example.com",
    "sub.example.org",
    "-example.com",
    "example-.com",
    "localhost",
    "example.c",
]

for domain in domains:
    print(domain, validate_domain(domain))
```

Explain why each case's result is as it is according to the current regular expression.

**Exercise 2 — Timeout Examination**

```python
timeouts = [1, 0.5, 0, -2]

for timeout in timeouts:
    print(timeout, validate_timeout(timeout))
```

What condition causes some values to be accepted and some to be rejected?

**Exercise 3 — Record Type**

```python
record_types = ["A", "aaaa", "TXT", "SOA", "cname"]

for record_type in record_types:
    print(record_type, validate_record_type(record_type))
```

Explain the role of `upper()` and why `SOA`, despite being known as a DNS record type, is not accepted in this implementation.

**Exercise 4 — Designing Better Validation**

Without changing the project's main code, suggest how the `validate_timeout()` function could be extended to also reject non-finite values. For this, read about the `math.isfinite()` function in the official Python documentation.

### 8. Summary

In this lesson, we examined the `validator.py` file and became familiar with three validation approaches:

1. Using `re.fullmatch()` to check string format
2. Using numerical comparison to control the positivity of `timeout`
3. Using `upper()` and `set` to check the DNS record type

The most important point is that **validation is only as accurate as the rules defined in the code**. When examining security code, in addition to the success path, boundary inputs, unexpected values, and the limitations of each method must also be examined.
