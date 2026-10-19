[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/src/03-scanner.md)

# A Complete Review of the `scanner.py` File

## Introduction

In the previous session, we reviewed the file:

```text
src/validator.py
```

We learned:

- What validation is
- How an IP is validated
- What a Port Range is
- What a Timeout is
- What a Worker is

But we have not built a port scanner yet.

So far, we only made sure the inputs are correct.

From this session, we enter the real heart of the project.

The file we are going to review:

```text
src/scanner.py
```

This file is the most important file of the project.

If we delete this file:

```text
The port scanner will no longer be able to scan any port.
```

---

# File Content

```python
import socket
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


def scan_port(ip: str, port: int, timeout: float = 0.5) -> bool:
    """
    Scan a single TCP port.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
        return result == 0
    except socket.error:
        return False


def scan_range(ip: str, start_port: int, end_port: int, timeout: float = 0.5, workers: int = 100) -> list[int]:
    """
    Scan a range of TCP ports.
    """
    open_ports = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(scan_port, ip, port, timeout): port
            for port in range(start_port, end_port + 1)
        }
        for future in as_completed(futures):
            port = futures[future]
            if future.result():
                open_ports.append(port)
    return sorted(open_ports)
```

---

# The First Import

```python
import socket
```

---

# What Is `socket`?

The main module for network communication in Python.

All TCP and UDP operations in our project are performed through this module.

---

## Why Do We Need `socket`?

Because to find out whether a port is open or closed, we must try to connect to it.

For example:

```text
127.0.0.1:80
```

If the connection succeeds:

```text
The port is open.
```

If the connection fails:

```text
The port is closed.
```

---

# The Second Import

```python
from concurrent.futures import ThreadPoolExecutor
```

---

# What Is a Thread?

Suppose we want to scan:

```text
1000 ports
```

If they are scanned one by one:

```text
Port 1
Port 2
Port 3
...
Port 1000
```

It takes a long time.

---

But if several scans are performed concurrently:

```text
Port 1
Port 2
Port 3
Port 4
Port 5
...
```

The speed increases significantly.

---

Each concurrent execution is called a:

```text
Thread
```

---

# What Is `ThreadPoolExecutor`?

A tool for managing a large number of Threads.

---

Instead of creating 100 Threads ourselves:

```python
Thread(...)
Thread(...)
Thread(...)
```

Python does this for us.

---

# The Third Import

```python
from concurrent.futures import as_completed
```

---

## What Is This Function's Job?

It waits for the Threads to finish their work.

Whichever Thread finishes first:

```python
as_completed()
```

returns its result.

---

# The First Function

```python
def scan_port(ip: str, port: int, timeout: float = 0.5) -> bool:
```

---

## The Function's Goal

Scanning a single port.

Example:

```python
scan_port("127.0.0.1", 80)
```

---

# The Docstring

```python
"""
Scan a single TCP port.
"""
```

---

This function checks only one port.

---

# Starting the try Block

```python
try:
```

---

Network errors may occur.

Example:

- The Host is unreachable
- The IP is wrong
- A Timeout occurs

To prevent the program from crashing, we use:

```python
try
except
```

---

# Creating the Socket

```python
with socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
) as sock:
```

---

This is the most important line of the entire project.

---

# What Is `AF_INET`?

It means:

```text
IPv4
```

---

Example:

```text
127.0.0.1
192.168.1.1
8.8.8.8
```

are all IPv4.

---

# What Is `SOCK_STREAM`?

It means:

```text
TCP
```

---

Our project is a:

```text
TCP Port Scanner
```

---

If we wanted UDP:

```python
socket.SOCK_DGRAM
```

would be used.

---

# Why Did We Use `with`?

```python
with socket.socket(...) as sock:
```

---

When the work is finished:

```python
sock.close()
```

is executed automatically.

---

Advantages:

- Less memory consumption
- Prevents Resource Leak
- Cleaner code

---

# Setting the Timeout

```python
sock.settimeout(timeout)
```

---

Example:

