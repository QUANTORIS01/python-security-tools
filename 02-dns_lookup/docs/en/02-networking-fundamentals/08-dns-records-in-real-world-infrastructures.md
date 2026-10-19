[🇮🇷 فارسی](/02-dns_lookup/docs/fa/02-networking-fundamentals/08-dns-records-in-real-world-infrastructures.md)

# Lesson 08: DNS Records in Real-World Infrastructure

## Introduction

In lesson 04, we became familiar with the types of DNS records:

- A
- AAAA
- MX
- NS
- TXT
- CNAME

But knowing the definition of a Record is not enough.

There is an important question:

```text
How are these Records used in the real world?
```

In this lesson, we will see that almost every Internet service we use daily is built on top of these Records.

---

# The A Record in Websites

The most common use of DNS:

```text
Website Hosting
```

---

Suppose the domain:

```text
example.com
```

exists.

---

The DNS record:

```text
example.com
→
93.184.216.34
```

---

is stored as:

```text
A Record
```

---

When the browser opens:

```text
https://example.com
```

first a DNS Query is performed.

---

The answer:

```text
93.184.216.34
```

is returned.

---

Then the browser connects to that IP.

---

# The AAAA Record in Modern Services

Today, many services offer IPv6.

---

Example:

```text
google.com
```

---

It might return:

```text
2001:4860:4802:32::78
```

---

This information is stored in:

```text
AAAA Record
```

---

Companies such as:

- Google
- Cloudflare
- Microsoft
- Amazon

use IPv6 extensively.

---

# The MX Record and the Email System

Suppose a user sends an email to:

```text
user@example.com
```

---

The Mail Server needs to know where to deliver the email.

---

First, a DNS Query is performed for:

```text
MX Record
```

---

Example:

```text
example.com
```

---

Answer:

```text
10 mail1.example.com
20 mail2.example.com
```

---

Then the email is sent to the appropriate Mail Server.

---

# Priority in the MX Record

The first number is:

```text
Priority
```

---

Example:

```text
10 mail1.example.com
20 mail2.example.com
```

---

The server with the lower number has:

```text
Higher priority
```

---

If the first server is not available:

```text
mail2.example.com
```

is used.

---

# The NS Record and DNS Management

Every domain must specify:

```text
Which servers are responsible for its DNS?
```

---

Example:

```text
example.com
```

---

It might return:

```text
ns1.example.com
ns2.example.com
```

---

This information is stored in:

```text
NS Record
```

---

Without an NS Record:

```text
DNS Resolution
```

is not possible.

---

# The TXT Record in Email Security

TXT is one of the most important Records today.

---

In the past, it held:

```text
Only plain text
```

---

Today:

```text
SPF
DKIM
DMARC
```

are built on top of the TXT Record.

---

# SPF

SPF specifies:

```text
Which servers
are allowed to send email.
```

---

Example:

```text
v=spf1 include:_spf.google.com ~all
```

---

This record is stored inside:

```text
TXT Record
```

---

# DKIM

DKIM is used for digital signatures of emails.

---

The public key is usually placed in:

```text
TXT Record
```

---

Goal:

```text
Preventing email spoofing
```

---

# DMARC

DMARC defines email security policies.

---

Example:

```text
v=DMARC1; p=reject;
```

---

This record is also of type:

```text
TXT
```

---

# Domain Verification

Many cloud services use TXT.

---

Example:

- Google Workspace
- Microsoft 365
- GitHub
- Cloudflare

---

For proving domain ownership.

---

Example:

```text
google-site-verification=
```

---

# The CNAME Record and CDNs

One of the most common uses of CNAME:

```text
CDN
```

---

Suppose:

```text
www.example.com
```

---

points to:

```text
cdn.provider.net
```

---

This connection is done through:

```text
CNAME
```

---

# The Advantage of CNAME

Instead of directly holding an IP:

```text
Alias
```

is created.

---

If the IP changes:

```text
Only the main destination changes.
```

---

There is no need to change all the records.

---

# A Cloudflare Example

Many domains connect:

```text
www.example.com
```

to:

```text
example.cloudflare.net
```

---

This connection is done with:

```text
CNAME
```

---

# Records Used in Our Project

The DNS Lookup tool supports these Records:

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

Each Record has its own real-world use:

| Record | Use |
|----------|----------|
| A | Websites |
| AAAA | IPv6 |
| MX | Email |
| NS | DNS Management |
| TXT | SPF / DKIM / DMARC |
| CNAME | CDN and Alias |

---

# Connection to the Project

When the user runs:

```bash
python -m src.cli google.com A
```

---

the project runs:

```python
lookup_record(
    "google.com",
    "A"
)
```

---

The same logic is used for:

```text
AAAA
MX
NS
TXT
CNAME
```

---

As a result, the user can examine the DNS infrastructure of a domain.

---

# Summary

In this lesson, we learned:

- How the A Record is used in websites
- What the AAAA Record is used for
- How the MX Record routes email
- What role the NS Record plays in DNS
- How the TXT Record is used in SPF and DKIM
- How CNAME supports CDNs
- How these Records relate to the DNS Lookup tool

