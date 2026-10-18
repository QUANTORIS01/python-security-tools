[🇮🇷 فارسی](/01-port_scanner/docs/fa/02-networking/06-dns-and-domain-names.md)

# Session 06 — DNS and Domain Names

# Introduction

So far, we have learned that to establish a network connection, we ultimately need an IP address.

For example:

```text
142.250.190.78
```

But imagine if we had to memorize the IP of every website to open it.

For example, to visit Google we would have to type:

```text
142.250.190.78
```

And for every other service, we would have to memorize another IP.

That would be very difficult.

The solution:

```text
Domain Name
```

And the system that converts a domain name into an IP:

```text
DNS
```

---

# What Is a Domain Name?

A Domain Name is a human-readable name that points to one or more services or Internet addresses.

Example:

```text
google.com
```

or:

```text
github.com
```

or:

```text
python.org
```

---

For a human:

```text
google.com
```

is much easier to remember than:

```text
142.250.190.78
```

---

# What Is DNS?

DNS stands for:

```text
Domain Name System
```

DNS's main job is to find information related to domain names.

One of its most important uses is:

```text
Domain Name
        ↓
      DNS
        ↓
    IP Address
```

---

# A Real Example

Suppose you type into your browser:

```text
google.com
```

The computer needs to know:

```text
google.com
```

corresponds to which IP.

DNS is used to find this information.

---

# Why Is DNS Compared to a Phone Book?

Imagine you know a person's name:

```text
Ali
```

But you do not know his phone number.

In a phone book, you look up:

```text
Ali
```

and find the number.

DNS has a similar idea:

We ask about:

```text
google.com
```

and find the information related to it.

---

# Does DNS Only Return an IP?

No.

DNS is not just a simple table of:

```text
Domain → IP
```

DNS can hold many different types of information.

We call this information:

```text
DNS Records
```

---

# The A Record

The record:

```text
A
```

is used to map a domain name to an IPv4 address.

For example:

```text
example.com
        ↓
192.0.2.10
```

---

# The AAAA Record

The record:

```text
AAAA
```

is used for IPv6 addresses.

For example:

```text
example.com
        ↓
2001:db8::10
```

---

# The CNAME Record

The record:

```text
CNAME
```

can associate one name with another domain name.

A conceptual example:

```text
www.example.com
        ↓
example.com
```

---

# The MX Record

The record:

```text
MX
```

is used to specify a domain's Mail Servers.

That is, it can specify which servers a domain's emails should be delivered to.

---

# How Does the Port Scanner Relate to DNS?

Our current project receives an IP directly:

```bash
python -m src.cli 127.0.0.1 1 1000
```

But in a more professional tool, the user might write:

```bash
scanner example.com 1 1000
```

In this case, the domain name must first be converted into information suitable for establishing a connection.

---

# Converting a Domain to an IP in Python

Python provides us with the module:

```python
socket
```

One of its functions is:

```python
socket.gethostbyname()
```

---

Example:

```python
import socket

ip = socket.gethostbyname("example.com")

print(ip)
```

The output might look something like this:

```text
93.184.216.34
```

---

# An Important Note

We should not assume that every domain has only one IP.

A domain can:

- Have multiple IPs.
- Point to different services.
- Receive different responses based on geographic location.
- Use both IPv4 and IPv6.

That is why more professional tools usually examine DNS information more precisely.

---

# DNS and the Port Scanner

Suppose the user enters this:

```text
example.com
```

A simple flow could be like this:

```text
example.com
      ↓
DNS Resolution
      ↓
IP Address
      ↓
Port Scan
      ↓
Open Ports
```

---

Meaning:

```text
DNS
```

can come before:

```text
Port Scanning
```

---

# A Complete Example

Suppose:

```text
example.com
```

resolves to:

```text
192.0.2.10
```

Now the scanner can check:

```text
192.0.2.10:22
192.0.2.10:80
192.0.2.10:443
```

---

The result might be:

```text
22  CLOSED
80  OPEN
443 OPEN
```

---

# What Is a DNS Server?

A computer that answers DNS requests is called:

```text
DNS Server
```

---

For example, on a network, your system might use your ISP's DNS Server.

Or you can use public DNS Resolvers.

A famous example:

```text
8.8.8.8
```

---

# Is DNS Always Over TCP?

No.

DNS usually uses:

```text
UDP
```

The famous DNS port is:

```text
53
```

---

But DNS can, under certain conditions, also use:

```text
TCP
```

So we should not assume that:

```text
DNS = always UDP
```

---

# Why Is This Important for the Port Scanner?

In an actual test of our project, we saw:

```text
53 OPEN domain
```

---

Meaning on port:

```text
53
```

a service related to DNS was running.

But simply seeing:

```text
domain
```

does not mean we have identified all the details of the DNS service.

This is exactly the important difference between:

```text
Service Name
```

and actual:

```text
Service Detection
```

---

# The Difference Between DNS and Domain

We should not confuse these two concepts.

```text
Domain
```

is a name.

For example:

```text
example.com
```

---

But:

```text
DNS
```

is the system and the protocols used to find information related to domain names.

---

# Summary

Today we learned:

✅ What a Domain is

✅ What DNS is

✅ Why we need DNS

✅ What the A record is

✅ What the AAAA record is

✅ What the CNAME record is

✅ What the MX record is

✅ What a DNS Server is

✅ How DNS relates to the Port Scanner

✅ How to resolve a Domain in Python

---

# Exercise

Write a program that:

1. Receives a Domain.
2. Converts it to an IP.
3. Displays the IP.
4. If Resolution encounters an error, the program does not crash.

Example:

```text
Domain: example.com
IP: 93.184.216.34
```

---

# Next Session

File:

```text
07-packets-and-protocols.md
```

Topic:

**What Are Packets and Protocols?**

In the next session, we go below the level of:

```text
Application
```

and examine how data is actually transferred across a network.

We will learn:

- What a Packet is
- What a Header is
- What a Payload is
- What a TCP Segment is
- What a UDP Datagram is
- Why data is divided into smaller pieces
- How Port and Protocol fit into the network communication structure

