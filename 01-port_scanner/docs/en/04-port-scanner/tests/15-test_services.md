[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/tests/15-test_services.md)

# A Complete Review of the `test_services.py` File

# Introduction

In the previous session, we learned how to test:

```python
scan_port()
```

and

```python
scan_range()
```

---

In that file, we tested:

```text
Real network behavior
```

---

But in this session, we enter a simpler but very important file:

```text
test_services.py
```

---

This file is responsible for testing:

```python
detect_service()
```

---

If you remember, in the file:

```text
src/services.py
```

we had the following function:

```python
def detect_service(port: int) -> str:
```

---

The function's task was:

```text
Converting a port number
to
a service name
```

---

Example:

```python
22
```

↓

```python
ssh
```

---

Or:

```python
80
```

↓

```python
http
```

---

Or:

```python
443
```

↓

```python
https
```

---

Now we must make sure this function really works correctly.

---

# File Content

```python
from src import detect_service


def test_detect_known_ssh_service():

    assert detect_service(22) == "ssh"


def test_detect_known_http_service():

    assert detect_service(80) == "http"


def test_detect_known_https_service():

    assert detect_service(443) == "https"


def test_detect_unknown_service():

    assert detect_service(65000) == "unknown"
```

---

# What Is the Goal of This File?

Goal:

```text
Verifying the correctness of Service Detection
```

---

Meaning making sure that:

```python
socket.getservbyport()
```

returns exactly what we expect.

---

# Import

```python
from src import detect_service
```

---

The function we want to test.

---

# The Test Type

This file is an example of:

```text
Known Values Testing
```

---

# What Is Known Values Testing?

One of the oldest testing methods.

---

The idea is very simple.

---

We already know the answer.

---

For example:

```python
22
```

is always:

```python
ssh
```

---

Or:

```python
80
```

is always:

```python
http
```

---

So we can compare the actual result with the expected result.

---

# The First Test

```python
def test_detect_known_ssh_service():
```

---

Goal:

```text
Checking the SSH port
```

---

Inside the test:

```python
assert detect_service(22) == "ssh"
```

---

Execution flow:

```python
detect_service(22)
```

↓

```python
socket.getservbyport(
    22,
    "tcp"
)
```

↓

```python
"ssh"
```

---

Then:

```python
assert
```

checks:

```python
"ssh" == "ssh"
```

---

Result:

```text
PASS
```

---

# Why Was SSH Chosen?

Because:

```python
22
```

is one of the most well-known TCP ports.

---

It is registered on almost all systems.

---

# The Second Test

```python
def test_detect_known_http_service():
```

---

Goal:

```text
Checking the HTTP service
```

---

Code:

```python
assert detect_service(80) == "http"
```

---

Execution flow:

```python
detect_service(80)
```

↓

```python
"http"
```

---

Then:

```python
assert
```

checks:

```python
"http" == "http"
```

---

Result:

```text
PASS
```

---

# Why Is HTTP Important?

Because:

```python
80
```

is the most famous web port.

---

Almost all operating system service databases recognize it.

---

# The Third Test

```python
def test_detect_known_https_service():
```

---

Goal:

```text
Checking HTTPS
```

---

Code:

```python
assert detect_service(443) == "https"
```

---

Flow:

```python
detect_service(443)
```

↓

```python
"https"
```

---

Then:

```python
assert
```

checks:

```python
"https" == "https"
```

---

Result:

```text
PASS
```

---

# Why Was HTTPS Chosen?

Because:

```python
443
```

is one of the most important ports on the Internet.

---

Today, almost all websites run on it.

---

# The Fourth Test

```python
def test_detect_unknown_service():
```

---

This is the most important test of the file.

---

Why?

---

Because we are checking:

```text
The error case
```

---

# Input

```python
65000
```

---

Why was this number chosen?

---

Because:

```python
65000
```

usually does not have a registered standard service.

---

So:

```python
socket.getservbyport()
```

cannot find a name for it.

---

As a result:

```python
OSError
```

is raised.

---

If you remember, in:

```python
services.py
```

we wrote:

```python
except OSError:
    return "unknown"
```

---

So we expect:

```python
detect_service(65000)
```

↓

```python
"unknown"
```

---

The test:

```python
assert detect_service(65000) == "unknown"
```

---

checks this behavior.

---

# Why Is Testing the Error Case More Important?

Many programmers only test:

```text
The success case
```

---

For example:

```python
22
80
443
```

---

But in practice:

```text
Errors are more important.
```

---

Because most bugs appear in unusual conditions.

---

That is why this test is very valuable.

---

# Does This Test Work on All Operating Systems?

Almost yes.

---

Because:

```python
ssh
http
https
```

are standard services.

---

But in very large projects, to avoid OS dependency, they usually use:

```text
Mock
```

---

We have not reached that stage yet.

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

# What Does This File Teach?

This file is an excellent example of:

```text
Testing Known Values
```

---

Meaning:

```text
Specific input
↓
Specific output
↓
Comparison
```

---

This type of test is used very often in real projects.

---

# Summary

In this session, we learned:

✅ How Service Detection is tested

✅ What Known Values Testing is

✅ Testing the SSH service

✅ Testing the HTTP service

✅ Testing the HTTPS service

✅ Testing the Unknown case

✅ The importance of testing error conditions

✅ The role of `assert` in comparing outputs

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
tests/test_exporter.py
```

---

There we will learn:

✅ Testing JSON files

✅ What a Temporary File is

✅ How to check output files

✅ How to validate JSON content

✅ How I/O testing is done in Python
