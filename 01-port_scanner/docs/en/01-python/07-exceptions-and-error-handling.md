[🇮🇷 فارسی](/01-port_scanner/docs/fa/01-python/07-exceptions-and-error-handling.md)

# Session 07 — Exceptions and Error Handling

# Why Is Error Handling Important?

There is no program in the world that always runs without errors.

It is possible that:

- The user enters invalid input.
- A file does not exist.
- The internet connection drops.
- The server does not respond.
- The target port is closed.

If we do not handle errors:

The program suddenly stops.

---

# A Simple Error

```python
number = int("hello")
```

Output:

```text
ValueError:
invalid literal for int()
```

The program stops.

---

# The Solution: `try` and `except`

```python
try:
    number = int("hello")
except ValueError:
    print("Invalid number")
```

Output:

```text
Invalid number
```

The program does not stop.

---

# Meaning of `try`

```python
try:
```

means:

> Execute this code.

---

# Meaning of `except`

```python
except:
```

means:

> If an error occurs, execute this part.

---

# A Real Example

```python
try:
    age = int(input("Age: "))
except:
    print("Please enter a number")
```

---

If the user types:

```text
abc
```

Output:

```text
Please enter a number
```

---

# Catching a Specific Type of Error

It is better to specify the type of error.

---

Wrong:

```python
except:
```

---

Better:

```python
except ValueError:
```

---

Example:

```python
try:
    age = int("hello")
except ValueError:
    print("Wrong value")
```

---

# Multiple Types of Errors

```python
try:
    ...
except ValueError:
    ...
except TypeError:
    ...
except FileNotFoundError:
    ...
```

---

Each error goes to its own specific block.

---

# Storing the Error in a Variable

```python
try:
    age = int("hello")
except ValueError as error:
    print(error)
```

Output:

```text
invalid literal for int()
```

---

# `finally`

Some code must always run.

Even if an error occurs.

---

Example:

```python
try:
    print("Start")
except:
    print("Error")
finally:
    print("Finished")
```

---

Output:

```text
Start
Finished
```

---

# Another Example

```python
try:
    int("abc")
except:
    print("Error")
finally:
    print("Finished")
```

Output:

```text
Error
Finished
```

---

# `finally` in the Real World

It is usually used for:

- Closing a file
- Closing a network connection
- Releasing resources

---

# What Is `raise`?

Sometimes we want to create an error ourselves.

---

Example:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

Output:

```text
ValueError:
Age cannot be negative
```

---

# A Real Example

```python
def validate_port(port):
    if port < 1 or port > 65535:
        raise ValueError("Invalid port")
```

---

This is exactly like the validations we have done in the Port Scanner.

---

# Well-Known Python Errors

---

# `ValueError`

Wrong value

```python
int("abc")
```

---

# `TypeError`

Wrong data type

```python
"5" + 5
```

---

# `FileNotFoundError`

File does not exist

```python
open("test.txt")
```

---

# `ZeroDivisionError`

Division by zero

```python
10 / 0
```

---

# `IndexError`

Invalid index

```python
items = [1, 2]

print(items[10])
```

---

# `KeyError`

Key does not exist

```python
data = {}

print(data["name"])
```

---

# Usage in the Port Scanner

One of the most important parts of our project:

---

Connecting to a port

```python
socket.connect()
```

---

It is possible that:

- A timeout occurs.
- The server does not respond.
- The port is closed.

---

That is why we use error-handling structures.

---

A simple example:

```python
try:
    socket.connect(...)
except OSError:
    return False
```

---

If this handling did not exist:

The first closed port would stop the entire program.

---

# A More Realistic Example

```python
def scan_port(ip, port):
    try:
        ...
        return True
    except OSError:
        return False
```

---

This same idea exists in most security tools in the world.

---

# A Common Mistake

Wrong:

```python
try:
    ...
except:
    pass
```

---

This hides the error.

Later, finding the problem becomes very hard.

---

Better:

```python
except OSError as error:
    print(error)
```

Or:

```python
logger.error(str(error))
```

---

# Connection to Our Project

In the Port Scanner project so far, we have:

✓ Validated inputs
✓ Handled network errors
✓ Controlled timeouts
✓ Made Banner Grabbing safe

---

All of these are built on top of error handling.

---

# What We Learned Today

✓ What an Exception is
✓ `try`
✓ `except`
✓ `finally`
✓ `raise`
✓ Common Python errors
✓ Handling network errors
✓ Direct connection to the Port Scanner

---

# Exercise

Write a function:

```python
def divide(a, b):
```

If the user enters zero:

```python
divide(10, 0)
```

Instead of crashing the program:

```text
Cannot divide by zero
```

should be displayed.

---

Next session:

**08-files-json-csv.md**

In the next session, we will learn how to read and save files — exactly what we have used for JSON and CSV outputs in the Port Scanner project.
