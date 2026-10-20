[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/src/03-resolver.md)

# Chapter Four: DNS Lookup Project Code Analysis

## Lesson 3: Executing DNS Requests and Managing Errors in Python

### 1. Lesson Goal

In this lesson, we examine the `src/resolver.py` file; the part that implements the main logic of looking up DNS records.

By the end of the lesson, you will become familiar with the following concepts:

- Using the `dnspython` library to send DNS requests
- Converting responses into strings usable in other parts of the program
- Managing common errors during DNS lookups
- Defining and chaining custom exceptions
- Designing a function that returns the lookup result in a simple and specific form

### 2. Importing Dependencies

At the top of the file:

```python
import dns.resolver

from .exception import DNSTimeoutError
```

The first line imports the `dns.resolver` module from the `dnspython` library. This module is used to perform DNS requests and receive their responses.

The second line imports the custom `DNSTimeoutError` exception from the project's internal module. Using a custom exception allows the program to manage the DNS request timeout error with a specific name related to the project's logic.

This separation clarifies the role of the two parts:

- The external library performs the DNS operation.
- The project manages the selected errors in a form suitable for its own logic.

### 3. The `lookup_record()` Function

The function code:

```python
def lookup_record(domain: str, record_type: str) -> list[str]:
    """
    Lookup DNS records.
    """
```

This function receives two inputs:

- `domain`: the name of the domain to be examined.
- `record_type`: the requested record type, such as `A` or `MX`.

The output type is specified with `list[str]`; meaning the function returns a list of strings.

This output contract allows other parts of the program to receive the DNS response without directly working with the `dnspython` library's response objects.

Note: This type hint describes the function's expected contract and does not by itself guarantee the value types at runtime.

### 4. Sending the DNS Request

The main part of the operation:

```python
answers = dns.resolver.resolve(domain, record_type)
return [str(answer) for answer in answers]
```

In the first line, the `dns.resolver.resolve()` function performs the DNS request for the specified domain and record type.

If a response is received, the `answers` variable holds the set of responses from the request.

The second line uses **List Comprehension**:

```python
[str(answer) for answer in answers]
```

This expression iterates over the responses and converts each response to a string with `str()`. Finally, a list of strings is returned to the caller.

For example, a hypothetical response for an `A` record might be displayed as a string like `192.0.2.10`. This is only a sample of the response format; the actual result depends on the domain and the DNS response.

This method makes the function's output simple and uniform and keeps the details of the library's internal objects away from consumers of this function.

### 5. Managing Request Timeout

The next part:

```python
except dns.resolver.LifetimeTimeout as exc:
    raise DNSTimeoutError('DNS query timed out') from exc
```

Sometimes the DNS request does not complete within the specified time limit. The `dnspython` library can raise the `LifetimeTimeout` exception in this situation.

This code catches the library's error and creates a custom exception called `DNSTimeoutError`.

The following expression is especially important:

```python
raise DNSTimeoutError('DNS query timed out') from exc
```

Using `from exc` preserves the original exception as the cause of the new exception. This capability is called **Exception Chaining** in Python.

As a result, the program can receive the project's custom error while also preserving the information about the original cause of the error for technical examination.

This design has an important advantage: other parts of the program can manage an error meaningful at the project's own level, instead of depending directly on the external library's error name.

### 6. Managing Failed or Empty Responses

The last part:

```python
except (
    dns.resolver.NXDOMAIN,
    dns.resolver.NoAnswer,
    dns.resolver.NoNameservers,
):
    return []
```

In this part, three conditions are managed:

| Exception | Meaning |
|---|---|
| `NXDOMAIN` | The domain name does not exist in DNS. |
| `NoAnswer` | For the performed request, the requested record's response is not available. |
| `NoNameservers` | The name servers used could not provide a usable response for the request. |

In this implementation, all three conditions are converted into one result: an empty list.

```python
return []
```

This decision keeps the function's output contract simple; the caller receives an empty list in these cases instead of receiving an exception.

However, the three conditions are not semantically identical. If another part of the program needs to distinguish between "the domain does not exist" and "the name server did not give an appropriate response," this information must be provided to that part through appropriate design.

The important point is that the current code converts exactly these three exceptions into an empty list. From this, one should not conclude that all possible DNS errors are managed in this part.

### 7. The Function's Execution Path

The general behavior of `lookup_record()` can be summarized like this:

1. The domain and record type are given to the function.
2. The function performs the DNS request.
3. If a response is received, the responses are converted to strings and returned as a list.
4. If the request encounters `LifetimeTimeout`, the custom error `DNSTimeoutError` is raised.
5. If one of the three exceptions `NXDOMAIN`, `NoAnswer`, or `NoNameservers` occurs, an empty list is returned.

Therefore, the function's behavior in different states is clear, and other parts of the program can interact with the lookup result based on this contract.

### 8. How `resolver.py` Relates to `validator.py`

In the previous lesson, we examined the domain and record type validation functions. In this file, `lookup_record()` directly performs the DNS request.

The architectural point is that, in the current code of `resolver.py`, the functions `validate_domain()` and `validate_record_type()` are not called. Therefore, one should not assume that this file by itself validates the inputs according to the same validation rules.

This separation can be useful: input validation and executing the DNS request are two different responsibilities. To understand the complete execution path of the program, the files that call this function must also be examined.

### 9. Practice Exercises

**Exercise 1 — Converting Responses**

Examine the following expression and explain why `str()` is used:

```python
[str(answer) for answer in answers]
```

Then rewrite it with a regular `for` loop.

**Exercise 2 — Exception Chaining**

Explain the difference between these two statements:

```python
raise DNSTimeoutError("DNS query timed out")
```

```python
raise DNSTimeoutError("DNS query timed out") from exc
```

**Exercise 3 — Output Contract**

Why can returning `[]` for some failed responses make using the function simpler? In what conditions does preserving the difference between different errors matter?

**Exercise 4 — Examining the Call Path**

By examining other files of the project, determine which part of the program calls `lookup_record()` and whether input validation is performed before it or not.

### 10. Summary

The `resolver.py` file is the core of executing the DNS request in this part of the project. Its design has several important points:

- Using `dnspython` to perform the DNS request
- Providing responses in the `list[str]` form
- Converting the timeout error into the project's custom exception
- Preserving the original error cause using `raise ... from exc`
- Managing several specific DNS conditions by returning an empty list

This file is a suitable example of separating the operation execution logic from the details of managing the errors of an external library.
