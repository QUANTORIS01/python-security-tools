[🇮🇷 فارسی](/02-dns_lookup/docs/fa/01-python-fundamentals/08-exception-handling.md)

# Lesson 8: Exception Handling in Python

## What Is an Exception?

During program execution, errors may occur that are predictable.

For example:

- A file does not exist.
- A network connection is not established.
- The user enters an invalid value.
- A DNS request fails.

These types of runtime errors are called **Exceptions** in Python.

---

## The Problem Without Exception Handling

Example:

```python
number = int(input("Enter a number: "))
print(number)
```

If the user types:

```text
abc
```

the program stops:

```text
ValueError: invalid literal for int()
```

In this case, the program crashes and its execution ends.

---

## The `try` / `except` Structure

To handle errors, we use `try` and `except` blocks.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number")
```

If the input is valid:

```text
10
```

Output:

```text
10
```

If the input is invalid:

```text
abc
```

Output:

```text
Invalid number
```

The program continues without crashing.

---

## How `try` Works

Any code that might raise an error is placed inside the `try` block.

```python
try:
    risky_operation()
```

If no error occurs:

```text
try
↓
program continues
```

If an error occurs:

```text
try
↓
Exception
↓
except
↓
program continues
```

---

## Catching a Specific Type of Error

Example:

```python
try:
    value = int("abc")
except ValueError:
    print("Value Error")
```

Output:

```text
Value Error
```

Only the `ValueError` is caught.

---

## Multiple `except` Blocks

We can handle several types of errors separately.

```python
try:
    number = int(input())
    result = 10 / number

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

Input:

```text
abc
```

Output:

```text
Invalid number
```

Input:

```text
0
```

Output:

```text
Cannot divide by zero
```

---

## Catching Multiple Exceptions in One `except`

```python
try:
    operation()

except (ValueError, TypeError):
    print("Input error")
```

---

## The Exception as a Variable

Sometimes we want to see the details of the error.

```python
try:
    value = int("abc")

except ValueError as error:
    print(error)
```

Output:

```text
invalid literal for int() with base 10: 'abc'
```

---

## A General `except`

```python
try:
    operation()

except Exception as error:
    print(error)
```

This approach catches almost all the usual Exceptions.

But it should not always be used.

It is better to handle specific Exceptions as much as possible.

---

## The `else` Block

The code inside `else` runs only when no error has occurred.

```python
try:
    number = int(input())

except ValueError:
    print("Invalid")

else:
    print("Valid number")
```

---

## The `finally` Block

The code inside `finally` always runs.

Whether an Exception occurred or not.

```python
try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found")

finally:
    print("Finished")
```

---

## A Practical File Example

```python
try:
    file = open("data.txt")

except FileNotFoundError:
    print("Missing file")

finally:
    print("Cleanup")
```

Output:

```text
Missing file
Cleanup
```

---

## Exception Raising

Sometimes we intentionally raise an Exception ourselves.

```python
raise ValueError("Invalid input")
```

Output:

```text
ValueError: Invalid input
```

---

## A Practical Example

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

---

## Connection to the DNS Lookup Project

In the file `resolver.py`, we used Exception Handling exactly.

Example:

```python
try:
    answers = dns.resolver.resolve(
        domain,
        record_type,
    )

except dns.resolver.NXDOMAIN:
    return []
```

---

## Important Errors We Handled in the Project

### NXDOMAIN

The domain does not exist.

```python
dns.resolver.NXDOMAIN
```

Example:

```text
does-not-exist-example.com
```

---

### NoAnswer

The domain exists but has no record of the requested type.

```python
dns.resolver.NoAnswer
```

Example:

```text
google.com CNAME
```

---

### NoNameservers

The DNS server did not provide a proper response.

```python
dns.resolver.NoNameservers
```

---

### LifetimeTimeout

The DNS request did not receive a response in time.

```python
dns.resolver.LifetimeTimeout
```

---

## The Final Version of the Project

```python
try:
    answers = dns.resolver.resolve(
        domain,
        record_type,
    )

    return [str(answer) for answer in answers]

except (
    dns.resolver.NXDOMAIN,
    dns.resolver.NoAnswer,
    dns.resolver.NoNameservers,
    dns.resolver.LifetimeTimeout,
):
    return []
```

Instead of the program crashing:

```text
Traceback ...
```

the user receives a clean and manageable result.

---

## Best Practices

✅ Catch specific Exceptions.

✅ Display an appropriate error message to the user.

✅ Use `finally` to release resources.

✅ Use `raise` for validation.

❌ Do not hide all errors with `except Exception` for no reason.

❌ Do not ignore errors without a log or an appropriate message.

---

## Summary

In this lesson, we learned:

- What an Exception is.
- Why programs crash.
- How to use `try` and `except`.
- How to use `else` and `finally`.
- How to raise an Exception with `raise`.
- How to handle DNS errors in the DNS Lookup project.
- Professional error-handling principles in real programs.

Exception Handling is one of the most important tools for building stable and professional software, and it is used in almost all real Python projects.
