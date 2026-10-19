[🇮🇷 فارسی](/02-dns_lookup/docs/fa/02-networking-fundamentals/10-public-dns-providers.md)

# Lesson 10: Public DNS Providers

## Introduction

So far, we have learned:

- What DNS is
- How a DNS Query is performed
- What a Recursive Resolver is
- What an Authoritative Server is
- How DNS Cache works

But one important question still remains:

```text
When we send a DNS Query,
which DNS Server are we actually using?
```

The answer is:

```text
It depends.
```

We might use the DNS of our Internet Service Provider (ISP) or public DNS Servers.

In this lesson, we will become familiar with the most famous public DNS Providers.

---

# What Is a DNS Provider?

A DNS Provider is a system that receives users' DNS requests and finds the appropriate answer.

---

In other words, the:

```text
Recursive Resolver
```

that we learned about earlier is usually provided by a DNS Provider.

---

# The Default DNS of the ISP

In many networks:

```text
Modem
↓
ISP DNS
```

is used.

---

Example:

```text
Home Router
↓
ISP DNS
```

---

Advantages:

- Does not require manual configuration
- Works automatically

---

Disadvantages:

- It might be slow
- It might have restrictions
- It might keep more logs

---

# Google Public DNS

One of the most famous DNS Servers in the world is:

```text
Google Public DNS
```

---

Addresses:

```text
8.8.8.8
8.8.4.4
```

---

Features:

- High speed
- Global infrastructure
- High reliability
- DNSSEC support

---

Example configuration:

```text
Primary:
8.8.8.8

Secondary:
8.8.4.4
```

---

# Cloudflare DNS

One of today's most popular DNS Providers is:

```text
Cloudflare
```

---

Addresses:

```text
1.1.1.1
1.0.0.1
```

---

Its main focus is:

```text
Privacy
```

---

Cloudflare claims:

```text
User-identifying logs
are not kept for a long time.
```

---

Advantages:

- Very high speed
- Focus on privacy
- DNSSEC support
- DNS over HTTPS support

---

# Quad9

Address:

```text
9.9.9.9
```

---

Important feature:

```text
Security Filtering
```

---

Quad9 blocks some known malicious domains.

---

Example:

```text
Malware Domains
Phishing Domains
```

---

Advantages:

- Focus on security
- Free
- DNSSEC support

---

# OpenDNS

Owned by:

```text
Cisco
```

---

Addresses:

```text
208.67.222.222
208.67.220.220
```

---

Capabilities:

- DNS Filtering
- Parental Control
- Security Features

---

It is very popular in enterprise environments.

---

# Comparing Providers

| Provider | Primary IP |
|-----------|-----------|
| Google DNS | 8.8.8.8 |
| Cloudflare DNS | 1.1.1.1 |
| Quad9 | 9.9.9.9 |
| OpenDNS | 208.67.222.222 |

---

# DNSSEC Support

Today, almost all reputable DNS Providers support:

```text
DNSSEC
```

---

DNSSEC's goal:

```text
Validating the DNS answer
```

---

We will examine this topic in detail in the cybersecurity chapter.

---

# DNS over HTTPS (DoH)

Some Providers support:

```text
DNS over HTTPS
```

---

Instead of:

```text
UDP/53
```

requests are sent over HTTPS.

---

Advantages:

- Increased privacy
- Prevention of simple DNS eavesdropping

---

Google and Cloudflare are among the most famous DoH providers.

---

# DNS over TLS (DoT)

Another method for encrypting DNS:

```text
DNS over TLS
```

---

Goal:

```text
Protecting DNS Queries
```

---

# Which DNS Does Our System's Resolver Use?

When we wrote in the project:

```python
dns.resolver.resolve(
    domain,
    record_type,
)
```

---

the library:

```text
dnspython
```

by default uses the system's Resolver.

---

Therefore:

```text
The Query's result
```

depends on the operating system's DNS settings.

---

# Viewing the Current DNS on Windows

In PowerShell:

```powershell
ipconfig /all
```

---

Or:

```powershell
Get-DnsClientServerAddress
```

---

It displays:

```text
DNS Servers
```

---

# Viewing the Current DNS on Linux

Example:

```bash
cat /etc/resolv.conf
```

---

Sample:

```text
nameserver 8.8.8.8
```

---

# Why Is This Important for the Project?

Sometimes a Query works on your system but not on someone else's.

---

The reason might be:

```text
A different Resolver
```

---

Or:

```text
DNS Filtering
```

on the Provider being used.

---

Therefore, when troubleshooting DNS, we need to know:

```text
Which DNS Server are we using?
```

---

# Summary

In this lesson, we learned:

- What a DNS Provider is
- What Google DNS is
- What Cloudflare DNS is
- What Quad9 is
- What OpenDNS is
- What DNS over HTTPS is
- What DNS over TLS is
- How the operating system chooses the DNS Resolver
- The DNS Lookup project uses the system's Resolver

