[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/src/07-formatter.md)

# Chapter Four: DNS Lookup Project Code Analysis

## Lesson 7: Output Formatting in Python

### 1. Lesson Goal

In this lesson, we will learn:

- How to convert structured data into readable text.
- How to align terminal output columns with f-strings.
- How to convert multiple lines of text into one string with `join()`.
- Why it is better to separate the output display logic from the DNS request execution logic.

### 2. Examining the `formatter.py` File Code

```python
from src import DNSRecord


def format_dns_results(results: list[DNSRecord]) -> str:
    """
    Format DNS lookup results for terminal output.
    """
    if not results:
        return 'No DNS records found.'

    lines = [f"{'DOMAIN':<30} {'TYPE':<8} {'VALUE'}", '-' * 70]
    for result in results:
        lines.append(
            f'{result.domain:<30} '
            f'{result.record_type:<8} '
            f'{result.value}'
        )

    return '\n'.join(lines)
```

This file defines the function `format_dns_results()`.

The function receives a list of `DNSRecord` objects and returns a string (`str`) ready for display in the terminal.

This means the function does not send DNS requests directly and does not create new records; its task is to format results that are already prepared.

### 3. Handling the No-Results Case

At the beginning of the function:

```python
if not results:
    return 'No DNS records found.'
```

In Python, an empty list in a condition is evaluated as False. That is why `if not results` checks the empty list state.

If there are no records to display, the function returns the following message:

```text
No DNS records found.
```

This causes the no-results case to also have a clear and understandable output; as a result, instead of building an empty table, the function provides an appropriate message for this state.

### 4. Building the Column Headers and Separator Line

The next line:

```python
lines = [f"{'DOMAIN':<30} {'TYPE':<8} {'VALUE'}", '-' * 70]
```

In this part, a list named `lines` is created that first contains the column headers and then the separator line.

The expression `'-' * 70` produces a string containing 70 dashes.

In f-strings, formats like `:<30` specify that the value should be left-aligned in a space of at least 30 characters.

For example:

```python
print(f"{'DOMAIN':<30} {'TYPE':<8} {'VALUE'}")
```

The output places the column headers next to each other with appropriate spacing.

- `DOMAIN` has a space of 30 characters.
- `TYPE` has a space of 8 characters.
- `VALUE` comes after them.

This method is useful for text alignment of columns in terminal output.

### 5. Adding Each Record to the Table

The loop:

```python
for result in results:
    lines.append(
        f'{result.domain:<30} '
        f'{result.record_type:<8} '
        f'{result.value}'
    )
```

The function iterates over all the records in `results`.

In each loop iteration:

1. The value of `result.domain` is read.
2. The record type is received from `result.record_type`.
3. The record value is read from `result.value`.
4. A formatted text line is added to `lines`.

Using the `DNSRecord` fields allows the code to receive each record's information with specific names; there is no need to extract data from numerical positions in a list or parts of a string.

Also, `append()` adds the new line to the end of the list and preserves the order of the received results.

### 6. Converting the Lines List into a Single String

At the end:

```python
return '\n'.join(lines)
```

The `join()` method concatenates the elements of a text sequence with the string written before it.

In this example, the separator is `'\n'`; meaning each element is separated from the next by a newline character.

If `lines` is like this:

```python
lines = [
    "DOMAIN                         TYPE     VALUE",
    "----------------------------------------------------------------------",
    "example.com                    A        192.0.2.10",
]
```

Calling `'\n'.join(lines)` places all elements in a multi-line string.

This method avoids building the output string with multiple concatenations and keeps the code more readable.

### 7. A Sample of the Final Output

Suppose the function receives two hypothetical records:

```python
results = [
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

Calling the function:

```python
output = format_dns_results(results)
print(output)
```

The output will be like this:

```text
DOMAIN                         TYPE     VALUE
----------------------------------------------------------------------
example.com                    A        192.0.2.10
example.com                    A        192.0.2.11
```

The above values are only educational samples. The function places the actual input data in this same format.

### 8. Why Have We Separated Formatting from the DNS Logic?

In the tool's architecture, these two responsibilities are independent:

- `resolver.py` performs the DNS request.
- `results.py` converts responses into `DNSRecord` objects.
- `formatter.py` converts objects into terminal-appropriate text.

This separation has important advantages:

- The display format can be improved without changing the DNS logic.
- Structured data can also be used in other formats such as JSON or CSV.
- The formatting function does not depend on communicating with the DNS server.
- Testing the formatting can be done by creating a few `DNSRecord` objects, without executing a network request each time.

In this way, each part has a specific task, and developing and maintaining the tool becomes simpler.

### 9. A Note About Column Width

Formats like `:<30` and `:<8` specify the minimum column width; they do not limit the length of the value.

If the domain name or record value is longer than the specified space, the text exceeds the minimum width and the subsequent columns might not appear fully aligned. This behavior is compatible with the current formatting and is usually acceptable for simple text output.

If in the future the output must remain fully aligned even for very long values, other solutions for table display can be considered.

### 10. Practice Exercises

**Exercise 1 — No-Results Case**

Call the function with an empty list and explain why the message `No DNS records found.` is returned.

**Exercise 2 — Column Formatting**

Run the following expression and explain what effect `:<20` has:

```python
print(f"{'DOMAIN':<20} {'TYPE':<8} {'VALUE'}")
```

**Exercise 3 — Using `join()`**

Convert the following list into a multi-line string:

```python
lines = ["First line", "Second line", "Third line"]
```

Then print the result.

**Exercise 4 — Separation of Responsibilities**

Explain why it is better for `format_dns_results()` to only format prepared data and not send a DNS request itself.

### 11. Summary

The `format_dns_results()` function converts a list of `DNSRecord` objects into text that can be displayed in the terminal.

In this lesson, we became familiar with several important Python capabilities:

- The `if not results` condition for detecting an empty list
- f-strings for aligning text columns
- `append()` for adding lines to a list
- `join()` for building a multi-line string

More importantly, we saw that keeping formatting separate from the DNS logic helps make the tool's architecture more orderly and extensible.
