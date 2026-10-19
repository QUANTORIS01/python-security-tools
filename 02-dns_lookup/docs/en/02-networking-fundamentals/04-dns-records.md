[🇮🇷 فارسی](/02-dns_lookup/docs/fa/02-networking-fundamentals/04-dns-records.md)

# Lesson 4: DNS Records

## Introduction

So far, we have learned that DNS is responsible for converting a domain name into usable information.

But DNS is not only for finding the IP of a website.

Each domain can store various types of information in DNS.

This information is stored in the form of:

```text
DNS Records
```

---

# What Is a DNS Record?

A DNS Record is a piece of information stored on a DNS Server.

Each record holds a particular type of information.

Example:

```text
google.com
```

might have the following records:

```text
A
AAAA
MX
NS
TXT
CNAME
```

Each one has a different purpose.

---

# The General Structure of a DNS Record

In simple terms:

```text
NAME    TYPE    VALUE
```

Example:

```text
google.com    A      216.239.38.120
```

---

Here:

```text
NAME
```

is the domain.

---

```text
TYPE
```

is the record type.

---

```text
VALUE
```

is the record value.

---

# The A Record

The most common DNS record.

A stands for:

```text
Address
```

This record maps a domain to an IPv4 Address.

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

Record display:

```text
google.com    A    216.239.38.120
```

---

In our project:

```bash
python -m src.cli google.com A
```

we are requesting exactly this record.

---

# The AAAA Record

This record is similar to A.

But it is used for IPv6.

---

Example:

```text
google.com
```

↓

```text
2001:4860:4802:32::78
```

---

Display:

```text
google.com    AAAA    2001:4860:4802:32::78
```

---

In the project:

```bash
python -m src.cli google.com AAAA
```

---

# The Difference Between A and AAAA

A:

```text
IPv4
```

Example:

```text
8.8.8.8
```

---

AAAA:

```text
IPv6
```

Example:

```text
2001:4860:4860::8888
```

---

# The MX Record

MX stands for:

```text
Mail Exchange
```

---

This record specifies which Mail Server a domain's emails should be sent to.

---

Example:

```text
google.com
```

↓

```text
smtp.google.com
```

---

Real example:

```text
gmail.com MX alt1.gmail-smtp-in.l.google.com
```

---

Purpose:

```text
Email Delivery
```

---

In the project:

```bash
python -m src.cli google.com MX
```

---

# Priority in the MX Record

MX records usually have priorities.

Example:

```text
10 mail1.example.com
20 mail2.example.com
```

---

Lower number:

```text
Higher priority
```

---

Therefore:

```text
10
```

is used before:

```text
20
```

---

# The NS Record

NS stands for:

```text
Name Server
```

---

This record specifies which DNS Servers are responsible for answering for the domain.

---

Example:

```text
google.com
```

↓

```text
ns1.google.com
ns2.google.com
```

---

Display:

```text
google.com NS ns1.google.com
```

---

Purpose:

```text
Delegation
```

and managing the domain's DNS.

---

In the project:

```bash
python -m src.cli google.com NS
```

---

# The TXT Record

TXT is used to store arbitrary text.

---

Example:

```text
google.com TXT "verification-code"
```

---

Today it has important uses:

---

## SPF

Preventing email spoofing

---

Example:

```text
v=spf1 include:_spf.google.com ~all
```

---

## DKIM

Validating email signatures

---

## Domain Verification

Proving domain ownership

---

Example:

```text
google-site-verification=abc123
```

---

In the project:

```bash
python -m src.cli google.com TXT
```

---

# The CNAME Record

CNAME stands for:

```text
Canonical Name
```

---

It is used to create an Alias.

---

Example:

```text
www.example.com
```

↓

```text
example.com
```

---

Display:

```text
www.example.com CNAME example.com
```

---

Meaning:

```text
www.example.com
```

is an alias for:

```text
example.com
```

---

In the project:

```bash
python -m src.cli www.example.com CNAME
```

---

# Why Is CNAME Important?

Suppose the site's main IP changes.

If a CNAME is used:

```text
www.example.com
```

automatically follows the new destination.

---

# Comparing the Records

| Record | Purpose |
|----------|----------|
| A | IPv4 Address |
| AAAA | IPv6 Address |
| MX | Mail Server |
| NS | Name Server |
| TXT | Text Information |
| CNAME | Alias |

---

# Direct Connection to the Project

In the file:

```python
validator.py
```

we defined the allowed records:

```python
SUPPORTED_RECORD_TYPES
```

---

Values:

```python
{
    "A",
    "AAAA",
    "MX",
    "NS",
    "TXT",
    "CNAME",
}
```

---

The function:

```python
validate_record_type()
```

checks that only these records are accepted.

---

In the file:

```python
resolver.py
```

the record type is sent directly to the DNS Resolver:

```python
lookup_record(
    domain,
    record_type,
)
```

---

Therefore:

```bash
python -m src.cli google.com MX
```

and

```bash
python -m src.cli google.com A
```

in fact send two completely different queries to DNS.

---

# Why Do Some Queries Return No Results?

You have probably seen during testing:

```bash
python -m src.cli google.com MX
```

Sometimes:

```text
No DNS records found.
```

is displayed.

---

The cause might be one of the following:

- Timeout
- DNS Server Failure
- No Answer
- Resolver Misconfiguration
- Network Issues

---

In the project, we handled these cases in:

```python
resolver.py
```

---

# Summary

In this lesson, we learned:

- What a DNS Record is
- What the A record is
- What the AAAA record is
- What the MX record is
- What the NS record is
- What the TXT record is
- What the CNAME record is
- What each record is used for
- How these records are used in the DNS Lookup project

---

# Next Lesson

In the next lesson, we will learn:

- What a DNS Query is
- Recursive Query
- Iterative Query
- How the Resolver works
- The complete path of a DNS request from the browser to the DNS Server

This lesson is one of the most important parts of Networking Fundamentals.
