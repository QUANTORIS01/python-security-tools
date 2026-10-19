[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/src/12-cli.md)

# A Complete Review of the `cli.py` File

# Introduction

We have reached the most important session of the entire course.

---

So far, we have learned all the pieces of the port scanner separately:

✅ validator.py

✅ scanner.py

✅ services.py

✅ exporter.py

✅ csv_exporter.py

✅ logger.py

✅ banner.py

✅ models.py

✅ results.py

✅ formatter.py

---

But one big question still remains.

---

How do all these files communicate with each other?

---

When the user runs this command:

```bash
python cli.py 127.0.0.1 1 100
```

---

What happens behind the scenes?

---

Which file runs first?

---

Which function is called?

---

How does data move between files?

---

The answer to all these questions is inside:

```text
src/cli.py
```

---

# The Role of the `cli.py` File

This file is the project's:

```text
Entry Point
```

---

Meaning:

```text
The starting point of the program's execution
```

---

In fact:

```text
The main brain of the project
```

---

All the files we built earlier:

```text
are tools
```

---

But:

```text
cli.py
```

is the leader of these tools.

---

# File Content

This file can be divided into several parts:

---

## Part One

Imports

---

## Part Two

Creating the Parser

---

## Part Three

Reading the arguments

---

## Part Four

Validating the input

---

## Part Five

Running the scan

---

## Part Six

Building the results

---

## Part Seven

Displaying the output

---

## Part Eight

Export

---

## Part Nine

Entry Point

---

# File Content

```python
import argparse
import sys
import time

from src import (
    scan_range,
    validate_ip,
    validate_port_range,
    validate_timeout,
    validate_workers,
    export_json,
    export_csv,
    setup_logger,
    build_scan_results,
    format_scan_results
)


def create_parser() -> argparse.ArgumentParser:
    """
    Create the command-line argument parser.
    """
    parser = argparse.ArgumentParser(description="TCP Port Scanner")
    parser.add_argument("ip", type=str, help="Target IPv4 address")
    parser.add_argument("start_port", type=int, help="Starting port number")
    parser.add_argument("end_port", type=int, help="Ending port number")
    parser.add_argument("-t", "--timeout", type=float, default=0.5, help="Connection timeout in seconds (default: 0.5)")
    parser.add_argument("-w", "--workers", type=int, default=100, help="Number of concurrent workers (default: 100)")
    parser.add_argument("--json", dest="json_file", type=str, help="Export results to a JSON file")
    parser.add_argument("--csv", dest="csv_file", type=str, help="Export results to a CSV file")
    return parser


def main() -> None:
    """
    Run the port scanner CLI.
    """
    parser = create_parser()
    args = parser.parse_args()
    if not validate_ip(args.ip):
        print(f"❌ Invalid IP address: {args.ip}")
        sys.exit(1)
    if not validate_port_range(args.start_port, args.end_port):
        print("❌ Invalid port range.")
        sys.exit(1)
    if not validate_timeout(args.timeout):
        print("❌ Timeout must be greater than 0.")
        sys.exit(1)

    if not validate_workers(args.workers):
        print("❌ Workers must be greater than 0.")
        sys.exit(1)
    logger = setup_logger("scan.log")
    print()
    print(f"🔍 Scanning {args.ip}")
    print(f"Port range: {args.start_port}-{args.end_port}")
    print(f"Timeout: {args.timeout}s")
    print(f"Workers: {args.workers}")
    print()
    start_time = time.perf_counter()
    logger.info("Scan started target=%s ports=%s-%s", args.ip, args.start_port, args.end_port)
    open_ports = scan_range(args.ip, args.start_port, args.end_port, timeout=args.timeout, workers=args.workers)
    results = build_scan_results(args.ip, open_ports, timeout=args.timeout)
    logger.info("Scan completed open_ports=%s", len(open_ports))
    elapsed_time = time.perf_counter() - start_time
    print("-" * 70)
    print(format_scan_results(results))
    print("-" * 70)
    print(f"Scan completed in {elapsed_time:.2f}s")
    print(f"Open ports found: {len(open_ports)}")
    export_data = {"target": args.ip, "start_port": args.start_port, "end_port": args.end_port, "open_ports": [
        {
            "port": result.port,
            "service": result.service,
            "banner": result.banner,
        } for result in results
    ]}
    if args.json_file:
        export_json(export_data, args.json_file)
        print(f"Results exported to {args.json_file}")

    if args.csv_file:
        export_csv(export_data, args.csv_file)
        print(f"Results exported to {args.csv_file}")


if __name__ == "__main__":
    main()

```

