[🇮🇷 فارسی](/01-port_scanner/docs/fa/03-cybersecurity/09-defense-in-depth.md)

# Session 09 — Defense in Depth

# Introduction

So far on our learning journey, we have become familiar with important cybersecurity concepts:

- What cybersecurity is
- Who attackers are
- What a vulnerability is
- The security lifecycle
- Threat modeling
- Authentication and authorization
- Injection attacks
- Input validation
- Logging and Monitoring

But one important question still remains:

> What happens if one of the security mechanisms fails?

Does the system's security collapse?

Unfortunately, in many weak systems, the answer to this question is:

> Yes

But in professional systems, the answer is:

> No

Why?

Because they use a concept called:

# Defense in Depth

---

# What Is Defense in Depth?

Literal meaning:

```text
Defense in depth
```

Or:

```text
Layered defense
```

---

The idea is very simple:

> Security should not depend on only one layer.

---

# A Real-World Example

Imagine a bank.

To protect the money, there is not just one door.

---

Usually:

- Walls
- The main door
- A guard
- Cameras
- An access card
- A safe

all work together.

---

If one layer fails:

The next layers still exist.

---

This is Defense in Depth.

---

# A Common Mistake

Many people think:

```text
We have a firewall
so we are secure.
```

Or:

```text
We have antivirus
so we are secure.
```

---

Real security is not like that.

No security tool is perfect.

---

# An Important Principle

In cybersecurity, we assume:

> Every layer might fail someday.

Therefore, we must have multiple layers.

---

# A Real Example

Suppose we have a website.

---

First layer:

```text
Firewall
```

---

Second layer:

```text
Input Validation
```

---

Third layer:

```text
Authentication
```

---

Fourth layer:

```text
Authorization
```

---

Fifth layer:

```text
Logging
```

---

Sixth layer:

```text
Monitoring
```

---

If the attacker gets past one:

The other layers are still there.

---

# First Layer: Physical Security

Many people forget that security starts with the building.

---

Example:

- The lock on the server room door
- Cameras
- Access cards
- Guards

---

If an attacker can get physical access directly to the server:

Many defenses become useless.

---

# Second Layer: Network Security

Examples:

- Firewall
- IDS
- IPS
- VLAN
- Network Segmentation

---

Goal:

Limiting the attacker's access to the network.

---

# What Is a Firewall?

A firewall is like the network's guard.

---

Example:

```text
Allow:
80
443
```

---

```text
Block:
All Others
```

---

This means only the required ports are open.

---

# How It Relates to the Port Scanner

The port scanner was built for exactly this purpose.

---

With a Port Scanner, the attacker checks:

```text
Which ports are open?
```

---

The system administrator also uses a Port Scanner to:

```text
Find unnecessary ports.
```

---

# Third Layer: Operating System Security

Examples:

- Updates
- Patches
- Restricting user access
- Removing unnecessary services

---

Example:

If the old SSH service is vulnerable:

Updating it is considered a layer of defense.

---

# What Is a Patch?

A Patch means:

> Fixing a vulnerability or an error

---

Almost all software receives patches over time.

---

# Fourth Layer: Application Security

The items we learned earlier:

- Validation
- Authentication
- Authorization

---

All of them are part of application security.

---

# Example

In the Port Scanner:

```python
validate_ip(ip)
```

---

This is a layer of defense.

---

Why?

Because it does not allow any data to enter the system.

---

# Fifth Layer: Data Security

Sometimes an attacker manages to access the information.

---

Therefore, the data itself must also be protected.

---

Example:

```text
Encryption
```

---

# What Is Encryption?

Converting information into an unreadable form.

---

Example:

```text
Hello
```

↓

```text
k38d92ks8a91
```

---

Only authorized people can recover it.

---

# Sixth Layer: Monitoring and Recording Events

The same thing we learned in the previous session.

---

It includes:

- Logging
- Monitoring
- Alerting

---

Goal:

Detecting attacks

---

Even if an attacker manages to enter the system.

---

# An Attack Example

Suppose:

The firewall has failed.

---

But:

Logging is enabled.

---

A log is recorded:

```text
Suspicious Connection
```

---

Monitoring is enabled.

---

An alert is sent:

```text
Possible Intrusion Detected
```

---

The security team takes action.

---

# What Is Zero Trust?

One of the modern security concepts.

---

Its motto:

> Trust Nothing, Verify Everything

---

Meaning:

```text
Trust nothing
Verify everything
```

---

Even users inside the network must be authenticated.

---

# Why Is Defense in Depth Important?

Because:

No defense is perfect.

---

A firewall:

Might be misconfigured.

---

Antivirus:

Might not recognize new malware.

---

A user:

Might leak their password.

---

Therefore:

Multiple layers of defense are necessary.

---

# Defense in Depth in the Port Scanner

Our project also has several layers.

---

Input:

```text
Validation
```

---

Recording events:

```text
Logging
```

---

Error handling:

```text
Exception Handling
```

---

Displaying results:

```text
Formatting
```

---

All of them make the program more stable and more secure.

---

# The Big Mistake of Beginners

Many people think about only one layer.

For example:

```text
I have a strong password.
```

---

But:

- They have no logs
- They have no monitoring
- They have no access restrictions
- They have no firewall

---

As a result, the system is still vulnerable.

---

# Summary

In this session, we learned:

- What Defense in Depth is
- Why layered security is important
- The role of a Firewall
- The role of Patches
- The role of Validation
- The role of Encryption
- The role of Logging and Monitoring
- The concept of Zero Trust
- The application of Defense in Depth in the Port Scanner project

---

# What Will We Learn in the Next Session?

In the tenth and final session of the cybersecurity chapter, we will learn:

# Secure Development

or

# Secure Software Development

We will examine:

- How professional programmers write code
- What Secure Coding is
- What the most common security mistakes by programmers are
- How we developed the Port Scanner project professionally

This session will be the bridge between the security chapter and the final Port Scanner chapter.
