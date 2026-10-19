[🇮🇷 فارسی](/02-dns_lookup/docs/fa/01-python-fundamentals/02-conditions.md)

# Lesson 2: Conditions and Decision-Making in Python

## Introduction

There is almost no real program that works without decision-making.

Programs must constantly check various conditions and make decisions based on the result.

For example, in the DNS Lookup project:

- Is the domain valid?
- Is the DNS record type valid?
- Has the user entered valid input?
- Has a result been received from DNS?

All of these decisions are made using conditional structures.

---

# The `if` Statement

The simplest decision-making structure in Python is `if`.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

Output:

```text
Adult
```

---

# How `if` Works

First, the condition is checked.

If the condition's result is:

```python
True
```

then the code inside the block runs.

If the result is:

```python
False
```

the code does not run.

Example:

```python
number = 5

if number > 10:
    print("Greater")
```

Output:

```text
(No output is produced)
```

---

# Indentation

Python uses indentation instead of curly braces.

Right:

```python
if True:
    print("Hello")
```

Wrong:

```python
if True:
print("Hello")
```

---

# Comparison Operators

Conditions are usually built with comparison operators.

Equal:

```python
==
```

Not equal:

```python
!=
```

Greater than:

```python
>
```

Less than:

```python
<
```

Greater than or equal to:

```python
>=
```

Less than or equal to:

```python
<=
```

Example:

```python
port = 53

if port == 53:
    print("DNS")
```

---

# The `else` Statement

Sometimes we want something else to happen when the condition is not met.

Example:

```python
port = 80

if port == 53:
    print("DNS")
else:
    print("Other Service")
```

Output:

```text
Other Service
```

---

# The `elif` Statement

Used to check several different cases.

Example:

```python
port = 443

if port == 80:
    print("HTTP")

elif port == 443:
    print("HTTPS")

else:
    print("Unknown")
```

Output:

```text
HTTPS
```

---

# The `and` Operator

For when several conditions must all be true at the same time.

Example:

```python
age = 25
verified = True

if age >= 18 and verified:
    print("Access Granted")
```

---

# The `or` Operator

If only one of the conditions is true.

Example:

```python
is_admin = False
is_owner = True

if is_admin or is_owner:
    print("Access Granted")
```

---

# The `not` Operator

Reversing the result of a condition.

Example:

```python
is_valid = False

if not is_valid:
    print("Invalid")
```

Output:

```text
Invalid
```

---

# Working with Strings

In the DNS Lookup project, we work a lot with strings.

Example:

```python
record_type = "A"

if record_type == "A":
    print("IPv4 Record")
```

---

# Membership in Collections

One of the important patterns we have used in the project:

```python
SUPPORTED_RECORD_TYPES = {
    "A",
    "AAAA",
    "MX",
    "NS",
    "TXT",
    "CNAME",
}
```

Checking membership:

```python
if record_type in SUPPORTED_RECORD_TYPES:
    print("Valid")
```

---

# Direct Connection to the Project

In the file:

```python
validator.py
```

we have the following function:

```python
def validate_record_type(record_type: str) -> bool:
    return record_type.upper() in SUPPORTED_RECORD_TYPES
```

Its logic:

1. It uppercases the input.

```python
record_type.upper()
```

2. It checks whether it exists in the list of allowed record types or not.

```python
in SUPPORTED_RECORD_TYPES
```

3. It returns the result as:

```python
True
```

or

```python
False
```

---

# Nested Conditions

Sometimes one condition is placed inside another.

Example:

```python
domain = "google.com"

if domain:
    if "." in domain:
        print("Looks Valid")
```

---

# Truthy and Falsy Values

In Python, some values are automatically equivalent to `False`.

Example:

```python
""
0
[]
{}
None
```

Example:

```python
records = []

if records:
    print("Found")
else:
    print("No Records")
```

Output:

```text
No Records
```

---

# Usage in DNS Lookup

In the file `formatter.py`, we have:

```python
if not results:
    return "No DNS records found."
```

If the results list is empty:

```python
[]
```

an appropriate message is displayed.

---

# Exercise

1. Create a variable named `record_type` and set its value to `"MX"`.

2. Check whether its value equals `"A"` or not.

3. Check whether its value exists in the following collection or not:

```python
{
    "A",
    "AAAA",
    "MX",
}
```

4. Write a program that, if the list is empty, prints:

```text
No Records
```

---

# Lesson Summary

In this lesson, we learned:

- `if`
- `else`
- `elif`
- Comparison operators
- `and`
- `or`
- `not`
- Membership checking with `in`
- Truthy and Falsy Values

These concepts are used extensively in the input validation and result processing parts of the DNS Lookup project.

In the next lesson, we will become familiar with Loops; a concept essential for processing a collection of DNS records.
