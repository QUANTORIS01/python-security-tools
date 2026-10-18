[🇮🇷 فارسی](/01-port_scanner/docs/fa/03-cybersecurity/04-security-lifecycle.md)

# Session 04 — Security Lifecycle

# Introduction

So far on this journey, we have become familiar with the basic concepts of cybersecurity step by step.

In the first session, we learned what cybersecurity is and why we even need it.

In the second session, we became familiar with threats, attackers, and types of attacks, and we learned that any system connected to a network can be a target.

In the third session, we learned the concept of the attack surface and understood that every extra service, port, or piece of software can become a path of entry for an attacker.

But one important question remains:

**If we secure our system today, will it stay secure forever?**

Answer:

**No.**

Security is not a destination.

Security is a continuous process.

A system that is secure today may become vulnerable tomorrow.

That is why, in the security world, a concept called:

**Security Lifecycle**

or

**The security lifecycle**

has emerged.

---

# Why Is Security a Continuous Process?

Suppose you set up a new server today.

- You install the operating system.
- You enable the firewall.
- You close unnecessary ports.
- You update the software.

At this moment, your security posture is good.

But a few weeks later:

- A new vulnerability is discovered.
- A piece of software releases a security update.
- A new service is installed.
- A new user is added to the system.

If these changes are not reviewed, the system gradually becomes insecure.

Therefore, security is not a one-time activity.

Security must be repeated continuously.

---

# What Is the Security Lifecycle?

The security lifecycle is a set of stages that are repeated continuously to maintain the security of a system.

Simply put:

```text
Identify
   ↓
Protect
   ↓
Monitor
   ↓
Detect
   ↓
Respond
   ↓
Recover
   ↓
Restart the cycle
```

This cycle never stops.

---

# Stage 1: Identify

The first step is to know what we have.

Many organizations do not even know which devices exist on their network.

Example:

```text
Web server
Database server
Router
Switch
CCTV camera
User computers
```

If you do not know something, you cannot protect it.

---

# The Role of the Port Scanner at This Stage

The project we have built is used exactly at this stage.

Example:

```bash
python -m src.cli 192.168.1.10 1 1000
```

Output:

```text
53     OPEN
80     OPEN
443    OPEN
```

Now we know which services are active on the system.

This is exactly the identification stage.

---

# Stage 2: Protect

After identification, we must protect the system.

Example:

- Enable the firewall
- Close unnecessary ports
- Use strong passwords
- Restrict access
- Encrypt data

Example:

If you realize port 21 is open but you do not use FTP:

```text
Port 21 → close it
```

---

# Stage 3: Monitor

We must keep the system under constant observation.

Because it is possible that:

- A new service starts running.
- A new user is added.
- An attacker makes a change.

Example:

Scan every day:

```bash
python -m src.cli 192.168.1.10 1 1000
```

If suddenly a new port opens:

```text
8080 OPEN
```

we must investigate the cause.

---

# Stage 4: Detect

At this stage, suspicious events are identified.

Example:

```text
Many failed logins
```

Or:

```text
An unexpected port opening
```

Or:

```text
A sudden increase in network traffic
```

Fast detection causes the attack to be discovered sooner.

---

# Stage 5: Respond

When an incident occurs, we must react.

Example:

Suppose an attacker has entered the system.

Actions:

```text
Disconnect the attacker
Disable the vulnerable service
Change passwords
Analyze logs
```

The goal of this stage is to prevent the damage from spreading.

---

# Stage 6: Recover

After the incident is contained, we must return the system to its normal state.

Example:

```text
Restore from backup
Reinstall the service
Apply the security patch
```

After recovery, the cycle starts again from the identification stage.

---

# A Real Example

Suppose you have a small company.

Day one:

```text
80 OPEN
443 OPEN
```

Everything is normal.

---

A month later:

```text
80 OPEN
443 OPEN
3306 OPEN
```

Port 3306 belongs to MySQL.

But you were not supposed to have the database directly exposed on the Internet.

During the monitoring stage, you notice this.

During the detection stage, you realize that a misconfiguration has occurred.

During the respond stage, you close the port.

During the recovery stage, you fix the configuration.

This is exactly the security lifecycle.

---

# How This Lesson Relates to the Port Scanner Project

The tool we have built is not just an educational project.

In the real world, it is also considered one of the first tools that security teams use for asset identification and discovering active services.

The port scanner is used in the following stages:

- Identify
- Monitor
- Detect

That is why learning this project is so important.

---

# Summary

In this session, we learned:

- Security is not a one-time activity.
- Security is a continuous process.
- The security lifecycle consists of six stages.
- Identification is the first stage of security.
- The Port Scanner project is part of the security lifecycle in the real world.
- Security teams repeat this cycle continuously.

---

# What Will We Learn in the Next Session?

In the next session, we enter one of the most important topics in cybersecurity:

# Threat Modeling

We will learn:

- What is a Threat?
- Why is Threat Modeling important?
- The goal of Threat Modeling
- What is an Asset?
- What is an Actor?
- How to identify the threats to a system

