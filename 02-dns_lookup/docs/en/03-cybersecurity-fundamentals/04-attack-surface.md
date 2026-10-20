[🇮🇷 فارسی](/02-dns_lookup/docs/fa/03-cybersecurity-fundamentals/04-attack-surface.md)

# Lesson 04: Attack Surface

## Introduction

One of the first things every attacker does is examine:

```text
Which paths can be used to approach the target?
```

---

The sum of all these paths is called:

```text
Attack Surface
```

---

Understanding the Attack Surface is one of the most important cybersecurity skills.

Because:

```text
You cannot defend against something
you do not know exists.
```

---

# What Is Attack Surface?

An Attack Surface refers to all the points through which an attacker can interact with a system.

---

In simple terms:

```text
All the doors, windows, and inputs of the system
```

---

The larger the Attack Surface:

```text
The more opportunities exist for attack.
```

---

# A Simple Example

Suppose we have a server.

---

The following services are active on this server:

```text
22   SSH
80   HTTP
443  HTTPS
3306 MySQL
```

---

Each service is:

```text
A potential entry point
```

---

As a result:

```text
It is part of the Attack Surface
```

---

# Components of the Attack Surface

The Attack Surface is usually divided into three categories.

---

## 1. Network Attack Surface

Anything that can be accessed over the network.

---

Examples:

- Open ports
- Network services
- DNS
- VPN
- APIs

---

Example:

```text
22/tcp
80/tcp
443/tcp
```

---

The Port Scanner tool is used precisely to discover this part.

---

## 2. Software Attack Surface

Weaknesses in software.

---

Examples:

- Application vulnerabilities
- Outdated versions
- Misconfigurations
- Insecure libraries

---

Example:

```text
Apache 2.2
```

---

Or:

```text
WordPress Plugin Vulnerability
```

---

## 3. Human Attack Surface

Sometimes the weakest part of a system is:

```text
Humans
```

---

Examples:

- Weak passwords
- Clicking on malicious links
- Information disclosure
- Social engineering

---

Example:

```text
Password = 123456
```

---

# Attack Surface in a Company

Suppose we have a company.

---

Its assets:

```text
Website
Mail Server
VPN
Employees
DNS Records
Cloud Services
```

---

All of these are part of the Attack Surface.

---

# Why Do Attackers Examine the Attack Surface?

Because the attacker is looking for:

```text
The easiest path of entry
```

---

Often, attackers:

```text
Do not choose the hardest target.
```

---

They find the weakest point.

---

# Example

Suppose:

```text
The website is completely secure.
```

---

But:

```text
SSH Password
=
admin123
```

---

In this case:

```text
SSH
```

becomes the path of entry.

---

# Attack Surface and Reconnaissance

The first stage of most attacks is:

```text
Reconnaissance
```

---

In this stage, the attacker tries to:

- Discover domains
- Examine DNS Records
- Find open ports
- Identify services

---

All these activities are performed to understand the Attack Surface.

---

# Connection to DNS Lookup

Our DNS Lookup tool can display information such as:

```text
A Records
AAAA Records
MX Records
NS Records
TXT Records
```

---

This information reveals part of the Attack Surface.

---

Example:

```text
mail.example.com
```

---

Or:

```text
vpn.example.com
```

---

The existence of these records can provide important clues about the organization's infrastructure.

---

# Connection to the Port Scanner

The Port Scanner is one of the most important tools for identifying the Attack Surface.

---

Sample output:

```text
22/tcp
80/tcp
443/tcp
```

---

Now we know:

```text
Which services are available.
```

---

This is exactly part of the Attack Surface.

---

# Reducing the Attack Surface

One of the most important security principles is:

```text
Attack Surface Reduction
```

---

Meaning:

```text
Reducing unnecessary entry points
```

---

# Examples

## Closing Unnecessary Ports

If you do not use FTP:

```text
Port 21
```

should be closed.

---

## Removing Unused Services

Every extra service is:

```text
Extra risk
```

---

## Removing Old Accounts

Unused users can become attack paths.

---

## Removing Old Subdomains

Example:

```text
old.example.com
```

---

If it is no longer used:

```text
It should be removed.
```

---

# An Important Principle

Many organizations think:

```text
We must protect everything.
```

---

But in practice:

```text
If something is not needed,
remove it.
```

---

This approach is usually more effective.

---

# Attack Surface and Our Projects

So far, we have built two tools:

---

## Port Scanner

For discovering:

```text
Open Ports
Services
```

---

## DNS Lookup

For discovering:

```text
DNS Infrastructure
```

---

Both tools are in fact designed for analyzing:

```text
Attack Surface
```

---

# Summary

In this lesson, we learned:

- What the Attack Surface is
- Why it matters
- The types of Attack Surface
- The role of Reconnaissance in discovering it
- How DNS Lookup and Port Scanner relate to the Attack Surface
- Methods for reducing the Attack Surface

---

# Next Lesson

In the next lesson, we enter one of the most important stages of the attack lifecycle:

```text
Reconnaissance
```

And we will learn:

- What Reconnaissance is
- What Passive Recon is
- What Active Recon is
- How attackers gather information
- Where our tools fit in this process

