[🇮🇷 فارسی](/01-port_scanner/docs/fa/02-networking/08-osi-model.md)

# Session 08 — The OSI Model: The Roadmap of All Networks

# Introduction

So far, we have become familiar with many concepts:

✅ IP

✅ Port

✅ TCP

✅ UDP

✅ DNS

✅ Packet

✅ Protocol

---

But one important question still remains:

When data moves across a network, exactly which stages does it go through?

---

To answer this question, the networking world introduced a model called:

```text
OSI Model
```

---

# What Is OSI?

OSI stands for:

```text
Open Systems Interconnection
```

---

OSI is a conceptual model.

---

That means:

```text
It is not real
```

---

Rather, it was designed for a better understanding of networks.

---

It can be thought of as a building's blueprint.

---

A building's blueprint is not the building itself.

But it helps us understand the building better.

---

OSI plays the same role in networking.

---

# Why Was OSI Created?

Before OSI, every company had its own method for network communication.

---

The problem:

```text
Systems were not compatible with each other
```

---

To solve this problem, a standard model was designed.

---

This model divided network communication into:

```text
7 Layers
```

---

# The OSI Layers

From top to bottom:

```text
7. Application
6. Presentation
5. Session
4. Transport
3. Network
2. Data Link
1. Physical
```

---

In the real world, they are usually examined from top to bottom.

---

# An Overview

```text
+------------------+
| 7 Application    |
+------------------+
| 6 Presentation   |
+------------------+
| 5 Session        |
+------------------+
| 4 Transport      |
+------------------+
| 3 Network        |
+------------------+
| 2 Data Link      |
+------------------+
| 1 Physical       |
+------------------+
```

---

# Layer 7 — Application

This is the layer closest to the user.

---

Protocols such as:

```text
HTTP
HTTPS
DNS
FTP
SMTP
SSH
```

are seen at this level.

---

When you open your browser and visit:

```text
https://github.com
```

you are using the Application layer.

---

# Layer 6 — Presentation

Task:

```text
Data presentation
```

---

Tasks such as:

- Encoding
- Compression
- Encryption

are performed at this level.

---

Example:

```text
UTF-8
```

---

Or:

```text
TLS Encryption
```

---

# Layer 5 — Session

Managing a session.

---

Task:

```text
Establishing
Managing
Ending the connection
```

---

Example:

When you visit a website and log in.

---

Your session is managed.

---

# Layer 4 — Transport

One of the most important layers.

---

Here:

```text
TCP
UDP
```

reside.

---

Task:

```text
Data transfer between programs
```

---

At this layer, the concept of:

```text
Port
```

comes into existence.

---

Example:

```text
80
443
22
53
```

---

# How the Port Scanner Relates to Layer 4

Our project works exactly on this layer.

---

We check:

```text
Which Port is open?
```

---

Meaning:

```text
Transport Layer
```

---

# Layer 3 — Network

This is where:

```text
IP
```

lives.

---

Example:

```text
192.168.1.10
```

---

Or:

```text
8.8.8.8
```

---

Task:

```text
Routing
```

---

Meaning determining where a packet should go.

---

# How the Port Scanner Relates to Layer 3

To scan, we need to know:

```text
What IP the target has
```

---

Therefore, our project also depends on Layer 3.

---

# Layer 2 — Data Link

Communication between devices on a local network.

---

At this layer, the concept of:

```text
MAC Address
```

exists.

---

Example:

```text
00:1A:2B:3C:4D:5E
```

---

Routers mostly work with IP.

---

Switches mostly work with MAC.

---

# Layer 1 — Physical

The lowest layer.

---

Everything is physical.

---

Example:

```text
Network cable
```

---

Or:

```text
Optical fiber
```

---

Or:

```text
Wi-Fi signals
```

---

At this layer, only bits are moved.

---

# The Path of a Real Request

Suppose the browser is opened and visits:

```text
https://github.com
```

---

First:

```text
Application
```

creates the request.

↓

```text
Presentation
```

encrypts it.

↓

```text
Session
```

manages the connection.

↓

```text
Transport
```

adds TCP.

↓

```text
Network
```

adds IP.

↓

```text
Data Link
```

adds MAC.

↓

```text
Physical
```

the data is transmitted.

---

# What Is Encapsulation?

Each layer adds its own information.

---

Example:

```text
Data
```

↓

```text
TCP Header
```

↓

```text
IP Header
```

↓

```text
Ethernet Header
```

---

This process is called:

```text
Encapsulation
```

---

# What Happens on the Receiving Side?

The reverse of the same process.

---

Each layer removes its own header.

---

This is called:

```text
Decapsulation
```

---

# In Which Layers Does the Port Scanner Operate?

Mostly:

```text
Layer 4
```

and

```text
Layer 3
```

---

Because:

```text
IP + Port
```

are the basis of how the scanner works.

---

# In Which Layers Does Nmap Operate?

Nmap is more professional.

---

Sometimes it goes down to:

```text
Layer 2
```

---

Sometimes it also analyzes:

```text
Layer 7
```

---

For example:

```text
Service Detection
Version Detection
OS Detection
```

---

# What Is the TCP/IP Model?

In the real world, the following is used more:

```text
TCP/IP Model
```

---

This model is a simplified version of OSI.

---

OSI:

```text
7 Layers
```

---

TCP/IP:

```text
4 Layers
```

---

But for teaching and understanding networks, OSI is usually better.

---

# What We Learned Today

✅ What OSI is

✅ Why it was created

✅ The seven OSI layers

✅ The role of each layer

✅ Where TCP sits

✅ Where UDP sits

✅ Where IP sits

✅ Where Port sits

✅ Encapsulation

✅ Decapsulation

✅ How OSI relates to the Port Scanner

---

# Exercise

Determine which layer each of the following belongs to:

```text
TCP
IP
HTTP
HTTPS
MAC Address
Port
DNS
WiFi Signal
```

---

# Next Session

File:

```text
09-how-port-scanners-work.md
```

Topic:

**How Do Port Scanners Actually Work?**

In this session, for the first time, we enter the heart of our own project and learn:

- What exactly a Port Scan is
- How an Open Port is detected
- What a Closed Port is
- What a Timeout is
- What a Connect Scan is
- What a SYN Scan is
- How Nmap scans
- What type of scan our current project actually performs

This session will be the bridge between networking education and the start of cybersecurity education.
