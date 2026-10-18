[🇮🇷 فارسی](/01-port_scanner/docs/fa/03-cybersecurity/05-threat-modeling.md)

## Session 05: Threat Modeling

# Introduction

So far on our learning journey, we have become familiar with important concepts:

- What cybersecurity is
- Who attackers are
- What a vulnerability is
- How the security lifecycle works

But one important question still remains:

> How do we figure out what risks actually threaten our system?

A security specialist, before building a system or defending it, must first know:

- What is worth protecting?
- Who might attack?
- By what method might an attack be carried out?
- Which part is more vulnerable?

This process is called:

# Threat Modeling

or

# Threat Modeling

# What Is a Threat?

A Threat means:

> Anything that can harm a system.

Example:

- A hacker
- Malware
- A disgruntled employee
- Human error
- Data leakage
- Network attacks

All of these count as threats.

---

# Why Is Threat Modeling Important?

Suppose you want to build a house.

Before installing cameras and alarms, you need to know:

- Where are the doors?
- Where are the windows?
- Where are the burglar's entry points?

If you do not know these, you might spend a fortune on security in the wrong places.

The same applies to cybersecurity.

---

# The Goal of Threat Modeling

The goal of this process is to find the following:

1. Assets
2. Threats
3. Vulnerabilities
4. Mitigations

---

# What Is an Asset?

An Asset means:

> Anything that has value to us.

Example:

- User information
- Passwords
- Servers
- Databases
- Project code
- API keys

---

# A Real Example

Suppose we have an online store.

Important assets:

- Customer information
- Orders
- Payment gateway
- Database

Now we must ask:

"Who might attack these?"

---

# What Is an Actor?

An Actor means:

> A person or entity that interacts with the system.

It might be:

- A normal user
- A site administrator
- A hacker
- A bot

---

# Example

The store system:

Actors:

- Customer
- Administrator
- Courier
- Hacker

---

# What Is Data Flow?

Data Flow means:

> How information moves through the system.

Example:

User:

Login

↓

Server

↓

Database

↓

Response

If we do not know this path, we cannot find the threats.

---

# The First Step in Threat Modeling

Drawing the system.

Example:

```text
User
  |
  v
Web Server
  |
  v
Database
```

Now we can find the attack paths.

---

# What Is STRIDE?

Microsoft introduced one of the most famous Threat Modeling models.

Its name is:

STRIDE

---

# The Letter S

Spoofing

Meaning:

> Identity spoofing

Example:

A hacker impersonates the administrator.

---

# The Letter T

Tampering

Meaning:

> Data tampering

Example:

Altering order information.

---

# The Letter R

Repudiation

Meaning:

> Denying an action

Example:

A user has transferred money but later claims they did not do it.

---

# The Letter I

Information Disclosure

Meaning:

> Information disclosure

Example:

Leaking users' passwords.

---

# The Letter D

Denial of Service

Meaning:

> Taking down a service

Example:

DDoS attacks.

---

# The Letter E

Elevation of Privilege

Meaning:

> Privilege escalation

Example:

A normal user becomes an Administrator.

---

# An Example Applied to the Port Scanner Project

Our assets:

- Source code
- Output files
- Logs

---

Threats:

- Tampering with scan output
- Deleting logs
- Running malicious code
- Invalid inputs

---

Mitigations:

- Validating inputs
- Logging
- Error handling
- Restricting access

---

# Why Is Threat Modeling Done Before Coding?

A professional programmer first asks:

> What threats exist?

Then writes code.

A beginner programmer:

Writes code first

Then later realizes the security problems.

---

# A Common Mistake

Many people think:

Security = installing antivirus

While real security starts at the design stage.

---

# What Happens in Large Projects?

Before writing even a single line of code:

- The system is designed
- Assets are identified
- Threats are identified
- Risks are reviewed

Then development begins.

---

# Summary

In this session, we learned:

- What a Threat is
- What Threat Modeling is
- What an Asset is
- What an Actor is
- What Data Flow is
- What the STRIDE model is
- How to identify the threats to a system
- Why security must start at the design stage

---

# What Will We Learn in the Next Session?

In the sixth session, we enter one of the most important topics in security:

# Authentication and Authorization

We will learn:

- What is the difference between authentication and authorization
- How login works
- What is a Session
- What is a Token
- What is JWT
- Why many attacks start from the authentication section

These topics are used in almost all modern software.