---

# Imports

```python
import argparse
import sys
import time
```

---

Three built-in Python modules.

---

# `argparse`

```python
import argparse
```

---

The most important CLI module in Python.

---

Task:

```text
Reading command-line arguments
```

---

Example:

```bash
python cli.py 127.0.0.1 1 100
```

---

Here:

```text
127.0.0.1
1
100
```

are arguments.

---

# `sys`

```python
import sys
```

---

For interacting with the operating system.

---

We only use:

```python
sys.exit()
```

---

# `time`

```python
import time
```

---

For measuring the scan's execution time.

---

# Imports from the Project

```python
from src import (...)
```

---

Pay attention.

---

All the files we built throughout this course are gathered here.

---

```python
scan_range
```

↓

Scanning

---

```python
validate_ip
```

↓

IP validation

---

```python
validate_port_range
```

↓

Port validation

---

```python
validate_timeout
```

↓

Timeout validation

---

```python
validate_workers
```

↓

Worker validation

---

```python
export_json
```

↓

JSON output

---

```python
export_csv
```

↓

CSV output

---

```python
setup_logger
```

↓

Log recording

---

```python
build_scan_results
```

↓

Building the models

---

```python
format_scan_results
```

↓

Displaying the output

---

# The `create_parser` Function

```python
def create_parser():
```

---

Goal:

```text
Building the CLI
```

---

# Creating the Parser

```python
parser = argparse.ArgumentParser(
    description="TCP Port Scanner"
)
```

---

This line:

```text
Builds the command-line program.
```

---

If the user writes:

```bash
python cli.py --help
```

---

The same Description is displayed.

---

# The First Argument

```python
parser.add_argument(
    "ip"
)
```

---

It is mandatory.

---

Example:

```bash
127.0.0.1
```

---

# The Second Argument

```python
start_port
```

---

Example:

```bash
1
```

---

# The Third Argument

```python
end_port
```

---

Example:

```bash
100
```

---

# Timeout

```python
-t
--timeout
```

---

Example:

```bash
--timeout 1
```

---

Or:

```bash
-t 1
```

---

# Workers

```python
-w
--workers
```

---

Example:

```bash
-w 500
```

---

# JSON Output

```python
--json
```

---

Example:

```bash
--json result.json
```

---

# CSV Output

```python
--csv
```

---

Example:

```bash
--csv result.csv
```

---

# Entering `main`

```python
def main():
```

---

All the program's execution starts here.

---

# Creating the Parser

```python
parser = create_parser()
```

---

# Reading the Arguments

```python
args = parser.parse_args()
```

---

Suppose we run:

```bash
python cli.py 127.0.0.1 1 100
```

---

Output:

```python
args.ip
```

↓

```python
127.0.0.1
```

---

```python
args.start_port
```

↓

```python
1
```

---

```python
args.end_port
```

↓

```python
100
```

---

# Validating the IP

```python
if not validate_ip(args.ip):
```

---

If the IP is not valid:

```python
print(...)
sys.exit(1)
```

---

The program stops.

---

# `sys.exit(1)`

```python
sys.exit(1)
```

---

Exit code:

```text
1
```

---

Usually meaning:

```text
Error
```

---

# Validating the Port

```python
validate_port_range(...)
```

---

Checking:

```text
0-65535
```

---

# Validating the Timeout

```python
validate_timeout(...)
```

---

Checking:

```text
Greater than zero
```

---

# Validating the Workers

```python
validate_workers(...)
```

---

Checking:

```text
Greater than zero
```

---

# Creating the Logger

```python
logger = setup_logger(
    "scan.log"
)
```

---

The file:

```text
scan.log
```

is created.

---

# Displaying the Initial Information

```python
print(...)
```

