[🇮🇷 فارسی](/01-port_scanner/docs/fa/02-networking/10-networking-summary.md)

# Session 10 — A Complete Networking Summary for Entering Cybersecurity

# Introduction

So far, we have learned almost all the networking concepts needed to build and understand the Port Scanner project.

---

In this session, we are not going to learn any new topics.

---

The goal of this session is to:

```text
Put all the puzzle pieces together
```

So we can understand exactly what happens behind the scenes when a port is scanned.

---

# From the Moment the Address Is Entered to Reaching the Server

Suppose the user types in the browser:

```text
https://github.com
```

---

On the surface, only an address has been typed.

---

But behind the scenes, dozens of things happen.

---

# Stage 1: DNS

The browser cannot communicate with:

```text
github.com
```

---

Computers work with IPs.

---

So first, a:

```text
DNS Query
```

is sent.

---

For example:

```text
github.com
↓
140.82.121.3
```

---

# Stage 2: Building the Packet

Now the destination IP is known.

---

The operating system builds a packet.

---

Various pieces of information go into this packet:

```text
Source IP
Destination IP
Source Port
Destination Port
Payload
```

---

# Stage 3: TCP Connection

If TCP is used:

---

First, a:

```text
Three Way Handshake
```

is performed.

---

Meaning:

```text
SYN
SYN-ACK
ACK
```

---

After that, the connection is established.

---

# Stage 4: Data Transfer

Now the browser can send a request.

---

For example:

```http
GET /
```

---

And the server responds.

---

# What Is a Packet?

All data that moves across a network travels in the form of packets.

---

A packet can be thought of as an envelope.

---

Written on the envelope:

```text
Where did it come from?
Where is it going?
```

---

And inside the envelope, there is data.

---

# What Exactly Does a Port Do?

An IP specifies:

```text
Which device
```

---

A Port specifies:

```text
Which program
```

---

Example:

```text
192.168.1.10
```

---

This only specifies the device.

---

But:

```text
192.168.1.10:80
```

---

specifies:

```text
Web Server
```

---

# TCP and UDP

Two important protocols of the transport layer.

---

TCP:

```text
Reliable
Connection Oriented
```

---

UDP:

```text
Fast
Connectionless
```

---

Our current project is a:

```text
TCP Scanner
```

---

# Why Can a Port Scanner Find Services?

Because every service usually runs on a specific port.

---

Example:

```text
22   SSH
53   DNS
80   HTTP
443  HTTPS
3306 MySQL
```

---

So when a port is open:

---

That service is probably active.

---

# What Does an Open Port Mean?

It means a program is listening on that port.

---

In the networking world, the term:

```text
Listening
```

is used.

---

Example:

```text
Apache
```

listens on:

```text
Port 80
```

---

# What Does a Closed Port Mean?

No program is waiting for a connection.

---

As a result, the system responds:

```text
Connection Refused
```

---

# What Does a Filtered Port Mean?

Usually, a firewall does not allow the response through.

---

As a result:

```text
Timeout
```

occurs.

---

# What Is a Firewall?

A firewall is the network's guard.

---

Task:

```text
Allowing
or
Blocking
```

connections.

---

Example:

```text
Allow: 80
Allow: 443
Block: 22
```

---

# What Is the Role of the Operating System?

When the scanner runs:

---

In fact:

```python
socket
```

talks to the operating system.

---

And the operating system:

```text
Sends the packets
```

---

So a large part of the scanning process is done by the operating system itself.

---

# What Is a Socket?

A Socket is the interface between the program and the network.

---

Example:

```python
socket.connect()
```

---

Meaning:

```text
Connect to this address
```

---

# How Does Our Project Work?

Step by step:

---

1)

The user runs:

```bash
python -m src.cli 127.0.0.1 1 1000
```

---

2)

The inputs are validated.

---

3)

The ports are generated:

```python
range(1, 1001)
```

---

4)

ThreadPoolExecutor runs.

---

5)

Several ports are scanned in parallel.

---

6)

For each port:

```python
connect_ex()
```

is executed.

---

7)

Open ports are stored.

---

8)

Banner Grab is performed.

---

9)

Service Detection is performed.

---

10)

The results are displayed.

---

# How All Networking Lessons Relate to the Project

**DNS**

For converting a Domain to an IP

---

**IP**

For identifying the target system

---

**Port**

For identifying the target service

---

**TCP**

For establishing the connection

---

**Packet**

For transferring information

---

**Protocol**

For defining communication rules

---

**OSI**

For understanding where the Port Scanner operates

---

**Firewall**

For understanding Filtered Ports

---

**Socket**

For implementing the scanner

---

# What Do We Understand Now?

If we see the following output:

```text
22   OPEN   ssh
80   OPEN   http
443  OPEN   https
```

---

We know:

---

On the target system:

```text
SSH Server
Web Server
HTTPS Server
```

are active.

---

And we know:

---

How the scanner found this information.

---

# What Do We Still Need to Build Nmap?

For now, we do not have:

```text
UDP Scan
SYN Scan
OS Detection
Version Detection
Host Discovery
Traceroute
Script Engine
```

---

But the foundation we have built is completely similar to the one Nmap is built on.

---

# Summary of the Entire Networking Chapter

In this chapter, we learned:

✅ What a Network is

✅ What an IP is

✅ What a Public IP is

✅ What a Private IP is

✅ What DNS is

✅ What a Port is

✅ What TCP is

✅ What UDP is

✅ What a Packet is

✅ What a Protocol is

✅ What OSI is

✅ What a Firewall is

✅ What a Socket is

✅ How a Port Scanner works

✅ How Nmap works

---

# End of the Second Chapter

```text
02-networking
```

---

# Next Chapter

```text
03-cybersecurity
```

---

The Cybersecurity chapter.

---

In this chapter, we will learn:

- What Cybersecurity is
- What a Hacker is
- Types of hackers
- What a Vulnerability is
- What an Exploit is
- What Reconnaissance is
- What Enumeration is
- What Penetration Testing is
- What role Port Scanning plays in the attack lifecycle

And finally, we will understand exactly where the project we have built fits into the world of cybersecurity.
