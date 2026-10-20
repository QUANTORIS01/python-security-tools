[🇮🇷 فارسی](/02-dns_lookup/docs/fa/03-cybersecurity-fundamentals/03-threats-vulnerabilities-and-risks.md)

# Lesson 03: Threats, Vulnerabilities and Risks

## Introduction

There are three terms used in almost all branches of cybersecurity:

```text
Threat
Vulnerability
Risk
```

---

Many people confuse these three concepts.

While each has a different meaning, and understanding the difference between them is essential for a security specialist.

---

# What Is a Threat?

A Threat is anything that can harm an asset.

---

In simple terms:

```text
A potential cause of damage
```

---

# Example

Examples of a Threat:

- Hackers
- Malware
- Ransomware
- DDoS attacks
- Disgruntled employees
- Human errors
- Natural disasters

---

All of these can cause harm to a system.

---

# What Is a Vulnerability?

A Vulnerability means:

```text
A weakness or flaw
that can be exploited by a Threat.
```

---

In other words:

```text
An open door
for the attacker to enter
```

---

# Example

Suppose a website has an:

```text
Admin Panel
```

---

And the admin password is:

```text
123456
```

---

This is a:

```text
Vulnerability
```

---

Because an attacker can exploit it.

---

# Another Example

An outdated version of a software:

```text
Outdated Software
```

---

might have a known vulnerability.

---

In this case:

```text
Outdated version = Vulnerability
```

---

# Threat Without Vulnerability

Suppose:

```text
An attacker exists
```

But the system has no weakness.

---

In this case:

```text
Threat Exists
```

But the probability of a successful attack is low.

---

# Vulnerability Without Threat

Suppose:

```text
The system is offline
and no attacker exists.
```

---

In this case:

```text
Vulnerability Exists
```

But there is no active threat.

---

# What Is Risk?

Risk is created when:

```text
Threat
+
Vulnerability
```

are combined.

---

A simple formula:

```text
Risk = Threat + Vulnerability
```

---

# Example

Asset:

```text
The company's website
```

---

Threat:

```text
An Internet attacker
```

---

Vulnerability:

```text
A weak password
```

---

Result:

```text
Risk
```

---

Because the attacker can exploit the existing weakness.

---

# A Real-World Example

Asset:

```text
Database Server
```

---

Threat:

```text
Ransomware
```

---

Vulnerability:

```text
Missing security patches
```

---

Result:

```text
Risk of Compromise
```

---

# Severity of Risk

Not all risks are the same.

---

Two important factors:

```text
Likelihood
Impact
```

---

# Likelihood

The probability of an incident occurring.

---

Example:

```text
Weak Password
```

has a high likelihood of being exploited.

---

# Impact

The severity of the damage.

---

Example:

Leaking banking information:

```text
High Impact
```

---

# A Comparison Example

## First Risk

Threat:

```text
Script Kiddie
```

---

Vulnerability:

```text
Password = admin
```

---

Likelihood:

```text
High
```

---

Impact:

```text
Medium
```

---

## Second Risk

Threat:

```text
Nation State Actor
```

---

Vulnerability:

```text
Zero-Day Vulnerability
```

---

Likelihood:

```text
Medium
```

---

Impact:

```text
Very High
```

---

# Reducing Risk

The goal of security is:

```text
Not eliminating all risks
```

---

Because that is almost impossible.

---

The goal is:

```text
Risk Reduction
```

---

# Methods for Reducing Risk

Examples:

- Installing patches
- Using MFA
- Backup
- Restricting access
- Monitoring
- Training users

---

# A Practical Example

Password:

```text
123456
```

---

Threat:

```text
Brute Force Attack
```

---

Vulnerability:

```text
Weak Password
```

---

Solution:

```text
Strong Password
+
MFA
```

---

As a result:

```text
Risk ↓
```

is reduced.

---

# Connection to the Port Scanner

When we find an open port in the Port Scanner:

```text
Open Port
```

---

this by itself is not a Vulnerability.

---

But it can be a sign of:

```text
Attack Surface
```

---

Then we must check:

```text
Is the service vulnerable?
```

---

# Connection to DNS Lookup

In DNS Lookup, too, we might find information that helps an attacker.

---

Example:

```text
TXT Records
```

---

Or:

```text
Internal Hostnames
```

---

This information is not directly a vulnerability.

But it can be useful in the later stages of an attack.

---

# A Common Mistake

Many people say:

```text
Open Port = Vulnerability
```

---

This is not always true.

---

Or:

```text
Threat = Risk
```

---

which is also wrong.

---

Remember the difference:

```text
Threat
=
The threatening factor

Vulnerability
=
The weakness

Risk
=
The probability of damage caused by exploitation
```

---

# Summary

In this lesson, we learned:

- What a Threat is
- What a Vulnerability is
- What Risk is
- The relationship between these three concepts
- How risk is created
- How risk is reduced
- How these concepts relate to our security tools

---

# Next Lesson

In the next lesson, we enter one of the most important concepts of offensive and defensive security:

```text
Attack Surface
```

And we will learn:

- What Attack Surface is
- How it is identified
- Why attackers examine it first
- What role tools like Port Scanner and DNS Lookup play in discovering it

