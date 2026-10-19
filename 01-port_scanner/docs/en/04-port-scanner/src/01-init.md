[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/src/01-init.md)

# Getting to Know the `__init__.py` File

## Introduction

So far in this course, we have learned:

- What Python is
- What a network is
- What cybersecurity is
- What a port scanner is
- How we designed the Port Scanner project

From this session, we enter the actual code of the project.

The first file we will review:

```text
src/__init__.py
```

At first glance, this file might seem very simple, but it plays an important role in the project's architecture.

---

## File Content

```python
from src.validator import validate_ip, validate_port_range, validate_timeout, validate_workers

from src.scanner import scan_port, scan_range

from src.services import detect_service

from src.exporter import export_json

from src.csv_exporter import export_csv

from src.logger import setup_logger

from src.banner import grab_banner

from src.models import ScanResult

from src.results import build_scan_results

from src.formatter import format_scan_results
```

---

# What Exactly Is the `__init__.py` File?

Whenever a file:

```text
__init__.py
```

exists in a folder, Python recognizes that folder as a Package.

Example:

```text
src/
│
├── __init__.py
├── validator.py
├── scanner.py
└── services.py
```

Python recognizes that:

```text
src
```

is a package.

---

# Why Didn't We Leave This File Empty?

Many projects leave the `__init__.py` file empty.

But we have used it to build an internal API.

Meaning, we want the user to be able to write:

```python
from src import scan_range
```

Instead of:

```python
from src.scanner import scan_range
```

---

# Reviewing the First Line

```python
from src.validator import validate_ip, validate_port_range, validate_timeout, validate_workers
```

---

## What Does This Line Do?

This line imports four functions from the file:

```text
validator.py
```

into the package.

The functions:

```python
validate_ip
validate_port_range
validate_timeout
validate_workers
```

---

## What Is the Result?

Now we can write:

```python
from src import validate_ip
```

Instead of:

```python
from src.validator import validate_ip
```

---

# Reviewing the Second Line

```python
from src.scanner import scan_port, scan_range
```

---

## What Does This Line Do?

It imports the two main scanning functions.

The first function:

```python
scan_port()
```

for scanning a single port.

The second function:

```python
scan_range()
```

for scanning a range of ports.

---

# Reviewing the Third Line

```python
from src.services import detect_service
```

---

## What Is This Function's Job?

When an open port is found:

```text
80
```

this function detects what service is probably running on it.

Example:

```python
detect_service(80)
```

Output:

```python
"http"
```

---

# Reviewing the Fourth Line

```python
from src.exporter import export_json
```

---

## What Is This Function's Job?

It saves the scan results to a:

```text
JSON
```

file.

Example:

```python
export_json(data, "result.json")
```

---

# Reviewing the Fifth Line

```python
from src.csv_exporter import export_csv
```

---

## What Is This Function's Job?

It saves the output to a:

```text
CSV
```

file.

Example:

```text
port,service
80,http
443,https
```

---

# Reviewing the Sixth Line

```python
from src.logger import setup_logger
```

---

## What Is This Function's Job?

It sets up the logging system.

Example:

```text
scanner.log
```

---

# Reviewing the Seventh Line

```python
from src.banner import grab_banner
```

---

## What Is This Function's Job?

It retrieves the service banner.

Example:

```text
SSH-2.0-OpenSSH_9.3
```

or

```text
Apache/2.4.58
```

---

# Reviewing the Eighth Line

```python
from src.models import ScanResult
```

---

## This Is Not a Function

This is a class.

We use it to store the scan results.

Example:

```python
ScanResult(
    port=80,
    service="http",
    banner="Apache"
)
```

---

# Reviewing the Ninth Line

```python
from src.results import build_scan_results
```

---

## What Is This Function's Job?

It converts the raw scan output into:

```python
ScanResult
```

objects.

---

# Reviewing the Tenth Line

```python
from src.formatter import format_scan_results
```

---

## What Is This Function's Job?

It prepares the results for display in the terminal.

Example:

```text
PORT     STATUS   SERVICE
80       OPEN     http
443      OPEN     https
```

---

# Why Didn't We Import `cli.py` Here?

The file:

```text
cli.py
```

is the entry point of the program.

This file is run directly by the user.

In tests, we also use it directly.

That is why we did not put it inside:

```python
__init__.py
```

---

# Summary

In this session, we learned:

✅ What the `__init__.py` file is

✅ What a package is in Python

✅ How we export functions

✅ Why we centralized the imports

✅ What each import in the file is used for

✅ Why `cli.py` was not placed in this file

---

# What Will We Learn in the Next Session?

In the next session, we enter the first real file of the project:

```text
src/validator.py
```

There we will learn:

- What validation is
- Why we should not trust user input
- How we validate an IP
- How we validate a Port Range
- How we validate a Timeout
- How we validate a Worker Count