```python
0.5
```

---

Meaning:

```text
Wait at most half a second for a response.
```

---

If no response arrives:

```text
The connection is aborted.
```

---

# Attempting the Connection

```python
result = sock.connect_ex((ip, port))
```

---

This line effectively scans the port.

---

Example:

```python
sock.connect_ex(
    ("127.0.0.1", 80)
)
```

---

# What Is the Difference Between `connect_ex` and `connect`?

```python
connect()
```

raises an Exception on error.

---

But:

```python
connect_ex()
```

returns a status code.

---

Example:

```python
0
```

Meaning:

```text
The connection succeeded.
```

---

# Checking the Result

```python
return result == 0
```

---

If:

```python
result
```

is zero:

```python
True
```

is returned.

---

Meaning:

```text
The port is open.
```

---

Otherwise:

```python
False
```

is returned.

---

Meaning:

```text
The port is closed.
```

---

# Error Handling

```python
except socket.error:
    return False
```

---

If any network error occurs:

```python
False
```

is returned.

---

# The Second Function

```python
def scan_range(...)
```

---

## The Function's Goal

Scanning a large number of ports.

---

Example:

```python
1 to 1000
```

---

# Creating the Results List

```python
open_ports = []
```

---

This list stores:

```text
The open ports
```

---

# Building the Thread Pool

```python
with ThreadPoolExecutor(
    max_workers=workers
) as executor:
```

---

Example:

```python
workers=100
```

---

Meaning:

```text
100 concurrent scans
```

---

# Creating the Tasks

```python
futures = {
    executor.submit(
        scan_port,
        ip,
        port,
        timeout
    ): port
    for port in range(
        start_port,
        end_port + 1
    )
}
```

---

This section is one of the most professional parts of the project.

---

# `range`

```python
range(
    start_port,
    end_port + 1
)
```

---

Example:

```python
1
1000
```

---

Output:

```text
1
2
3
...
1000
```

---

# `submit`

```python
executor.submit(...)
```

---

It sends each port to a Thread.

---

Example:

```python
scan_port(127.0.0.1, 80)
```

---

```python
scan_port(127.0.0.1, 81)
```

---

```python
scan_port(127.0.0.1, 82)
```

---

And so on.

---

# What Are Futures?

Each operation in progress is called a:

```text
Future
```

---

A Future means:

```text
A result that is not yet ready.
```

---

# Waiting for the Threads to Finish

```python
for future in as_completed(futures):
```

---

Whichever Thread finishes first:

```python
future
```

is returned.

---

# Finding the Port Number

```python
port = futures[future]
```

---

Because the Future only has the result.

To know which port it was related to:

We kept:

```python
futures
```

---

# Checking the Result

```python
if future.result():
```

---

If the output is:

```python
True
```

---

Meaning:

```text
The port is open.
```

---

# Adding to the List

```python
open_ports.append(port)
```

---

Example:

```python
[80, 443]
```

---

# Sorting

```python
return sorted(open_ports)
```

---

Because the Threads finish in random order.

The output might be:

```python
[443, 80]
```

---

So we sort it:

```python
[80, 443]
```

---

# An Important Architectural Note

This file is only responsible for scanning.

---

It does not perform the following tasks:

❌ Displaying output

❌ Saving JSON

❌ Saving CSV

❌ Retrieving a Banner

❌ Logging

---

This is exactly the important principle:

```text
Single Responsibility Principle
```

---

# Summary

In this session, we learned:

✅ What a Socket is

✅ What TCP is

✅ What `AF_INET` is

✅ What `SOCK_STREAM` is

✅ What a Timeout is

✅ How `connect_ex` works

✅ What a Thread is

✅ What `ThreadPoolExecutor` is

✅ What a Future is

✅ What `as_completed` is

✅ How concurrent scanning is performed

✅ How the results are sorted

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
src/services.py
```

There we will learn:

- What Service Detection is
- Why port 80 is usually HTTP
- Why port 443 is usually HTTPS
- What IANA is
- How we detect service names

