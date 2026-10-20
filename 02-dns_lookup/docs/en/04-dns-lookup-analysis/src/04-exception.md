[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/src/04-exception.md)

# Chapter Four: DNS Lookup Project Code Analysis

## Lesson 4: Designing Custom Exceptions in Python

### 1. Lesson Goal

In this lesson, we examine how to define custom exceptions for a project and, using inheritance, establish a relationship between general errors and specific errors.

### 2. Examining the `exception.py` Code

The content of the `src/exception.py` file:

```python
class DNSLookupError(Exception):
    pass


class DNSTimeoutError(DNSLookupError):
    pass
```

This code defines two classes:

- `DNSLookupError`: the base exception for errors related to the DNS Lookup tool
- `DNSTimeoutError`: a specific exception for the timeout condition of the DNS request

### 3. The `DNSLookupError` Class

```python
class DNSLookupError(Exception):
    pass
```

In Python, exceptions usually inherit from the base class `Exception` or one of its subclasses.

Here, `DNSLookupError` is defined as the base class for the project's custom errors.

The `pass` statement means that the class body currently does not define additional operations or features. This is completely valid; a custom class does not have to have a new method or feature to be useful.

The existence of this class has a design advantage: errors related to DNS can be grouped under a common type. As a result, other parts of the program can, if needed, manage errors of this family together.

### 4. The `DNSTimeoutError` Class

```python
class DNSTimeoutError(DNSLookupError):
    pass
```

This class inherits from `DNSLookupError`.

Therefore, the relationship between these two classes is as follows:

```text
Exception
    └── DNSLookupError
            └── DNSTimeoutError
```

`DNSTimeoutError` is considered a specific type of `DNSLookupError`; that is, every `DNSTimeoutError` exception, in terms of type, is also a member of the `DNSLookupError` family.

This relationship is established using inheritance and does not need to override the base `Exception` behavior.

### 5. Why Do We Use Custom Exceptions?

Suppose different parts of the program encounter DNS-related errors. If all errors are managed only with text messages, distinguishing the error type might become difficult.

Custom exceptions allow the program to decide based on the error type, not just its message text.

For example:

```python
try:
    # اجرای عملیات DNS
    ...
except DNSTimeoutError:
    print("درخواست DNS در مهلت تعیین‌شده کامل نشد.")
```

This code snippet is only an educational example of how to manage exceptions; the ellipsis replaces the actual operation.

### 6. An Important Advantage of the Exception Hierarchy

Given the inheritance defined in this file, both the specific error and the more general error can be managed in two ways.

**Managing Only the Timeout:**

```python
try:
    ...
except DNSTimeoutError:
    print("مهلت درخواست DNS به پایان رسید.")
```

**Managing All Custom Errors of the DNS Family:**

```python
try:
    ...
except DNSLookupError:
    print("خطایی در عملیات DNS رخ داد.")
```

In the second case, `DNSTimeoutError` is also caught; because it is a subclass of `DNSLookupError`.

This feature allows the program to choose between detailed and general error management, depending on the need.

### 7. How This File Relates to `resolver.py`

In the `resolver.py` file, the `DNSTimeoutError` class is imported and used when receiving the `dns.resolver.LifetimeTimeout` error:

```python
except dns.resolver.LifetimeTimeout as exc:
    raise DNSTimeoutError("DNS query timed out") from exc
```

In this path, the specific error of the `dnspython` library is converted into the project's custom exception.

Using `from exc` also preserves the original cause of the error so that the exception chain is available when examining the error.

These two files together show how external library errors can be converted into an error interface belonging to the project itself.

### 8. Is It Necessary for Every Exception to Have a Custom Message?

No. The current classes are defined with `pass` and inherit the base behavior of `Exception`. When creating an instance of these classes, you can pass the desired message to the constructor:

```python
error = DNSTimeoutError("DNS query timed out")
print(error)
```

Output:

```text
DNS query timed out
```

Therefore, defining simple exceptions does not require writing an `__init__` method; unless the project needs additional specific behavior or information.

### 9. Practice Exercises

**Exercise 1 — Examining Inheritance**

Predict the output of each statement and then run the code:

```python
error = DNSTimeoutError("Request timed out")

print(isinstance(error, DNSTimeoutError))
print(isinstance(error, DNSLookupError))
print(isinstance(error, Exception))
```

**Exercise 2 — General and Specific Management**

Explain why `except DNSLookupError` can also catch `DNSTimeoutError`.

**Exercise 3 — Extending the Design**

Suppose an error for an invalid DNS response is to be added. Choose an appropriate name for its class and specify which class it is better to inherit from. Explain your answer according to the current hierarchy.

### 10. Summary

The `exception.py` file, with two simple classes, creates an extensible structure for error management:

- `DNSLookupError` is the base class for the project's custom errors.
- `DNSTimeoutError` displays a specific type of DNS error.
- Inheritance allows errors to be managed both specifically and at the level of a family.
- This design reduces the program logic's dependence on the names of external library exceptions.

The simplicity of this file is its strength: its responsibility is only to define the project's error types, and it performs this responsibility clearly and directly.
