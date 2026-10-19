[🇮🇷 فارسی](/02-dns_lookup/docs/fa/01-python-fundamentals/04-functions.md)

# Lesson 4: Functions in Python

## Introduction

If we want to write a professional, maintainable, and testable program, we cannot place all the code back-to-back in a single file.

Instead, we divide the code into smaller parts, each with a specific task.

These smaller parts are called **Functions** in Python.

In fact, almost the entire DNS Lookup project is built on top of functions.

For example:

```python
validate_domain()
```

```python
validate_record_type()
```

```python
lookup_record()
```

```python
build_dns_results()
```

```python
format_dns_results()
```

are all functions.

---

# What Is a Function?

A function is a set of instructions written to perform a specific task.

Example:

```python
def greet():
    print("Hello")
```

Running the function:

```python
greet()
```

Output:

```text
Hello
```

---

# The Structure of a Function

A function usually consists of the following parts:

```python
def function_name():
    pass
```

Its components:

```python
def
```

the keyword for defining a function

```python
function_name
```

the function name

```python
()
```

the parameters

```python
:
```

the beginning of the function body

---

# Parameters

A function can receive input.

Example:

```python
def greet(name):
    print(f"Hello {name}")
```

Usage:

```python
greet("Ali")
```

Output:

```text
Hello Ali
```

---

# Multiple Parameters

Example:

```python
def add(a, b):
    print(a + b)
```

Usage:

```python
add(10, 20)
```

Output:

```text
30
```

---

# Return Value

Most functions do not just print something.

Rather, they return a result.

Example:

```python
def add(a, b):
    return a + b
```

Usage:

```python
result = add(10, 20)
print(result)
```

Output:

```text
30
```

---

# The Difference Between `print` and `return`

A common mistake:

```python
def add(a, b):
    print(a + b)
```

In this case:

```python
result = add(10, 20)
```

the value of:

```python
result
```

will be:

```python
None
```

Because the function has not returned anything.

---

# Type Hints

In the project, we have used Type Hints.

Example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Meaning:

- `a` is an integer.
- `b` is an integer.
- The output is an integer.

---

# An Example from the Project

In the file:

```python
validator.py
```

we have:

```python
def validate_timeout(
    timeout: float
) -> bool:
    return timeout > 0
```

Meaning:

Input:

```python
float
```

Output:

```python
bool
```

---

# Multiple Return Values

Python can return several values at the same time.

Example:

```python
def get_user():
    return "Ali", 25
```

Usage:

```python
name, age = get_user()
```

---

# Functions Without Parameters

Example:

```python
def show_banner():
    print("DNS Lookup")
```

Usage:

```python
show_banner()
```

---

# Functions with Default Values

Example:

```python
def greet(name="User"):
    print(f"Hello {name}")
```

Usage:

```python
greet()
```

Output:

```text
Hello User
```

---

# Scope

A variable inside a function is only accessible inside that function.

Example:

```python
def test():
    name = "Ali"
```

This code raises an error:

```python
print(name)
```

Because the variable does not exist outside the function.

---

# Docstring

In the project, we have used Docstrings for all functions.

Example:

```python
def lookup_record(
    domain: str,
    record_type: str,
) -> list[str]:
    """
    Lookup DNS records.
    """
```

Advantages:

- Better documentation
- Greater readability
- Automatic generation of documentation

---

# Direct Connection to `validator.py`

The function:

```python
def validate_domain(
    domain: str
) -> bool:
```

Task:

- Receive a domain
- Validate it
- Return `True` or `False`

---

# Direct Connection to `resolver.py`

The function:

```python
def lookup_record(
    domain: str,
    record_type: str,
) -> list[str]:
```

Task:

- Send a DNS request
- Receive the response
- Convert the response into a list of strings

---

# Direct Connection to `results.py`

The function:

```python
def build_dns_results(
    domain: str,
    record_type: str,
) -> list[DNSRecord]:
```

Task:

- Receive raw DNS data
- Convert it into the `DNSRecord` model

---

# Direct Connection to `formatter.py`

The function:

```python
def format_dns_results(
    results: list[DNSRecord],
) -> str:
```

Task:

- Receive the results
- Produce output ready for display in the terminal

---

# An Important Design Principle

Each function should have only one specific responsibility.

A good example:

```python
validate_domain()
```

only validates the domain.

A good example:

```python
lookup_record()
```

only performs a DNS query.

This is exactly the famous principle:

```text
Single Responsibility Principle
```

---

# Why Did We Design the Project Around Functions?

Advantages:

- Easier testing
- Greater readability
- Simpler maintenance
- Easier extension
- Fewer errors

That is why almost every file in the project is a collection of small, independent functions.

---

# Exercise

1. Write a function that receives a domain name and prints it.

2. Write a function that receives two numbers and returns their sum.

3. Write a function that receives a `Timeout` value and returns `True` if it is greater than zero.

4. Write a Docstring for one of the above functions.

5. Add a Type Hint for one of the above functions.

---

# Lesson Summary

In this lesson, we learned:

- Defining a function
- Parameters
- Return value
- The difference between `print` and `return`
- Type Hints
- Scope
- Docstring
- Single Responsibility Principle

These concepts are the main foundation of the DNS Lookup project's architecture, and almost all the project's files are built on them.

In the next lesson, we will become familiar with Modules and Imports; a concept that explains why we divided the project into multiple files.
