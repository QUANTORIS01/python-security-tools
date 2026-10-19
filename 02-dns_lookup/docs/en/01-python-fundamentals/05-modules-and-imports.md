[🇮🇷 فارسی](/02-dns_lookup/docs/fa/01-python-fundamentals/05-modules-and-imports.md)

# Lesson 5: Modules and Imports in Python

## Introduction

So far, our programs have been small.

But in real projects, we cannot put everything into a single file.

Suppose we placed all the DNS Lookup code in one file:

```python
validate_domain()
lookup_record()
build_dns_results()
format_dns_results()
main()
```

And hundreds of other lines of code.

Very quickly, the project would become:

- Hard to read
- Hard to develop
- Hard to test
- Hard to maintain

That is why professional projects are divided into multiple files.

---

# What Is a Module?

In Python, every `.py` file is considered a Module.

Example:

```text
validator.py
```

is a module.

Also:

```text
resolver.py
```

is also a module.

---

# Why Do We Use Modules?

Advantages:

- Separation of responsibilities
- Greater readability
- Easier testing
- Easier extension
- Code reuse

---

# What Is an Import?

To use the code of one module in another module, we use `import`.

Example:

File:

```python
math_utils.py
```

```python
def add(a, b):
    return a + b
```

Second file:

```python
from math_utils import add

print(add(10, 20))
```

Output:

```text
30
```

---

# Full Import

Example:

```python
import math
```

Usage:

```python
math.sqrt(25)
```

Output:

```text
5.0
```

---

# Importing Part of a Module

Example:

```python
from math import sqrt
```

Usage:

```python
sqrt(25)
```

---

# Importing Multiple Members

Example:

```python
from math import sqrt, pi
```

---

# Alias

Sometimes the module name is long.

Example:

```python
import dns.resolver as resolver
```

Usage:

```python
resolver.resolve(...)
```

---

# The Structure of the DNS Lookup Project

Our project consists of several modules:

```text
src/

├── validator.py
├── resolver.py
├── models.py
├── results.py
├── formatter.py
├── exporter.py
├── csv_exporter.py
├── logger.py
├── cli.py
└── __init__.py
```

Each file has a specific task.

---

# `validator.py`

Responsible for:

```text
Input Validation
```

Example:

```python
validate_domain()
```

```python
validate_record_type()
```

---

# `resolver.py`

Responsible for:

```text
DNS Resolution
```

Example:

```python
lookup_record()
```

---

# `models.py`

Responsible for:

```text
Data Models
```

Example:

```python
DNSRecord
```

---

# `results.py`

Responsible for:

```text
Result Processing
```

Example:

```python
build_dns_results()
```

---

# `formatter.py`

Responsible for:

```text
Terminal Output
```

Example:

```python
format_dns_results()
```

---

# `cli.py`

Responsible for:

```text
Application Entry Point
```

Meaning the starting point of the program.

---

# Import in the Project

In the file:

```python
results.py
```

we have:

```python
from src import (
    DNSRecord,
    lookup_record,
)
```

This means:

- Use the data model
- Use the DNS Resolver module

---

# The Project's Execution Flow

When the user runs the following command:

```bash
python -m src.cli google.com A
```

the following things happen:

```text
cli.py

    │

    ▼

validator.py

    │

    ▼

results.py

    │

    ▼

resolver.py

    │

    ▼

models.py

    │

    ▼

formatter.py

    │

    ▼

output display
```

---

# What Is `__init__.py`?

In the folder:

```text
src/
```

we have a file:

```text
__init__.py
```

This file turns the folder into a Python Package.

---

# What Is a Package?

When we place several related modules together:

```text
src/
```

we have created a Package.

Example:

```text
src/
    validator.py
    resolver.py
    results.py
```

They are all members of the same Package.

---

# Exporting Members

Usually, inside:

```python
__init__.py
```

we export the important members of the project.

Example:

```python
from .validator import (
    validate_domain,
    validate_record_type,
)
```

Now we can write:

```python
from src import validate_domain
```

Instead of:

```python
from src.validator import validate_domain
```

---

# The Advantage of This Approach

The code becomes more readable.

Example:

```python
from src import (
    validate_domain,
    lookup_record,
    DNSRecord,
)
```

is much cleaner than scattered imports.

---

# An Important Architectural Principle

Each module should have one specific responsibility.

Example:

```text
validator.py
```

only validation.

---

Example:

```text
resolver.py
```

only DNS Query.

---

Example:

```text
formatter.py
```

only output display.

---

This is exactly the principle:

```text
Separation of Concerns
```

---

# Why Did We Choose This Architecture?

If the entire project had been placed inside:

```python
main.py
```

then:

- Testing would become hard.
- Development would become hard.
- Errors would increase.
- Maintaining the project would become difficult.

Therefore, we divided the project into several small modules.

---

# Connection to the Tests

Because the project is modular, we were able to write separate tests for each file:

```text
test_validator.py
```

```text
test_resolver.py
```

```text
test_results.py
```

```text
test_formatter.py
```

etc.

---

# Exercise

1. Create a file named:

```text
math_utils.py
```

---

2. Place the following function inside it:

```python
def add(a, b):
    return a + b
```

---

3. Create another file:

```text
main.py
```

---

4. Import the function.

---

5. Print the result of:

```python
add(5, 10)
```

---

6. Check how you can use:

```python
import
```

and

```python
from ... import ...
```

---

# Lesson Summary

In this lesson, we learned:

- What a module is
- What a Package is
- What an Import is
- Types of Import
- The `__init__.py` file
- Modular architecture
- Separation of Concerns

These concepts are exactly the reason for the current structure of the DNS Lookup project, and are considered the most fundamental concepts for building professional Python projects.

In the next lesson, we will enter **Regular Expressions (Regex)**; a concept used directly in `validator.py` for validating domains.
