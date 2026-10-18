[🇮🇷 فارسی](/01-port_scanner/docs/fa/01-python/09-networking-with-python.md)

# Session 09 — Networking in Python and Sockets

# Why Should We Learn Networking?

So far in this course:

- We got to know Python.
- We learned about functions.
- We learned about modules.
- We learned about error handling.
- We learned about files, JSON, and CSV.

But we still do not know:

> How does a port scanner communicate with another computer?

The answer to this question is:

```text
Socket
```

---

# What Is a Network?

Suppose there are two computers.

```text
Computer A
```

and

```text
Computer B
```

These two computers communicate with each other over a network.

---

Example:

- A browser connects to a website.
- Telegram connects to Telegram's servers.
- An online game connects to the game's server.

All of these are network communications.

---

# What Is an IP?

Every device on a network has an address.

Example:

```text
192.168.1.1
```

or

```text
8.8.8.8
```

or

```text
127.0.0.1
```

---

An IP is like a house address.

---

Without an address:

We cannot know where the message should be sent.

---

# What Is a Port?

A computer may run dozens of different services.

Example:

```text
Web Server
SSH
Database
FTP
DNS
```

---

All of these services share one IP.

So how do we tell them apart?

---

With a port.

---

Example:

```text
80   → HTTP
443  → HTTPS
22   → SSH
21   → FTP
53   → DNS
```

---

So:

```text
IP = device

Port = service on the device
```

---

# A Real Address

Example:

```text
142.250.190.78:443
```

---

First part:

```text
142.250.190.78
```

is the device address.

---

Second part:

```text
443
```

is the service port.

---

# What Is a Socket?

A Socket is a gateway for network communication.

---

When a program wants to connect to a service:

It first creates a Socket.

---

Mental picture:

```text
Application
     │
     ▼
 Socket
     │
     ▼
 Network
     │
     ▼
 Remote Server
```

---

# The First Socket in Python

```python
import socket

sock = socket.socket()
```

---

Meaning of the code

```python
socket.socket()
```

means:

> Create a new socket.

---

# Connecting to a Server

```python
import socket

sock = socket.socket()

sock.connect(("google.com", 80))

print("Connected")
```

---

If the connection succeeds:

```text
Connected
```

is displayed.

---

# Sending Data

After connecting, we can send data.

---

Example:

```python
sock.send(b"Hello")
```

---

The letter `b` means:

```python
bytes
```

---

In a network, data is transferred as bytes.

---

# Receiving Data

```python
data = sock.recv(1024)

print(data)
```

---

The number:

```python
1024
```

means:

Receive at most 1024 bytes.

---

# Closing the Connection

After we are done:

```python
sock.close()
```

---

We must close the connection.

---

# What Is a Timeout?

Sometimes the server does not respond.

If we have no timeout:

The program may wait forever.

---

Example:

```python
sock.settimeout(1)
```

---

Meaning:

```text
Wait at most one second
```

---

If no response arrives:

Raise an error.

---

# Why Is Timeout Important in a Port Scanner?

Suppose we are scanning:

```text
65535
```

ports.

---

If each port hangs for:

```text
30 seconds
```

the scan would take several days.

---

That is why in our project we have:

```python
timeout=0.5
```

---

# Checking Whether a Port Is Open

The core idea of the Port Scanner is very simple.

---

If we can connect to the port:

```text
OPEN
```

---

If we cannot:

```text
CLOSED
```

---

A simple example:

```python
import socket

sock = socket.socket()

result = sock.connect_ex(
    ("127.0.0.1", 80)
)

print(result)
```

---

# What Is `connect_ex`?

A more suitable version of `connect`.

---

If the connection succeeds:

```text
0
```

is returned.

---

If the connection fails:

A different number is returned.

---

# Example

```python
if result == 0:
    print("OPEN")
else:
    print("CLOSED")
```

---

This is exactly the heart of a port scanner.

---

# Connection to Our Project

In the file:

```text
scanner.py
```

almost the same thing happens.

---

Steps:

```text
Create Socket

↓

Set Timeout

↓

Connect to Port

↓

Check Result

↓

Close Socket
```

---

# A Complete Example

```python
import socket

sock = socket.socket()

sock.settimeout(1)

result = sock.connect_ex(
    ("127.0.0.1", 80)
)

if result == 0:
    print("OPEN")
else:
    print("CLOSED")

sock.close()
```

---

# How Does Banner Grabbing Work?

After connecting:

```python
sock.recv()
```

is used.

---

Some services send information.

Example:

```text
Apache
nginx
OpenSSH
Microsoft IIS
```

---

This is exactly what we have implemented in:

```text
banner.py
```

---

# What We Learned Today

✓ Networking
✓ What an IP is
✓ What a Port is
✓ What a Socket is
✓ Creating a Socket
✓ `connect`
✓ `connect_ex`
✓ `send`
✓ `recv`
✓ `close`
✓ `timeout`
✓ Direct connection to `scanner.py`
✓ Direct connection to `banner.py`

---

# Exercise

Write a program that:

1. Connects to

```text
google.com
```

on port

```text
80
```

2. If successful, displays:

```text
Connected
```

3. Otherwise, displays:

```text
Connection Failed
```

---

Next session:

**10-python-for-port-scanner.md**

In this session, we put together all the knowledge we have learned so far and build the first simple version of the Port Scanner from scratch.
