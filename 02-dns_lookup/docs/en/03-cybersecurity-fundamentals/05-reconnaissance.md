[🇮🇷 فارسی](/02-dns_lookup/docs/fa/03-cybersecurity-fundamentals/05-reconnaissance.md)

# Lesson 05: Reconnaissance

## Introduction

Almost no attacker starts an attack directly.

---

Before any successful attack, there is usually a stage called:

```text
Reconnaissance
```

---

which is also called:

```text
Recon
```

---

The goal of Reconnaissance is:

```text
Gathering information about the target
```

---

The more information is gathered:

```text
The higher the likelihood of a successful attack.
```

---

# What Is Reconnaissance?

Reconnaissance is the process of identifying and gathering information about a target.

---

This information can include:

- Domains
- Subdomains
- IP addresses
- DNS Records
- Network services
- Technologies used
- Emails
- Employee information

---

In simple terms:

```text
Knowing the target before the attack
```

---

# Why Is Recon Important?

Suppose an attacker has no information about the target.

---

In this case:

```text
The attack will be almost blind.
```

---

But if the attacker knows:

```text
What services does the target have?
What DNS Records does it have?
What technologies does it use?
```

---

they can design much more effective attacks.

---

# Types of Reconnaissance

Recon is usually divided into two categories:

```text
Passive Reconnaissance
Active Reconnaissance
```

---

# Passive Reconnaissance

In Passive Recon, the attacker gathers information without directly interacting with the target.

---

Goal:

```text
Gathering information
without drawing attention
```

---

# Examples

## Searching Search Engines

Example:

```text
site:example.com
```

---

## Examining Social Networks

Example:

- LinkedIn
- X
- GitHub

---

## Examining WHOIS Information

Example:

```text
Domain Registration Data
```

---

## Examining Certificate Transparency Logs

For finding subdomains.

---

# The Advantage of Passive Recon

```text
The target usually does not notice the attacker's activity.
```

---

# Active Reconnaissance

In Active Recon, the attacker directly communicates with the target system.

---

Example:

- Sending DNS Queries
- Port Scanning
- Banner Grabbing
- Service Detection

---

In this case:

```text
The target might log the activity.
```

---

# Example

When we run:

```bash
python -m src.cli example.com A
```

---

the DNS Lookup tool sends a real DNS Query.

---

This activity is considered:

```text
Active Recon
```

---

# Another Example

The Port Scanner establishes:

```text
TCP Connection
```

---

This is also:

```text
Active Recon
```

---

# What Information Is Gathered During Recon?

Usually, the attacker seeks answers to these questions:

---

## What domains does the target have?

Example:

```text
example.com
```

---

## What subdomains exist?

Example:

```text
mail.example.com

vpn.example.com

api.example.com
```

---

## What IPs are used?

Example:

```text
93.184.216.34
```

---

## What services are running?

Example:

```text
SSH
HTTP
HTTPS
SMTP
```

---

## What technologies are used?

Example:

```text
Apache
Nginx
WordPress
```

---

# How Recon Relates to Attack Surface

In the previous lesson, we learned about:

```text
Attack Surface
```

---

Recon is the process performed to discover the Attack Surface.

---

In simple terms:

```text
Recon
=
Discovery of Attack Surface
```

---

# Recon Tools

Some common tools:

- DNS Lookup
- Port Scanner
- Whois Tools
- Subdomain Finder
- Network Mapper

---

Interestingly:

```text
We have built
the first two tools ourselves.
```

---

# A Practical Example

Suppose we examine:

```text
example.com
```

---

DNS Lookup finds:

```text
MX Record
```

---

Output:

```text
mail.example.com
```

---

Now the attacker knows:

```text
A Mail Server exists.
```

---

Then, with the Port Scanner, they scan:

```text
mail.example.com
```

---

And discover that:

```text
25/tcp
465/tcp
587/tcp
```

are open.

---

This information can be used for the later stages of the attack.

---

# Is Recon Illegal?

Answer:

```text
It depends.
```

---

If it is performed on systems you do not own or do not have permission to test:

it may create legal issues.

---

That is why all our security tools emphasize:

```text
Only use on systems
you own or have permission to test.
```

---

# Recon and Blue Team

Recon is not just for attackers.

---

Defenders also use Recon.

---

For example:

- Discovering forgotten services
- Finding old subdomains
- Examining the organization's Attack Surface

---

# An Important Note

Most successful attacks:

```text
Do not start with Exploitation.
```

---

Rather, they start with:

```text
Reconnaissance
```

---

Because:

```text
Information
is power.
```

---

# Connection to Our Projects

## Port Scanner

Used for:

```text
Service Discovery
```

---

## DNS Lookup

Used for:

```text
DNS Recon
```

---

Both tools sit in the Reconnaissance phase.

---

# Summary

In this lesson, we learned:

- What Reconnaissance is
- What Passive Recon is
- What Active Recon is
- What information attackers gather
- How Recon reveals the Attack Surface
- What role DNS Lookup and Port Scanner play in Recon

---

# Next Lesson

In the next lesson, we enter the stage after Recon:

```text
Enumeration
```

And we will learn:

- What Enumeration is
- How it differs from Recon
- Why attackers move to Enumeration after Recon
- How they turn raw information into usable information

