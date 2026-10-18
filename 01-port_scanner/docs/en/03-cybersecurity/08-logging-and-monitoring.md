[🇮🇷 فارسی](/01-port_scanner/docs/fa/03-cybersecurity/08-logging-and-monitoring.md)

# Session 08 — Logging and Monitoring

# Introduction

So far on our learning journey, we have become familiar with important security topics:

- What cybersecurity is
- Who attackers are
- What a vulnerability is
- The security lifecycle
- Threat modeling
- Authentication and authorization
- Injection attacks
- Input validation

But one important question remains:

> If an attack occurs, how do we find out?

Or even more importantly:

> After an attack occurs, how do we figure out what happened?

This is where Logging and Monitoring come into play.

---

# Suppose...

One morning you walk into the company.

The system administrator says:

> The server was hacked last night.

What is your first question?

Probably:

> What exactly happened?

But if no information was recorded:

Nobody knows the answer to this question.

---

# What Is Logging?

Logging means:

> Recording system events and occurrences

---

In simple terms:

Writing a history of events.

---

# A Real-World Example

Imagine a CCTV camera.

The camera:

Records the events.

---

A log does the same thing.

But for software and systems.

---

# A Simple Example

A user logs in to the system.

We record:

```text
2025-01-01 10:00:00
User admin logged in
```

---

The user logs out:

```text
2025-01-01 10:30:00
User admin logged out
```

---

This information will be very valuable later.

---

# Why Is Logging Important?

A few main reasons:

---

## 1. Finding Errors

Example:

The program has crashed.

If we have a log:

We can find the cause.

---

## 2. Finding Attacks

Example:

Thousands of failed logins have been recorded.

It might be a Brute Force attack.

---

## 3. Incident Analysis

Example:

A hacker has entered the system.

Logs show:

- Where they came from
- When they came
- What they did

---

## 4. Legal Accountability

In many organizations:

Recording events is mandatory.

---

# An Example of a Real Log

```text
2025-01-01 12:30:00
INFO User login success
```

---

```text
2025-01-01 12:31:00
WARNING Invalid password
```

---

```text
2025-01-01 12:32:00
ERROR Database connection failed
```

---

# Different Log Levels

Logs usually have several levels.

---

# DEBUG

Very detailed

For developers

---

Example:

```text
DEBUG Connecting to database
```

---

# INFO

Normal information

---

Example:

```text
INFO User logged in
```

---

# WARNING

An unusual event

But not critical

---

Example:

```text
WARNING Invalid login attempt
```

---

# ERROR

An important error

---

Example:

```text
ERROR Database unavailable
```

---

# CRITICAL

A critical error

---

Example:

```text
CRITICAL Server compromised
```

---

# Logging in the Port Scanner Project

We have already implemented the Logging feature.

---

Example:

```text
scan.log
```

---

When a scan is performed:

We can record information such as:

- The scan time
- The scan target
- The scan result

---

# Why Is This Feature Important?

If later we want to know:

When and what was scanned

We can refer to the logs.

---

# What Is Monitoring?

Monitoring means:

> Continuously observing and reviewing the state of the system

---

Logging:

Recording events

---

Monitoring:

Continuously reviewing events

---

# Example

Suppose the temperature of a car engine is recorded.

This is:

Logging

---

If the temperature is continuously checked and an alert is raised:

This is:

Monitoring

---

# The Difference Between Logging and Monitoring

Logging:

```text
Record Events
```

---

Monitoring:

```text
Watch Events
```

---

# An Example in Networking

Recording connections:

```text
Logging
```

---

Alerting on an attack:

```text
Monitoring
```

---

# What Is an Alert?

An Alert means:

> A security warning

---

Example:

If more than 1000 failed logins are recorded:

An alert is sent.

---

# An Example of an Alert

```text
High Failed Login Attempts
```

---

Or:

```text
Possible Brute Force Attack
```

---

# What Is SIEM?

One of the most important security concepts.

---

Short for:

```text
Security Information and Event Management
```

---

A system that:

- Collects logs
- Analyzes them
- Generates alerts

---

# Famous SIEM Examples

- Splunk
- QRadar
- ArcSight
- Elastic SIEM

---

# How Does SIEM Work?

Hundreds of servers produce logs.

↓

SIEM collects them all.

↓

It examines the patterns.

↓

It detects attacks.

↓

It raises alerts.

---

# A Real Example

If it is observed:

```text
500 Login Failed
```

in one minute

It may be detected as:

```text
Brute Force Attack
```

---

# Why Do Attackers Delete Logs?

Because logs are evidence.

---

After a breach:

Some attackers try to:

```text
Delete Logs
```

---

To erase their tracks.

---

# The Best Practice

Record logs on a separate server

---

Meaning:

If the main server is hacked

The logs are still safe.

---

# What Is Incident Detection?

Detecting a security incident

---

Goal:

Finding attacks as quickly as possible.

---

The sooner an attack is detected:

The less the damage will be.

---

# An Important Rule

In cybersecurity, they say:

> You cannot defend against what you cannot see.

---

That is why:

Logging and Monitoring are among the most important defensive tools.

---

# Summary

In this session, we learned:

- What Logging is
- Why logs are important
- The different log levels
- What Monitoring is
- The difference between Logging and Monitoring
- What an Alert is
- What SIEM is
- What Incident Detection is
- Why attackers delete logs
- The role of Logging in the Port Scanner project

---

# What Will We Learn in the Next Session?

In the ninth session, we enter one of the most fascinating security topics:

# Defense in Depth

or

# Layered Defense

We will learn:

- Why one layer of security is not enough
- What role a firewall plays
- What role antivirus plays
- What role authentication plays
- How large organizations design their security layer by layer

This concept is one of the most important principles of security architecture in the world.
