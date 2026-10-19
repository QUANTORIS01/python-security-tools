[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/tests/19-test-models.md)

# A Complete Review of the `test_models.py` File

# Introduction

So far, we have reviewed almost all the practical parts of the project:

✅ Input validation

✅ Port scanning

✅ Service detection

✅ Output storage

✅ CLI

✅ Banner Grabbing

---

But one important part still remains.

---

A part on which almost all components of the project depend:

```text
The Data Model
```

---

If you remember, in the file:

```text
src/models.py
```

we built the following class:

```python
@dataclass(frozen=True)
class ScanResult:
```

---

This class's task was:

```text
Holding the result of each open port
```

---

Example:

```python
ScanResult(
    port=22,
    service="ssh",
    banner="SSH-2.0-OpenSSH"
)
```

---

Now we must make sure:

```python
ScanResult
```

is built correctly and behaves exactly as we expect.

---

# File Content

```python
import pytest

from src import ScanResult


def test_scan_result_creation():
    result = ScanResult(port=22, service="ssh", banner="SSH-2.0-TestServer")
    assert result.port == 22
    assert result.service == "ssh"
    assert result.banner == "SSH-2.0-TestServer"


def test_scan_result_banner_defaults_to_none():
    result = ScanResult(port=80, service="http")
    assert result.banner is None


def test_scan_result_is_immutable():
    result = ScanResult(port=22, service="ssh")

    with pytest.raises(AttributeError):
        result.port = 80
```

---

# The First Import

```python
import pytest
```

---

For testing errors.

---

# The Second Import

```python
from src import ScanResult
```

---

The model that is going to be tested.

---

# What Is the Goal of This File?

Checking three important things:

---

```text
Correct object creation
```

---

```text
The default value of Banner
```

---

```text
Immutability of the model
```

---

# The First Test

```python
def test_scan_result_creation():
```

---

Goal:

```text
Checking that the object is created correctly
```

---

# Creating an Instance

```python
result = ScanResult(
    port=22,
    service="ssh",
    banner="SSH-2.0-TestServer"
)
```

---

Here, we create an object of the class:

```python
ScanResult
```

---

In memory, something like this is created:

```python
{
    "port": 22,
    "service": "ssh",
    "banner": "SSH-2.0-TestServer"
}
```

---

Of course, this is not a dictionary.

---

But for understanding the structure, we can imagine it this way.

---

# Checking the Port

```python
assert result.port == 22
```

---

We check that:

```python
port
```

was stored correctly.

---

# Checking the Service

```python
assert result.service == "ssh"
```

---

We check that:

```python
service
```

was initialized correctly.

---

# Checking the Banner

```python
assert (
    result.banner
    ==
    "SSH-2.0-TestServer"
)
```

---

We check that:

```python
banner
```

was also stored correctly.

---

# What Does This Test Prove?

This test proves:

```text
The Dataclass is built correctly.
```

---

And the fields are stored with the exact values we passed.

---

# The Second Test

```python
def test_scan_result_banner_defaults_to_none():
```

---

Goal:

```text
Checking the default value of Banner
```

---

If you remember, in:

```python
models.py
```

we had:

```python
banner: str | None = None
```

---

Pay attention:

```python
= None
```

---

Meaning:

```text
The parameter is optional.
```

---

# Creating the Object

```python
result = ScanResult(
    port=80,
    service="http"
)
```

---

Notice:

```python
banner
```

was not passed.

---

# What Happens?

Python uses the default value:

```python
banner = None
```

---

# Checking

```python
assert result.banner is None
```

---

This test verifies:

```text
The default value
was defined correctly.
```

---

# Why Is This Test Important?

Because in our project:

```text
Not all services have a Banner.
```

---

For example:

```python
80
```

might return a Banner.

---

But:

```python
53
```

usually does not have a Banner.

---

That is why:

```python
None
```

is a completely valid value.

---

# The Third Test

```python
def test_scan_result_is_immutable():
```

---

The most important test of the file.

---

Why?

---

Because it is related to the:

```python
frozen=True
```

feature.

---

# Creating the Object

```python
result = ScanResult(
    port=22,
    service="ssh"
)
```

---

So far, everything is normal.

---

# The Important Part of the Test

```python
with pytest.raises(
    AttributeError
):
```

---

Goal:

```text
We expect an error.
```

---

# Attempting to Change the Value

```python
result.port = 80
```

---

If this were a regular class:

```python
class Example:
```

---

There would be no problem.

---

But:

```python
ScanResult
```

is defined like this:

```python
@dataclass(
    frozen=True
)
```

---

Meaning:

```text
After it is created
it cannot be changed.
```

---

This feature is called:

```text
Immutability
```

---

# What Is Immutable?

The word:

```text
Immutable
```

means:

```text
Unchangeable
```

---

Example:

```python
result.port = 80
```

↓

```text
Forbidden
```

---

Python raises an error.

---

# Which Error?

```python
AttributeError
```

---

That is why:

```python
pytest.raises(
    AttributeError
)
```

waits for exactly this error.

---

# If the Error Is Raised

```text
PASS
```

---

# If the Error Is Not Raised

```text
FAIL
```

---

# Why Is Immutability Important?

Suppose a scan result has been created:

```python
ScanResult(
    port=22,
    service="ssh"
)
```

---

Now, somewhere in the program:

```python
result.port = 9999
```

---

If such a thing were allowed:

```text
The scan data would be corrupted.
```

---

But with:

```python
frozen=True
```

this is impossible.

---

# Advantages of Immutable Objects

✅ Greater safety

✅ Prevents accidental data mutation

✅ Easier debugging

✅ Suitable for multi-threaded systems

✅ Suitable for data models

---

# What Exactly Does Dataclass Build?

Behind the scenes:

```python
@dataclass
```

generates approximately this:

```python
class ScanResult:
    def __init__(
        self,
        port,
        service,
        banner=None
    ):
        self.port = port
        self.service = service
        self.banner = banner
```

---

But:

```python
frozen=True
```

is also added.

---

Which prevents modifying the fields after the object is created.

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

✅ What a Dataclass is

✅ How to test a Dataclass

✅ Testing object creation

✅ Testing the default value

✅ What Immutable means

✅ What `frozen=True` does

✅ Why `AttributeError` is raised

✅ How `pytest.raises` works

✅ The advantages of immutable data models

---

# The Current Status of the Project

By now, we have completely reviewed the following files:

```text
test_validator.py
test_scanner.py
test_services.py
test_exporter.py
test_cli.py
test_banner.py
test_models.py
```

---

Meaning we have completed a large part of the project's tests.

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
tests/test_results.py
```

---

There we will learn:

✅ Testing the creation of `ScanResult`s

✅ Testing `build_scan_results()`

✅ Mocking `detect_service()`

✅ Mocking `grab_banner()`

✅ Testing the scan-results processing

✅ What Dependency Isolation is
