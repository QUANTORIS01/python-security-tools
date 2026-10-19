[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/tests/17-test-cli.md)

# A Complete Review of the `test_cli.py` File

# Introduction

Congratulations 🎉

We have reached the most important test file of the entire project.

---

So far, we have tested files that had:

```text
One function
↓
One input
↓
One output
```

---

For example:

```python
validate_ip()
```

---

Or:

```python
detect_service()
```

---

But the file:

```text
test_cli.py
```

is different.

---

Why?

---

Because this time we are testing:

```text
The entire program
```

---

Meaning exactly what the user runs:

```bash
python cli.py ...
```

---

In fact, this file is the closest test to the real user experience.

---

# The Goal of the File

Testing:

```python
create_parser()
```

and

```python
main()
```

---

Meaning making sure:

✅ Parameters are read correctly

✅ Validation works correctly

✅ Errors are displayed

✅ Terminal output is correct

✅ The JSON file is created

✅ The CSV file is created

✅ The log is recorded

---

# File Content

```python
import pytest

from src.cli import create_parser, main
from src import ScanResult


def test_create_parser():
    parser = create_parser()
    args = parser.parse_args(["127.0.0.1", "1", "1000"])
    assert args.ip == "127.0.0.1"
    assert args.start_port == 1
    assert args.end_port == 1000
    assert args.timeout == 0.5
    assert args.workers == 100


def test_main_with_valid_arguments(monkeypatch, capsys):
    def fake_scan_range(ip, start_port, end_port, timeout, workers):
        return [22, 80, 443]

    monkeypatch.setattr("src.cli.scan_range", fake_scan_range)
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "1000"])
    main()
    captured = capsys.readouterr()
    assert "ssh" in captured.out
    assert "http" in captured.out
    assert "https" in captured.out

    assert "22" in captured.out
    assert "80" in captured.out
    assert "443" in captured.out


def test_main_with_invalid_ip(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["cli.py", "999.999.999.999", "1", "1000"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Invalid IP address" in captured.out


def test_main_with_invalid_port_range(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "5000", "1000"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Invalid port range" in captured.out


def test_main_with_invalid_timeout(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "1000", "--timeout", "0"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Timeout must be greater than 0" in captured.out


def test_main_with_invalid_workers(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "1000", "--workers", "0"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Workers must be greater than 0" in captured.out


def test_main_shows_service_names(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["port_scanner", "127.0.0.1", "1", "1000"])
    monkeypatch.setattr("src.cli.scan_range", lambda *args, **kwargs: [80, 443])
    monkeypatch.setattr("src.cli.build_scan_results", lambda *args, **kwargs: [
        ScanResult(
            port=80,
            service="http",
            banner=None,
        ),
        ScanResult(
            port=443,
            service="https",
            banner=None,
        ),
    ])
    main()
    captured = capsys.readouterr()
    assert "http" in captured.out
    assert "https" in captured.out


def test_main_exports_json(monkeypatch, capsys):
    exported = {}

    def fake_scan_range(*args, **kwargs):
        return [80, 443]

    def fake_export_json(data, filename):
        exported["data"] = data
        exported["filename"] = filename

    monkeypatch.setattr("src.cli.scan_range", fake_scan_range)
    monkeypatch.setattr("src.cli.export_json", fake_export_json)
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "1000", "--json", "result.json"])
    main()
    assert exported["filename"] == "result.json"


def test_main_exports_csv(monkeypatch):
    exported = {}

    def fake_scan_range(*args, **kwargs):
        return [80, 443]

    def fake_export_csv(data, filename):
        exported["data"] = data
        exported["filename"] = filename

    monkeypatch.setattr("src.cli.scan_range", fake_scan_range)
    monkeypatch.setattr("src.cli.export_csv", fake_export_csv)
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "1000", "--csv", "result.csv"])
    main()
    assert exported["filename"] == "result.csv"
    assert exported["data"]["target"] == "127.0.0.1"
    assert exported["data"]["open_ports"] == [
        {
            "port": 80,
            "service": "http",
            "banner": None,
        },
        {
            "port": 443,
            "service": "https",
            "banner": None,
        },
    ]


def test_main_creates_log_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "10"])
    monkeypatch.setattr("src.cli.scan_range", lambda *args, **kwargs: [3, 5])
    main()
    log_file = tmp_path / "scan.log"
    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert "Scan started" in content
    assert "target=127.0.0.1" in content
    assert "ports=1-10" in content
    assert "Scan completed" in content
    assert "open_ports=2" in content
```

