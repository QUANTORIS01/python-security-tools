[🇮🇷 فارسی](/02-dns_lookup/docs/fa/02-networking-fundamentals/02-introduction-to-ip-addresses-and-ipv4.md)

# Lesson 2: Introduction to IP Addresses and IPv4

## Introduction

In the previous lesson, we learned that DNS converts a domain name into an IP Address.

But we still do not know exactly what an IP is and what structure it has.

In this lesson, we become familiar with the most important networking concept:

```text
IP Address
```

---

## What Is an IP Address?

An IP Address stands for:

```text
Internet Protocol Address
```

Every device on an IP-based network must have a unique address.

Similar to a postal address:

```text
House ← postal address
Computer ← IP Address
```

Without an IP, no device can communicate with another device.

---

## Sample IPs

Example:

```text
8.8.8.8
```

Or:

```text
142.250.186.14
```

Or:

```text
192.168.1.10
```

These are all examples of IPv4 addresses.

---

## What Is IPv4?

The fourth version of the IP protocol is called:

```text
IPv4
```

Today, a large part of the Internet still uses IPv4.

---

## The Structure of IPv4

An IPv4 consists of four numbers:

```text
192.168.1.10
```

Each part is called an:

```text
Octet
```

So we have:

```text
192 | 168 | 1 | 10
```

---

## The Range of Each Octet

Each octet can have a value between:

```text
0 and 255
```

Valid example:

```text
192.168.1.1
```

Invalid example:

```text
300.168.1.1
```

Because:

```text
300 > 255
```

---

## Why Only Up to 255?

Each octet equals:

```text
8 bits
```

So it covers:

```text
00000000
```

through:

```text
11111111
```

The maximum possible value is:

```text
255
```

---

## Binary Representation of IPv4

Example:

```text
192.168.1.10
```

in binary:

```text
11000000.10101000.00000001.00001010
```

---

## The Total Number of IPv4 Addresses

IPv4 has:

```text
32 bits
```

Therefore, there are:

```text
2^32
```

possible addresses.

Approximately:

```text
4.3 billion
```

addresses.

---

## Network and Host

An IP usually has two parts:

```text
Network Portion
Host Portion
```

Example:

```text
192.168.1.10
```

In many home networks:

```text
192.168.1
```

is the network part.

And:

```text
10
```

is considered the device identifier.

---

## What Is a Public IP?

A Public IP is an address that is visible on the Internet.

Example:

```text
8.8.8.8
```

This IP belongs to Google's public DNS.

Any device on the Internet can access it.

---

## What Is a Private IP?

Some IPs are only used inside internal networks.

We call them:

```text
Private IP
```

---

## Private IP Ranges

### Class A

```text
10.0.0.0
to
10.255.255.255
```

---

### Class B

```text
172.16.0.0
to
172.31.255.255
```

---

### Class C

```text
192.168.0.0
to
192.168.255.255
```

---

## A Home Network Example

Usually, your home router assigns IPs similar to these:

```text
192.168.1.2
192.168.1.3
192.168.1.4
```

These IPs are not visible on the Internet.

---

## Converting a Private IP to a Public IP

The router uses a technique called:

```text
NAT
```

Process:

```text
Laptop
192.168.1.10
      ↓
Router (NAT)
      ↓
Public IP
      ↓
Internet
```

---

## IPv4 in the DNS Lookup Project

When we run this command:

```bash
python -m src.cli google.com A
```

the answer will usually include an IPv4 address:

```text
google.com
↓
216.239.38.120
```

The record:

```text
A
```

is used to retrieve IPv4 addresses.

---

## The Difference Between A and AAAA

The record:

```text
A
```

is for IPv4.

Example:

```text
216.239.38.120
```

But:

```text
AAAA
```

is used for IPv6.

Example:

```text
2001:4860:4860::8888
```

We will examine IPv6 in later lessons.

---

## Common Errors

Valid IP:

```text
192.168.1.1
```

Invalid IP:

```text
192.168.1.300
```

---

Valid IP:

```text
8.8.8.8
```

Invalid IP:

```text
8.8.8
```

---

Valid IP:

```text
10.0.0.1
```

Invalid IP:

```text
10.0.0.1.5
```

---

## Summary

In this lesson, we learned:

- What an IP Address is
- What IPv4 is
- The four-part structure of IPv4
- The concept of Octet
- The difference between Public and Private IPs
- What NAT is
- How the A record relates to IPv4
- The initial difference between IPv4 and IPv6

---

## Next Lesson

In the next lesson, we will learn:

- What a Domain is
- What a Subdomain is
- What FQDN is
- How the DNS Name Hierarchy works

These concepts are directly at the heart of the DNS Lookup project.
