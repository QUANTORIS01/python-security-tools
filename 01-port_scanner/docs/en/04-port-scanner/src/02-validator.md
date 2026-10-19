[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/src/02-validator.md)

# A Complete Review of the `validator.py` File

## Introduction

In the previous session, we became familiar with the file:

```text
src/__init__.py
```

We learned how we centralized all the important functions of the project in one place to make them easier to use.

In this session, we review the first real file of the project:

```text
src/validator.py
```

This file is responsible for one of the most important parts of any software:

```text
Input Validation
```

---

# Why Is Validation Important?

Suppose the user runs this command:

```bash
python -m src.cli hello 80 443
```

Or:

```bash
python -m src.cli 192.168.1.1 -10 999999
```

Or:

```bash
python -m src.cli 192.168.1.1 1 1000 --workers -5
```

If the program does not validate these values:

- Errors occur
- The program crashes
- Incorrect results are produced
- Software security is reduced

That is why, before doing anything, we must make sure the inputs are valid.

---

# File Content

```python
import socket


def validate_ip(ip: str) -> bool:
    """
    Validate IPv4 address.
    """
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def validate_port_range(start_port: int, end_port: int) -> bool:
    """
    Validate port range.
    """
    if not (0 <= start_port <= 65535):
        return False

    if not (0 <= end_port <= 65535):
        return False

    if start_port > end_port:
        return False

    return True


def validate_timeout(timeout: float) -> bool:
    """
    Validate connection timeout.
    """
    return timeout > 0


def validate_workers(workers: int) -> bool:
    """
    Validate number of concurrent workers.
    """
    return workers > 0
```

---

# The First Line

```python
import socket
```

---

## What Does This Line Do?

The module:

```python
socket
```

is one of the most important standard Python modules for networking tasks.

Our port scanner is also built on top of this module.

---

## Uses of `socket`

With this module, we can:

- Establish network connections
- Validate an IP
- Scan ports
- Find servers
- Retrieve network information

---

# The First Function

```python
def validate_ip(ip: str) -> bool:
```

---

## The Function's Goal

Checking whether an IP is valid.

---

## Input

```python
ip: str
```

Meaning:

```python
"127.0.0.1"
```

or:

```python
"192.168.1.1"
```

---

## Output

```python
bool
```

Meaning:

```python
True
```

or:

```python
False
```

---

# The Docstring

```python
"""
Validate IPv4 address.
"""
```

---

## What Is a Docstring?

It is an explanation written for programmers.

When someone studies the project later, they understand what the purpose of this function is.

---

# The try Block

```python
try:
```

---

## Why Do We Use try?

The user might enter an invalid IP.

Example:

```python
"hello"
```

or:

```python
"999.999.999.999"
```

In such cases, the network function raises an error.

To prevent the program from stopping, we use:

```python
try
except
```

---

# The Most Important Line of the Function

```python
socket.inet_aton(ip)
```

---

## What Does This Function Do?

Python tries to convert the IP into the network's binary format.

If the IP is valid:

```python
socket.inet_aton("127.0.0.1")
```

runs without error.

---

## Example

```python
socket.inet_aton("192.168.1.1")
```

Succeeds.

---

But:

```python
socket.inet_aton("hello")
```

raises an error.

---

# On Success

```python
return True
```

---

Meaning:

```text
The IP is valid.
```

---

# On Error

```python
except socket.error:
```

---

If the conversion of the IP fails, we enter this block.

---

Then:

```python
return False
```

---

Meaning:

```text
The IP is not valid.
```

---

# The Second Function

```python
def validate_port_range(start_port: int, end_port: int) -> bool:
```

---

## The Function's Goal

Checking whether the port range is valid.

---

# The Allowed Port Range

In TCP and UDP:

```text
0
to
65535
```

are allowed.

---

# The First Condition

```python
if not (0 <= start_port <= 65535):
    return False
```

---

## Meaning of the Condition

If the start port is out of range:

```python
-1
```

or:

```python
70000
```

it is invalid.

---

# The Second Condition

```python
if not (0 <= end_port <= 65535):
    return False
```

---

The same check is done for the end port.

---

# The Third Condition

```python
if start_port > end_port:
    return False
```

---

## Why Is This Condition Important?

This range is invalid:

```python
1000
100
```

Because the start is greater than the end.

---

# Finally

```python
return True
```

---

Meaning:

```text
The port range is valid.
```

---

# The Third Function

```python
def validate_timeout(timeout: float) -> bool:
```

---

# What Is Timeout?

The amount of time the program waits for a response.

Example:

```python
0.5
```

Meaning:

```text
Half a second
```

---

# The Check

```python
return timeout > 0
```

---

If the value is:

```python
0
```

or:

```python
-1
```

Then:

```python
False
```

is returned.

---

Because a negative or zero wait time does not make sense.

---

# The Fourth Function

```python
def validate_workers(workers: int) -> bool:
```

---

# What Is a Worker?

The number of threads or concurrent workers.

---

Example:

```python
100
```

Meaning:

```text
100 concurrent operations
```

---

# The Check

```python
return workers > 0
```

---

If the value is:

```python
0
```

or:

```python
-10
```

Then:

```python
False
```

is returned.

---

## Why Is This Check Important?

If the number of workers is zero:

```text
No scan is performed.
```

---

If it is negative:

```text
It is logically impossible.
```

---

# An Interesting Design Choice in This File

An important point visible in this file:

Every function has only one job.

Example:

```python
validate_ip()
```

only validates an IP.

---

```python
validate_timeout()
```

only validates a Timeout.

---

This approach is one of the important principles of software design:

```text
Single Responsibility Principle
```

Meaning:

```text
Each function should have only one responsibility.
```

---

# Summary

In this session, we learned:

✅ What validation is

✅ Why validation is important

✅ What the `socket` module is

✅ How the `validate_ip` function works

✅ How the `validate_port_range` function works

✅ How the `validate_timeout` function works

✅ How the `validate_workers` function works

✅ What the Single Responsibility Principle is

---

# What Will We Learn in the Next Session?

In the next session, we enter the main heart of the port scanner:

```text
src/scanner.py
```

There we will learn:

- How a Socket is created
- How we connect to a port
- How we determine whether a port is open or closed
- How the Timeout is applied
- How `ThreadPoolExecutor` works
- How concurrent scanning of ports is performed

