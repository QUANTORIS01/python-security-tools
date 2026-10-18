[🇮🇷 فارسی](/01-port_scanner/docs/fa/01-python/08-files-json-csv.md)

# Session 08 — Working with Files, JSON, and CSV

# Why Should We Learn to Work with Files?

Suppose we have run the port scanner.

Output:

```text
53
135
445
```

has been displayed.

But after closing the program:

All the information is lost.

---

What is the solution?

Saving the information to a file.

---

# Opening a File

To open a file, we use the function:

```python
open()
```

---

Example:

```python
file = open("test.txt")
```

---

# Reading a File

Suppose the file:

```text
test.txt
```

has the following content:

```text
Hello World
```

---

Code:

```python
file = open("test.txt")

content = file.read()

print(content)
```

Output:

```text
Hello World
```

---

# Closing a File

After we are done, the file must be closed.

---

Example:

```python
file = open("test.txt")

content = file.read()

file.close()
```

---

# A More Professional Way

In the real world, we almost always use:

```python
with
```

---

Example:

```python
with open("test.txt") as file:
    content = file.read()

print(content)
```

---

Advantage:

Even if an error occurs, the file is closed automatically.

---

# Writing to a File

Write mode:

```python
w
```

---

Example:

```python
with open("result.txt", "w") as file:
    file.write("Hello")
```

---

Output:

```text
result.txt
```

Value:

```text
Hello
```

---

# Appending to a File

If we do not want the previous content to be erased:

```python
a
```

---

Example:

```python
with open("log.txt", "a") as file:
    file.write("New Log\n")
```

---

# What Is JSON?

JSON stands for:

```text
JavaScript Object Notation
```

---

It is one of the most popular data storage formats in the world.

---

Sample JSON:

```json
{
  "ip": "127.0.0.1",
  "port": 80,
  "service": "http"
}
```

---

# The JSON Module

Python has the following module by default:

```python
json
```

---

# Converting a Dictionary to JSON

```python
import json

data = {
    "port": 80,
    "service": "http"
}

print(json.dumps(data))
```

Output:

```json
{"port": 80, "service": "http"}
```

---

# Saving JSON to a File

```python
import json

data = {
    "port": 80,
    "service": "http"
}

with open("result.json", "w") as file:
    json.dump(data, file)
```

---

The generated file:

```json
{
  "port": 80,
  "service": "http"
}
```

---

# Reading JSON

```python
import json

with open("result.json") as file:
    data = json.load(file)

print(data)
```

---

Output:

```python
{'port': 80, 'service': 'http'}
```

---

# Connection to Our Project

The file:

```python
exporter.py
```

does exactly this.

---

Example output:

```json
{
  "target": "127.0.0.1",
  "open_ports": [
    {
      "port": 80,
      "service": "http"
    }
  ]
}
```

---

# What Is CSV?

CSV stands for:

```text
Comma Separated Values
```

---

Example:

```csv
port,service
80,http
443,https
```

---

This format is very suitable for:

- Excel
- LibreOffice
- Google Sheets

---

# The CSV Module

Python has a built-in module:

```python
csv
```

---

# Writing CSV

```python
import csv

with open("result.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["port", "service"])

    writer.writerow([80, "http"])

    writer.writerow([443, "https"])
```

---

The generated file:

```csv
port,service
80,http
443,https
```

---

# Reading CSV

```python
import csv

with open("result.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

Output:

```python
['port', 'service']
['80', 'http']
['443', 'https']
```

---

# Connection to Our Project

The file:

```python
csv_exporter.py
```

uses exactly these concepts.

---

A real sample output:

```csv
port,service,banner
80,http,Apache
443,https,nginx
```

---

# What We Learned Today

✓ Working with files
✓ `open`
✓ `read`
✓ `write`
✓ `with`
✓ JSON
✓ `json.dump`
✓ `json.load`
✓ CSV
✓ `csv.writer`
✓ Direct connection to `exporter.py`
✓ Direct connection to `csv_exporter.py`

---

# Exercise

Create a file named:

```text
ports.json
```

that stores the following information:

```python
{
    "port": 22,
    "service": "ssh"
}
```

Then read the file and print the value of `service`.

---

Next session:

**09-networking-with-python.md**

In the next session, we enter the world of networking and learn what a Socket is — the most important prerequisite for building a Port Scanner.
