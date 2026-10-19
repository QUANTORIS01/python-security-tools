[🇮🇷 فارسی](/02-dns_lookup/docs/fa/02-networking-fundamentals/01-how-the-internet-works.md)

# Lesson 1: How Does the Internet Really Work?

## Introduction

Before we learn DNS, we need to understand what happens behind the scenes when we type in a browser:

```text
google.com
```

---

## What Is the Internet?

In simple terms:

```text
Internet = Network of Networks
```

Meaning:

```text
A network of networks
```

Thousands of ISPs, data centers, universities, companies, and organizations have been connected to each other and have formed what we call the Internet.

---

## Every Device Needs an Address

Just as your home has a postal address, every device connected to the Internet must also have an address.

We call this address:

```text
IP Address
```

Example:

```text
8.8.8.8
```

Or:

```text
142.250.186.14
```

---

## The Problem with IP Addresses

Computers work with IPs, but humans are poor at remembering numbers.

Memorizing addresses such as:

```text
142.250.186.14
151.101.1.140
104.18.33.45
```

is a difficult task.

---

## The Solution

Instead of using IPs, we use human-readable names:

```text
google.com
github.com
openai.com
```

But computers do not understand these names.

They only know IPs.

---

## What Is DNS?

DNS stands for:

```text
Domain Name System
```

DNS's task is to convert a domain name into an IP Address.

Example:

```text
google.com
      ↓
142.250.186.14
```

We call this process:

```text
DNS Lookup
```

or:

```text
Name Resolution
```

---

## What Happens When You Open a Website?

When you type in your browser:

```text
https://google.com
```

the following steps occur:

```text
Browser
   ↓
DNS Lookup
   ↓
IP Address
   ↓
TCP Connection
   ↓
HTTP Request
   ↓
Google Server
   ↓
HTTP Response
   ↓
Browser
```

---

## Where the DNS Lookup Project Fits

The tool we have built in this project works exactly in the DNS part:

```text
Browser
   ↓
DNS Lookup   ← DNS Lookup Tool
   ↓
IP Address
```

We ask DNS:

```text
What is the IP for google.com?
```

And we receive the answer.

---

## Connection to the Port Scanner Project

In the previous project:

```text
Port Scanner
```

we received an IP and checked its ports.

Example:

```text
142.250.186.14
```

But to reach this IP, we usually have to perform a DNS Lookup first.

Therefore, DNS Lookup is, in practice, considered one of the stages before Port Scanning.

---

## Why Might a Domain Have Multiple IPs?

The DNS answer is not always the same.

For example:

```text
google.com
```

might return different IPs at different times.

The reasons for this are:

- Load Balancing
- Content Delivery Networks (CDN)
- Geographic Routing
- High Availability

---

## The Importance of DNS in Cybersecurity

DNS is one of the most important components of network security.

Many security activities depend on DNS:

- Subdomain Enumeration
- Threat Intelligence
- Malware Analysis
- Phishing Detection
- DNS Monitoring
- DNS Tunneling Detection

That is why understanding DNS is essential for any security specialist.

---

## Summary

In this lesson, we learned:

- What the Internet is
- What an IP Address is
- Why DNS was created
- What DNS Lookup is
- Where DNS sits in network communication
- How DNS relates to the Port Scanner
- The importance of DNS in cybersecurity

---

## Next Lesson

In the next lesson, we will become familiar with the following concepts:

- IPv4
- Network Address
- Host Address
- Public IP
- Private IP

These concepts are the most fundamental part of networking and are essential for understanding how DNS works.
