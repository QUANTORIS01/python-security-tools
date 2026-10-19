[🇮🇷 فارسی](/02-dns_lookup/docs/fa/02-networking-fundamentals/06-dns-caching-and-ttl.md)

# Lesson 6: DNS Caching & TTL

## Introduction

In the previous lesson, we saw that several DNS Servers might be involved in converting a domain to an IP:

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

If this process were repeated for every request:

```text
DNS would become very slow.
```

To solve this problem, the following is used:

```text
DNS Cache
```

---

# What Is DNS Cache?

The Cache is a local place to temporarily store DNS responses.

---

Instead of resolving:

```text
google.com
```

again every time,

the previous response is stored.

---

Example:

```text
google.com
→
216.239.38.120
```

---

This result is placed in the Cache.

---

On the next request for:

```text
google.com
```

the system uses the Cache directly.

---

# Advantages of DNS Cache

### Greater Speed

Without needing a new Query:

```text
The response is received instantly.
```

---

### Reduced DNS Traffic

The number of outgoing requests is reduced.

---

### Reduced Load on DNS Servers

DNS Infrastructure endures less pressure.

---

### Improved Application Performance

Websites open faster.

---

# Where Does Cache Exist?

Cache is not in just one place.

---

It might exist in:

### Browser

```text
Chrome
Firefox
Edge
```

---

### Operating System

```text
Windows
Linux
macOS
```

---

### Local DNS Resolver

---

### ISP DNS Server

---

### Enterprise DNS Server

---

# A Real Example

The user enters:

```text
google.com
```

---

For the first time:

```text
DNS Query
```

is sent.

---

Answer:

```text
216.239.38.120
```

---

It is stored in the Cache.

---

A few seconds later:

```text
google.com
```

is requested again.

---

The system returns the answer directly from the Cache.

---

Without any new Query.

---

# What Is the Problem with Cache?

DNS information might change.

---

Example:

```text
google.com
```

Today:

```text
216.239.38.120
```

---

Tomorrow:

```text
216.239.38.121
```

---

If the Cache always remained:

```text
Old information would be used.
```

---

To solve this problem, the following is used:

```text
TTL
```

---

# What Is TTL?

TTL stands for:

```text
Time To Live
```

---

TTL specifies:

```text
How many seconds a DNS record
remains in the Cache.
```

---

Example:

```text
TTL = 300
```

---

Meaning:

```text
5 minutes
```

---

After 5 minutes:

The Cache is removed.

---

And a new Query will be sent.

---

# TTL Example

Suppose:

```text
google.com
```

has:

```text
TTL = 300
```

---

The first request:

```text
12:00
```

---

The record is stored in the Cache.

---

Until:

```text
12:05
```

---

The answer is used from the Cache.

---

After that:

```text
A new DNS Query
```

will be sent.

---

# High TTL

Example:

```text
86400
```

---

Meaning:

```text
24 hours
```

---

Advantages:

- Greater speed
- Fewer Queries
- Reduced DNS load

---

Disadvantages:

- DNS changes are applied more slowly

---

# Low TTL

Example:

```text
60
```

---

Meaning:

```text
1 minute
```

---

Advantages:

- Changes are propagated faster

---

Disadvantages:

- More Queries
- Greater load on DNS

---

# Viewing TTL

DNS tools usually display TTL.

---

Example:

```text
google.com

A Record

216.239.38.120

TTL: 300
```

---

# Why Is TTL Important?

Suppose you are the administrator of a website.

---

You want to change the server.

---

Before the change:

```text
You reduce the TTL.
```

---

Example:

```text
86400
↓
300
```

---

Then you register the new IP.

---

This way, changes are propagated faster across the Internet.

---

# How TTL Relates to Security

TTL is not just a performance issue.

---

In certain attacks:

```text
DNS Poisoning
```

or:

```text
Cache Poisoning
```

TTL becomes very important.

---

Because malicious responses might be stored in the Cache.

---

TTL specifies:

```text
How long this data
remains.
```

---

# What Is DNS Cache Poisoning?

The attacker tries to inject:

```text
A fake DNS response
```

into the Cache.

---

Example:

The user requests:

```text
bank.com
```

---

But the Cache has been poisoned.

---

As a result:

```text
A fake IP
```

is returned.

---

And the user enters a fake website.

---

# The Role of TTL in Cache Poisoning

If the TTL is large:

```text
The malicious data
remains longer.
```

---

If the TTL is short:

```text
It is removed more quickly.
```

---

Of course, TTL alone does not prevent the attack.

---

# Connection to the DNS Lookup Project

In the current version of the project:

```python
dns.resolver.resolve()
```

we only retrieve the record value.

---

For now:

```text
We do not display the TTL.
```

---

But in more advanced versions, we could also extract:

- TTL
- Authority
- Nameserver
- Additional Records

---

# Why Is This Lesson Important?

Because in the real world:

```text
A large part of DNS speed
depends on Cache.
```

---

And many DNS problems are also:

```text
Related to Cache and TTL.
```

---

# Summary

In this lesson, we learned:

- What DNS Cache is
- Why Cache exists
- What TTL is
- How TTL works
- The difference between high and low TTL
- The role of TTL in DNS management- How Cache relates to security
- What DNS Cache Poisoning is
- How these concepts relate to the DNS Lookup project

---

# Next Lesson

In the next lesson, we enter one of the most important technical parts of DNS:

```text
Recursive Resolver vs Authoritative Server
```

- What a Recursive Resolver is
- What an Authoritative Name Server is
- Which paths a DNS request passes through
- What Google DNS is
- What Cloudflare DNS is
- What ISP DNS is

