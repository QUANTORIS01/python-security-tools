[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/src/06-csv_exporter.md)

# A Complete Review of the `csv_exporter.py` File

# Introduction

In the previous session, we reviewed the file:

```text
src/exporter.py
```

There we learned:

- What JSON is
- How to save scan results
- How `json.dump` works
- What UTF-8 is
- Why security tools use JSON

---

But an important question arises:

What if we want to open the output in:

- Excel
- LibreOffice Calc
- Google Sheets

?

---

JSON is excellent for machines.

But it is not always the best option for working with tables.

That is why we created the file:

```text
src/csv_exporter.py
```

---

# File Content

```python
import csv


def export_csv(data: dict, filename: str) -> None:
    """
    Export scan results to a CSV file.
    """
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["port", "service", "banner"])

        for item in data["open_ports"]:
            writer.writerow(
                [
                    item["port"],
                    item["service"],
                    item.get("banner")
                ]
            )
```

---

# What Is the Goal of This File?

Goal:

```text
Save scan results in tabular format
```

---

# What Is CSV?

CSV stands for:

```text
Comma Separated Values
```

---

Meaning:

```text
Values separated by commas
```

---

Example:

```csv
port,service,banner
80,http,Apache
443,https,Nginx
22,ssh,OpenSSH
```

---

Each line:

```text
A record
```

---

Each column:

```text
A field
```

---

# Why Is CSV Important?

Because almost all spreadsheet software in the world supports it.

---

Example:

- Microsoft Excel
- Google Sheets
- LibreOffice Calc
- Apple Numbers

---

Many data analysis tools also support CSV:

- Pandas
- NumPy
- Power BI
- Tableau

---

# Import

```python
import csv
```

---

This module is one of Python's standard libraries.

---

Task:

```text
Creating and reading CSV files
```

---

# The Function Definition

```python
def export_csv(
    data: dict,
    filename: str
) -> None:
```

---

## First Parameter

```python
data
```

---

The scan information.

Example:

```python
{
    "open_ports": [
        {
            "port": 80,
            "service": "http",
            "banner": "Apache"
        }
    ]
}
```

---

## Second Parameter

```python
filename
```

---

The output file name.

Example:

```python
"result.csv"
```

---

# Output

```python
None
```

---

The function returns nothing.

---

It only creates a file.

---

# The Docstring

```python
"""
Export scan results to a CSV file.
"""
```

---

Meaning:

```text
Save the scan results in CSV format.
```

---

# Opening the File

```python
with open(
    filename,
    "w",
    newline="",
    encoding="utf-8"
) as file:
```

---

Here we see almost the same thing as in the JSON file.

---

But a new parameter has been added:

```python
newline=""
```

---

# What Is `newline`?

This part is one of the most important points when working with CSV.

---

On Windows, if we do not write this parameter:

```python
open(file, "w")
```

The output file might look like this:

```text
row1

row2

row3
```

---

Meaning, an extra blank line is created between each row.

---

To prevent this problem:

```python
newline=""
```

is placed.

---

This is one of the points many beginner programmers do not know.

---

# Creating the Writer

```python
writer = csv.writer(file)
```

---

Here a new object is created.

---

This object's job is:

```text
Convert data into CSV format.
```

---

It can be imagined as:

```text
writer = a CSV-generating machine
```

---

# Creating the Table Header

```python
writer.writerow(
    [
        "port",
        "service",
        "banner"
    ]
)
```

---

It creates the first row of the file.

---

Output:

```csv
port,service,banner
```

---

This row is:

```text
The column names
```

---

If we do not write this row:

```csv
80,http,Apache
443,https,Nginx
```

---

It becomes hard to tell what each column means.

---

That is why we always write the Header.

---

# The Main Loop

```python
for item in data["open_ports"]:
```

---

Suppose our data is:

```python
{
    "open_ports": [
        {
            "port": 80,
            "service": "http",
            "banner": "Apache"
        },
        {
            "port": 443,
            "service": "https",
            "banner": "Nginx"
        }
    ]
}
```

---

On each iteration of the loop:

```python
item
```

becomes one of these dictionaries.

---

First iteration:

```python
{
    "port": 80,
    "service": "http",
    "banner": "Apache"
}
```

---

Second iteration:

```python
{
    "port": 443,
    "service": "https",
    "banner": "Nginx"
}
```

---

# Writing Each Row

```python
writer.writerow(
    [
        item["port"],
        item["service"],
        item.get("banner")
    ]
)
```

---

# `item["port"]`

Example:

```python
80
```

---

# `item["service"]`

Example:

```python
"http"
```

---

# `item.get("banner")`

Example:

```python
"Apache"
```

---

# Why Was `get` Used?

An important question.

Why did we not write:

```python
item["banner"]
```

?

---

Suppose the banner does not exist.

---

Example:

```python
{
    "port": 53,
    "service": "domain"
}
```

---

If we write:

```python
item["banner"]
```

An error occurs:

```python
KeyError
```

---

But:

```python
item.get("banner")
```

In case the value does not exist:

```python
None
```

is returned.

---

And the program does not crash.

---

This is one of the good design decisions in the project.

---

# The Final Output

If the data is:

```python
{
    "open_ports": [
        {
            "port": 80,
            "service": "http",
            "banner": "Apache"
        },
        {
            "port": 443,
            "service": "https",
            "banner": "Nginx"
        }
    ]
}
```

---

The output file:

```csv
port,service,banner
80,http,Apache
443,https,Nginx
```

will be.

---

# The Difference Between CSV and JSON

| CSV | JSON |
|-------|-------|
| Tabular | Structured |
| Suitable for Excel | Suitable for APIs |
| Fast to read | Highly flexible |
| Lightweight | More descriptive |
| Column-oriented | Object-oriented |

---

# Why Did We Implement Both?

Because users are different.

---

Some want to:

```text
Open the output in Excel.
```

---

Some want to:

```text
Import the output into another program.
```

---

That is why:

```text
JSON + CSV
```

are both supported.

---

This is exactly what professional tools do.

---

# Summary

In this session, we learned:

✅ What CSV is

✅ What the difference between CSV and JSON is

✅ What `csv.writer` is

✅ What `writerow` is

✅ What a Header is

✅ Why `newline=""` is used

✅ How the record-saving loop works

✅ Why `item.get` was used

✅ How to import the output into Excel

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
src/logger.py
```

There we will learn:

- What Logging is
- What the difference between `print` and log is
- Why security tools produce logs
- What a Handler is
- What a Formatter is
- What a FileHandler is
- How to save scan events

