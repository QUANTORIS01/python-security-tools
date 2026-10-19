[🇮🇷 فارسی](/02-dns_lookup/docs/fa/02-networking-fundamentals/07-recursive-resolver-vs-authoritative-name-server.md)

# Lesson 07: Recursive Resolver vs Authoritative Name Server

## Introduction

So far, we have learned:

- What DNS is
- What a DNS Record is
- How a DNS Query is performed
- How Cache and TTL work

But one important question still remains:

```text
Who produces the final DNS answer?
```

And:

```text
Who finds that answer for us?
```

To answer this question, we need to become familiar with two very important concepts:

```text
Recursive Resolver
```

and

```text
Authoritative Name Server
```

---

# Who Performs the DNS Query?

Suppose the user types in the browser:

```text
google.com
```

The browser itself cannot directly search the entire DNS of the Internet.

Therefore, it sends the request to a DNS Resolver.

---

Example:

```text
Client
  ↓
8.8.8.8
```

---

In this example:

```text
8.8.8.8
```

is a Resolver.

---

# What Is a Recursive Resolver?

A Recursive Resolver is a system responsible for finding the DNS answer for the user.

---

Its task:

```text
Find the answer
and return it to the user
```

---

The user sends only one request:

```text
google.com
```

---

The Resolver itself performs all the subsequent steps.

---

# Why Is It Called "Recursive"?

Because the Resolver searches through the Internet step by step until it reaches the final answer.

---

Example:

```text
Client
 ↓
Resolver
 ↓
Root Server
 ↓
TLD Server
 ↓
Authoritative Server
 ↓
Answer
```

---

All these steps are performed by the Resolver.

---

The user only receives the final result.

---

# Examples of Recursive Resolvers

The most famous public Resolvers:

### Google DNS

```text
8.8.8.8
8.8.4.4
```

---

### Cloudflare DNS

```text
1.1.1.1
1.0.0.1
```

---

### Quad9

```text
9.9.9.9
```

---

### OpenDNS

```text
208.67.222.222
```

---

# What Is an Authoritative Name Server?

An Authoritative Server is the original source of a domain's DNS information.

---

If we want to know:

```text
google.com
```

what IP it has,

we must ultimately ask a server that owns the DNS information of that domain.

---

That server is called:

```text
Authoritative Name Server
```

---

# Example

Suppose the domain:

```text
example.com
```

exists.

---

Its Name Servers might be:

```text
ns1.example.com
ns2.example.com
```

---

These servers hold the actual records of the domain.

---

Example:

```text
example.com
→
93.184.216.34
```

---

This information is stored on the Authoritative Server.

---

# The Difference Between a Resolver and an Authoritative Server

Many people confuse these two.

---

Resolver:

```text
Searches for the answer.
```

---

Authoritative Server:

```text
Owns the answer.
```

---

In other words:

```text
Resolver = Finder
Authoritative = Source
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
8.8.8.8
```

begins searching.

---

It eventually reaches Google's Name Servers.

---

Those Name Servers say:

```text
google.com
=
216.239.38.120
```

---

Then the Resolver returns the answer to the user.

---

# The Role of Cache in the Resolver

Most Resolvers have a Cache.

---

Example:

```text
google.com
```

has been requested before.

---

The Resolver stores the answer.

---

On the next request:

```text
Without contacting the Internet
```

it returns the answer from the Cache.

---

This causes:

- Increased speed
- Reduced traffic
- Reduced DNS load

---

# Does an Authoritative Server Have a Cache?

It might have some internal caches.

But its main task is:

```text
Holding the original records
```

---

Unlike the Resolver, whose focus is on:

```text
Caching
```

---

# Connection to the DNS Lookup Project

In our project:

```python
dns.resolver.resolve(
    domain,
    record_type,
)
```

is used.

---

The library:

```text
dnspython
```

uses the system's Resolver behind the scenes.

---

The system Resolver might be:

- A local Resolver
- The ISP's Resolver
- Google DNS
- Cloudflare DNS

---

Our tool does not directly talk to the Authoritative Server.

---

Rather, it uses the existing Resolver.

---

# Why Is This Important?

Because when troubleshooting DNS, we need to know:

```text
Is the problem from the Resolver?
```

or

```text
Is the problem from the Authoritative Server?
```

---

These two scenarios are completely different.

---

# Summary

In this lesson, we learned:

- What a Recursive Resolver is
- What an Authoritative Name Server is
- What the difference between them is
- How the Resolver finds the answer
- How the Authoritative Server holds the answer
- What the role of Cache in the Resolver is
- Which part the DNS Lookup project uses

