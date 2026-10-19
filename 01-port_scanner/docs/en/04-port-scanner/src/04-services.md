[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/src/04-services.md)

# A Complete Review of the `services.py` File

## Introduction

In the previous session, we reviewed the most important file of the project:

```text
src/scanner.py
```

We learned:

- What a Socket is
- What TCP is
- How a port is scanned
- How several ports are scanned concurrently
- What `ThreadPoolExecutor` is
- What a Future is

But there was a problem.

Suppose the scan output is:

```text
80
443
22
53
```

These numbers alone do not tell us much.

A network specialist, when seeing the port:

```text
80
```

immediately realizes that:

```text
HTTP
```

is running on it.

But a regular user does not know this.

To solve this problem, we created the file:

```text
services.py
```

---

# File Content

```python
import socket


def detect_service(port: int) -> str:
    """
    Detect the registered TCP service for a port.
    """
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"
```

---

# What Is the Goal of This File?

This file is responsible for:

```text
Service Detection
```

---

# What Is Service Detection?

Detecting what service sits behind a port.

Example:

```text
22
```

Usually:

```text
SSH
```

---

```text
80
```

Usually:

```text
HTTP
```

---

```text
443
```

Usually:

```text
HTTPS
```

---

```text
53
```

Usually:

```text
DNS
```

---

# Import

```python
import socket
```

---

## Why `socket` Again?

In the Scanner file, we used Socket to connect.

But here we use a different feature of the same module.

---

# The Function Definition

```python
def detect_service(port: int) -> str:
```

---

## Input

```python
port: int
```

Example:

```python
80
```

or:

```python
443
```

---

## Output

```python
str
```

Meaning:

```python
"http"
```

or:

```python
"https"
```

or:

```python
"unknown"
```

---

# The Docstring

```python
"""
Detect the registered TCP service for a port.
"""
```

---

Meaning:

```text
Detect the registered TCP service for a port.
```

---

# Starting the try Block

```python
try:
```

---

Why?

Because a port might exist for which no known service is registered.

---

Example:

```python
12345
```

---

In such cases, Python raises an error.

---

# The Most Important Line of the File

```python
return socket.getservbyport(port, "tcp")
```

---

# What Is `getservbyport`?

This function uses the operating system's known-services database.

---

Example:

```python
socket.getservbyport(80, "tcp")
```

Output:

```python
"http"
```

---

Example:

```python
socket.getservbyport(443, "tcp")
```

Output:

```python
"https"
```

---

Example:

```python
socket.getservbyport(22, "tcp")
```

Output:

```python
"ssh"
```

---

# Where Does This Information Come From?

Many well-known ports are registered by:

```text
IANA
```

---

# What Is IANA?

Short for:

```text
Internet Assigned Numbers Authority
```

---

This organization is responsible for managing many Internet standards.

Including:

- Port numbers
- IP addresses
- The DNS Root Zone
- Protocol Numbers

---

# A Few Examples of Famous Ports

| Port | Service |
|--------|--------|
| 20 | FTP Data |
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 3306 | MySQL |
| 5432 | PostgreSQL |

---

# Why Did We Specify "tcp"?

```python
socket.getservbyport(
    port,
    "tcp"
)
```

---

Because some ports can have different meanings for TCP and UDP.

---

Example:

```python
53
```

is used for both:

```text
TCP
```

and:

```text
UDP
```

---

That is why we specified the protocol type.

---

# Error Handling

```python
except OSError:
```

---

If the port does not exist in the services database:

```python
getservbyport()
```

raises an error.

---

Example:

```python
socket.getservbyport(
    55555,
    "tcp"
)
```

---

Such an error may occur:

```text
OSError
```

---

# The Output on Error

```python
return "unknown"
```

---

If the service is unknown:

```text
unknown
```

is returned.

---

Example:

```python
detect_service(55555)
```

Output:

```python
"unknown"
```

---

# Why Is This Design Good?

If we did not handle the Exception:

```python
detect_service(55555)
```

the entire program would stop.

---

But now:

```text
The project is more stable.
```

---

# A Real Example

Suppose the Scanner finds these ports:

```python
[22, 80, 443]
```

---

Then:

```python
detect_service(22)
```

Output:

```python
"ssh"
```

---

```python
detect_service(80)
```

Output:

```python
"http"
```

---

```python
detect_service(443)
```

Output:

```python
"https"
```

---

The final result:

```text
PORT     SERVICE
22       ssh
80       http
443      https
```

---

# An Important Security Note

Pay attention:

```text
Service Detection
```

does not mean:

```text
Actual detection of the running service
```

---

Example:

A programmer might run a web server on:

```text
8080
```

---

In this case:

```python
detect_service(8080)
```

might return:

```python
"unknown"
```

---

But in reality:

```text
An HTTP web server is running on it.
```

---

So this file only performs:

```text
Service detection based on the standard port number
```

---

Actual service detection is done much more precisely in later chapters and when reviewing:

```text
banner.py
```

---

# Summary

In this session, we learned:

✅ What Service Detection is

✅ How the `detect_service` function works

✅ What `getservbyport` is

✅ What IANA is

✅ Why we specified TCP

✅ Why we handled the Exception

✅ What the difference between Service Detection and Banner Grabbing is

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
src/exporter.py
```

There we will learn:

- What JSON is
- Why we produce JSON output
- What Serialization is
- How we save scan results
- What JSON is used for in security tools

