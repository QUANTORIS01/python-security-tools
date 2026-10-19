[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/tests/18-test-banner.md)

# A Complete Review of the `test_banner.py` File

# Introduction

So far, we have tested almost all the main parts of the project:

✅ Validator

✅ Scanner

✅ Services

✅ Exporter

✅ CLI

---

But one of the most fascinating features of the port scanner still remains:

```text
Banner Grabbing
```

---

If you remember, in the networking and security chapters, we said:

```text
Some services send information
about themselves after connecting.
```

---

For example:

```text
SSH-2.0-OpenSSH_9.3
```

---

Or:

```text
220 FTP Server Ready
```

---

Or:

```text
Apache/2.4.58
```

---

This information is called:

```text
Banner
```

---

And the function:

```python
grab_banner()
```

was responsible for retrieving it.

---

Now we must make sure:

```python
grab_banner()
```

works correctly in various conditions.

---

# File Content

```python
import socket

from src import grab_banner


def test_grab_banner_returns_banner(monkeypatch):
    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass

        def settimeout(self, timeout):
            self.timeout = timeout

        def connect(self, address):
            self.address = address

        def recv(self, size):
            return b"SSH-2.0-TestServer\r\n"

    monkeypatch.setattr(socket, "socket", lambda *args, **kwargs: FakeSocket())
    result = grab_banner("127.0.0.1", 22)
    assert result == "SSH-2.0-TestServer"


def test_grab_banner_returns_none_on_connection_error(monkeypatch):
    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass

        def settimeout(self, timeout):
            pass

        def connect(self, address):
            raise socket.error("Connection failed")

    monkeypatch.setattr(socket, "socket", lambda *args, **kwargs: FakeSocket())
    result = grab_banner("127.0.0.1", 9999)
    assert result is None


def test_grab_banner_returns_none_for_empty_response(monkeypatch):
    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass

        def settimeout(self, timeout):
            pass

        def connect(self, address):
            pass

        def recv(self, size):
            return b""

    monkeypatch.setattr(socket, "socket", lambda *args, **kwargs: FakeSocket())
    result = grab_banner("127.0.0.1", 80)
    assert result is None


def test_grab_banner_sets_timeout(monkeypatch):
    captured = {}

    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass

        def settimeout(self, timeout):
            captured["timeout"] = timeout

        def connect(self, address):
            pass

        def recv(self, size):
            return b"Test Banner"

    monkeypatch.setattr(socket, "socket", lambda *args, **kwargs: FakeSocket())
    grab_banner("127.0.0.1", 80, timeout=2.5)
    assert captured["timeout"] == 2.5
```

---

# The First Import

```python
import socket
```

---

For mocking the Socket.

---

# The Second Import

```python
from src import grab_banner
```

---

The function that is going to be tested.

---

# Why Is Mocking Used in This File?

If we wanted to:

```python
grab_banner()
```

to actually run:

---

We would need:

```text
A real server
```

---

And that server would have to:

```text
Actually send a Banner.
```

---

This makes the test:

❌ Slow

❌ Complicated

❌ Network-dependent

---

That is why we build:

```python
FakeSocket
```

---

# The First Test

```python
test_grab_banner_returns_banner()
```

---

Goal:

```text
Checking successful retrieval of a Banner
```

---

# The FakeSocket Class

```python
class FakeSocket:
```

---

This class is:

```text
A replacement for a real Socket
```

---

# The `__enter__` Method

```python
def __enter__(self):
    return self
```

---

If you remember, in:

```python
grab_banner()
```

we had:

```python
with socket.socket(...) as sock:
```

---

For:

```python
with
```

to work, we need:

```python
__enter__
```

to exist.

---

# The `__exit__` Method

```python
def __exit__(...)
```

---

For exiting the:

```python
with
```

block.

---

# `settimeout`

```python
def settimeout(...)
```

---

It just stores the value.

---

It does nothing real.

---

# `connect`

```python
def connect(...)
```

---