---

# Imports

```python
import pytest
```

---

For:

```python
pytest.raises()
```

---

Which we will examine a bit further ahead.

---

```python
from src.cli import (
    create_parser,
    main
)
```

---

The functions under test.

---

```python
from src import ScanResult
```

---

For building test data.

---

# The First Test

```python
def test_create_parser():
```

---

Goal:

```text
Checking the Argument Parser
```

---

# Creating the Parser

```python
parser = create_parser()
```

---

The same function we wrote in:

```text
cli.py
```

---

# Simulating Input

```python
args =
    parser.parse_args(
        [
            "127.0.0.1",
            "1",
            "1000"
        ]
    )
```

---

It is equivalent to:

```bash
python cli.py 127.0.0.1 1 1000
```

---

# Checking the IP

```python
assert args.ip == "127.0.0.1"
```

---

# Checking the Start Port

```python
assert args.start_port == 1
```

---

# Checking the End Port

```python
assert args.end_port == 1000
```

---

# Checking the Default Timeout

```python
assert args.timeout == 0.5
```

---

If the user does not provide a value:

```python
0.5
```

is used.

---

# Checking the Default Workers

```python
assert args.workers == 100
```

---

This test makes sure:

```text
The Parser behaves exactly as designed.
```

---

# What Is Monkeypatch?

Before continuing, we must become familiar with the most important tool in this file.

---

```python
monkeypatch
```

---

One of pytest's wonderful features.

---

Task:

```text
Temporarily replacing objects
```

---

For example:

```python
scan_range()
```

---

is replaced with a fake version.

---

# Why Is Monkeypatch Important?

Suppose in every test:

```python
scan_range()
```

actually runs.

---

Problems:

❌ The test becomes slow

❌ A network is required

❌ Results become variable

---

That is why:

```python
Fake Functions
```

are built.

---

# The Second Test

```python
test_main_with_valid_arguments()
```

---

One of the most important tests of the project.

---

# The Fake Function

```python
def fake_scan_range(...):
```

---

Instead of the real scan:

```python
return [22, 80, 443]
```

---

is returned.

---

# Replacing

```python
monkeypatch.setattr(
    "src.cli.scan_range",
    fake_scan_range
)
```

---

From this moment:

```python
scan_range()
```

does not actually run.

---

Rather:

```python
fake_scan_range()
```

runs.

---

# Simulating the Command Line

```python
monkeypatch.setattr(
    "sys.argv",
    [...]
)
```

---

This is extremely important.

---

In fact, we are pretending the user ran:

```bash
python cli.py 127.0.0.1 1 1000
```

---

# Running the Program

```python
main()
```

---

The program runs.

---

# What Is `capsys`?

Another pytest feature.

---

```python
capsys
```

---

It captures all the output:

```python
print()
```

calls.

---

# Getting the Output

```python
captured =
    capsys.readouterr()
```

---

Now:

```python
captured.out
```

contains the terminal output.

---

# Checking the Output

```python
assert "ssh" in captured.out
```

---

And:

```python
assert "http" in captured.out
```

---

And:

```python
assert "https" in captured.out
```

---

This test makes sure:

```text
Service Detection
```

is visible in the output.

---

# Checking the Port Numbers

```python
assert "22" in captured.out
```

---

```python
assert "80" in captured.out
```

---

```python
assert "443" in captured.out
```

---

So the table's output is also checked.

---

# What Is `pytest.raises`?

In the following tests, we will see this pattern several times:

```python
with pytest.raises(SystemExit):
```

---

Goal:

