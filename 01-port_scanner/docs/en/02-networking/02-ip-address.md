[🇮🇷 فارسی](/01-port_scanner/docs/fa/02-networking/02-ip-address.md)

# Session 02 — What Is an IP Address?

# Introduction

In the previous session, we learned that:

- What a network is
- What a Client is
- What a Server is

But one important question still remains:

❓ When billions of devices are connected to a network, how can we find a specific device?

Answer:

```text
IP Address
```

---

# What Is an IP?

An IP is short for:

```text
Internet Protocol Address
```

In simple terms:

An IP is the address of every device on a network.

Just like a house address.

---

# A Real-World Example

Suppose you want to send a letter to your friend.

If you only write on the envelope:

```text
Ali
```

The post office will not know where to take the letter.

But if you write:

```text
Tehran
Street ...
Alley ...
Number ...
```

The letter will reach its destination.

---

Computers have exactly the same problem.

That is why every device has an address.

We call this address:

```text
IP Address
```

---

# Sample IPs

```text
192.168.1.10
```

or:

```text
8.8.8.8
```

or:

```text
1.1.1.1
```

---

# Why Does a Port Scanner Need an IP?

Suppose we write:

```python
scan_target()
```

It is not clear which device we are scanning.

But if we write:

```python
scan_target("192.168.1.10")
```

Now we know which device is the target.

---

# What Is IPv4?

The most common type of IP:

```text
IPv4
```

Example:

```text
192.168.1.10
```

---

IPv4 consists of 4 parts.

Example:

```text
192.168.1.10
```

First part:

```text
192
```

Second part:

```text
168
```

Third part:

```text
1
```

Fourth part:

```text
10
```

---

Each part is a number between:

```text
0 and 255
```

---

# Valid Examples

```text
192.168.1.1
```

```text
10.0.0.1
```

```text
172.16.5.20
```

---

# Invalid Examples

```text
300.1.1.1
```

Because:

```text
300 > 255
```

---

```text
192.168.1
```

Because it does not have four parts.

---

```text
abc.def.ghi.jkl
```

Because it is not numeric.

---

# The Reason for Creating `validator.py`

That is why in the Port Scanner project we created the following file:

```text
validator.py
```

---

Its task:

Checking the validity of an IP.

---

Example:

```python
validate_ip("192.168.1.10")
```

Output:

```python
True
```

---

Example:

```python
validate_ip("500.1.1.1")
```

Output:

```python
False
```

---

# IPv4 Has a Limitation

IPv4 produces approximately:

```text
4.3 Billion
```

addresses.

---

In the past, this number was very large.

But today:

- Mobile phones
- Laptops
- Servers
- TVs
- Cameras
- Smart watches

all need IPs.

---

As a result, IPv4 gradually ran into an address shortage problem.

---

# What Is IPv6?

To solve this problem:

```text
IPv6
```

was created.

---

Sample IPv6:

```text
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

---

The number of IPv6 addresses is so large that it will practically never run out.

---

# Does Our Port Scanner Support IPv6?

For now, no.

---

The current project only supports:

```text
IPv4
```

---

Later, if we want to bring the project closer to a more professional level, we can add:

```text
IPv6 Support
```

---

# What Is a Public IP?

When you connect to the Internet:

Your internet service provider gives you an IP.

Example:

```text
85.x.x.x
```

This IP is visible on the entire Internet.

---

This type is called:

```text
Public IP
```

---

# What Is a Private IP?

Inside a home network, we usually have addresses like:

```text
192.168.1.10
```

or:

```text
192.168.1.20
```

---

These IPs are only valid inside the home network.

---

This type is called:

```text
Private IP
```

---

# The Most Famous Private IP Ranges

---

## First Class

```text
10.0.0.0
to
10.255.255.255
```

---

## Second Class

```text
172.16.0.0
to
172.31.255.255
```

---

## Third Class

```text
192.168.0.0
to
192.168.255.255
```

---

# How Do We See Our Own Computer's IP?

On Windows:

```powershell
ipconfig
```

---

On Linux:

```bash
ip addr
```

or:

```bash
ifconfig
```

---

# A Real Example

The output might look something like this:

```text
IPv4 Address: 192.168.1.100
```

---

This means:

Your computer has this address on the local network.

---

# How IP Relates to the Port Scanner

When we run this command:

```bash
python -m src.cli 127.0.0.1 1 1000
```

The part:

```text
127.0.0.1
```

is, in fact, the target IP.

---

The scanner tries to connect to this IP.

And checks the status of the ports.

---

# What Is Loopback?

One of the most famous IPs:

```text
127.0.0.1
```

---

It is called:

```text
Loopback
```

or:

```text
localhost
```

---

This IP points to the computer itself.

---

Example:

```bash
ping 127.0.0.1
```

---

Meaning:

"Is myself reachable?"

---

That is why most of our tests were done on:

```text
127.0.0.1
```

---

# What We Learned Today

✅ What an IP is

✅ What IPv4 is

✅ What IPv6 is

✅ What a Public IP is

✅ What a Private IP is

✅ What Loopback is

✅ How IP relates to the Port Scanner

✅ Why `validate_ip` exists

---

# Next Session

File:

```text
03-tcp-and-udp.md
```

Topic:

**What Are TCP and UDP?**

In the next session, we will learn:

- What TCP is
- What UDP is
- The difference between TCP and UDP
- Why our Port Scanner is a TCP Scanner
- Why UDP scanning is harder
- How Nmap performs UDP scanning

