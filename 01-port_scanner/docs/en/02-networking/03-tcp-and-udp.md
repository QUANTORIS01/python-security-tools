[🇮🇷 فارسی](/01-port_scanner/docs/fa/02-networking/03-tcp-and-udp.md)

# Session 03 — What Are TCP and UDP?

# Introduction

So far, we have learned:

✅ What a network is

✅ What an IP is

But one very important question still remains:

When two computers connect to each other, how is data transferred?

---

The answer to this question is:

```text
Protocol
```

---

# What Is a Protocol?

A protocol means:

```text
A set of communication rules
```

---

A real-world example:

If two people want to talk on the phone, they must follow some rules.

For example:

- One speaks
- The other listens
- The voice is understandable
- The call is not disconnected

---

Computers also need rules to communicate.

---

We call these rules:

```text
Protocol
```

---

# The Most Important Internet Protocols

# HTTP

For websites

---

# HTTPS

The secure version of HTTP

---

# FTP

File transfer

---

# DNS

Converting a domain name to an IP

---

# TCP

Reliable data transfer

---

# UDP

Fast data transfer

---

In this session, we focus on TCP and UDP.

---

# What Is TCP?

TCP stands for:

```text
Transmission Control Protocol
```

---

TCP's goal:

```text
Reliable data transfer
```

---

TCP wants to make sure that:

- Data is not lost
- Data is not corrupted
- The order of the data is preserved

---

# A Real Example

Suppose you want to send a 100-page book to your friend.

---

TCP is like a postal service that:

- Numbers every page
- Gets a delivery receipt
- Resends a page if it is lost

---

As a result:

The entire book arrives safely.

---

But it takes a bit more time.

---

# What Is a Handshake?

Before transferring data over TCP:

The connection must be established.

---

This process is called:

```text
Three-Way Handshake
```

---

# Step 1

The client says:

```text
SYN
```

Meaning:

```text
I want to establish a connection
```

---

# Step 2

The server responds:

```text
SYN + ACK
```

Meaning:

```text
I received your request
```

---

# Step 3

The client says:

```text
ACK
```

Meaning:

```text
I received your response
```

---

The connection is now established.

---

# A Simple Handshake Diagram

```text
Client -------- SYN --------> Server

Client <---- SYN/ACK -------- Server

Client -------- ACK --------> Server
```

---

After this stage, data transfer begins.

---

# Why Is TCP Important for the Port Scanner?

Our current port scanner uses exactly this feature.

---

When this code runs:

```python
socket.connect()
```

Behind the scenes:

```text
TCP Handshake
```

is performed.

---

If a response is received:

```text
Port Open
```

---

If no response is received:

```text
Port Closed
```

---

As simple as that.

---

# What Is UDP?

UDP stands for:

```text
User Datagram Protocol
```

---

UDP's goal:

```text
High speed
```

---

Unlike TCP, UDP:

- Does not receive receipts
- Does not check whether data arrived
- Does not resend

---

It just sends the data.

---

# A Real Example

TCP is like:

```text
Registered mail
```

---

UDP is like:

```text
A loudspeaker
```

---

The loudspeaker shouts:

```text
Announcement!
```

---

If no one hears it:

It doesn't matter.

---

# Advantage of UDP

It is very fast.

---

# Disadvantage of UDP

It has lower reliability.

---

# Which Services Use UDP?

# DNS

Port:

```text
53
```

---

# DHCP

Ports:

```text
67
68
```

---

# VoIP

Internet calls

---

# Online Games

Online games

---

# Streaming

Live streaming

---

# Why Do Online Games Love UDP?

Suppose in a game:

A player's position is sent 60 times per second.

---

If one of the packets is lost:

It doesn't matter.

---

The next packet arrives immediately.

---

But if TCP were used:

The lost packet would have to be resent.

---

This causes:

```text
Lag
```

---

# TCP vs UDP

| TCP | UDP |
|------|------|
| Reliable | Fast |
| Has Handshake | No Handshake |
| Has Error Checking | Minimal Error Checking |
| Slower | Faster |
| Suitable for the web | Suitable for games |

---

# Why Is UDP Scanning Harder?

This part is very important.

---

In TCP:

If the port is open:

We receive a response.

---

But in UDP:

Many services do not respond at all.

---

Example:

We send a:

```text
UDP Packet
```

---

We might receive:

```text
No response
```

---

Now we do not know:

- Is the port open?
- Is the port closed?
- Did a firewall drop it?

---

That is why:

```text
UDP Scanning
```

is much harder.

---

# How Does Nmap Perform UDP Scanning?

Nmap sends a UDP packet.

---

If it receives the following message:

```text
ICMP Port Unreachable
```

it understands:

```text
Port Closed
```

---

If it does not receive a response:

It guesses:

```text
Open | Filtered
```

---

That is why UDP scan results are usually not definitive.

---

# Does Our Port Scanner Perform UDP Scanning?

For now, no.

---

The current scanner is a:

```text
TCP Scanner
```

---

And that is exactly what most simple scanners do.

---

# Will We Add UDP Scanning Later?

Yes.

---

On the path to bringing the project closer to Nmap:

One of the important features will be:

```text
UDP Scanning
```

---

# How TCP Relates to Banner Grabbing

When we retrieve a service banner:

```python
socket.recv()
```

---

We are, in fact, working over a TCP connection.

---

Therefore:

- Port Scan
- Banner Grabbing

are both based on TCP.

---

# What We Learned Today

✅ What a protocol is

✅ What TCP is

✅ What UDP is

✅ What a Handshake is

✅ The difference between TCP and UDP

✅ Why our Port Scanner is a TCP Scanner

✅ Why UDP scanning is hard

✅ How Nmap performs UDP scanning

✅ How TCP relates to Banner Grabbing

---

# Next Session

File:

```text
04-ports-and-services.md
```

Topic:

**What Is a Port?**

In the next session, we will learn:

- What a Port is
- Why one IP has multiple services
- What a Port Range is
- What Well-Known Ports are
- Famous security ports
- How Port relates directly to the Port Scanner project

