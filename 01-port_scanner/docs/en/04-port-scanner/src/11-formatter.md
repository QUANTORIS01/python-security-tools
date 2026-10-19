[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/src/11-formatter.md)

# A Complete Review of the `formatter.py` File

# Introduction

So far in the project, we have collected almost all the required data.

---

We can:

✅ Scan ports

✅ Detect services

✅ Retrieve Banners

✅ Store results inside a Model

---

For example, our output might now look something like this:

```python
[
    ScanResult(
        port=22,
        service="ssh",
        banner="OpenSSH_9.5"
    ),

    ScanResult(
        port=80,
        service="http",
        banner="Apache/2.4.58"
    )
]
```

---

But there is a problem.

---

If we print this output directly:

```python
print(results)
```

---

The user sees something like this:

```python
[
    ScanResult(port=22, service='ssh', banner='OpenSSH_9.5'),
    ScanResult(port=80, service='http', banner='Apache/2.4.58')
]
```

---

This output is understandable to a programmer.

---

But for the end user:

```text
It is not very beautiful.
```

---

That is why the file:

```text
src/formatter.py
```

was created.

---

The task of this file:

```text
Convert raw data
into
human-readable output
```

---

# File Content

```python
from src import ScanResult


def format_scan_results(
    results: list[ScanResult],
    max_banner_length: int = 40
) -> str:
    """
    Format scan results for terminal output.
    """

    if not results:
        return "No open ports found."

    lines = [
        f"{'PORT':<8} {'STATUS':<8} {'SERVICE':<16} {'BANNER'}",
        "-" * 70
    ]

    for result in results:

        banner = result.banner or "-"

        if len(banner) > max_banner_length:
            banner = (
                banner[: max_banner_length - 3]
                + "..."
            )

        lines.append(
            f"{result.port:<8} "
            f"{'OPEN':<8} "
            f"{result.service:<16} "
            f"{banner}"
        )

    return "\n".join(lines)
```

---

# What Is the Goal of This File?

Goal:

```text
Professional display of results in the terminal
```

---

Before:

```python
[
    ScanResult(...),
    ScanResult(...)
]
```

---

After:

```text
PORT     STATUS   SERVICE          BANNER
------------------------------------------------------
22       OPEN     ssh              OpenSSH_9.5
80       OPEN     http             Apache/2.4.58
```

---

# Import

```python
from src import ScanResult
```

---

We built this model earlier in:

```text
models.py
```

---

All the project results are stored in the form of:

```python
ScanResult
```

---

# The Function Definition

```python
def format_scan_results(
```

---

The function name:

```python
format_scan_results
```

---

Meaning:

```text
Format the scan results.
```

---

# The First Parameter

```python
results: list[ScanResult]
```

---

Example:

```python
[
    ScanResult(...),
    ScanResult(...)
]
```

---

Meaning:

```text
A list of scan results
```

---

# The Second Parameter

```python
max_banner_length: int = 40
```

---

Default value:

```python
40
```

---

Goal:

```text
Limiting the Banner length
```

---

Why?

---

Suppose the Banner is:

```text
Apache/2.4.58 Ubuntu OpenSSL/3.0.5 PHP/8.2.1 Very Long Text...
```

---

If it is displayed in full:

```text
The table breaks.
```

---

That is why its length is limited.

---

# The Function's Output

```python
-> str
```

---

Meaning:

```text
A text string ready for printing
```

---

# The Docstring

```python
"""
Format scan results for terminal output.
"""
```

---

Meaning:

```text
Format the scan results for display in the terminal.
```

---

# Checking the No-Results Case

```python
if not results:
```

---

Let's remember:

```python
[]
```

in Python:

```python
False
```

is considered.

---

So:

```python
if not results:
```

means:

```text
If the list is empty
```

---

# Output

```python
return "No open ports found."
```

---

Example:

```python
[]
```

↓

```text
No open ports found.
```

---

This makes the program produce meaningful output.

---

# Building the Initial Table Lines

```python
lines = [
```

---

We create a new list.

---

This list holds all the output lines.

---

# The Header Line

```python
f"{'PORT':<8} {'STATUS':<8} {'SERVICE':<16} {'BANNER'}"
```

---

Output:

```text
PORT     STATUS   SERVICE          BANNER
```

---

This row is the column headings.

---

# Introduction to Format Alignment

The part:

```python
:<8
```

is very important.

---

Example:

