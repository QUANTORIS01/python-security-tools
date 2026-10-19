[🇮🇷 فارسی](/02-dns_lookup/docs/fa/01-python-fundamentals/13-csv-handling.md)

# Lesson 13: CSV Handling in Python

## Introduction

CSV stands for:

```text
Comma-Separated Values
```

CSV is considered one of the most common data storage and interchange formats in the world.

Many tools and software support CSV:

- Microsoft Excel
- Google Sheets
- LibreOffice Calc
- Monitoring tools
- Logging systems
- Security tools
- Data-analysis programs

In security projects, too, scan results, logs, and reports are usually stored in CSV format.

---

# What Is a CSV File?

A sample CSV file:

```csv
port,service,banner
22,ssh,OpenSSH
80,http,Apache
443,https,Nginx
```

Each line is a record.

Each column is separated from the next by a comma.

---

# The Relationship Between CSV and Python

In Python, to work with CSV, we use the built-in module:

```python
import csv
```

This module is part of the Standard Library and does not need to be installed.

---

# Writing a CSV File

Example:

```python
import csv

with open(
    "ports.csv",
    "w",
    newline="",
    encoding="utf-8",
) as file:

    writer = csv.writer(file)

    writer.writerow(
        ["port", "service"]
    )

    writer.writerow(
        [22, "ssh"]
    )

    writer.writerow(
        [80, "http"]
    )
```

The created file:

```csv
port,service
22,ssh
80,http
```

---

# Reading a CSV File

Example:

```python
import csv

with open(
    "ports.csv",
    encoding="utf-8",
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```python
['port', 'service']
['22', 'ssh']
['80', 'http']
```

---

# Each Line Is a List

Example:

```python
row = ['22', 'ssh']
```

Access:

```python
print(row[0])
```

Output:

```text
22
```

---

# Skipping the Header

Usually, the first line contains the column names.

Example:

```python
import csv

with open(
    "ports.csv",
    encoding="utf-8",
) as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row)
```

Output:

```python
['22', 'ssh']
['80', 'http']
```

---

# Using `DictReader`

Sometimes it is better to read the data as a Dictionary.

Example:

```python
import csv

with open(
    "ports.csv",
    encoding="utf-8",
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

Output:

```python
{
    'port': '22',
    'service': 'ssh'
}

{
    'port': '80',
    'service': 'http'
}
```

---

# Accessing the Columns

```python
print(row["service"])
```

Output:

```text
ssh
```

---

# Writing CSV with `DictWriter`

Example:

```python
import csv

with open(
    "ports.csv",
    "w",
    newline="",
    encoding="utf-8",
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "port",
            "service",
        ]
    )

    writer.writeheader()

    writer.writerow(
        {
            "port": 22,
            "service": "ssh",
        }
    )
```

---

# Why Is `newline` Important?

On Windows, if we do not set:

```python
newline=""
```

extra blank lines might be created.

Always use it when writing CSV.

---

# CSV in the DNS Lookup Project

In the file:

```text
csv_exporter.py
```

the lookup results are converted to CSV.

Sample output:

```csv
domain,record_type,value
google.com,A,8.8.8.8
google.com,A,8.8.4.4
```

---

# CSV in the Port Scanner Project

Sample:

```csv
port,service,banner
22,ssh,OpenSSH
80,http,Apache
443,https,Nginx
```

This type of output is very suitable for:

- Excel
- Google Sheets
- Data analysis
- Reporting

---

# CSV and Automation

One of the most common uses of CSV:

```text
Export → Analyze → Report
```

Example:

```text
Port Scanner
      ↓
CSV Export
      ↓
Excel
      ↓
Security Report
```

---

# Error Handling

The file might not exist.

Example:

```python
import csv

try:
    with open(
        "missing.csv"
    ) as file:
        reader = csv.reader(file)

except FileNotFoundError:
    print("File not found")
```

---

# Data Validation

We should not assume that the CSV data is always valid.

Example:

```python
for row in reader:

    if len(row) != 2:
        continue
```

---

# Common Mistakes

## Forgetting the Header

Inappropriate:

```csv
22,ssh
80,http
```

---

Better:

```csv
port,service
22,ssh
80,http
```

---

## Forgetting `newline`

Inappropriate:

```python
open("file.csv", "w")
```

---

Better:

```python
open(
    "file.csv",
    "w",
    newline=""
)
```

---

## Assuming the Data Type

All CSV data is read as strings.

Example:

```python
row["port"]
```

Output:

```python
"22"
```

Conversion:

```python
port = int(
    row["port"]
)
```

---

# Advantages of CSV

- Simple
- Lightweight
- Portable
- Readable
- Broad support
- Suitable for reporting

---

# Limitations of CSV

- Lacks nested structure
- Lacks data types
- Lacks built-in validation
- Not suitable for complex data

For complex data, JSON is usually used.

---

# Comparing JSON and CSV

| Feature          | CSV        | JSON  |
| ---------------- | ---------- | ----- |
| Readability      | High       | High  |
| Simplicity       | Very high  | High  |
| Nested structure | No         | Yes   |
| Size             | Smaller    | Larger |
| Suitable for reports | Excellent | Good  |
| Suitable for APIs    | Weak      | Excellent |

---

# Summary

In this lesson, we learned:

- What CSV is
- The `csv` module
- `csv.reader`
- `csv.writer`
- `DictReader`
- `DictWriter`
- Reading a CSV file
- Writing a CSV file
- Error handling
- Data validation
- The use of CSV in security projects

CSV is one of the most important output formats in security, networking, and automation tools, and you will encounter it in almost all practical projects.
