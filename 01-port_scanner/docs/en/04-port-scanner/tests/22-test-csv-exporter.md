[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/tests/22-test-csv-exporter.md)

# A Complete Review of the `test_csv_exporter.py` File

# Introduction

So far, we have reviewed almost all parts of the project.

---

If you remember, in the Python chapter we said:

```text
CSV is one of the most common data storage formats.
```

---

Many tools can open a CSV file:

✅ Excel

✅ LibreOffice Calc

✅ Google Sheets

✅ Pandas

✅ Power BI

---

That is why in the Port Scanner project we implemented:

```text
Export CSV
```

---

If you remember, in the file:

```text
src/csv_exporter.py
```

we had the following function:

```python
export_csv()
```

---

Its task was:

```text
Converting scan results
into a CSV file
```

---

Now we must make sure:

✅ The file is created

✅ The file content is correct

✅ The Headers are correct

✅ The data is stored in the correct order

---

File content:

```python
import csv

from src import export_csv


def test_export_csv_creates_file(tmp_path):
    output_file = tmp_path / "results.csv"
    data = {
        "target": "127.0.0.1",
        "open_ports": [
            {
                "port": 80,
                "service": "http",
            },
            {
                "port": 443,
                "service": "https",
            },
        ],
    }
    export_csv(data, str(output_file))
    assert output_file.exists()


def test_export_csv_content(tmp_path):
    output_file = tmp_path / "results.csv"
    data = {
        "target": "127.0.0.1",
        "open_ports": [
            {
                "port": 80,
                "service": "http",
                "banner": "HTTP/1.1 200 OK",
            },
            {
                "port": 443,
                "service": "https",
                "banner": "HTTPS Server",
            },
        ],
    }
    export_csv(data, str(output_file))

    with open(output_file, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
    assert rows == [
        ["port", "service", "banner"],
        ["80", "http", "HTTP/1.1 200 OK"],
        ["443", "https", "HTTPS Server"],
    ]
```

---

# Imports

```python
import csv

from src import export_csv
```

---

# The First Import

```python
import csv
```

---

For reading the generated CSV file.

---

# The Second Import

```python
from src import export_csv
```

---

The function that is going to be tested.

---

# What Is the Goal of This File?

Checking two important things:

```text
The file is created
```

---

And:

```text
The file content is correct
```

---

# The First Test

```python
def test_export_csv_creates_file(
    tmp_path
):
```

---

Goal:

```text
Checking that the CSV file is created
```

---

# What Is `tmp_path`?

One of pytest's wonderful features.

---

```python
tmp_path
```

---

Creates a temporary directory.

---

For example, something like:

```text
/tmp/pytest-12345/
```

---

Or on Windows:

```text
C:\Temp\pytest-xxxxx\
```

---

Advantage:

✅ Test files do not clutter the project

✅ They are deleted after the test ends

✅ Each test has an independent environment

---

# Building the File Path

```python
output_file =
    tmp_path / "results.csv"
```

---

Result:

```text
/tmp/.../results.csv
```

---

# Building Test Data

```python
data = {
    ...
}
```

---

Data structure:

```python
{
    "target": "127.0.0.1",
    "open_ports": [...]
}
```

---

We have two open ports:

```python
80
```

and

```python
443
```

---

# Running the Function

```python
export_csv(
    data,
    str(output_file)
)
```

---

The function:

```python
export_csv()
```

is executed.

---

And it must create:

```text
results.csv
```

---

# Checking the File's Existence

```python
assert output_file.exists()
```

---

If the file has been created:

```text
PASS
```

---

If the file does not exist:

```text
FAIL
```

---

# The Importance of This Test

This test verifies:

```text
The write operation
has actually been performed.
```

---

Not just that the function ran.

---

# The Second Test

```python
def test_export_csv_content(
    tmp_path
):
```

---

Goal:

```text
Checking the content of the CSV file
```

---

This test is more important than the previous one.

---

Why?

---

