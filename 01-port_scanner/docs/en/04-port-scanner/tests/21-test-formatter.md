[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/tests/21-test-formatter.md)

# A Complete Review of the `test_formatter.py` File

# Introduction

We have reached one of the last test files of the project.

---

So far, we have learned:

✅ How ports are scanned

✅ How services are detected

✅ How Banners are retrieved

✅ How results are built

---

But one question still remains:

```text
How are these results displayed to the user?
```

---

If you remember, in the file:

```text
src/formatter.py
```

we had a function:

```python
format_scan_results()
```

---

This function's task was:

```text
Converting scan results
into a readable table
```

---

For example:

```python
[
    ScanResult(...),
    ScanResult(...)
]
```

---

was converted to:

```text
PORT     STATUS   SERVICE      BANNER
------------------------------------------------------
22       OPEN     ssh          SSH-2.0-TestServer
80       OPEN     http         Apache/2.4.62
```

---

Now we must make sure:

```python
format_scan_results()
```

works correctly under all conditions.

---

File content:

```python
from src import format_scan_results, ScanResult


def test_format_scan_results():
    results = [
        ScanResult(
            port=22,
            service="ssh",
            banner="SSH-2.0-TestServer",
        ),
        ScanResult(
            port=80,
            service="http",
            banner="Apache/2.4.62",
        ),
    ]
    output = format_scan_results(results)

    assert "PORT" in output
    assert "STATUS" in output
    assert "SERVICE" in output
    assert "BANNER" in output

    assert "22" in output
    assert "ssh" in output
    assert "SSH-2.0-TestServer" in output

    assert "80" in output
    assert "http" in output
    assert "Apache/2.4.62" in output


def test_format_scan_results_with_missing_banner():
    results = [
        ScanResult(
            port=53,
            service="domain",
            banner=None,
        )
    ]

    output = format_scan_results(results)

    assert "53" in output
    assert "domain" in output
    assert "-" in output


def test_format_scan_results_with_empty_results():
    output = format_scan_results([])
    assert output == "No open ports found."


def test_format_scan_results_truncates_long_banner():
    long_banner = "A" * 100
    results = [
        ScanResult(
            port=80,
            service="http",
            banner=long_banner,
        )
    ]
    output = format_scan_results(results)

    assert "..." in output
    assert long_banner not in output
```

---

# Imports

```python
from src import (
    format_scan_results,
    ScanResult
)
```

---

The function under test:

```python
format_scan_results()
```

---

And the data model:

```python
ScanResult
```

---

# What Is the Goal of This File?

Checking:

✅ Table formatting

✅ Displaying port information

✅ Displaying the service

✅ Displaying the Banner

✅ Handling an empty Banner

✅ Handling an empty list

✅ Truncating long Banners

---

# The First Test

```python
def test_format_scan_results():
```

---

Goal:

```text
Checking the standard table output
```

---

# Building Test Data

```python
results = [
    ...
]
```

---

We build two scan results.

---

First result:

```python
ScanResult(
    port=22,
    service="ssh",
    banner="SSH-2.0-TestServer"
)
```

---

Second result:

```python
ScanResult(
    port=80,
    service="http",
    banner="Apache/2.4.62"
)
```

---

# Running the Function

```python
output =
    format_scan_results(
        results
    )
```

---

Now:

```python
output
```

is a multi-line string.

---

Something like:

```text
PORT     STATUS   SERVICE      BANNER
------------------------------------------------------
22       OPEN     ssh          SSH-2.0-TestServer
80       OPEN     http         Apache/2.4.62
```

---

# Checking the Header

```python
assert "PORT" in output
```

---

We check that:

```text
The PORT column
```

exists.

---

The same is done for:

```python
STATUS
```

---

```python
SERVICE
```

---

And

```python
BANNER
```

---

# Why Is This Test Important?

If someone changes the Header in the future:

```python
"PORT"
↓
"PORTS"
```

---

This test fails.

---

As a result, we notice the unwanted change.

---

# Checking the First Port's Information

```python
assert "22" in output
```

---

```python
assert "ssh" in output
```

---

```python
assert "SSH-2.0-TestServer" in output
```

---

Meaning:

```text
Port 22's information
is displayed in the table.
```

---

# Checking the Second Port's Information

```python
assert "80" in output
```

---

```python
assert "http" in output
```

---

```python
assert "Apache/2.4.62" in output
```

---

This test makes sure:

```text
All the data
has been transferred to the output.
```

