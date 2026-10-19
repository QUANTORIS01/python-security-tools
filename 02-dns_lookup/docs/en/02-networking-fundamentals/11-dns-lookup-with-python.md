[🇮🇷 فارسی](/02-dns_lookup/docs/fa/02-networking-fundamentals/11-dns-lookup-with-python.md)

# Lesson 11: DNS Lookup with Python

## Introduction

So far, we have learned all the DNS concepts we need:

- What DNS is
- What a Domain is
- How a DNS Query is performed
- What DNS Records are
- What a Recursive Resolver is
- What Public DNS Providers are

Now it is time to move into the practical part.

In this lesson, we will learn how to perform a real DNS Query with Python.

This is exactly the knowledge we have used to build the tool:

```text
DNS Lookup Tool
```

---

# Why Is Python Suitable for DNS?

Python has several libraries for working with DNS.

The most famous one is:

```text
dnspython
```

---

This library enables:

- Sending DNS Queries
- Receiving answers
- Working with different Records
- Handling DNS errors

---

# Installing dnspython

In a virtual environment:

```bash
pip install dnspython
```

---

Then we can import it:

```python
import dns.resolver
```

---

# The First DNS Query

Example:

```python
import dns.resolver

answers = dns.resolver.resolve(
    "google.com",
    "A",
)
```

---

In this example:

```text
google.com
```

is the target domain.

---

And:

```text
A
```

is the type of record we want.

---

# Reading the Answer

The answer is a list of Answers.

---

To display it:

```python
for answer in answers:
    print(answer)
```

---

Sample output:

```text
216.239.38.120
```

---

Or:

```text
142.250.185.14
```

---

Depending on the time and geographic location, the IP might differ.

---

# Retrieving an AAAA Record

Example:

```python
answers = dns.resolver.resolve(
    "google.com",
    "AAAA",
)
```

---

Output:

```text
2001:4860:4802:32::78
```

---

This is an IPv6 address.

---

# Retrieving an MX Record

Example:

```python
answers = dns.resolver.resolve(
    "google.com",
    "MX",
)
```

---

Display:

```python
for answer in answers:
    print(answer)
```

---

Sample output:

```text
10 smtp.google.com.
```

---

Or several different records.

---

# Retrieving an NS Record

Example:

```python
answers = dns.resolver.resolve(
    "google.com",
    "NS",
)
```

---

Sample output:

```text
ns1.google.com.
ns2.google.com.
ns3.google.com.
```

---

These are the domain's Authoritative Name Servers.

---

# Retrieving a TXT Record

Example:

```python
answers = dns.resolver.resolve(
    "google.com",
    "TXT",
)
```

---

The output might include:

```text
SPF
Site Verification
Security Records
```

---

# Converting Answers to Strings

In our project, we used:

```python
[str(answer) for answer in answers]
```

---

Example:

```python
records = [
    str(answer)
    for answer in answers
]
```

---

Output:

```python
[
    "216.239.38.120"
]
```

---

This is exactly what we did in the file:

```text
resolver.py
```

---

# The `lookup_record` Function

In the project:

```python
def lookup_record(
    domain,
    record_type,
):
```

---

Its task is to perform:

```text
DNS Query
↓
Process Results
↓
Return List[str]
```

---

Example:

```python
lookup_record(
    "google.com",
    "A",
)
```

---

Output:

```python
[
    "216.239.38.120"
]
```

---

# Error Handling

A Query is not always successful.

---

Example:

```python
dns.resolver.resolve(
    "fake-domain.xyz",
    "A",
)
```

---

might raise:

```python
dns.resolver.NXDOMAIN
```

---

Therefore:

```python
try:
    ...
except:
    ...
```

is essential.

---

# Handling NXDOMAIN

Example:

```python
try:
    answers = dns.resolver.resolve(
        domain,
        record_type,
    )
except dns.resolver.NXDOMAIN:
    return []
```

---

# Handling NoAnswer

Example:

```python
except dns.resolver.NoAnswer:
    return []
```

---

This case occurs when:

```text
The domain exists
but the requested record does not exist.
```

---

# Handling Timeout

Example:

```python
except dns.resolver.LifetimeTimeout:
    return []
```

---

This is exactly the problem we observed when manually testing the project.

---

# Professional Design

In real tools:

```text
Exception
↓
Logging
↓
Graceful Handling
```

is performed.

---

Not letting the program crash.

---

That is why our project returns:

```python
[]
```

---

And then:

```text
No DNS records found.
```

is displayed.

---

# Connection to `build_dns_results`

In the project:

```python
lookup_record()
```

returns only the raw data.

---

Then:

```python
build_dns_results()
```

converts that data into:

```python
DNSRecord
```

---

Example:

```python
DNSRecord(
    domain="google.com",
    record_type="A",
    value="216.239.38.120",
)
```

---

This is the same multi-layered architecture we used in the Port Scanner.

---

# Connection to the CLI

The user runs:

```bash
python -m src.cli google.com A
```

---

Then:

```text
CLI
 ↓
build_dns_results()
 ↓
lookup_record()
 ↓
dnspython
 ↓
DNS Resolver
```

---

And the final answer is displayed to the user.

---

# Summary

In this lesson, we learned:

- What `dnspython` is
- How to perform a DNS Query
- How to read an A Record
- How to read an AAAA Record
- How to read an MX Record
- How to read an NS Record
- How to read a TXT Record
- How to handle errors
- How the DNS Lookup project uses `dnspython`

---

# End of the Second Chapter

With the end of this lesson, the chapter:

```text
Networking Fundamentals
```

comes to an end.

In this chapter, we learned:

- How the Internet works
- What an IP Address is
- What a Domain and FQDN are
- What DNS is
- What DNS Records are
- How a DNS Query is performed
- What DNS Cache is
- What a Recursive Resolver is
- What DNS Providers are
- How DNS Lookup is implemented in Python

---

# Next Chapter

In the next chapter, we enter:

```text
Cybersecurity Fundamentals
```

And we will become familiar with concepts used directly in security tools:

- CIA Triad
- Threats
- Vulnerabilities
- Reconnaissance
- Enumeration
- Attack Surface
- Defense in Depth
- Security Controls

And many of the fundamental concepts of the cybersecurity world.
