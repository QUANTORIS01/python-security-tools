[🇮🇷 فارسی](/02-dns_lookup/docs/fa/02-networking-fundamentals/03-domain-subdomain-and-fqdn.md)

# Lesson 3: Domain, Subdomain, and FQDN

## Introduction

In the previous lesson, we became familiar with IP Addresses.

But humans are not comfortable memorizing addresses like:

```text
142.250.186.14
```

That is why we use human-readable names:

```text
google.com
github.com
python.org
```

These names are converted to IPs by DNS.

To understand DNS better, we must first become familiar with the structure of domain names.

---

# What Is a Domain?

A Domain Name is a human-readable name that points to one or more IPs.

Example:

```text
google.com
```

When we enter this name:

```text
google.com
```

DNS converts it to an IP.

Example:

```text
216.239.38.120
```

---

## Why Was the Domain Invented?

Imagine having to memorize the addresses of all the websites in the world in IP form:

```text
142.250.186.14
151.101.193.140
140.82.121.3
```

It is almost impossible.

Domains allow users to use meaningful names instead of IPs.

---

# The Structure of a Domain

Example:

```text
google.com
```

This name consists of two parts:

```text
google
com
```

---

## Top-Level Domain (TLD)

The last part of the domain:

```text
.com
```

is called:

```text
Top-Level Domain
```

or, for short:

```text
TLD
```

---

### Examples of TLDs

```text
.com
.org
.net
.edu
.gov
```

---

### Country TLDs

Each country also has its own TLD.

Example:

```text
.ir
.uk
.de
.fr
.jp
```

---

Example:

```text
google.ir
bbc.co.uk
```

---

# Second-Level Domain

In the domain:

```text
google.com
```

the part:

```text
google
```

is called the Second-Level Domain.

---

Example:

```text
python.org
```

Here:

```text
python
```

is the main domain name.

---

# What Is a Subdomain?

Sub-divisions can be defined for a domain.

Example:

```text
mail.google.com
```

Here:

```text
mail
```

is a Subdomain.

---

Structure:

```text
mail.google.com
│
├── Subdomain
├── Domain
└── TLD
```

---

## Common Examples of Subdomains

### Mail Server

```text
mail.google.com
```

---

### API Server

```text
api.example.com
```

---

### Documentation

```text
docs.python.org
```

---

### Blog

```text
blog.example.com
```

---

## Does a Subdomain Have a Limit?

No.

Several levels of subdomains can exist.

Example:

```text
dev.api.example.com
```

---

Structure:

```text
dev
api
example
com
```

---

# What Is the Root Domain?

At the top of DNS, there is something called:

```text
Root Domain
```

which is represented by:

```text
.
```

In fact:

```text
google.com.
```

is the full form of the domain.

But the trailing dot is usually not written.

---

# What Is FQDN?

Short for:

```text
Fully Qualified Domain Name
```

Meaning the complete and exact domain name.

Example:

```text
mail.google.com.
```

This is considered an FQDN.

---

## The Difference Between Domain and FQDN

Domain:

```text
google.com
```

---

FQDN:

```text
mail.google.com.
```

---

FQDN specifies the complete path from the Root DNS.

---

# The DNS Hierarchy

The DNS structure is like a large tree.

Example:

```text
.
│
└── com
     │
     └── google
             │
             └── mail
```

---

For the domain:

```text
mail.google.com
```

the path is as follows:

```text
Root
↓
com
↓
google
↓
mail
```

---

# Connection to DNS Lookup

In our project:

```bash
python -m src.cli google.com A
```

Input:

```text
google.com
```

is a Domain.

---

Another example:

```bash
python -m src.cli docs.python.org AAAA
```

Here:

```text
docs
```

is a Subdomain.

---

And:

```text
python.org
```

is considered the main domain.

---

# Domain Validation in the Project

In the file:

```text
validator.py
```

we wrote a function:

```python
validate_domain()
```

which checks:

- The domain structure is valid
- There are no illegal characters
- The overall format is correct

---

Valid examples:

```text
google.com
```

```text
docs.python.org
```

```text
mail.yahoo.com
```

---

Invalid examples:

```text
google
```

```text
.com
```

```text
!!!.com
```

```text
google..com
```

---

# Domains and DNS Records

Each domain can have different records.

Example:

```text
google.com
```

might have:

```text
A
AAAA
MX
TXT
NS
```

---

In fact, what DNS Lookup does is:

```text
Domain
↓
DNS Query
↓
Record Type
↓
Result
```

---

Example:

```text
google.com
↓
MX
↓
Mail Servers
```

---

Or:

```text
google.com
↓
A
↓
IPv4 Address
```

---

# Summary

In this lesson, we learned:

- What a Domain is
- What TLD is
- What Second-Level Domain is
- What Subdomain is
- What Root Domain is
- What FQDN is
- How the DNS hierarchical structure works
- How these concepts relate to the DNS Lookup project

---

# Next Lesson

In the next lesson, we enter the actual core of DNS and learn:

- What a DNS Record is
- Types of DNS records
- A, AAAA, MX, NS, TXT, and CNAME records
- What each record is used for

This lesson is directly related to the features of the DNS Lookup tool.
