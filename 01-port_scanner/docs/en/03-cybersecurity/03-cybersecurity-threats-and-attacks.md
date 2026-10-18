[🇮🇷 فارسی](/01-port_scanner/docs/fa/03-cybersecurity/03-cybersecurity-threats-and-attacks.md)

# Session 03 — Threats, Vulnerabilities, and Attacks

# Introduction

In the previous session, we learned:

```text
Who is a hacker?
```

And we understood that:

```text
Cybersecurity is not just hacking
```

---

But one important question still remains:

---

How does an attacker even get into a system?

---

The answer to this question lies in three important concepts:

```text
Threat
Vulnerability
Attack
```

---

If we understand these three concepts:

---

We have understood almost the entire foundation of cybersecurity.

---

# What Is a Threat?

A Threat means:

```text
Threat
```

---

Anything that can harm a system.

---

Example:

```text
Hacker
Malware
Virus
Ransomware
Insider
```

---

All of these are:

```text
Threats
```

---

# A Real Example

Suppose you have a house.

---

There is a thief in the neighborhood.

---

Even if he has not entered the house yet:

---

He is a:

```text
Threat
```

---

Because he has the potential to cause harm.

---

# What Is a Vulnerability?

A Vulnerability means:

```text
Vulnerability
```

or

```text
Weakness
```

---

A weakness that can be exploited.

---

Example:

```text
Weak password
```

---

Or:

```text
Outdated software
```

---

Or:

```text
An unprotected open port
```

---

All of these are vulnerabilities.

---

# The House Example

Imagine the house's door.

---

If the door has no lock:

---

This is a:

```text
Vulnerability
```

---

# What Is an Attack?

An Attack means:

```text
Attack
```

---

It occurs when an attacker exploits a vulnerability.

---

Example:

```text
Weak Password
```

↓

```text
Password Guessing
```

↓

```text
Unauthorized Access
```

---

This is an:

```text
Attack
```

---

# How These Three Concepts Relate

Almost all security attacks follow this pattern:

---

```text
Threat
+
Vulnerability
=
Attack
```

---

Example:

```text
Hacker
+
Weak Password
=
Login Attack
```

---

# What Is an Exploit?

The next important term:

```text
Exploit
```

---

A tool or method used to exploit a vulnerability.

---

Example:

---

Suppose a program has a security weakness.

---

The code that uses that weakness is called:

```text
Exploit
```

---

# A Real Example

Vulnerability:

```text
SQL Injection
```

---

Attack code:

```text
Exploit
```

---

Result:

```text
Unauthorized access
```

---

# What Is Malware?

Malware stands for:

```text
Malicious Software
```

---

Meaning:

```text
Malicious software
```

---

Goal:

```text
Causing harm
```

or

```text
Exploitation
```

---

# Types of Malware

# Virus

Virus

---

Attaches itself to files.

---

And spreads when executed.

---

# Worm

Worm

---

To spread:

```text
It does not require user interaction
```

---

It uses the network.

---

# Trojan

Trojan

---

Looks useful.

---

But behind the scenes:

```text
Malicious behavior
```

it performs.

---

Example:

```text
Game.exe
```

---

But in reality:

```text
Malware
```

---

# Spyware

Spyware

---

Collects user information.

---

Example:

```text
Passwords
Browser History
Cookies
```

---

# Keylogger

A type of Spyware.

---

Records all keys pressed by the user.

---

Example:

---

When you type a password.

---

# Ransomware

One of the most dangerous types of malware.

---

It:

```text
Encrypts
```

files.

---

Then demands money.

---

Example:

```text
Pay 1000$
or
Lose Your Files
```

---

# Why Is Ransomware Dangerous?

Because it can:

---

Lock down an entire company's data.

---

Real examples:

```text
WannaCry
LockBit
Conti
```

---

# What Is Social Engineering?

Sometimes the attacker does not hack the system at all.

---

Rather:

```text
They hack the human
```

---

This method is called:

```text
Social Engineering
```

---

# Example

Message:

```text
Your account has been blocked.
Click here to reactivate.
```

---

The user clicks.

---

Enters their password.

---

The attack succeeds.

---

# What Is Phishing?

The most famous type of Social Engineering.

---

Goal:

```text
Stealing information
```

---

Through:

```text
Email
SMS
Website
```

---

# Is Port Scanning Also an Attack?

No.

---

Port scanning is usually:

```text
Reconnaissance
```

---

Meaning:

```text
Gathering information
```

---

Before an attack.

---

Example:

---

First, the attacker checks:

```text
Which ports are open?
```

---

Then decides:

```text
Is there a vulnerability?
```

---

# The Role of Our Project

The project we have built:

```text
Port Scanner
```

---

sits in the first stage of the security lifecycle:

---

```text
Information Gathering
```

---

or:

```text
Reconnaissance
```

---

# A Real Scenario

Suppose an attacker has found a server.

---

First:

```text
Port Scan
```

is performed.

---

Result:

```text
22
80
3306
```

are open.

---

Now he knows:

```text
SSH
HTTP
MySQL
```

are active.

---

Then he begins examining vulnerabilities.

---

# What We Learned Today

✅ What a Threat is

✅ What a Vulnerability is

✅ What an Attack is

✅ What an Exploit is

✅ What Malware is

✅ What a Virus is

✅ What a Worm is

✅ What a Trojan is

✅ What Spyware is

✅ What a Keylogger is

✅ What Ransomware is

✅ What Social Engineering is

✅ What Phishing is

✅ Where the Port Scanner fits into the attack process

---

# Exercise

For each item, determine:

```text
Threat
or
Vulnerability
or
Attack
```

---

### First Example

```text
Password = 123456
```

---

### Second Example

```text
Ransomware
```

---

### Third Example

```text
Using a weak password to log in to an account
```

---

### Fourth Example

```text
SQL Injection Exploit
```

---

# Next Session

File:

```text
04-security-lifecycle.md
```

Topic:

**The Complete Attack and Defense Lifecycle in Cybersecurity**

In the next session, we will learn:

- Reconnaissance
- Scanning
- Enumeration
- Exploitation
- Privilege Escalation
- Persistence
- Covering Tracks

And we will see exactly at which stage of an attack or penetration test the Port Scanner sits.
