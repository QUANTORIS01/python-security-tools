[🇮🇷 فارسی](/01-port_scanner/docs/fa/01-python/03-variables-and-data-types.md)

# Session 03 — Variables and Data Types

## Introduction

Suppose we want to store an IP address inside a program:

```python
127.0.0.1
```

or a port number:

```python
80
```

or the name of a service:

```python
http
```

The computer must keep this information somewhere so we can use it later.

This is where the concept of a **Variable** comes in.

---

# What Is a Variable?

A variable is a place for storing information in the computer's memory.

Example:

```python
ip = "127.0.0.1"
```

In this example:

- `ip` is the name of the variable.
- `=` is the assignment operator.
- `"127.0.0.1"` is the value being stored.

---

## A Real Example

Suppose we want to store the target IP:

```python
target_ip = "192.168.1.1"
```

Later, we can use it:

```python
print(target_ip)
```

Output:

```text
192.168.1.1
```

---

# Why Do We Need Variables?

Without variables, we would have to repeat everything many times.

Bad:

```python
print("192.168.1.1")
print("192.168.1.1")
print("192.168.1.1")
```

Better:

```python
ip = "192.168.1.1"

print(ip)
print(ip)
print(ip)
```

---

# Variable Naming Rules

A variable name must:

✅ Start with a letter

```python
ip = "127.0.0.1"
```

✅ May contain digits

```python
port80 = 80
```

✅ May contain `_`

```python
target_ip = "127.0.0.1"
```

---

Examples of invalid names:

```python
1port = 80
```

```python
target-ip = "127.0.0.1"
```

```python
class = "python"
```

---

# What Are Data Types?

Not all information is the same.

A number is different from text.

Text is different from true/false.

That is why Python has different data types.

---

# String

Used to store text.

Example:

```python
service = "http"
```

or:

```python
banner = "Apache Server"
```

---

Checking the data type:

```python
print(type(service))
```

Output:

```text
<class 'str'>
```

---

# Integer

Used to store whole numbers (without decimals).

Example:

```python
port = 80
```

```python
workers = 100
```

---

Checking the data type:

```python
print(type(port))
```

Output:

```text
<class 'int'>
```

---

# Float

Used to store decimal numbers.

Example:

```python
timeout = 0.5
```

---

Checking the data type:

```python
print(type(timeout))
```

Output:

```text
<class 'float'>
```

---

# Boolean

Used to store true or false.

Values:

```python
True
```

and

```python
False
```

Example:

```python
is_open = True
```

---

In the Port Scanner project:

```python
is_port_open = True
```

Which means:

```text
This port is open.
```

---

Checking the data type:

```python
print(type(is_open))
```

Output:

```text
<class 'bool'>
```

---

# Changing a Variable's Value

A variable's value can change.

```python
port = 80
```

Then:

```python
port = 443
```

Now the variable's value is:

```text
443
```

---

# Printing Multiple Variables

```python
ip = "127.0.0.1"
port = 80

print(ip, port)
```

Output:

```text
127.0.0.1 80
```

---

# A Real Example from the Port Scanner Project

An example similar to what we use in the project:

```python
target_ip = "127.0.0.1"
port = 80
service = "http"
timeout = 0.5
is_open = True
```

Each variable holds specific information.

---

# How This Lesson Connects to the Project

In the Port Scanner project, we constantly deal with variables.

Example:

```python
ip
```

for the target IP.

---

```python
port
```

for the port number.

---

```python
service
```

for the service name.

---

```python
timeout
```

for the wait time.

---

```python
banner
```

for the information received from the service.

---

# Summary

✅ A variable is a place for storing information.

✅ We use `=` to store a value.

✅ The most important data types:

- `str`
- `int`
- `float`
- `bool`

✅ The Port Scanner project heavily uses variables.

---

# Exercise

Create the following variables:

```python
target_ip
port
service
timeout
```

Then display all of them using `print()`.
