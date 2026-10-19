[🇮🇷 فارسی](/02-dns_lookup/docs/fa/01-python-fundamentals/11-file-handling.md)

# Lesson 11: File Handling in Python

## Introduction

Many programs do not work only with data in memory. In the real world, we usually need to store information in files or read it from files.

Some common uses of File Handling:

- Storing logs
- Storing application configuration
- Reading text files
- Producing JSON files
- Producing CSV files
- Storing the results of processing

In the DNS Lookup project, too, we have used File Handling to store logs and JSON and CSV outputs.

---

# Opening a File

The main function for working with files in Python:

```python
open()
```

Example:

```python
file = open("data.txt")
```

---

# Reading the File's Content

Suppose the file `data.txt` contains the following:

```text
Hello
World
Python
```

Code:

```python
file = open("data.txt")

content = file.read()

print(content)

file.close()
```

Output:

```text
Hello
World
Python
```

---

# Closing the File

After finishing the work, the file must be closed:

```python
file.close()
```

If the file is not closed, it is possible that:

- System resources are not released
- The file becomes locked
- Data is not stored properly

---

# Using `with`

The standard approach in Python:

```python
with open("data.txt") as file:
    content = file.read()

print(content)
```

Advantage:

```text
The file is closed automatically.
```

---

# Reading the File Line by Line

```python
with open("data.txt") as file:
    for line in file:
        print(line)
```

---

# Reading All the Lines

```python
with open("data.txt") as file:
    lines = file.readlines()

print(lines)
```

Output:

```python
[
    "Hello\n",
    "World\n",
    "Python\n"
]
```

---

# Writing to a File

To write, we use the `w` mode:

```python
with open("output.txt", "w") as file:
    file.write("Hello")
```

---

# The Behavior of `w` Mode

If the file exists, its previous content is erased.

Initial file:

```text
Old Data
```

Code:

```python
with open("output.txt", "w") as file:
    file.write("New Data")
```

Result:

```text
New Data
```

---

# Appending to a File

To add content without erasing the previous data, the `a` mode is used.

```python
with open("log.txt", "a") as file:
    file.write("New Log\n")
```

---

# The Difference Between `w` and `a`

`w` mode:

```text
Overwrite
```

`a` mode:

```text
Append
```

---

# Writing Multiple Lines

```python
with open("notes.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
```

---

# Encoding

To avoid problems with Persian characters, it is better to always specify the Encoding.

```python
with open(
    "data.txt",
    encoding="utf-8"
) as file:
    print(file.read())
```

---

# Storing Persian Text

```python
with open(
    "data.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write("Hello World")
```

---

# Error Handling

The target file might not exist.

```python
try:
    with open("missing.txt") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")
```

---

# File Paths

Relative path:

```python
open("data.txt")
```

Full path:

```python
open("C:/Projects/data.txt")
```

---

# Checking Whether a File Exists

The `pathlib` library provides a modern way to work with paths.

```python
from pathlib import Path

path = Path("data.txt")

print(path.exists())
```

Output:

```python
True
```

Or:

```python
False
```

---

# File Handling in the DNS Lookup Project

In the DNS Lookup project, File Handling has been used in several places.

## Logger

File:

```text
dns.log
```

For storing the program's events.

---

## JSON Export

File:

```text
results.json
```

For storing the structured output.

---

## CSV Export

File:

```text
results.csv
```

For storing the results in CSV format.

---

# A Real Example from the Project

```python
with open(
    filename,
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        data,
        file,
        indent=4
    )
```

---

# Common Mistakes

## Forgetting to `close`

Inappropriate:

```python
file = open("data.txt")
```

Appropriate:

```python
with open("data.txt") as file:
    ...
```

---

## Incorrect Use of `w`

Inappropriate:

```python
open("log.txt", "w")
```

This might erase the entire log file.

---

## Not Specifying Encoding

Inappropriate:

```python
open("data.txt")
```

Appropriate:

```python
open(
    "data.txt",
    encoding="utf-8"
)
```

---

# Summary

In this lesson, we learned:

- The `open()` function
- The `read()` method
- The `readlines()` method
- The `write()` method
- The `r`, `w`, and `a` modes
- Using `with`
- Handling Encoding
- Handling file errors
- Using `pathlib`
- The use of File Handling in the DNS Lookup project

File Handling is one of the basic skills for developing real tools, and it is used in almost all practical projects.
