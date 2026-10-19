[🇮🇷 فارسی](/02-dns_lookup/docs/fa/01-python-fundamentals/09-working-with-argparse-and-getting-command-line-input.md)

# Lesson 9: Working with `argparse` and Getting Command-Line Input

## Lesson Goal

In this lesson, we will learn how to control Python programs from the command line and receive user input.

Our DNS Lookup tool uses this capability so that the user can specify the domain and the DNS record type when running the program.

---

# Why `argparse`?

Suppose we run the following program:

```bash
python app.py google.com A
```

In this case:

- `google.com` is the target domain.
- `A` is the DNS record type.

Python does not automatically process these values.

To manage command-line arguments professionally, we use the standard module `argparse`.

---

# The First Example

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")

args = parser.parse_args()

print(args.name)
```

Run:

```bash
python app.py Ali
```

Output:

```text
Ali
```

---

# Multiple Arguments

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("domain")
parser.add_argument("record_type")

args = parser.parse_args()

print(args.domain)
print(args.record_type)
```

Run:

```bash
python app.py google.com MX
```

Output:

```text
google.com
MX
```

---

# Optional Arguments

Sometimes we want some options to be optional.

Example:

```python
parser.add_argument(
    "--timeout",
    type=float,
)
```

Run:

```bash
python app.py --timeout 2
```

Output:

```text
2.0
```

---

# Specifying the Data Type

`argparse` can control the data type.

```python
parser.add_argument(
    "--workers",
    type=int,
)
```

If the user enters an invalid value:

```bash
python app.py --workers hello
```

`argparse` raises an error.

---

# Displaying the Help

```python
parser = argparse.ArgumentParser(
    description="DNS Lookup Tool"
)
```

The user can write:

```bash
python app.py --help
```

Sample output:

```text
usage: app.py domain record_type

DNS Lookup Tool

positional arguments:
  domain
  record_type
```

This capability makes our tools more professional.

---

# Usage in the DNS Lookup Project

In our project:

```python
parser.add_argument(
    "domain",
    type=str,
    help="Target domain name",
)

parser.add_argument(
    "record_type",
    type=str,
    help="DNS record type",
)
```

And also:

```python
parser.add_argument(
    "--json",
    dest="json_file",
)

parser.add_argument(
    "--csv",
    dest="csv_file",
)
```

That is why we can run the program like this:

```bash
python -m src.cli google.com A
```

Or:

```bash
python -m src.cli google.com MX --json result.json
```

Or:

```bash
python -m src.cli google.com NS --csv result.csv
```

---

# Advantages of `argparse`

- High readability
- Automatic error handling
- Automatic help generation
- Support for both mandatory and optional arguments
- Suitable for professional command-line tools

---

# Summary

In this lesson, we learned:

- What `argparse` is
- How to receive arguments
- The difference between mandatory and optional arguments
- Using `type`
- Using `help`
- How `argparse` is used in the DNS Lookup project

This module is the main foundation for building professional CLI tools in Python, and it is used in almost all security and automation projects.
