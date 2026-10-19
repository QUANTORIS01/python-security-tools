[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/tests/20-test-results.md)

# A Complete Review of the `test_results.py` File

# Introduction

So far, we have reviewed almost all the components of the project:

✅ Validator

✅ Scanner

✅ Services

✅ Exporter

✅ Logger

✅ Banner

✅ Models

✅ CLI

---

But now we have reached one of the most important files of the project:

```text
results.py
```

---

If you remember, this file's task was:

```text
To convert the raw scan output
```

into:

```text
Structured results
```

---

Meaning from this:

```python
[22, 80]
```

---

To this:

```python
[
    ScanResult(
        port=22,
        service="ssh",
        banner="SSH-2.0-TestServer"
    ),
    ScanResult(
        port=80,
        service="http",
        banner="HTTP/1.1 200 OK"
    )
]
```

---

In fact:

```python
build_scan_results()
```

is the bridge between:

```text
The scanner
```

and

```text
The final output
```

---

# File Content

```python
from src import ScanResult, build_scan_results


def test_build_scan_results(monkeypatch):
    def fake_detect_service(port):
        return "ssh"

    def fake_grab_banner(ip, port, timeout):
        return "SSH-2.0-TestServer"

    monkeypatch.setattr("src.results.detect_service", fake_detect_service)
    monkeypatch.setattr("src.results.grab_banner", fake_grab_banner)
    results = build_scan_results("127.0.0.1", [22], timeout=2.0)
    assert results == [
        ScanResult(
            port=22,
            service="ssh",
            banner="SSH-2.0-TestServer",
        )
    ]


def test_build_scan_results_with_multiple_ports(monkeypatch):
    def fake_detect_service(port):
        services = {22: "ssh", 80: "http"}
        return services[port]

    def fake_grab_banner(ip, port, timeout):
        banners = {22: "SSH-2.0-TestServer", 80: "HTTP/1.1 200 OK"}
        return banners[port]

    monkeypatch.setattr("src.results.detect_service", fake_detect_service)
    monkeypatch.setattr("src.results.grab_banner", fake_grab_banner)
    results = build_scan_results("127.0.0.1", [22, 80])
    assert results == [
        ScanResult(
            port=22,
            service="ssh",
            banner="SSH-2.0-TestServer",
        ),
        ScanResult(
            port=80,
            service="http",
            banner="HTTP/1.1 200 OK",
        ),
    ]


def test_build_scan_results_handles_missing_banner(monkeypatch):
    monkeypatch.setattr("src.results.detect_service", lambda port: "http")
    monkeypatch.setattr("src.results.grab_banner", lambda ip, port, timeout: None)
    results = build_scan_results("127.0.0.1", [80])
    assert results == [
        ScanResult(
            port=80,
            service="http",
            banner=None,
        )
    ]
```

---

# What Is the Goal of This File?

Verifying that:

```python
build_scan_results()
```

under various conditions:

✅ Detects the service correctly

✅ Retrieves the Banner correctly

✅ Builds the `ScanResult` correctly

✅ Processes multiple ports correctly

✅ Handles a missing Banner correctly

---

# The First Test

```python
def test_build_scan_results(
    monkeypatch
):
```

---

Goal:

```text
Checking the construction of a result for one port
```

---

# Fake Detect Service

```python
def fake_detect_service(
    port
):
    return "ssh"
```

---

Whatever port is received:

```python
"ssh"
```

is returned.

---

# Fake Banner

```python
def fake_grab_banner(
    ip,
    port,
    timeout
):
    return "SSH-2.0-TestServer"
```

---

It always returns a specific Banner.

---

# Monkeypatch

```python
monkeypatch.setattr(
    "src.results.detect_service",
    fake_detect_service
)
```

---

From this moment:

```python
detect_service()
```

does not actually run.

---

Rather:

```python
fake_detect_service()
```

runs.

---

The same thing happens for:

```python
grab_banner()
```

---

# Running the Function

```python
results =
    build_scan_results(
        "127.0.0.1",
        [22],
        timeout=2.0
    )
```

---

Input:

```python
[22]
```

---

Execution flow:

```python
22
```

↓

```python
detect_service()
```

↓

```python
"ssh"
```

↓

```python
grab_banner()
```