```python
f"{'PORT':<8}"
```

---

Meaning:

```text
Left-align the string in an 8-character space.
```

---

Example:

```text
PORT____
```

(underscores are only for showing spaces)

---

# The Second Column

```python
{'STATUS':<8}
```

---

Output:

```text
STATUS
```

---

In a space of length:

```text
8
```

---

# The Third Column

```python
{'SERVICE':<16}
```

---

Output:

```text
SERVICE
```

---

In a space of length:

```text
16
```

---

Why 16?

---

Because service names are usually longer.

---

# The Separator Line

```python
"-" * 70
```

---

Let's remember:

```python
"-" * 5
```

↓

```text
-----
```

---

So:

```python
"-" * 70
```

↓

```text
----------------------------------------------------------------------
```

---

# Starting to Process the Results

```python
for result in results:
```

---

Example:

```python
ScanResult(
    port=22,
    service="ssh",
    banner="OpenSSH"
)
```

---

On each iteration:

```python
result
```

is a `ScanResult` object.

---

# Handling an Empty Banner

```python
banner = result.banner or "-"
```

---

If:

```python
result.banner
```

equals:

```python
None
```

---

The output will be:

```python
"-"
```

---

Example:

Before:

```python
None
```

---

After:

```text
-
```

---

Why?

---

To make the table cleaner.

---

# Checking the Banner Length

```python
if len(banner) > max_banner_length:
```

---

If the Banner length is more than:

```python
40
```

---

It enters the condition.

---

Example:

```text
Apache Ubuntu OpenSSL PHP Version Very Long Banner...
```

---

# Shortening the Banner

```python
banner[: max_banner_length - 3]
```

---

Suppose:

```python
40
```

---

Then:

```python
37
```

characters are taken.

---

# Adding Three Dots

```python
+ "..."
```

---

Output:

```text
Apache Ubuntu OpenSSL PHP Version...
```

---

This technique is called:

```text
Text Truncation
```

---

It is used in almost all professional software.

---

# Building the Table Row

```python
lines.append(
```

---

Meaning:

```text
Add a new line to the table.
```

---

# The Port Column

```python
{result.port:<8}
```

---

Example:

```python
22
```

↓

```text
22
```

in an 8-character space.

---

# The Status Column

```python
{'OPEN':<8}
```

---

Output:

```text
OPEN
```

---

For now, since we only display open ports, it is always:

```text
OPEN
```

---

# The Service Column

```python
{result.service:<16}
```

---

Example:

```python
"http"
```

↓

```text
http
```

---

# The Banner Column

```python
{banner}
```

---

Example:

```text
Apache
```

---

Or:

```text
OpenSSH
```

---

# A Sample Final Output

```text
22       OPEN     ssh              OpenSSH
80       OPEN     http             Apache
443      OPEN     https            Nginx
```

---

# Building the Final String

```python
"\n".join(lines)
```

---

This part is very important.

---

Suppose:

```python
[
    "line1",
    "line2",
    "line3"
]
```

---

If we write:

```python
"\n".join(lines)
```

---

The output:

```text
line1
line2
line3
```

---

will be.

---

Meaning:

```text
All the lines are converted into one multi-line string.
```

---

# The Function's Final Output

Example:

```text
PORT     STATUS   SERVICE          BANNER
----------------------------------------------------------------------
22       OPEN     ssh              OpenSSH
80       OPEN     http             Apache
443      OPEN     https            Nginx
```

---

# Why Is This File Important?

At first glance, it might seem simple.

---

But in the real world:

```text
User Experience
```

is very important.

---

The user sees the output.

---

If the output is messy:

```text
The entire program looks unprofessional.
```

---

That is why almost all professional tools:

- Nmap
- Wireshark
- Metasploit
- Docker

work hard on Formatting.

---

# Summary

In this session, we learned:

✅ What a Formatter is

✅ Why Formatting is important

✅ What f-strings are

✅ What Alignment is

✅ What `:<8` is

✅ What `:<16` is

✅ What Text Truncation is

✅ What `join` is

✅ What `append` is

✅ How tabular output is built

---

# What Will We Learn in the Next Session?

In the next session, we enter the last file of the directory:

```text
src
```

which is:

```text
src/cli.py
```

This is the most important file of the entire project.

---

There we will learn:

- What `argparse` is
- What a CLI is
- What the Program Entry Point is
- How all the project's modules are connected
- What the complete execution flow of the port scanner is from start to finish

