[🇮🇷 فارسی](/02-dns_lookup/docs/fa/02-networking-fundamentals/05-the-dns-query-process.md)

# Lesson 5: The DNS Query Process

## Introduction

So far, we have learned:

- What DNS is
- What a Domain is
- What an IP Address is
- What DNS Records are

But one important question still remains:

```text
When we type google.com into the browser,
what exactly happens?
```

---

# What Is a DNS Query?

A DNS Query is the request sent to find the information of a domain.

Example:

```text
google.com
```

---

Here, the system asks DNS:

```text
What is the IP Address for google.com?
```

---

This question is a:

```text
DNS Query
```

---

# The Goal of a DNS Query

Converting:

```text
Domain Name
```

into:

```text
IP Address
```

or other DNS records.

---

Example:

```text
google.com
```

↓

```text
216.239.38.120
```

---

# Who Sends the Query?

Usually:

- Browser
- Operating System
- Application
- Script

---

In our project:

```python
dns.resolver.resolve()
```

is the sender of the Query.

---

Example:

```python
dns.resolver.resolve(
    "google.com",
    "A"
)
```

---

# What Is a Resolver?

A Resolver is a software component that sends the Query.

---

The Resolver's task:

```text
Send the DNS question
Receive the answer
Return the result
```

---

In the project:

```python
lookup_record()
```

is built on the Resolver of the `dnspython` library.

---

# The Complete Path of a DNS Request

Suppose the user enters:

```text
google.com
```

---

Steps:

```text
Browser
    ↓
Operating System
    ↓
DNS Resolver
    ↓
DNS Server
    ↓
Answer
```

---

Then the IP is returned.

---

# DNS Cache

Before sending a new Query, the system checks the Cache.

---

If the answer is already stored:

```text
There is no need for a new Query
```

---

This increases speed.

---

# A Real Example

The user opens:

```text
google.com
```

---

The system first checks:

```text
Is the answer in the Cache?
```

---

If it exists:

```text
The IP is used directly
```

---

If it does not exist:

```text
A DNS Query is sent
```

---

# What Is a Recursive Query?

The most common type of Query.

---

In a Recursive Query:

The Resolver says:

```text
Find the final answer and return it to me
```

---

Example:

```text
What is the IP of google.com?
```

---

The Resolver expects to receive:

```text
The final answer
```

---

# Recursive Resolution

In this mode, the Resolver asks only one question.

The DNS Server does the rest of the work.

---

Diagram:

```text
Client
  ↓
Resolver
  ↓
DNS Infrastructure
  ↓
Final Answer
```

---

# What Is an Iterative Query?

In an Iterative Query, the final answer is not necessarily provided.

---

The Server might say:

```text
I do not know the answer,
ask this DNS Server.
```

---

Then the Resolver continues to the next step.

---

# The Difference Between Recursive and Iterative

Recursive:

```text
Find the final answer for me
```

---

Iterative:

```text
If you do not know,
tell me who to ask
```

---

# The Role of the Root DNS Server

When no information exists:

The Resolver starts from the Root Server.

---

The Root Server says:

```text
For .com,
refer to the TLD Server
```

---

# What Is a TLD Server?

TLD stands for:

```text
Top Level Domain
```

---

Example:

```text
.com
.net
.org
```

---

The TLD Server is responsible for these domains.

---

# Continuing the Path

For:

```text
google.com
```

the path is as follows:

```text
Root
 ↓
.com TLD
 ↓
Google Name Server
 ↓
Answer
```

---

# What Is an Authoritative DNS Server?

The final source of the answer.

---

This server owns the domain's actual information.

---

Example:

```text
ns1.google.com
```

---

The final answer is received from this server.

---

# The Complete Resolution Path

```text
Client
 ↓
Resolver
 ↓
Root Server
 ↓
TLD Server
 ↓
Authoritative DNS
 ↓
Answer
```

---

# A Real Example

The user requests:

```text
google.com
```

---

Resolver:

```text
What is the IP of google.com?
```

---

Root:

```text
Ask .com
```

---

TLD:

```text
Ask Google's DNS
```

---

Authoritative DNS:

```text
216.239.38.120
```

---

The answer is returned to the user.

---

# Connection to the Project

In the file:

```python
resolver.py
```

we have the following code:

```python
dns.resolver.resolve(
    domain,
    record_type,
)
```

---

The library:

```text
dnspython
```

performs all the Resolution steps for us.

---

We only send:

```python
google.com
```

and

```python
A
```

---

The Resolver:

- Builds the Query
- Finds the DNS Server
- Receives the answer
- Returns the result

---

# Why Does a Timeout Occur?

You have probably seen during testing:

```text
LifetimeTimeout
```

---

This means:

```text
The Resolver did not receive a response
within the specified time.
```

---

Common causes:

- DNS Server Down
- Firewall
- Network Issue
- Packet Loss
- Slow DNS Response

---

In the project, we handled this error:

```python
dns.resolver.LifetimeTimeout
```

---

# Summary

In this lesson, we learned:

- What a DNS Query is
- What a Resolver is
- What a Recursive Query is
- What an Iterative Query is
- What the Root DNS Server is
- What a TLD Server is
- What an Authoritative DNS Server is
- How the complete conversion of a Domain to an IP is performed
- How the `dnspython` library performs this process for us

---

# Next Lesson

In the next lesson, we enter one of the most important topics in DNS:

```text
DNS Caching & TTL
```

Meaning:

- What DNS Cache is
- What TTL is
- Why DNS is fast
- How Cache affects DNS performance
- How TTL relates to security and DNS management

