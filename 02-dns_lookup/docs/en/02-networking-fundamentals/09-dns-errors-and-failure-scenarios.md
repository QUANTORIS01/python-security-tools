[🇮🇷 فارسی](/02-dns_lookup/docs/fa/02-networking-fundamentals/09-dns-errors-and-failure-scenarios.md)

# Lesson 09: DNS Errors and Failure Scenarios

## Introduction

When we send a DNS Query, we are not always supposed to receive a successful answer.

In the real world, various problems can occur:

- The domain does not exist
- The requested record does not exist
- The DNS Server does not respond
- The network connection is lost
- The domain's Name Servers are broken

That is why DNS tools must be able to handle these conditions.

In the DNS Lookup project, too, we have done exactly this in the file:

```text
resolver.py
```

---

# DNS Success Response

The most successful case:

```text
google.com
→
216.239.38.120
```

---

In this case:

```python
answers = dns.resolver.resolve(
    "google.com",
    "A"
)
```

runs successfully.

---

The answer will be:

```python
[
    "216.239.38.120"
]
```

---

# NXDOMAIN

One of the most common DNS errors:

```text
NXDOMAIN
```

---

Short for:

```text
Non-Existent Domain
```

---

Meaning:

```text
This domain does not exist.
```

---

Example:

```text
this-domain-does-not-exist-12345.com
```

---

In this case:

```python
dns.resolver.NXDOMAIN
```

is raised.

---

In the project, we handled:

```python
except dns.resolver.NXDOMAIN:
```

---

# The Difference Between NXDOMAIN and NoAnswer

Many people confuse these two.

---

NXDOMAIN:

```text
The domain does not exist.
```

---

Example:

```text
fake-domain-xyz.com
```

---

But:

```text
NoAnswer
```

means:

```text
The domain exists
but that specific record does not exist.
```

---

Example:

```text
google.com
```

exists.

---

But:

```text
CNAME
```

it might not have.

---

In this case:

```python
dns.resolver.NoAnswer
```

is raised.

---

# NoAnswer

Example:

```python
dns.resolver.resolve(
    "google.com",
    "CNAME"
)
```

---

If no record exists:

```python
dns.resolver.NoAnswer
```

is raised.

---

In the project:

```python
except dns.resolver.NoAnswer:
```

is handled.

---

And the output:

```python
[]
```

is returned.

---

# Timeout

Sometimes the DNS Server does not respond.

---

Example:

```text
Network Problem
```

or:

```text
Server Overloaded
```

---

In this case, the Query waits for a while.

---

If no response is received:

```python
dns.resolver.LifetimeTimeout
```

is raised.

---

```text
The resolution lifetime expired
```

---

# Why Is Timeout Important?

If this error is not handled:

```text
The program crashes.
```

---

That is why in the project we added:

```python
except dns.resolver.LifetimeTimeout:
```

---

# NoNameservers

Sometimes the domain exists, but its Name Servers are not responding.

---

Example:

```text
Broken DNS Configuration
```

---

or:

```text
Name Servers Offline
```

---

In these conditions:

```python
dns.resolver.NoNameservers
```

is raised.

---

In the project, too, we handled this Exception.

---

# SERVFAIL

Another DNS response is:

```text
SERVFAIL
```

---

Meaning:

```text
Server Failure
```

---

Meaning the DNS Server tried to find the answer but failed.

---

Example:

```text
Resolver Error
```

or:

```text
Upstream Failure
```

---

Many Resolvers display this error in the form of:

```python
NoNameservers
```

or similar errors.

---

# REFUSED

Some DNS Servers refuse the request.

---

Example:

```text
Access Denied
```

---

In this case, the answer is:

```text
REFUSED
```

---

It is usually seen with private DNS Servers.

---

# DNS Failure Flow

A DNS Query can end in the following ways:

```text
DNS Query
    │
    ├── Success
    │
    ├── NXDOMAIN
    │
    ├── NoAnswer
    │
    ├── Timeout
    │
    ├── NoNameservers
    │
    └── SERVFAIL
```

---

# Error Handling in the Project

In the file:

```python
resolver.py
```

we wrote:

```python
except (
    dns.resolver.NXDOMAIN,
    dns.resolver.NoAnswer,
    dns.resolver.NoNameservers,
    dns.resolver.LifetimeTimeout,
):
    return []
```

---

Goal:

```text
Preventing the program from crashing
```

---

As a result:

```bash
python -m src.cli google.com MX
```

instead of showing a Traceback:

```text
No DNS records found.
```

is displayed.

---

# Why Is This Design Good?

Because:

- The program remains stable
- The user does not see Python's internal errors
- The user experience is better
- The tool behaves more professionally

---

# Connection to the Tests

For each error, we wrote a separate test:

```python
test_lookup_record_handles_nxdomain()
```

---

```python
test_lookup_record_handles_no_answer()
```

---

```python
test_lookup_record_handles_timeout()
```

---

These tests guarantee that the program behaves correctly even under error conditions.

---

# Summary

In this lesson, we learned:

- What NXDOMAIN is
- What NoAnswer is
- What Timeout is
- What NoNameservers is
- What SERVFAIL is
- What the difference between NXDOMAIN and NoAnswer is
- Why handling Exceptions matters
- How the DNS Lookup project handles these errors

