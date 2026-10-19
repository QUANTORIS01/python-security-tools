[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/src/08-banner.md)

# A Complete Review of the `banner.py` File

# Introduction

So far on our learning journey, we have learned:

### Python Chapter

- Functions
- Conditions
- Loops
- Exceptions
- Files
- JSON
- CSV
- Modules

---

### Networking Chapter

- What an IP is
- What a Port is
- What TCP is
- What a Socket is
- What a Client and a Server are
- How services work

---

### Cybersecurity Chapter

- Reconnaissance
- Enumeration
- Attack Surface
- CIA Triad
- Threat Modeling
- Logging
- Vulnerability Assessment

---

And in the previous sessions of the project chapter, we learned:

- `validate_ip`
- `validate_port_range`
- `scan_port`
- `scan_range`
- `detect_service`
- `export_json`
- `export_csv`
- `setup_logger`

---

But we still have a big problem.

---

Suppose the port:

```text
80
```

is open.

---

We only find out:

```text
Port 80 Open
```

---

But we do not know:

```text
Apache?
Nginx?
IIS?
```

---

Or for example:

```text
Port 22 Open
```

---

But we do not know:

```text
OpenSSH?
Dropbear?
Cisco SSH?
```

---

That is why we use something called:

```text
Banner Grabbing
```

---

# What Is a Banner?

When we connect to some services,

they send back information about themselves.

---

Example:

```text
SSH-2.0-OpenSSH_9.5
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

# What Is Banner Grabbing?

It means:

```text
Retrieving service-identification information
```

---

Goal:

```text
More precise service detection
```

---

# Why Is It Important in Security?

Almost all professional tools do this.

---

Example:

- Nmap
- Masscan
- Nessus
- OpenVAS
- Metasploit

---

Because:

```text
Port Open
```

gives little information.

---

But:

```text
Apache 2.4.58
```

gives much more information.

---

# File Content

```python
import socket


def grab_banner(
    ip: str,
    port: int,
    timeout: float = 1.0
) -> str | None:
    """
    Attempt to retrieve a TCP service banner.
    """
    try:
        with socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        ) as sock:

            sock.settimeout(timeout)

            sock.connect((ip, port))

            banner = sock.recv(1024)

        return (
            banner
            .decode(
                "utf-8",
                errors="ignore"
            )
            .strip()
            or None
        )

    except (
        socket.timeout,
        socket.error
    ):
        return None
```

---

# What Is the Function's Goal?

Goal:

```text
Retrieve a Banner from a service
```

---

# The Function Definition

```python
def grab_banner(
    ip: str,
    port: int,
    timeout: float = 1.0
) -> str | None:
```

---

# The First Parameter

```python
ip
```

---

Example:

```python
"192.168.1.10"
```

---

# The Second Parameter

```python
port
```

---

Example:

```python
22
```

---

# The Third Parameter

```python
timeout
```

---

Example:

```python
1.0
```

---

Meaning:

```text
Wait at most 1 second
```

---

# Output

```python
str | None
```

---

In newer Python:

```python
|
```

means:

```python
Union
```

---

Meaning:

```python
str
```

or

```python
None
```

---

Example:

```python
"SSH-2.0-OpenSSH_9.5"
```

---

Or:

```python
None
```

---

# The Docstring

```python
"""
Attempt to retrieve a TCP service banner.
"""
```

---

Meaning:

```text
Try to retrieve the service Banner.
```

---

Pay attention:

```text
Attempt
```

is used.

---

Why?

Because there is no guarantee that the service will provide a Banner.

---

# The try Block

```python
try:
```

---

In network operations, errors are always possible.

---

Example:

- Timeout
- Connection Refused
- Reset Connection

---

That is why we use:

```python
try
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

We learned this part in the `scanner.py` file.

---

# `AF_INET`

```python
socket.AF_INET
```

---

Meaning:

```text
IPv4
```

---

# `SOCK_STREAM`

```python
socket.SOCK_STREAM
```

---

Meaning:

```text
TCP
```

---

So:

```text
Create a TCP Socket for IPv4
```

---

# Setting the Timeout

```python
sock.settimeout(timeout)
```

---

Example:

```python
1.0
```

---

Meaning:

```text
Do not wait more than one second
```

---

Why is it important?

---

Suppose:

```text
The server does not respond
```

---

If we have no Timeout:

```text
The program might hang for a long time.
```

---

# Connecting to the Service

```python
sock.connect(
    (
        ip,
        port
    )
)
```

