[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/src/05-exporter.md)

# A Complete Review of the `exporter.py` File

## Introduction

In the previous session, we reviewed the file:

```text
src/services.py
```

We learned:

- What Service Detection is
- What IANA is
- How `getservbyport` works
- What the difference between Service Detection and Banner Grabbing is

So far, our port scanner can:

✅ Scan ports

✅ Detect services

But there is a problem.

---

Suppose a scan of 1000 ports has been performed.

The result is only displayed on the screen:

```text
80
443
22
53
```

If we close the terminal:

```text
All the results are lost.
```

---

To solve this problem, we must save the results.

That is why the file:

```text
src/exporter.py
```

was created.

---

# File Content

```python
import json


def export_json(data: dict, filename: str) -> None:
    """
    Export scan results to a JSON file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
```

---

# What Is the Goal of This File?

The task of this file:

```text
Save scan results in JSON format
```

---

# What Is JSON?

JSON stands for:

```text
JavaScript Object Notation
```

---

JSON is one of the most popular data storage and transfer formats in the world.

---

Almost all modern technologies use it:

- Python
- JavaScript
- Node.js
- Go
- Java
- PHP
- APIs
- Cloud Services

---

# A Sample of JSON

```json
{
    "ip": "127.0.0.1",
    "open_ports": [
        80,
        443
    ]
}
```

---

# Why Is JSON Popular?

Because:

✅ Humans can read it

✅ Machines can process it

✅ It is lightweight

✅ It is a global standard

---

# Import

```python
import json
```

---

## What Is This Module?

One of Python's standard modules.

---

Task:

```text
Convert Python data to JSON
```

and vice versa.

---

# The Function Definition

```python
def export_json(
    data: dict,
    filename: str
) -> None:
```

---

## First Input

```python
data: dict
```

---

Meaning:

```python
{
    "ip": "127.0.0.1",
    "ports": [80, 443]
}
```

---

A Python dictionary.

---

## Second Input

```python
filename: str
```

---

Example:

```python
"result.json"
```

---

Or:

```python
"scan_report.json"
```

---

## Output

```python
None
```

---

Meaning the function returns nothing.

---

It only creates a file.

---

# The Docstring

```python
"""
Export scan results to a JSON file.
"""
```

---

Meaning:

```text
Export the scan results to a JSON file.
```

---

# The Most Important Section of the File

```python
with open(
    filename,
    "w",
    encoding="utf-8"
) as file:
```

---

# What Is `open`?

It is used to work with files.

---

Example:

```python
open("result.json")
```

---

# The First Parameter

```python
filename
```

---

The file name.

---

Example:

```python
result.json
```

---

# The Second Parameter

```python
"w"
```

---

Meaning:

```text
Write Mode
```

---

In this mode:

- The file is created
- If the file already exists, it is overwritten

---

Example:

```python
open("data.json", "w")
```

---

# The Third Parameter

```python
encoding="utf-8"
```

---

# What Is Encoding?

A method for storing text.

---

UTF-8 is the global standard for storing text.

---

Advantage:

```text
Support for Persian
```

---

Example:

```json
{
    "message": "Hello World"
}
```

---

Without UTF-8, Persian characters might get corrupted.

---

# Why Did We Use `with`?

```python
with open(...) as file:
```

---

When the work is finished:

```python
file.close()
```

is executed automatically.

---

Advantages:

✅ Cleaner

✅ Safer

✅ Prevents resource leaks

---

# The Most Important Line of the Entire File

```python
json.dump(
    data,
    file,
    indent=4
)
```

---

# What Is `dump`?

A function that converts Python data to JSON.

---

Example:

```python
data = {
    "port": 80,
    "service": "http"
}
```

---

After:

```python
json.dump(...)
```

the file:

```json
{
    "port": 80,
    "service": "http"
}
```

is created.

---

# The First Parameter

```python
data```

---

The information we want to save.

---

Example:

```python
{
    "ip": "127.0.0.1",
    "open_ports": [80, 443]
}
```

---

# The Second Parameter

```python
file
```

---

The opened file.

---

Meaning:

```text
Write this data into this file.
```

---

# The Third Parameter

```python
indent=4
```

---

This parameter makes the JSON look nicer.

---

Without indent:

```json
{"ip":"127.0.0.1","ports":[80,443]}
```

---

It is hard to read.

---

With:

```python
indent=4
```

The output:

```json
{
    "ip": "127.0.0.1",
    "ports": [
        80,
        443
    ]
}
```

---

It is much more readable.

---

# Why Is JSON Important for Security Tools?

Suppose we want to scan:

```text
100 servers
```

---

Terminal output is not enough.

---

But JSON can be:

- Stored
- Processed
- Sent
- Analyzed
- Imported into a database

---

That is why almost all modern security tools produce JSON output.

---

Examples:

- Nmap
- Nessus
- Burp Suite
- OpenVAS
- Security Dashboards

---

# A Real Example in Our Project

Suppose the scan output is:

```python
{
    "ip": "127.0.0.1",
    "open_ports": [
        53,
        135,
        445
    ]
}
```

---

The call:

```python
export_json(
    data,
    "result.json"
)
```

---

produces the following file:

```json
{
    "ip": "127.0.0.1",
    "open_ports": [
        53,
        135,
        445
    ]
}
```

---

# A Design Note

This file has only one job:

```text
Export JSON
```

---

It does not perform:

❌ Port scanning

❌ Service detection

❌ Banner grabbing

❌ Printing output

❌ Logging

---

This is exactly the principle:

```text
Single Responsibility Principle
```

---

# Summary

In this session, we learned:

✅ What JSON is

✅ Why JSON is important

✅ What the `json` module is

✅ How the `export_json` function works

✅ What `open` is

✅ What UTF-8 is

✅ What `dump` is

✅ What `indent=4` is

✅ Why security tools produce JSON output

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
src/csv_exporter.py
```

There we will learn:

- What CSV is
- What the difference between CSV and JSON is
- Why we support both formats
- How tabular files are created
- How to import the scan output into Excel