It simulates a successful connection.

---

# `recv`

The most important part of the test.

---

```python
def recv(self, size):
```

---

Returns:

```python
b"SSH-2.0-TestServer\r\n"
```

---

Pay attention:

```python
b"..."
```

---

Meaning:

```text
Bytes
```

---

Exactly what a real Socket returns.

---

# Monkeypatch

```python
monkeypatch.setattr(
    socket,
    "socket",
    ...
)
```

---

From this moment:

```python
socket.socket()
```

is not actually executed.

---

Rather:

```python
FakeSocket()
```

is created.

---

# Running the Function

```python
result =
    grab_banner(
        "127.0.0.1",
        22
    )
```

---

Flow:

```python
recv()
```

↓

```python
b"SSH-2.0-TestServer\r\n"
```

↓

```python
decode()
```

↓

```python
"SSH-2.0-TestServer"
```

---

# Checking the Output

```python
assert result ==
    "SSH-2.0-TestServer"
```

---

If the value is exactly this:

```text
PASS
```

---

# The Second Test

```python
test_grab_banner_returns_none_on_connection_error()
```

---

Goal:

```text
Checking a connection error
```

---

# FakeSocket

This time:

```python
connect()
```

has been changed.

---

```python
raise socket.error(
    "Connection failed"
)
```

---

Meaning:

```text
The connection should fail.
```

---

# Running the Function

```python
grab_banner(...)
```

---

In:

```python
banner.py
```

we had:

```python
except (
    socket.timeout,
    socket.error
):
    return None
```

---

So we expect:

```python
None
```

to be returned.

---

# Checking

```python
assert result is None
```

---

This test verifies:

```text
Error handling works correctly.
```

---

# The Third Test

```python
test_grab_banner_returns_none_for_empty_response()
```

---

Goal:

```text
Checking an empty Banner
```

---

# `recv`

This time:

```python
return b""
```

---

Meaning:

```text
No data was received.
```

---

# Execution Flow

In:

```python
grab_banner()
```

we had:

```python
banner.decode(...)
```

↓

```python
""
```

↓

```python
strip()
```

↓

```python
""
```

---

Then:

```python
"" or None
```

↓

```python
None
```

---

# Checking

```python
assert result is None
```

---

This test proves:

```text
An empty Banner
is not accepted as a valid Banner.
```

---

# The Fourth Test

```python
test_grab_banner_sets_timeout()
```

---

Goal:

```text
Checking correct delivery of the Timeout
```

---

This test is very professionally designed.

---

Why?

---

Because it does not:

```text
Check the function's output.
```

---

Rather:

```text
It checks the function's internal behavior.
```

---

# The Helper Dictionary

```python
captured = {}
```

---

For storing information.

---

# The `settimeout` Method

```python
def settimeout(
    self,
    timeout
):
```

---

Instead of performing a real operation:

```python
captured["timeout"] =
    timeout
```

---

is stored.

---

# Running the Function

```python
grab_banner(
    "127.0.0.1",
    80,
    timeout=2.5
)
```

---

Inside the function:

```python
sock.settimeout(
    2.5
)
```

is executed.

---

# Checking

```python
assert captured["timeout"] == 2.5
```

---

If the value:

```python
2.5
```

was recorded:

```text
PASS
```

---

# What Is This Type of Test Called?

This type of test is called:

```text
Behavior Verification
```

---

Meaning:

```text
Checking internal behavior
```

---

Not just the final output.

---

# A Very Important Point

This file contains almost all professional Mocking concepts:

✅ Fake Class

✅ Fake Socket

✅ Monkeypatch

✅ Error Simulation

✅ Empty Response Simulation

✅ Behavior Verification

---

That is why it is one of the most educational test files in the project.

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

✅ How to mock a Socket

✅ How to build a fake Banner

✅ How to simulate a connection error

✅ How to test an empty response

✅ How to validate the Timeout

✅ What Behavior Verification is

✅ What Fake Objects are

✅ How Mocking is done in network tests