↓

```python
"SSH-2.0-TestServer"
```

↓

```python
ScanResult(...)
```

---

# The Expected Output

```python
[
    ScanResult(
        port=22,
        service="ssh",
        banner="SSH-2.0-TestServer"
    )
]
```

---

# Checking

```python
assert results == [...]
```

---

An interesting point:

```python
Dataclass
```

objects have automatic comparison.

---

Meaning:

```python
ScanResult(...)
==
ScanResult(...)
```

---

is compared field by field.

---

# The Second Test

```python
test_build_scan_results_with_multiple_ports()
```

---

Goal:

```text
Checking the processing of multiple ports
```

---

This test is closer to the reality of the project.

---

Because usually:

```python
scan_range()
```

returns several ports.

---

# Fake Service

```python
services = {
    22: "ssh",
    80: "http"
}
```

---

Then:

```python
return services[port]
```

---

Result:

```python
22 → ssh
80 → http
```

---

# Fake Banner

```python
banners = {
    22: "SSH-2.0-TestServer",
    80: "HTTP/1.1 200 OK"
}
```

---

Result:

```python
22
```

↓

```python
SSH Banner
```

---

And:

```python
80
```

↓

```python
HTTP Banner
```

---

# Running the Function

```python
results =
    build_scan_results(
        "127.0.0.1",
        [22, 80]
    )
```

---

# Expectation

```python
[
    ScanResult(...),
    ScanResult(...)
]
```

---

Meaning:

```text
Two independent objects
```

must be created.

---

# Why Is This Test Important?

Because it verifies:

```python
for port in open_ports:
```

---

in:

```python
results.py
```

works correctly.

---

If the loop has a problem:

```text
This test fails.
```

---

# The Third Test

```python
test_build_scan_results_handles_missing_banner()
```

---

One of the most important tests of the file.

---

Goal:

```text
Checking a missing Banner
```

---

# Fake Service

```python
lambda port: "http"
```

---

Always returns:

```python
"http"
```

---

# Fake Banner

```python
lambda ip, port, timeout: None
```

---

Always returns:

```python
None
```

---

Meaning:

```text
There is no Banner.
```

---

# Running the Function

```python
results =
    build_scan_results(
        "127.0.0.1",
        [80]
    )
```

---

# Expectation

```python
[
    ScanResult(
        port=80,
        service="http",
        banner=None
    )
]
```

---

# Why Is This Test Important?

Because in the real world:

```text
Not all services have a Banner.
```

---

Some services return an empty:

```python
recv()
```

---

Or send no data at all.

---

In this case:

```python
grab_banner()
```

↓

```python
None
```

---

And the program must continue without errors.

---

This test guarantees that behavior.

---

# An Important Concept: Dependency Isolation

This file is one of the best examples of:

```text
Dependency Isolation
```

---

Meaning we test:

```python
build_scan_results()
```

---

Without actually running:

```python
detect_service()
```

---

And without actually running:

```python
grab_banner()
```

---

Why?

---

Because we only want to check:

```python
build_scan_results()
```

---

Not its dependencies.

---

This is one of the most important principles of professional testing.

---

# The Real Execution Path

In the main program:

```python
scan_range()
```

↓

```python
open_ports
```

↓

```python
build_scan_results()
```

↓

```python
detect_service()
```

↓

```python
grab_banner()
```

↓

```python
ScanResult
```

↓

```python
results
```

---

This file tests exactly the middle part of this chain.

---

# pytest Output

If everything is correct:

```bash
pytest
```

---

Output:

```text
==== 3 passed ====
```

---

# Summary

In this session, we learned:

✅ Testing `build_scan_results()`

✅ Mocking `detect_service()`

✅ Mocking `grab_banner()`

✅ Building `ScanResult`s

✅ Testing multiple ports at once

✅ Handling an empty Banner

✅ What Dependency Isolation is

✅ How Dataclass comparison works

✅ The importance of testing result processing

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
```

---

Meaning we are almost at the end of the testing section.

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
tests/test_formatter.py
```

---

There we will learn:

✅ Testing terminal output

✅ Testing table formatting

✅ Testing long Banners

✅ Testing Empty Results

✅ Testing multi-line strings

✅ How to validate CLI output
