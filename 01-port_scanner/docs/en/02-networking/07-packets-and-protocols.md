[🇮🇷 فارسی](/01-port_scanner/docs/fa/02-networking/07-packets-and-protocols.md)

# Session 07 — What Are Packets and Protocols?

# Introduction

So far, we have learned:

✅ What an IP is

✅ What a Port is

✅ What TCP is

✅ What UDP is

✅ What DNS is

✅ What a Client and a Server are

---

But one important question still remains:

When data is sent across a network, what actually happens?

---

Suppose you type into your browser:

```text
google.com
```

Or, in our own project:

```python
socket.connect()
```

---

Is all the information transferred at once?

No.

---

The network almost never moves data as one huge piece.

Instead, it divides it into smaller pieces.

We call these pieces:

```text
Packet
```

---

# What Is a Packet?

A Packet is the smallest unit that is moved across a network.

---

Example:

Suppose you want to send a file:

```text
10 MB
```

---

Usually, the file is divided into many packets.

---

A simple diagram:

```text
File
 │
 ├── Packet 1
 ├── Packet 2
 ├── Packet 3
 ├── Packet 4
 └── ...
```

---

Then these packets travel across the network.

---

# Why Do We Have Packets?

If the network had to send files all at once:

---

If only a small part were corrupted:

```text
The entire file would have to be resent
```

---

But with packets:

Only the corrupted part is resent.

---

It is faster.

---

It is more efficient.

---

# What Parts Does a Packet Consist Of?

A packet usually has two main parts:

```text
Header
```

and

```text
Payload
```

---

# What Is a Header?

The Header holds the packet's management information.

---

Such as:

```text
Source IP
Destination IP
Protocol
Port
Flags
Length
```

---

In fact, the Header tells the network:

```text
Where did this packet come from?
Where is it going?
What kind of data does it carry?
```

---

# What Is a Payload?

The Payload is the actual data.

---

Example:

If we download a web page:

```html
<html>
Hello
</html>
```

---

This content goes inside the Payload.

---

Therefore:

```text
Header = control information
```

---

and

```text
Payload = actual data
```

---

# A Visual Example

```text
+----------------------+
|       Header         |
+----------------------+
|       Payload        |
+----------------------+
```

---

# What Is a Protocol?

A Protocol means:

```text
A communication rule
```

---

Just as humans have rules for speaking:

---

The network also has its own rules.

---

We call these rules:

```text
Protocol
```

---

# A Real Example

Suppose I speak Persian.

And the other person only knows Japanese.

---

Communication becomes almost impossible.

---

In a network, too, if two systems do not use a shared Protocol:

```text
Communication is not established
```

---

# Sample Protocols

# HTTP

For websites

```text
http://example.com
```

---

# HTTPS

The secure version of HTTP

```text
https://example.com
```

---

# DNS

For converting a Domain to an IP

---

# FTP

For file transfer

---

# SSH

For remote management

---

# SMTP

For sending email

---

# TCP and UDP Are Also Protocols

Yes.

---

TCP is a Protocol.

---

UDP is also a Protocol.

---

But they sit at a lower layer than HTTP.

---

Example:

```text
HTTP
  ↓
TCP
  ↓
IP
```

---

# A Packet While Traveling Across the Network

Suppose the browser sends the following request:

```text
GET /
```

---

This data is turned into a packet.

---

Each packet has a Header and a Payload.

---

Then it travels across the network.

---

# Source and Destination

Each packet usually contains:

```text
Source
```

and

```text
Destination
```

---

Example:

```text
Source:
192.168.1.10
```

---

```text
Destination:
142.250.190.78
```

---

This information goes into the Header.

---

# How Packets Relate to Ports

In addition to IPs, ports are also included in the communication information.

---

Example:

```text
192.168.1.10:50000
```

↓

```text
142.250.190.78:443
```

---

Meaning:

```text
Source Port
```

and

```text
Destination Port
```

also exist.

---

# How Packets Relate to the Port Scanner

When the Port Scanner runs:

---

For example:

```python
socket.connect()
```

---

Behind the scenes, packets are created.

---

These packets are sent toward the target.

---

And their responses are examined.

---

# If the Port Is Open

The target responds.

---

Result:

```text
OPEN
```

---

# If the Port Is Closed

The target does not give an appropriate connection response.

---

Result:

```text
CLOSED
```

---

# Banner Grabbing and Packets

When we retrieve a Banner:

---

The server sends packets.

---

Inside the Payload, there might be something like:

```text
OpenSSH_9.7
```

---

Or:

```text
Apache/2.4.58
```

---

The scanner extracts it.

---

# Service Detection and Packets

Service detection is also performed based on the information exchanged between packets.

---

In more professional versions of Nmap, even very specific service responses are examined.

---

To identify the exact type of software.

---

# Why Is This Important?

Because now we realize:

---

The port scanner:

```text
Does not do magic
```

---

Rather:

```text
It sends packets
```

and

```text
It receives packets
```

---

And decides based on them.

---

# What We Learned Today

✅ What a Packet is

✅ What a Header is

✅ What a Payload is

✅ What a Protocol is

✅ Sample Protocols

✅ How TCP and UDP relate to Protocol

✅ How Packets relate to Ports

✅ How Packets relate to the Port Scanner

✅ How Packets relate to Banner Grabbing

---

# Exercise

Suppose you want to visit:

```text
https://github.com
```

Write the following steps on paper:

1. What does DNS do?
2. How is the IP found?
3. On which port is the connection established?
4. Which Protocols are involved?
5. What role do packets play?

---

# Next Session

File:

```text
08-osi-model.md
```

Topic:

**The OSI Model**

In the next session, we will learn:

- What OSI is
- Why it was created
- What the 7 OSI layers are
- How TCP/IP differs from OSI
- In which layers the Port Scanner operates
- Where DNS, TCP, UDP, and HTTP sit in this model

This session will be one of the most important sessions of the entire networking section.
