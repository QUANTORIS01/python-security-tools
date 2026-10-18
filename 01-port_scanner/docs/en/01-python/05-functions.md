[🇮🇷 فارسی](/01-port_scanner/docs/fa/01-python/05-functions.md)

# Session 05 — Functions

# Why Do We Need Functions?

Suppose we are going to write a port scanner.

If we were to rewrite all the code every time we scan a port, the program would become very large and unmanageable.

That is why we use **Functions**.

A function means:

> A piece of code that performs a specific task, and we can call it whenever we want.

---

# The First Function

```python
def say_hello():
    print("Hello")
```

---

# Meaning of the Code

```python
def
```

is the keyword for creating a function.

---

```python
say_hello
```

is the name of the function.

---

```python
()
```

is where the function's inputs go.

---

```python
:
```

marks the beginning of the function body.

---

```python
print("Hello")
```

is the code that will run when the function is executed.

---

# Calling a Function

```python
def say_hello():
    print("Hello")

say_hello()
```

Output:

```text
Hello
```

---

# What Happens If We Don't Call the Function?

```python
def say_hello():
    print("Hello")
```

No output is produced.

Because the function has only been defined.

It has not been executed.

---

# Input (Parameter)

Often a function needs to receive information.

Example:

```python
def greet(name):
    print(f"Hello {name}")
```

---

Usage:

```python
greet("Ali")
greet("Sara")
```

Output:

```text
Hello Ali
Hello Sara
```

---

# Multiple Inputs

```python
def add(a, b):
    print(a + b)
```

---

Usage:

```python
add(5, 10)
```

Output:

```text
15
```

---

# Returning a Value

Many beginners think `print` and `return` are the same.

But they are completely different.

---

# `print`

Only displays.

```python
def add(a, b):
    print(a + b)
```

---

# `return`

Returns the value.

```python
def add(a, b):
    return a + b
```

---

Usage:

```python
result = add(5, 10)

print(result)
```

Output:

```text
15
```

---

# Why Is `return` Important?

In the Port Scanner project, we use it almost everywhere.

Example:

```python
def validate_ip(ip):
    return True
```

---

Or:

```python
def scan_port(ip, port):
    return True
```

---

Or:

```python
def detect_service(port):
    return "http"
```

---

All of these functions must return a result.

---

# Default Value

```python
def greet(name="Guest"):
    print(f"Hello {name}")
```

---

Usage:

```python
greet()
```

Output:

```text
Hello Guest
```

---

And:

```python
greet("Ali")
```

Output:

```text
Hello Ali
```

---

# Small Functions Are Better

Wrong:

```python
def scanner():
    # 200 lines of code
```

---

Right:

```python
def validate_ip():
    pass

def scan_port():
    pass

def detect_service():
    pass

def export_json():
    pass
```

---

This is exactly why our project has separate files.

---

# A Real Example from the Port Scanner

```python
def is_open(port):
    if port == 80:
        return True

    return False
```

---

Usage:

```python
if is_open(80):
    print("Port is open")
```

Output:

```text
Port is open
```

---

# What We Learned Today

✓ Creating a function with `def`
✓ Calling a function
✓ Taking input
✓ Multiple inputs
✓ `return`
✓ The difference between `return` and `print`
✓ Default value
✓ Modular design
✓ Use of functions in the Port Scanner

---

# Exercise

Write a function that:

1. Receives a port number.
2. If the port is 80, returns the text `HTTP`.
3. If the port is 443, returns the text `HTTPS`.
4. Otherwise, returns `Unknown`.

Example:

```python
print(detect_service(80))
```

Output:

```text
HTTP
```

---

Next session:

**06-modules-and-imports.md**

In the next session, we will learn how to split large projects into multiple files — exactly what we have done in the Port Scanner.
