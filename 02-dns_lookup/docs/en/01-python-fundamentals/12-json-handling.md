[🇮🇷 فارسی](/02-dns_lookup/docs/fa/01-python-fundamentals/12-json-handling.md)

# Lesson 12: JSON Handling in Python

## Introduction

JSON stands for:

```text
JavaScript Object Notation
```

JSON is considered one of the most common data interchange formats in the world, and it is used in almost all software domains:

- APIs
- Web services
- Web applications
- Mobile applications
- Configuration files
- Security tools
- Monitoring systems
- Log processing

In the DNS Lookup project, too, we store the results in JSON format.

---

# A Sample of JSON

Example:

```json
{
    "domain": "google.com",
    "record_type": "A",
    "records": [
        {
            "value": "8.8.8.8"
        }
    ]
}
```

---

# The Structure of JSON

JSON consists of two main structures:

## Object

Similar to a Dictionary in Python

```json
{
    "name": "Ali",
    "age": 25
}
```

---

## Array

Similar to a List in Python

```json
[
    "A",
    "MX",
    "TXT"
]
```

---

# The Relationship Between JSON and Python

Python:

```python
data = {
    "domain": "google.com",
    "record_type": "A",
}
```

JSON:

```json
{
    "domain": "google.com",
    "record_type": "A"
}
```

---

# The `json` Module

To work with JSON, we use the Python built-in module:

```python
import json
```

This module is part of the Standard Library and does not need to be installed.

---

# Converting Python to JSON

The method:

```python
json.dumps()
```

Example:

```python
import json

data = {
    "domain": "google.com",
    "record_type": "A",
}

result = json.dumps(data)

print(result)
```

Output:

```json
{"domain": "google.com", "record_type": "A"}
```

---

# Pretty-Printing JSON

For greater readability:

```python
import json

data = {
    "domain": "google.com",
    "record_type": "A",
}

print(
    json.dumps(
        data,
        indent=4
    )
)
```

Output:

```json
{
    "domain": "google.com",
    "record_type": "A"
}
```

---

# Converting JSON to Python

The method:

```python
json.loads()
```

Example:

```python
import json

raw = '''
{
    "domain": "google.com",
    "record_type": "A"
}
'''

data = json.loads(raw)

print(data)
```

Output:

```python
{
    'domain': 'google.com',
    'record_type': 'A'
}
```

---

# The Output Data Type

```python
type(data)
```

Output:

```python
dict
```

---

# Saving JSON to a File

The method:

```python
json.dump()
```

Example:

```python
import json

data = {
    "domain": "google.com",
    "record_type": "A",
}

with open(
    "result.json",
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

# Reading JSON from a File

The method:

```python
json.load()
```

Example:

```python
import json

with open(
    "result.json",
    encoding="utf-8"
) as file:
    data = json.load(file)

print(data)
```

---

# JSON Containing a List

Example:

```python
data = {
    "records": [
        "8.8.8.8",
        "1.1.1.1"
    ]
}
```

Output:

```json
{
    "records": [
        "8.8.8.8",
        "1.1.1.1"
    ]
}
```

---

# Nested JSON

Example:

```python
data = {
    "domain": "google.com",
    "records": [
        {
            "type": "A",
            "value": "8.8.8.8"
        }
    ]
}
```

---

# Accessing the Data

```python
print(
    data["records"][0]["value"]
)
```

Output:

```text
8.8.8.8
```

---

# JSON in the DNS Lookup Project

In the file:

```text
exporter.py
```

the lookup results are converted to JSON.

Output structure:

```json
{
    "domain": "google.com",
    "record_type": "A",
    "records": [
        {
            "domain": "google.com",
            "record_type": "A",
            "value": "8.8.8.8"
        }
    ]
}
```

---

# Advantages of JSON

## Human-Readable

```json
{
    "name": "Ali"
}
```

---

## Broad Support

Almost all programming languages support JSON.

---

## Suitable for APIs

Most modern APIs use JSON.

---

## Suitable for Storage

Configuration files and reports are usually stored as JSON.

---

# Error Handling

JSON might be invalid.

Example:

```python
import json

try:
    json.loads("{")
except json.JSONDecodeError:
    print("Invalid JSON")
```

Output:

```text
Invalid JSON
```

---

# Common Mistakes

## Using Single Quotes

Invalid:

```json
{
    'name': 'Ali'
}
```

---

Valid:

```json
{
    "name": "Ali"
}
```

---

## Adding an Extra Comma

Invalid:

```json
{
    "name": "Ali",
}
```

---

Valid:

```json
{
    "name": "Ali"
}
```

---

# JSON and Security

When processing JSON from external sources:

- Validate the data.
- Do not trust the data types.
- Handle parsing errors.
- Examine the received data.

---

# Summary

In this lesson, we learned:

- What JSON is
- The relationship between JSON and Python
- The `json` module
- The `dumps()` method
- The `loads()` method
- The `dump()` method
- The `load()` method
- Saving JSON to a file
- Reading JSON from a file
- Nested JSON
- Error handling
- The use of JSON in the DNS Lookup project

JSON is one of the most important skills in modern software development, and it is used in almost all networking, security, automation, and API projects.