---

Sample output:

```text
Scanning 127.0.0.1
Port range: 1-100
Timeout: 0.5s
Workers: 100
```

---

# Starting the Time Measurement

```python
start_time = time.perf_counter()
```

---

This function is much more precise than:

```python
time.time()
```

---

It is suitable for Benchmarking.

---

# Recording the Scan Start

```python
logger.info(...)
```

---

Sample:

```text
Scan started
```

---

# Running the Scan

```python
open_ports = scan_range(...)
```

---

Here the file:

```python
scanner.py
```

runs.

---

Output:

```python
[22, 80, 443]
```

---

# Building the Results

```python
results = build_scan_results(...)
```

---

Here:

```python
results.py
```

runs.

---

Output:

```python
[
    ScanResult(...),
    ScanResult(...)
]
```

---

# Recording the Scan End

```python
logger.info(...)
```

---

Records the number of open ports.

---

# Calculating the Time

```python
elapsed_time =
    time.perf_counter()
    - start_time
```

---

Example:

```python
2.35
```

seconds.

---

# Displaying the Table

```python
format_scan_results(
    results
)
```

---

Here:

```python
formatter.py
```

runs.

---

Output:

```text
PORT
STATUS
SERVICE
BANNER
```

---

# Displaying the Statistics

```python
Open ports found
```

---

Example:

```text
3
```

---

# Building the Export Data

```python
export_data = {...}
```

---

This dictionary:

```python
ScanResult
```

converts the models into a file-suitable structure.

---

# List Comprehension

Here:

```python
[
    {
        ...
    }
    for result in results
]
```

---

It uses:

```python
List Comprehension
```

---

This part:

```python
ScanResult
```

converts the models into:

```python
dict
```

---

Example:

Before:

```python
ScanResult(...)
```

---

After:

```python
{
    "port": 80,
    "service": "http",
    "banner": "Apache"
}
```

---

# JSON Output

```python
if args.json_file:
```

---

If the user entered:

```bash
--json result.json
```

---

The JSON file is created.

---

# CSV Output

```python
if args.csv_file:
```

---

If:

```bash
--csv result.csv
```

exists.

---

The CSV file is created.

---

# The Most Important Part of the File

```python
if __name__ == "__main__":
    main()
```

---

This is one of the most important Python concepts.

---

# What Is `__name__`?

Every Python file has an internal variable:

```python
__name__
```

---

If the file is run directly:

```python
__name__
```

↓

```python
"__main__"
```

---

But if it is imported:

```python
import cli
```

---

Then:

```python
__name__
```

↓

```python
"cli"
```

---

# Why Is This Condition Important?

It makes:

```python
main()
```

run only when the file is run directly.

---

Not when it is imported.

---

# The Complete Execution Flow of the Project

```text
cli.py
    │
    ▼

validate_ip()

    │
    ▼

validate_port_range()

    │
    ▼

scan_range()

    │
    ▼

detect_service()

    │
    ▼

grab_banner()

    │
    ▼

ScanResult()

    │
    ▼

build_scan_results()

    │
    ▼

format_scan_results()

    │
    ▼

export_json()
export_csv()
```

---

This is the complete architecture of the port scanner we have built.

---

# Summary

In this session, we learned:

✅ What a CLI is

✅ What `argparse` is

✅ What a Parser is

✅ What `parse_args` is

✅ What `sys.exit` is

✅ What `perf_counter` is

✅ What the Entry Point is

✅ What `__name__` is

✅ What `__main__` is

✅ What List Comprehension is

✅ What the complete execution flow of the project is

---

# End of the `src` Directory

Congratulations 🎉

---

We have now reviewed all the main files of the project:

```text
line by line
```

---

A student should now be able to:

✅ Understand the project's structure

✅ Build a similar port scanner

✅ Add new features

✅ Extend the project's architecture

---

# What Will We Learn in the Next Chapter?

We now enter the directory:

```text
04-port-scanner/tests
```

---

In this part, we will learn:

✅ What a test is

✅ What a Unit Test is

✅ What `pytest` is

✅ What a Mock is

✅ What Monkeypatch is

✅ How to write professional tests for real projects
