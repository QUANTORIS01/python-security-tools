[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/src/06-results.md)

# Chapter Four: DNS Lookup Project Code Analysis

## Lesson 6: Building Structured Results in Python

### 1. Lesson Goal

In this lesson, we examine the `src/results.py` file; the part of the DNS Lookup tool that converts the raw responses received from the resolver into an orderly and usable structure for the rest of the program.

By the end of this lesson, you will become familiar with the following concepts:

- Using a function to combine the logic of several parts of the project
- Converting DNS response strings into `DNSRecord` model objects
- The use of List Comprehension
- The importance of data structure consistency in software architecture

### 2. The `results.py` File Code

```python
from src import DNSRecord, lookup_record


def build_dns_results(domain: str, record_type: str) -> list[DNSRecord]:
    """
    Build structured DNS results.
    """
    values = lookup_record(domain, record_type)
    return [
        DNSRecord(
            domain=domain,
            record_type=record_type,
            value=value,
        )
        for value in values
    ]
```

This file imports two names from the `src` package:

- `DNSRecord`: the data model we defined in the `models.py` file.
- `lookup_record`: the function that performs the DNS request in the `resolver.py` file and returns responses in string form.

In this way, `results.py` sits between executing the DNS request and building the structured output.

### 3. Executing the Request and Receiving Values

At the beginning of the function:

```python
values = lookup_record(domain, record_type)
```

The `lookup_record()` function performs the DNS request using the domain and record type.

According to the resolver implementation, successful responses are returned in the `list[str]` form. In states such as the domain not existing, the response not existing, or the name servers not being available, the resolver can return an empty list. The request timeout error is also propagated as `DNSTimeoutError`.

Therefore, `build_dns_results()` does not need to manage the details of executing the DNS request itself; this responsibility is in the resolver.

### 4. Converting Responses into `DNSRecord` Objects

The main part of the function:

```python
return [
    DNSRecord(
        domain=domain,
        record_type=record_type,
        value=value,
    )
    for value in values
]
```

This expression uses **List Comprehension** to build the list.

For each value in `values`, a `DNSRecord` object is created. Each object has three fields:

- `domain`: the domain for which the request was performed.
- `record_type`: the requested record type.
- `value`: one of the values received from the resolver.

For example, suppose the resolver returns the following two values:

```python
values = ["192.0.2.10", "192.0.2.11"]
```

The function produces a result equivalent to this list:

```python
[
    DNSRecord(
        domain="example.com",
        record_type="A",
        value="192.0.2.10",
    ),
    DNSRecord(
        domain="example.com",
        record_type="A",
        value="192.0.2.11",
    ),
]
```

These values are only educational samples; the goal is to show the shape of the output.

### 5. Why Do We Use a Data Model?

If responses were only passed as strings, to understand which domain and record type each value belongs to, other information would also need to be available.

The `DNSRecord` model keeps this information alongside the record value. As a result, each result is displayed as a specific object.

For example, accessing the record value is done as follows:

```python
record.value
```

And the domain and record type are also available:

```python
record.domain
record.record_type
```

This structure makes consuming the data in other parts of the tool easier; especially when the results are to be formatted or exported.

### 6. What Happens If the Resolver Has No Result?

If `lookup_record()` returns an empty list, the loop in the List Comprehension does not execute at all, and `build_dns_results()` also returns an empty list.

In terms of behavior:

```python
values = []
results = [
    DNSRecord(domain="example.com", record_type="A", value=value)
    for value in values
]

print(results)
```

Output:

```text
[]
```

This behavior keeps the function's output contract consistent: in the normal case, the result is a list of `DNSRecord` objects; even if no records were found.

In contrast, if the resolver raises an error like `DNSTimeoutError`, this function does not catch it; therefore, the error is propagated to the higher caller to be managed at the appropriate layer.

### 7. The Position of `results.py` in the Tool's Architecture

The data flow we have implemented in this part of the tool is as follows:

```text
Domain and record type input
          |
          v
lookup_record()
          |
          v
List of DNS response strings
          |
          v
build_dns_results()
          |
          v
List of DNSRecord objects
```

Each part has a specific responsibility:

- `resolver.py` performs the DNS request.
- `models.py` defines the structure of each record.
- `results.py` organizes the resolver's responses in the project model format.

This separation of responsibilities gives each part simpler logic, and changes in one layer do not necessarily require rewriting all other parts.

### 8. Practice Exercises

**Exercise 1 — Building the Output**

Suppose the resolver returned three string values. How many `DNSRecord` objects are created by `build_dns_results()`? Explain your reasoning.

**Exercise 2 — Empty List**

If no records are returned, what will the function's output be? Explain why.

**Exercise 3 — Rewriting with a Loop**

Rewrite the List Comprehension part with a regular `for` loop and compare the result with the original version.

**Exercise 4 — Layer Responsibilities**

Explain why converting string responses into `DNSRecord` objects is done in this function, not in `lookup_record()` itself.

### 9. Summary

The `results.py` file plays the role of interface between the resolver's responses and the project's data model.

In this lesson, we saw that the `build_dns_results()` function:

- Performs the DNS request through `lookup_record()`.
- Receives the response values.
- For each value, creates a `DNSRecord` object.
- If it receives an empty list, returns an empty list.
- Does not manage the errors propagated from the resolver at this layer.

This design helps the data from the DNS lookup be provided to the next parts of the tool with an orderly structure.