---

Example:

```python
sock.connect(
    (
        "127.0.0.1",
        22
    )
)
```

---

Meaning:

```text
Connect to SSH.
```

---

# The Difference Between `connect` and `connect_ex`

In `scanner.py`, we had:

```python
connect_ex()
```

---

But here we have:

```python
connect()
```

---

Why?

---

Because:

```python
connect_ex()
```

only returns the connection status.

---

But:

```python
connect()
```

actually establishes the connection.

---

And after connecting, we can receive data.

---

# Receiving the Banner

```python
banner = sock.recv(1024)
```

---

This is the most important line of the file.

---

# What Is `recv`?

Short for:

```text
Receive
```

---

Meaning:

```text
Receiving data
```

---

# What Is the Number 1024?

```python
recv(1024)
```

---

Meaning:

```text
Receive at most 1024 bytes
```

---

If the service sends this:

```text
SSH-2.0-OpenSSH_9.5
```

---

It is stored in the variable:

```python
banner
```

---

But there is an important point.

---

# The Return Data Type

```python
recv()
```

does not return a string.

---

It returns:

```python
bytes
```

---

Example:

```python
b"SSH-2.0-OpenSSH_9.5"
```

---

Pay attention:

```python
b
```

exists at the start of the string.

---

Meaning:

```text
Binary data
```

---

# Converting Bytes to String

```python
banner.decode(
    "utf-8",
    errors="ignore"
)
```

---

Here the binary data is converted to:

```python
str
```

---

Example:

Before:

```python
b"SSH-2.0-OpenSSH_9.5"
```

---

After:

```python
"SSH-2.0-OpenSSH_9.5"
```

---

# UTF-8

```python
"utf-8"
```

---

Specifies:

```text
How to convert the bytes.
```

---

# `errors="ignore"`

This part is very important.

---

Some services send corrupted data.

---

Example:

```python
b"\xff\xfe\xab"
```

---

If we write:

```python
decode("utf-8")
```

We might get an error.

---

But:

```python
errors="ignore"
```

causes:

```text
Corrupted bytes to be ignored.
```

---

# `strip`

```python
.strip()
```

---

Removes:

```text
Space
Tab
Newline
```

from the beginning and end of the string.

---

Example:

Before:

```python
"SSH-2.0-OpenSSH_9.5\r\n"
```

---

After:

```python
"SSH-2.0-OpenSSH_9.5"
```

---

# `or None`

```python
or None
```

---

This part is very clever.

---

Suppose:

```python
banner = ""
```

---

After decode and strip:

```python
""
```

---

An empty string in Python:

```python
False
```

is considered.

---

So:

```python
"" or None
```

equals:

```python
None
```

---

Meaning:

```text
If the Banner is empty, return None.
```

---

# Error Handling

```python
except (
    socket.timeout,
    socket.error
):
```

---

Two important errors are handled.

---

# Timeout

```python
socket.timeout
```

---

Example:

```text
The server did not respond.
```

---

# Socket Error

```python
socket.error
```

---

Example:

```text
Connection Refused
```

Or:

```text
Network Unreachable
```

---

# Output on Error

```python
return None
```

---

Meaning:

```text
No Banner was found.
```

---

# A Real Execution Sample

Suppose:

```python
grab_banner(
    "127.0.0.1",
    22
)
```

---

Output:

```python
"SSH-2.0-OpenSSH_9.5"
```

---

Or:

```python
None
```

---

# An Important Security Note

A Banner is not always trustworthy.

---

Some system administrators intentionally change it.

---

Example:

Reality:

```text
Apache
```

---

Fake Banner:

```text
Nginx
```

---

That is why professional tools do not rely on the Banner alone.

---

They combine:

- Banner
- Fingerprinting
- Protocol Analysis
- Active Probing

---

But for our current project:

```text
Banner Grabbing
```

is a very valuable and professional feature.

---

# Summary

In this session, we learned:

✅ What a Banner is

✅ What Banner Grabbing is

✅ What `recv` is

✅ What `bytes` is

✅ What `decode` is

✅ What UTF-8 is

✅ What `errors="ignore"` is

✅ What `strip` is

✅ How `or None` works

✅ What the difference between `connect` and `connect_ex` is

✅ How network errors are handled

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
src/models.py
```

There we will learn:

- What a Data Model is
- What a Dataclass is
- Why we used a class
- What an Immutable Object is
- How `ScanResult` is designed
- Why this design matters for professional projects

