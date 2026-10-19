[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/tests/13-test-validator.md)

# A Complete Review of the `test_validator.py` File

# Introduction

Congratulations 🎉

We have entered the last part of the course:

```text
tests/
```

---

So far on our learning journey, we have learned:

✅ Python

✅ Networking

✅ Cybersecurity

✅ All the files in `src/`

---

But one very important skill still remains.

---

# Why Do We Write Tests?

Suppose the project works correctly today.

---

Tomorrow, you want to add a new feature.

---

For example:

```text
IPv6 Support
```

---

Or:

```text
UDP Scan
```

---

Or:

```text
Banner Detection Improvement
```

---

The question:

How do we find out whether the new feature has broken the existing code?

---

Answer:

```text
Testing
```

---

# What Is a Test?

A test means:

```text
Automatically verifying the correctness of the program's behavior
```

---

Instead of manually testing every time:

```text
Does the IP work correctly?
Does the Port Range work correctly?
Does the Timeout work correctly?
```

---

We write a test file.

---

Then we run:

```bash
pytest
```

---

And all the tests run automatically.

---

# File Content

```python
from src import (
    validate_ip,
    validate_port_range,
    validate_timeout,
    validate_workers,
)


def test_valid_ip():
    assert validate_ip("127.0.0.1")


def test_invalid_ip():
    assert not validate_ip("999.999.999.999")


def test_valid_port_range():
    assert validate_port_range(1, 1000)


def test_invalid_port_range():
    assert not validate_port_range(5000, 1000)


def test_valid_timeout():
    assert validate_timeout(0.5)
    assert validate_timeout(1.0)


def test_invalid_timeout():
    assert not validate_timeout(0)
    assert not validate_timeout(-1)


def test_valid_workers():
    assert validate_workers(1)
    assert validate_workers(100)


def test_invalid_workers():
    assert not validate_workers(0)
    assert not validate_workers(-5)


def test_valid_timeout_boundary():
    assert validate_timeout(0.001)


def test_valid_workers_boundary():
    assert validate_workers(1)
```

---

# What Is the Goal of This File?

Goal:

```text
Test all the functions in validator.py
```

---

Meaning verifying that:

```python
validate_ip()

validate_port_range()

validate_timeout()

validate_workers()
```

really work correctly or not.

---

# Import

```python
from src import (
    validate_ip,
    validate_port_range,
    validate_timeout,
    validate_workers,
)
```

---

They are imported from the file:

```text
src/__init__.py
```

---

Exactly what we did in the project's main code.

---

# How Does pytest Find the Tests?

The pytest rule:

---

File name:

```python
test_*
```

---

Or:

```python
*_test.py
```

---

Function name:

```python
test_*
```

---

So:

```python
def test_valid_ip():
```

is run automatically by pytest.

---

# What Is `assert`?

The most important keyword in testing.

---

```python
assert
```

means:

```text
This condition must be true.
```

---

Example:

```python
assert 1 == 1
```

---

It passes.

---

But:

```python
assert 1 == 2
```

---

The test fails.

---

# The First Test

```python
def test_valid_ip():
```

---

Goal:

```text
Checking a valid IP
```

---

Inside the test:

```python
assert validate_ip(
    "127.0.0.1"
)
```

---

The function:

```python
validate_ip()
```

must return:

```python
True
```

---

If it returns:

```python
True
```

---

```text
PASS
```

---

If it returns:

```python
False
```

---

```text
FAIL
```

---

# The Second Test

```python
def test_invalid_ip():
```

---

Goal:

```text
Checking an invalid IP
```

---

Input:

```python
999.999.999.999
```

---

Such an IP does not exist.

---

So we expect it to return:

```python
False
```

---

# `not` in `assert`

```python
assert not validate_ip(...)
```

---

Is equivalent to:

```python
assert validate_ip(...) == False
```

---

# The Valid Port Range Test

```python
def test_valid_port_range():
```

---

Input:

```python
1
1000
```

---

Because:

```python
1 <= 1000
```

---

And both are within the valid range.

---

It must return:

```python
True
```

---

# The Invalid Port Range Test

```python
def test_invalid_port_range():
```

---

Input:

```python
5000
1000
```

---

The problem:

```python
start_port > end_port
```

---

So it must return:

```python
False
```

---

# The Valid Timeout Test

```python
def test_valid_timeout():
```

---

Two values are tested:

```python
0.5
```

---

And:

```python
1.0
```

---

Both are:

```python
> 0
```

---

So they are valid.

---

# Why Are Multiple Values Tested?

This point is very important.

---

Professional programmers do not test just:

```python
A single value
```

---

Rather:

```text
Several different samples
```

are checked.

---

# The Invalid Timeout Test

```python
def test_invalid_timeout():
```

---

First input:

```python
0
```

---

Second input:

```python
-1
```

---

Our function said:

```python
timeout > 0
```

---

So both must be:

```python
False
```

---

# The Valid Worker Test

```python
def test_valid_workers():
```

---

First value:

```python
1
```

---

Second value:

```python
100
```

---

Both are valid.

---

# The Invalid Worker Test

```python
def test_invalid_workers():
```

---

First value:

```python
0
```

---

Second value:

```python
-5
```

---

Both are invalid.

---

# Boundary Testing

Now we reach the most important part of the file.

---

# What Is Boundary Testing?

One of the most important techniques in testing.

---

Errors usually occur at:

```text
The edges of a range
```

---

Example:

```python
timeout > 0
```

---

The question:

What is the smallest valid value?

---

Answer:

```python
0.001
```

---

That is why the following test is written:

```python
def test_valid_timeout_boundary():
```

---

Inside it:

```python
assert validate_timeout(
    0.001
)
```

---

This test checks:

```text
The validity boundary of Timeout
```

---

# The Worker Boundary Test

```python
def test_valid_workers_boundary():
```

---

Our function said:

```python
workers > 0
```

---

So:

```python
1
```

is the smallest valid value.

---

That is why:

```python
assert validate_workers(1)
```

is written.

---

# Why Is Boundary Testing Important?

Suppose the programmer makes a mistake and writes:

```python
workers >= 2
```

---

In this case:

```python
workers=1
```

breaks.

---

But the Boundary Test quickly finds the problem.

---

# pytest Output

If all tests succeed:

```bash
pytest
```

---

Output:

```text
========== 10 passed ==========
```

---

If one fails:

```text
FAILED
```

is displayed.

---

# What Type of Test Is This File?

This file is a:

```text
Unit Test
```

---

Why?

---

Because it tests each function:

```text
Independently
```

---

Example:

```python
validate_ip()
```

---

Without dependency on:

```python
scanner.py
```

---

Or:

```python
cli.py
```

---

# Advantages of This File

✅ Fast

✅ Simple

✅ Independent

✅ Understandable

✅ Suitable for Regression Testing

---

# Summary

In this session, we learned:

✅ What Testing is

✅ How pytest works

✅ What `assert` is

✅ What a Unit Test is

✅ What Boundary Testing is

✅ What a Positive Test is

✅ What a Negative Test is

✅ How we tested `validator.py`

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
tests/test_scanner.py
```

---

There we will learn:

✅ What a Mock is

✅ What Monkeypatch is

✅ Why we should not actually scan the network in tests

✅ How to simulate a Socket

✅ How to write professional tests for network functions
