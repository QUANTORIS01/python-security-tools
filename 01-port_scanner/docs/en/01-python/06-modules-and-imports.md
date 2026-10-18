[🇮🇷 فارسی](/01-port_scanner/docs/fa/01-python/06-modules-and-imports.md)

# Session 06 — Modules and Import

# Why Do We Need Modules?

Suppose we write the entire Port Scanner project in a single file.

```python
scanner.py
```

And this file gradually grows to 1000 lines.

Then:

- Finding bugs becomes hard.
- Developing the project becomes hard.
- Writing tests becomes hard.
- Maintaining the project becomes hard.

That is why programmers split a project into multiple files.

Every Python file is called:

> a Module

---

# The First Module

First file:

```python
math_tools.py
```

```python
def add(a, b):
    return a + b
```

---

Second file:

```python
main.py
```

```python
from math_tools import add

result = add(10, 20)

print(result)
```

Output:

```text
30
```

---

# What Is `import`?

The word `import` means:

> Bring the code of another file into this file.

---

Example:

```python
import math
```

Now we can use the features of the `math` module.

---

Example:

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

---

# Using `from`

First way:

```python
import math

print(math.sqrt(25))
```

---

Second way:

```python
from math import sqrt

print(sqrt(25))
```

Output:

```text
5.0
```

---

# The Difference Between These Two Ways

First way:

```python
import math
```

We must write the module name.

```python
math.sqrt()
```

---

Second way:

```python
from math import sqrt
```

We call the function directly.

```python
sqrt()
```

---

# Importing Multiple Functions

```python
from math import sqrt, pow
```

---

Usage:

```python
print(sqrt(16))
print(pow(2, 3))
```

Output:

```text
4.0
8.0
```

---

# Importing Everything

```python
from math import *
```

This is possible.

But it is not recommended in real projects.

Because it is not clear where each function came from.

---

# The Real Structure of Our Project

The Port Scanner project:

```text
src/
│
├── scanner.py
├── validator.py
├── services.py
├── banner.py
├── results.py
├── formatter.py
├── exporter.py
├── csv_exporter.py
└── cli.py
```

---

Each file is responsible for only one task.

---

# A Real Example from the Project

File:

```python
validator.py
```

```python
def validate_ip(ip):
    return True
```

---

File:

```python
cli.py
```

```python
from validator import validate_ip

validate_ip("127.0.0.1")
```

---

# The Big Advantage of Modules

If we want to change the IP validation:

We only change the following file:

```python
validator.py
```

The rest of the project remains untouched.

---

# Python's Built-in Modules

Python has hundreds of ready-made modules.

---

# `socket`

For networking

```python
import socket
```

---

# `json`

For JSON files

```python
import json
```

---

# `csv`

For CSV files

```python
import csv
```

---

# `time`

For time

```python
import time
```

---

# `threading`

For multithreading

```python
import threading
```

---

# An Example with `socket`

```python
import socket

print(socket.gethostname())
```

---

Sample output:

```text
DESKTOP-ABC123
```

---

# The Concept of a Package

When we place several modules inside one folder:

```text
src/
│
├── scanner.py
├── validator.py
├── services.py
└── __init__.py
```

It is called:

> Package

---

# What Is the `__init__.py` File?

The existence of this file tells Python:

> This folder is a Package.

---

In our project:

```text
src/__init__.py
```

exists.

---

# Import in Our Project

A real example:

```python
from src.scanner import scan_range
```

---

Or:

```python
from src.validator import validate_ip
```

---

Or:

```python
from src.results import build_scan_results
```

---

# One of the Most Important Programming Skills

A beginner programmer:

```python
all_code.py
```

5000 lines of code in one file.

---

A professional programmer:

```text
project/
│
├── network.py
├── security.py
├── database.py
├── api.py
└── cli.py
```

Each file has one specific responsibility.

---

# What We Learned Today

✓ The concept of Module
✓ The concept of Import
✓ `import`
✓ `from ... import ...`
✓ Python's built-in modules
✓ Package
✓ The `__init__.py` file
✓ The real architecture of the Port Scanner project
✓ Why we split the project into multiple files

---

# Exercise

Create two files:

First file:

```python
calculator.py
```

```python
def multiply(a, b):
    return a * b
```

---

Second file:

```python
main.py
```

Import the `multiply` function and print the product of 5 and 8.

Output:

```text
40
```

---

Next session:

**07-exceptions-and-error-handling.md**

In the next session, we will learn how to handle program errors — exactly what we have used in the Port Scanner to handle network errors.