---

# The Second Test

```python
def test_format_scan_results_with_missing_banner():
```

---

Goal:

```text
Checking an empty Banner
```

---

If you remember, in:

```python
formatter.py
```

we had:

```python
banner =
    result.banner or "-"
```

---

Meaning:

```python
None
```

↓

```python
"-"
```

is converted.

---

# Test Data

```python
ScanResult(
    port=53,
    service="domain",
    banner=None
)
```

---

The Banner does not exist.

---

# Running the Function

```python
output =
    format_scan_results(...)
```

---

# Checking the Port

```python
assert "53" in output
```

---

# Checking the Service

```python
assert "domain" in output
```

---

# Checking the Banner Replacement

```python
assert "-" in output
```

---

This test guarantees:

```text
The user sees "-"
instead of None.
```

---

Which is much more readable.

---

# The Third Test

```python
def test_format_scan_results_with_empty_results():
```

---

Goal:

```text
Checking the no-open-ports case
```

---

This case is very common.

---

For example:

```bash
python cli.py 192.168.1.50 1 100
```

---

And no port is open.

---

# Running the Function

```python
output =
    format_scan_results([])
```

---

The list is completely empty.

---

# If You Remember

In:

```python
formatter.py
```

we had:

```python
if not results:
    return "No open ports found."
```

---

# Checking

```python
assert output ==
    "No open ports found."
```

---

This test guarantees:

```text
An appropriate output
is displayed to the user.
```

---

And an empty table is not produced.

---

# The Fourth Test

```python
def test_format_scan_results_truncates_long_banner():
```

---

The most interesting test of the file.

---

Goal:

```text
Checking the truncation of long Banners
```

---

# Building a Long Banner

```python
long_banner =
    "A" * 100
```

---

Meaning:

```text
AAAAAAAAAAAAAAAAAAAAAAAA...
```

---

One hundred A characters.

---

# Building the Result

```python
ScanResult(
    port=80,
    service="http",
    banner=long_banner
)
```

---

# Running the Function

```python
output =
    format_scan_results(...)
```

---

If you remember, in:

```python
formatter.py
```

we had:

```python
if len(banner) > max_banner_length:
```

---

And then:

```python
banner =
    banner[: max_banner_length - 3]
    + "..."
```

---

Meaning:

```text
The Banner is shortened.
```

---

# The First Check

```python
assert "..." in output
```

---

Three dots must be present.

---

# The Second Check

```python
assert long_banner not in output
```

---

This is the most important part of the test.

---

Meaning:

```text
The full Banner
must not be displayed.
```

---

If the entire 100-character string is still in the output:

```text
The test fails.
```

---

# Why Is This Feature Important?

Suppose the Banner is:

```text
Microsoft-IIS/10.0 Build...
+ hundreds of other characters
```

---

If it is not truncated:

```text
The entire terminal table
breaks.
```

---

That is why we defined:

```python
max_banner_length
```

---

# What Types of Tests Are in This File?

This file has several different types of tests:

---

# Content Testing

Checking content

```python
assert "ssh" in output
```

---

# Empty State Testing

Checking the no-data case

```python
[]
```

---

# Fallback Testing

Checking the replacement value

```python
None
↓
"-"
```

---

# Truncation Testing

Checking truncation

```python
Long Banner
↓
...
```

---

# How This File Relates to the CLI

If you remember, in:

```python
cli.py
```

we had:

```python
print(
    format_scan_results(
        results
    )
)
```

---

Meaning:

```python
format_scan_results()
```

is the last stage before displaying the output.

---

Therefore, if this function breaks:

```text
The entire terminal output breaks.
```

---

That is why these tests are so important.

---

# pytest Output

If everything is correct:

```bash
pytest
```

---

Output:

```text
==== 4 passed ====
```

---

# Summary

In this session, we learned:

✅ Testing text output

✅ Testing the terminal table

✅ Testing Headers

✅ Testing an empty Banner

✅ Testing an empty list

✅ Testing the truncation of long strings

✅ What a Fallback Value is

✅ What Truncation is

✅ The importance of the Formatter in the CLI

---

# The Current Status of the Project

Files reviewed:

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
```

---

We are almost at the end of the tests walkthrough chapter.

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
tests/test_csv_exporter.py
```

---

There we will learn:

✅ Testing CSV files

✅ Testing CSV content

✅ Testing Headers

✅ Testing output rows

✅ Working with temporary files in pytest
