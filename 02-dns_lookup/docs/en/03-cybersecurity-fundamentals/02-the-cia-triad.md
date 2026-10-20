[🇮🇷 فارسی](/02-dns_lookup/docs/fa/03-cybersecurity-fundamentals/02-the-cia-triad.md)

# Lesson 02: CIA Triad

## Introduction

Almost all cybersecurity concepts go back to a very important model:

```text
CIA Triad
```

---

This model is the foundation of many security decisions.

When a system is designed or a security control is implemented, the goal is usually to protect one or more parts of the CIA Triad.

---

# What Does CIA Stand For?

CIA stands for three main concepts:

```text
Confidentiality
Integrity
Availability
```

---

# Confidentiality

## What Is Confidentiality?

Confidentiality means:

```text
Only authorized people
should have access to information.
```

---

The goal is:

```text
Preventing information disclosure
```

---

# Example

Suppose we have a database containing customer information:

```text
Names
Emails
Phone Numbers
Passwords
```

---

This information should not be made available to unauthorized people.

---

If an attacker can view this information:

```text
Confidentiality Breach
```

has occurred.

---

# Methods for Protecting Confidentiality

Examples:

- Encryption
- Authentication
- Access Control
- Authorization

---

Example:

```text
HTTPS
```

causes information to be encrypted in transit.

---

# Integrity

## What Is Integrity?

Integrity means:

```text
Information remains unchanged
and correct.
```

---

The goal is:

```text
Preventing data tampering
```

---

# Example

Suppose the bank account balance is:

```text
1000$
```

---

If an attacker changes the amount to:

```text
100000$
```

```text
Integrity Violation
```

has occurred.

---

# Another Example

A software file:

```text
installer.exe
```

---

If the file is tampered with during download:

```text
Integrity
```

has been lost.

---

# Methods for Protecting Integrity

Examples:

- Hashing
- Checksums
- Digital Signatures
- Version Control

---

Example:

```text
SHA256
```

is used to verify that a file has not changed.

---

# Availability

## What Is Availability?

Availability means:

```text
The system and data
are available
when needed.
```

---

The goal is:

```text
Preventing service disruption
```

---

# Example

Suppose the company website:

```text
example.com
```

---

is taken offline due to a:

```text
DDoS
```

attack.

---

In this case:

```text
Availability Failure
```

has occurred.

---

# Another Example

A hard disk failure:

```text
Disk Failure
```

---

might cause data to become unavailable.

---

# Methods for Protecting Availability

Examples:

- Backup
- Redundancy
- Load Balancing
- Disaster Recovery
- High Availability Systems

---

# A Real Example

Suppose we have a banking system.

---

Confidentiality:

```text
Only the account holder
should see the account information.
```

---

Integrity:

```text
The account balance
should be recorded correctly.
```

---

Availability:

```text
The bank should be
available 24/7.
```

---

# Are All Three Always Important?

Yes.

But their importance varies across different systems.

---

Example:

A military system:

```text
Confidentiality
```

is very important.

---

Example:

An air traffic control system:

```text
Availability
```

is of very high importance.

---

Example:

A financial system:

```text
Integrity
```

has high priority.

---

# Connection to Our Tools

## Port Scanner

In the Port Scanner, we mostly dealt with:

```text
Availability
```

---

Because we were checking:

```text
Which services
are available.
```

---

## DNS Lookup

In DNS Lookup, too:

```text
Availability
```

matters.

---

If the DNS Server does not respond:

```text
Domain Resolution
```

cannot be performed.

---

# Connection to Attacks

Almost all cyber attacks target one of these three parts.

---

Information theft:

```text
Confidentiality
```

---

Data tampering:

```text
Integrity
```

---

Service disruption:

```text
Availability
```

---

# Why Is the CIA Triad Important?

Because when designing any security system, we can ask:

```text
Is confidentiality preserved?
Is integrity preserved?
Is availability preserved?
```

---

If the answer to all three questions is positive:

```text
The security system will be stronger.
```

---

# Summary

In this lesson, we learned:

- What the CIA Triad is
- What Confidentiality is
- What Integrity is
- What Availability is
- What threats each part faces
- How each part is protected
- How the CIA Triad relates to security tools

---

# Next Lesson

In the next lesson, we enter one of the most important security concepts:

```text
Threats, Vulnerabilities and Risks
```

And we will learn:

- What a Threat is
- What a Vulnerability is
- What Risk is
- What the difference between these three concepts is
- Why most people confuse them