Because:

```text
The file's existence alone is not enough.
```

---

The file might be created but:

❌ The data might be wrong

❌ The column order might be wrong

❌ The Header might be broken

---

This test checks all of these.

---

# The File Path

```python
output_file =
    tmp_path / "results.csv"
```

---

The same temporary directory.

---

# Test Data

```python
data = {
    ...
}
```

---

This time, in addition to:

```python
port
```

and

```python
service
```

---

we also store:

```python
banner
```

---

First port:

```python
80
```

↓

```python
http
```

↓

```python
HTTP/1.1 200 OK
```

---

Second port:

```python
443
```

↓

```python
https
```

↓

```python
HTTPS Server
```

---

# Running the Function

```python
export_csv(
    data,
    str(output_file)
)
```

---

The file is created.

---

# Opening the File

```python
with open(
    output_file,
    "r",
    newline="",
    encoding="utf-8"
) as file:
```

---

In read mode.

---

# Reading the File

```python
rows =
    list(
        csv.reader(file)
    )
```

---

If the file is like this:

```csv
port,service,banner
80,http,HTTP/1.1 200 OK
443,https,HTTPS Server
```

---

The output will be:

```python
[
    ["port","service","banner"],
    ["80","http","HTTP/1.1 200 OK"],
    ["443","https","HTTPS Server"]
]
```

---

# Checking the Header

The first row:

```python
["port", "service", "banner"]
```

---

is exactly what we wrote in:

```python
writer.writerow(...)
```

---

# Checking the First Row

```python
[
    "80",
    "http",
    "HTTP/1.1 200 OK"
]
```

---

Verifies:

```text
Port 80's information
has been stored correctly.
```

---

# Checking the Second Row

```python
[
    "443",
    "https",
    "HTTPS Server"
]
```

---

Verifies:

```text
Port 443's information
has been stored correctly.
```

---

# An Interesting Point

Pay attention:

In the original data:

```python
80
```

---

was a number.

---

But in the output:

```python
"80"
```

---

is a string.

---

Why?

---

Because:

```python
csv.reader()
```

returns all data as:

```python
str
```

---

That is why the test also uses:

```python
"80"
```

---

Not:

```python
80
```

---

# How This Test Relates to `csv_exporter.py`

If you remember:

```python
writer.writerow(
    ["port", "service", "banner"]
)
```

---

This test checks exactly that.

---

Also:

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

is also validated by this test.

---

# What If the Column Order Changes?

Suppose someone writes:

```python
["service", "port", "banner"]
```

---

The output:

```csv
service,port,banner
```

---

The test immediately:

```text
FAIL
```

---

# What If the Banner Is Not Stored?

For example:

```python
writer.writerow([
    item["port"],
    item["service"]
])
```

---

The test:

```text
FAIL
```

---

# What If the Rows Are Stored in the Wrong Order?

For example:

```python
443
```

comes before:

```python
80
```

---

Again:

```text
FAIL
```

---

# pytest Output

If everything is correct:

```bash
pytest
```

---

Output:

```text
==== 2 passed ====
```

---

# Summary

In this session, we learned:

✅ Testing CSV files

✅ Using `tmp_path`

✅ Reading CSV with `csv.reader`

✅ Testing Headers

✅ Testing data rows

✅ Validating column order

✅ Validating file content

✅ The difference between numbers and strings in CSV

✅ The importance of testing file outputs

---

# The Current Status of the Project

Test files reviewed:

```text
test_validator.py
test_scanner.py
test_services.py
test_exporter.py
test_cli.py
test_banner.py
test_models.py
test_results.py
test_formatter.py
test_csv_exporter.py
```

---

Only a few test files remain, and then:

```text
The entire project
from beginning to end
will have been walked through.
```

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
tests/test_logger.py
```

---

There we will learn:

✅ Testing Logging

✅ Testing FileHandler

✅ Checking log content

✅ Preventing duplicate Handlers

✅ Testing the event-recording system
