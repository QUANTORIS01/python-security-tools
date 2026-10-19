[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/tests/14-test-scanner.md)

# A Complete Review of the `test_scanner.py` File

# Introduction

So far, we have reviewed the first tests of the project:

```text
test_validator.py
```

---

In that file, we tested:

```text
Simple functions
```

---

For example:

```python
validate_timeout()
```

---

Or:

```python
validate_workers()
```

---

But now we enter a more interesting part of testing.

---

The file:

```text
test_scanner.py
```

---

Why is it more interesting?

---

Because this time we are testing:

```text
Networking Code
```

---

And testing networking code is always harder than testing regular functions.

---

# What Is the Goal of This File?

Goal:

```text
Testing scanner.py
```

---

Meaning verifying that:

```python
scan_port()
```

and

```python
scan_range()
```

really work correctly.

---

# File Content

```python
import socket
import threading

from src import scan_port, scan_range
```

---

# The First Import

```python
import socket
```

---

For creating a test server.

---

# The Second Import

```python
import threading
```

---

For running the server in a separate Thread.

---

# Why Do We Need a Thread?

Suppose this code runs:

```python
server.accept()
```

---

This command:

```text
Waits for a connection.
```

---

Until a Client connects:

```python
accept()
```

does not return.

---

If it runs in the same Thread:

```text
The entire test locks up.
```

---

That is why we use:

```python
Thread
```

---

# Imports from the Project

```python
from src import (
    scan_port,
    scan_range
)
```

---

The functions we want to test.

---

# The `create_test_server` Function

```python
def create_test_server():
```

---

This function:

```text
Creates a temporary TCP server
```

---

All the following tests use this function.

---

# Creating the Socket

```python
server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
```

---

If you remember, in the networking chapter we said:

---

```python
AF_INET
```

↓

IPv4

---

```python
SOCK_STREAM
```

↓

TCP

---

So:

```python
TCP Server
```

is created.

---

# Bind

```python
server.bind(
    ("127.0.0.1", 0)
)
```

---

A very important point:

```python
0
```

---

Why port zero?

---

The operating system itself chooses a free port.

---

For example:

```text
54321
```

---

Or:

```text
61500
```

---

Or any other free port.

---

Advantage:

```text
Tests do not conflict with each other.
```

---

# Listen

```python
server.listen(1)
```

---

Meaning:

```text
Wait for a connection.
```

---

# Getting the Actual Port

```python
port =
    server.getsockname()[1]
```

---

For example:

```python
54321
```

---

Now we know which port the server is running on.

---

# The Inner Function

```python
def accept_connection():
```

---

Task:

```text
Accept a connection
```

---

# Accepting the Connection

```python
connection, _ =
    server.accept()
```

---

When the Scanner connects:

```python
accept()
```

returns.

---

# Closing the Connection

```python
connection.close()
```

---

To free up resources.

---

# Error Handling

```python
except OSError:
```

---

If the server is closed:

```python
accept()
```

might raise an error.

---

This error is ignored.

---

# Creating the Thread

```python
thread = threading.Thread(
```

---

Goal:

```text
Running the server in the background
```

---

# `daemon=True`

```python
daemon=True
```

---

Meaning:

```text
If the program ends
this Thread also stops.
```

---

# Starting the Thread

```python
thread.start()
```

---

The server is now active.

---

# The Function's Output

```python
return (
    server,
    port,
    thread
)
```

---

For use in tests.

---

# The First Test

```python
def test_scan_open_port():
```

---

Goal:

```text
Checking detection of an open port
```

---

# Creating the Server

```python
server, port, _ =
    create_test_server()
```

---

We have a real open port.

---

For example:

```python
54321
```

---

# Running the Scan

```python
result =
    scan_port(
        "127.0.0.1",
        port
    )
```

---

Because the port is open:

```python
True
```

we expect.

---

# Checking the Result

```python
assert result is True
```

---

If it returns:

```python
False
```

---

```text
The test fails.
```

---

# finally

```python
finally:
    server.close()
```

---

Very important.

---

Even if the test fails:

```text
The server is closed.
```

---

# The Second Test

```python
def test_scan_closed_port():
```

---

Goal:

```text
Checking detection of a closed port
```

---

# Creating the Port

```python
server.bind(...)
```

---

# Getting the Port Number

```python
port =
    server.getsockname()[1]
```

---

# Closing the Server

```python
server.close()
```

---

Now:

```text
The port is closed.
```

---

# Scanning

```python
scan_port(...)
```

---

We expect:

```python
False
```

to be returned.

---

# The Third Test

```python
test_scan_single_port_range()
```

---

Goal:

```text
Scanning a range containing only one port
```

---

Example:

```python
1000
to
1000
```

---

Meaning:

```text
Only one port
```

---

# Expectation

```python
[port]
```

---

The output should contain exactly that port.

---

# The Fourth Test

```python
test_scan_range_returns_sorted_ports()
```

---

One of the most important tests of the file.

---

# Creating Two Servers

```python
server1
server2
```

---

For example:

```python
55000
```

and

```python
53000
```

---

# Determining the Range

```python
start_port =
    min(...)
```

---

```python
end_port =
    max(...)
```

---

# Running the Scan

```python
scan_range(...)
```

---

# Expectation

```python
sorted([
    port1,
    port2
])
```

---

Why?

---

Because in:

```python
scanner.py
```

at the end we wrote:

```python
return sorted(open_ports)
```

---

This test checks exactly that behavior.

---

# The Fifth Test

```python
test_scan_with_custom_timeout()
```

---

Goal:

```text
Checking a custom Timeout
```

---

Input:

```python
timeout=1.0
```

---

Expectation:

```python
True
```

---

This test checks:

```text
The function correctly receives the timeout parameter.
```

---

# The Sixth Test

```python
test_scan_with_different_worker_count()
```

---

Goal:

```text
Checking custom Workers
```

---

Input:

```python
workers=1
```

---

Meaning:

```text
Without Parallel Scan
```

---

If the function is designed correctly:

```python
[port]
```

is returned.

---

# A Very Important Point

Pay attention.

---

This file:

```text
Does not use Mock
```

---

And that is completely intentional.

---

Why?

---

Because:

```text
We want to test the real network behavior.
```

---

That is why:

```python
A real Socket
```

is created.

---

This type of test is usually called:

```text
Integration-like Unit Test
```

---

Meaning:

```text
A unit test
using real resources
```

---

# pytest Output

If all tests succeed:

```bash
pytest
```

---

Output:

```text
====== 6 passed ======
```

---

# Summary

In this session, we learned:

✅ Testing network code

✅ Creating a temporary TCP Server

✅ What a Thread is

✅ What a daemon Thread is

✅ Testing an open port

✅ Testing a closed port

✅ Testing a Port Range

✅ Testing the sortedness of the output

✅ Testing the Timeout

✅ Testing the Worker Count

✅ The difference between Mock and Real Resource Testing

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
tests/test_services.py
```

---

There we will learn:

✅ How to test Service Detection

✅ Testing OS-dependent functions

✅ The concept of Known Values Testing

✅ Why testing famous services like HTTP and SSH is important
