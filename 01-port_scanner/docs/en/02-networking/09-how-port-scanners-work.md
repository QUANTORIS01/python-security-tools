[🇮🇷 فارسی](/01-port_scanner/docs/fa/02-networking/09-how-port-scanners-work.md)

# Session 09 — How Do Port Scanners Actually Work?

# Introduction

So far, we have learned almost all the necessary prerequisites:

✅ IP

✅ Port

✅ TCP

✅ UDP

✅ DNS

✅ Packet

✅ Protocol

✅ OSI Model

---

Now it is time to answer the main question of the project:

---

# What Is a Port Scanner?

A Port Scanner is a tool that checks:

```text
Which ports are open on a system?
```

---

Example:

```text
192.168.1.10
```

---

The port scanner tries to connect to different ports:

```text
21
22
25
53
80
110
443
3306
8080
...
```

---

And it determines the status of each one.

---

# What Is the Goal of Port Scanning?

Identifying active services.

---

Example:

If these ports are open:

```text
22
80
443
```

---

The following services are probably running:

```text
SSH
HTTP
HTTPS
```

---

# Why Is This Important?

For a network administrator:

```text
Managing services
```

---

For a security specialist:

```text
Identifying the attack surface
```

---

For an attacker:

```text
Identifying potential targets
```

---

That is why Port Scanning is the first step in many penetration tests.

---

# What Is an Open Port?

Suppose a Web Server is active on the target system.

---

For example:

```text
Port 80
```

---

When the scanner connects to it:

```text
Connection Successful
```

---

Result:

```text
OPEN
```

---

# What Is a Closed Port?

If no service is running on that port:

---

The connection is rejected.

---

Result:

```text
CLOSED
```

---

# What Is a Filtered Port?

Sometimes a firewall is in the middle.

---

The firewall might hide the response.

---

In this case:

```text
OPEN ?
CLOSED ?
```

---

It is not clear.

---

This state is called:

```text
FILTERED
```

---

# What Does Our Current Project Do?

Our scanner uses this command:

```python
socket.connect_ex()
```

---

This function tries to establish a TCP connection.

---

If it succeeds:

```text
Port Open
```

---

If it fails:

```text
Port Closed
```

---

# The Real Process Behind the Scenes

Suppose we are scanning:

```text
127.0.0.1:80
```

---

The scanner runs:

```python
socket.connect()
```

---

The operating system starts establishing a TCP connection.

---

# TCP Three-Way Handshake

In TCP, before sending data, the connection must be established.

---

There are three stages:

```text
SYN
SYN-ACK
ACK
```

---

# Stage 1

The scanner sends:

```text
SYN
```

---

Meaning:

```text
Hello, can I connect?
```

---

# Stage 2

If the port is open:

The server responds:

```text
SYN-ACK
```

---

Meaning:

```text
Yes, you can connect.
```

---

# Stage 3

The client sends:

```text
ACK
```

---

Meaning:

```text
Thank you, the connection is established.
```

---

# A Visual Diagram

```text
Scanner
   |
   | SYN
   |
Server
   |
   | SYN-ACK
   |
Scanner
   |
   | ACK
   |
Connection Established
```

---

# What Happens If the Port Is Closed?

The server gives a different response.

---

Usually:

```text
RST
```

---

Meaning:

```text
This port does not exist
```

---

Result:

```text
CLOSED
```

---

# What Is a Timeout?

Sometimes we receive no response at all.

---

Example:

```text
Firewall
```

---

Or:

```text
Packet Loss
```

---

In this case, the scanner waits for a while.

---

For example:

```python
timeout = 0.5
```

---

Meaning:

```text
Wait half a second
```

---

If no response arrives:

```text
Timeout
```

---

# Why Is Timeout Important?

Suppose we are scanning:

```text
1000 Ports
```

---

If the Timeout is:

```text
5 Seconds
```

---

The scan will be very slow.

---

That is why in our project we used:

```text
0.5 Second
```

---

# What Is a Connect Scan?

Our current scanner uses:

```text
TCP Connect Scan
```

---

This is the simplest type of Port Scan.

---

Advantages:

✅ Easy to implement

✅ No Administrator access required

✅ Stable

---

Disadvantages:

❌ Relatively slow

❌ Detectable

---

# What Is a SYN Scan?

Nmap's famous scan.

---

It is also called:

```text
Half Open Scan
```

---

Or:

```text
Stealth Scan
```

---

# The Difference from Connect Scan

In Connect Scan:

```text
SYN
SYN-ACK
ACK
```

---

The connection is completed.

---

But in SYN Scan:

```text
SYN
SYN-ACK
RST
```

---

The connection is not completed.

---

As a result, it is:

```text
Faster
```

and

```text
Stealthier
```

---

# Why Is Our Project Not a SYN Scan?

Because SYN Scan requires using:

```text
Raw Socket
```

---

It also usually requires Administrator access.

---

It is not suitable for initial learning.

---

That is why for now we use:

```text
TCP Connect Scan
```

---

# How Does Banner Grabbing Work?

After connecting:

```python
recv()
```

is executed.

---

Some services send information.

---

Example:

```text
OpenSSH_9.7
```

---

Or:

```text
Apache/2.4.58
```

---

We store this information.

---

# How Does Service Detection Work?

Sometimes from the port number:

---

Example:

```text
22 → SSH
80 → HTTP
443 → HTTPS
```

---

The type of service is guessed.

---

In more advanced versions:

The Banner is also examined.

---

# What Is Parallel Scanning?

Suppose we have:

```text
1000 Ports
```

---

If they are scanned one by one:

```text
It will be slow
```

---

That is why our project uses:

```python
ThreadPoolExecutor
```

---

And scans several ports at the same time.

---

# What More Does Nmap Do?

Nmap is not just a port scanner.

---

Features:

```text
TCP Scan
UDP Scan
SYN Scan
OS Detection
Version Detection
Traceroute
Script Engine
Service Enumeration
Host Discovery
```

---

That is why it is one of the most powerful security tools in the world.

---

# What Level Is Our Project Currently At?

Currently, it has the following features:

✅ TCP Connect Scan

✅ Multi Threading

✅ Validation

✅ Banner Grabbing

✅ Service Detection

✅ JSON Export

✅ CSV Export

✅ Logging

✅ Structured Output

---

For a portfolio project, this is considered a very good level.

---

# What We Learned Today

✅ What a Port Scan is

✅ What an Open Port is

✅ What a Closed Port is

✅ What a Filtered Port is

✅ What a Timeout is

✅ What a Connect Scan is

✅ What a SYN Scan is

✅ What a TCP Handshake is

✅ How Banner Grabbing works

✅ How Service Detection works

✅ How Nmap differs from our project

---

# Exercise

Suppose:

```text
192.168.1.15
```

has the following ports:

```text
22
80
443
```

---

Determine:

1. Which services are probably active?
2. How does the port scanner find them?
3. What happens if there is a Firewall?
4. What is the difference between Connect Scan and SYN Scan?

---

# Next Session

File:

```text
10-networking-summary.md
```

Topic:

**A Complete Networking Summary for Entering the Cybersecurity Section**

In this session, we put together all the networking topics and get a complete picture of how the Internet, services, ports, and the Port Scanner project work.

After that, we enter the third chapter:

```text
03-cybersecurity
```

And we will begin cybersecurity education.
