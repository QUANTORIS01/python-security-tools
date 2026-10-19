[🇮🇷 فارسی](/02-dns_lookup/docs/fa/01-python-fundamentals/01-variables-and-data-types.md)

# Lesson 1: Variables and Data Types in Python

## Introduction

Every program we write must be able to store and process information.

In the DNS Lookup project, too, we deal with various pieces of information, such as:

- A domain name
- A DNS record type
- Returned values
- Various program states

To hold this information, we use **Variables**.

---

# What Is a Variable?

A variable is a name that refers to a value in memory.

Example:

```python
domain = "google.com"
```

In this example:

- `domain` is the name of the variable.
- `"google.com"` is the value stored in it.

---

# Creating a Variable

In Python, there is no need to declare the variable's type before using it.

Example:

```python
name = "Ali"
age = 25
```

Python automatically detects the data type.

---

# The Main Data Types

Python has various data types, but in this project, we mostly deal with a few main ones.

---

## String

Used to hold text.

Example:

```python
domain = "google.com"
record_type = "A"
```

In the DNS Lookup project, almost all user inputs are first received as strings.

Example:

```python
python -m src.cli google.com A
```

Values:

```python
domain = "google.com"
record_type = "A"
```

---

## Integer

Used to hold whole numbers.

Example:

```python
count = 5
```

Common examples:

```python
records_found = 10
```

---

## Float

Used for numbers with a decimal part.

Example:

```python
timeout = 2.5
```

---

## Boolean

Has only two values:

```python
True
False
```

Example:

```python
is_valid = True
```

In our project, the validation functions use this type.

Example:

```python
validate_domain("google.com")
```

Output:

```python
True
```

---

# Checking the Data Type

To see a variable's type, we use the function `type()`.

Example:

```python
domain = "google.com"

print(type(domain))
```

Output:

```python
<class 'str'>
```

Another example:

```python
number = 10

print(type(number))
```

Output:

```python
<class 'int'>
```

---

# Type Conversion

Sometimes we need to convert one data type into another.

Example:

```python
number = "10"

converted = int(number)
```

Now:

```python
converted
```

equals:

```python
10
```

of type:

```python
int
```

---

# Variable Naming

It is better for variable names to be meaningful.

Good:

```python
domain
record_type
dns_server
```

Weak:

```python
x
a
test
```

---

# Naming Rules

A variable name:

- Must not start with a digit.
- Must not contain spaces.
- Must not use Python reserved keywords.

Wrong:

```python
1domain = "google.com"
```

Wrong:

```python
record type = "A"
```

Right:

```python
record_type = "A"
```

---

# Naming Style in the Project

In the DNS Lookup project, we have used the:

```python
snake_case
```

style.

Example:

```python
record_type
validate_domain
lookup_record
build_dns_results
```

This style is the standard recommended by PEP 8.

---

# How This Relates to the DNS Lookup Project

In the real project, we will encounter variables similar to the following:

```python
domain = "google.com"
record_type = "A"
```

And then:

```python
lookup_record(
    domain,
    record_type,
)
```

Here:

- `domain` is a string.
- `record_type` is a string.
- The function's result will be a list of strings.

---

# Exercise

1. Create a variable named `domain` and store the value `"example.com"` in it.

2. Create a variable named `record_type` and set its value to `"MX"`.

3. Use `type()` to display the type of both variables.

4. Create a variable named `records_found` and store the value `5` in it.

5. Check what type `records_found` is.

---

# Lesson Summary

In this lesson, we learned:

- What a variable is.
- How to create a variable.
- What the main data types in Python are.
- How to check a data type.
- What the rules for naming variables are.
- How these concepts are used in the DNS Lookup project.

In the next lesson, we will become familiar with decision-making structures (`if`, `elif`, `else`); concepts that play an important role in validating the project's inputs.