```text
Checking errors
```

---

# The Invalid IP Test

```python
test_main_with_invalid_ip()
```

---

Input:

```python
999.999.999.999
```

---

The program must:

```python
sys.exit(1)
```

execute.

---

In Python:

```python
sys.exit()
```

in fact:

```python
SystemExit
```

is raised.

---

That is why:

```python
pytest.raises()
```

catches it.

---

# Checking the Exit Code

```python
assert exc_info.value.code == 1
```

---

Meaning:

```text
The program has exited with an error.
```

---

# Checking the Error Message

```python
assert "Invalid IP address"
```

---

This test makes sure:

```text
The user receives an appropriate message.
```

---

# The Invalid Port Range Test

The same logic:

```python
5000
1000
```

---

And expectation:

```python
SystemExit(1)
```

---

# The Invalid Timeout Test

Input:

```python
--timeout 0
```

---

Because:

```python
timeout > 0
```

was required.

---

We must get an error.

---

# The Invalid Workers Test

Input:

```python
--workers 0
```

---

Must:

```python
SystemExit(1)
```

happen.

---

# The Service Names Display Test

```python
test_main_shows_service_names()
```

---

In this test:

```python
scan_range()
```

and

```python
build_scan_results()
```

are both mocked.

---

# Why?

Because we do not want to:

```text
Actually perform a scan.
```

---

We only want to test:

```text
The output display
```

---

# Fake Data

```python
ScanResult(
    port=80,
    service="http"
)
```

---

And:

```python
ScanResult(
    port=443,
    service="https"
)
```

---

# Checking the Output

```python
assert "http"
```

---

And:

```python
assert "https"
```

---

# The JSON Export Test

```python
test_main_exports_json()
```

---

Here:

```python
export_json()
```

is mocked.

---

Instead of creating a real file:

```python
exported = {}
```

---

is filled.

---

# The Fake Function

```python
def fake_export_json(...)
```

---

Saves the data.

---

# Checking

```python
assert exported["filename"]
```

---

This test makes sure:

```text
The correct file name was passed.
```

---

# The CSV Export Test

Similar to the previous test.

---

But this time:

```python
export_csv()
```

is checked.

---

An important point:

```python
assert exported["data"]
```

---

It checks both the data structure and the content.

---

# The Log File Test

The last and most professional test in the file.

---

```python
test_main_creates_log_file()
```

---

# Changing the Working Directory

```python
monkeypatch.chdir(
    tmp_path
)
```

---

Meaning:

```text
Enter the temporary directory.
```

---

# Running the Program

```python
main()
```

---

# Checking the File

```python
scan.log
```

---

must have been created.

---

# Checking the File's Existence

```python
assert log_file.exists()
```

---

# Reading the File

```python
content =
    log_file.read_text(...)
```

---

# Checking the Content

```python
assert "Scan started"
```

---

```python
assert "target=127.0.0.1"
```

---

```python
assert "ports=1-10"
```

---

```python
assert "Scan completed"
```

---

```python
assert "open_ports=2"
```

---

This test proves:

```text
The project's logging system
works correctly.
```

---

# The Importance of This File

If I had to keep only one test file in the entire project:

```text
test_cli.py
```

would be the top choice.

---

Why?

---

Because it involves almost:

```text
All the components of the project
```

---

# New Concepts We Learned in This File

✅ Monkeypatch

✅ Fake Functions

✅ Mocking

✅ `capsys`

✅ `sys.argv`

✅ `pytest.raises`

✅ `SystemExit`

✅ CLI Testing

✅ Log Testing

✅ Export Testing

---

# Summary

In this session, we learned:

✅ How to test the CLI

✅ How to simulate command-line input

✅ How to check terminal output

✅ How to test errors

✅ How to test export files

✅ How to test the logging system

✅ How to use Monkeypatch

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
tests/test_banner.py
```

---

There we will learn:

✅ Testing Banner Grabbing

✅ Creating a test server to send a Banner

✅ Testing data received from a Socket

✅ Testing the Timeout

✅ Testing the Service Response
