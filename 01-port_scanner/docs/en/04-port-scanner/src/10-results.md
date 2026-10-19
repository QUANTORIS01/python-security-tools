[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/src/10-results.md)

# A Complete Review of the `results.py` File

# Introduction

So far in the project chapter, we have reviewed almost all the main pieces of the port scanner:

✅ validator.py

✅ scanner.py

✅ services.py

✅ exporter.py

✅ csv_exporter.py

✅ logger.py

✅ banner.py

✅ models.py

---

But one important question still remains.

---

Suppose the scan has been performed and we have this output:

```python
[22, 80, 443]
```

---

This is just a list of port numbers.

---

But we want more information.

---

For each port, we need to know:

```text
Port Number
Service Name
Banner
```

---

Example:

```python
22 → ssh → OpenSSH
80 → http → Apache
443 → https → Nginx
```

---

The question:

How do we put this information together?

---

Answer:

```text
results.py
```

---

This file plays the role of:

```text
Data Processing Pipeline
```

in the project.

---

# File Content

```python
from src import (
    grab_banner,
    ScanResult,
    detect_service
)


def build_scan_results(
    ip: str,
    open_ports: list[int],
    timeout: float = 1.0
) -> list[ScanResult]:
    """
    Build structured scan results for open ports.
    """

    results = []

    for port in open_ports:

        service = detect_service(port)

        banner = grab_banner(
            ip,
            port,
            timeout=timeout
        )

        results.append(
            ScanResult(
                port=port,
                service=service,
                banner=banner,
            )
        )

    return results
```

---

# What Is the Goal of This File?

Goal:

```text
Converting the list of open ports
into
structured results
```

---

Before:

```python
[22, 80, 443]
```

---

After:

```python
[
    ScanResult(
        port=22,
        service="ssh",
        banner="OpenSSH"
    ),

    ScanResult(
        port=80,
        service="http",
        banner="Apache"
    )
]
```

---

# Imports

```python
from src import (
    grab_banner,
    ScanResult,
    detect_service
)
```

---

If you remember, in the file:

```python
src/__init__.py
```

we exported all the important functions of the project.

---

That is why here, instead of:

```python
from src.banner import grab_banner
from src.models import ScanResult
from src.services import detect_service
```

---

we just write:

```python
from src import ...
```

---

This is one of the advantages of building a real Package.

---

# The Main Function

```python
def build_scan_results(
```

---

The function name:

```python
build_scan_results
```

---

Meaning:

```text
Build the final scan results
```

---

# The First Parameter

```python
ip: str
```

---

Example:

```python
"127.0.0.1"
```

---

Or:

```python
"192.168.1.10"
```

---

This IP is used for Banner Grabbing.

---

# The Second Parameter

```python
open_ports: list[int]
```

---

Example:

```python
[22, 80, 443]
```

---

The output of the file:

```python
scanner.py
```

is exactly this.

---

# The Third Parameter

```python
timeout: float = 1.0
```

---

Used for:

```python
grab_banner()
```

---

# The Function's Output

```python
list[ScanResult]
```

---

Meaning:

```python
[
    ScanResult(...),
    ScanResult(...),
]
```

---

Not:

```python
list[int]
```

---

Not:

```python
dict
```

---

Rather:

```python
A list of ScanResult models
```

---

# The Docstring

```python
"""
Build structured scan results for open ports.
"""
```

---

Meaning:

```text
Create structured results for open ports.
```

---

# Creating the Results List

```python
results = []
```

---

At first, the list is empty.

---

Example:

```python
[]
```

---

Later, the results are stored in it.

---

# Starting the Loop

```python
for port in open_ports:
```

---

Suppose:

```python
open_ports = [22, 80]
```

---

First iteration:

```python
port = 22
```

---

Second iteration:

```python
port = 80
```

---

# Detecting the Service

```python
service = detect_service(port)
```

---

Example:

```python
22
```

↓

```python
"ssh"
```

---

Or:

```python
80
```

↓

```python
"http"
```

---

This is the same function we reviewed in:

```python
services.py
```

---

# Retrieving the Banner

```python
banner = grab_banner(
    ip,
    port,
    timeout=timeout
)
```

---

Example:

```python
grab_banner(
    "127.0.0.1",
    22
)
```

---

Output:

```python
"SSH-2.0-OpenSSH_9.5"
```

---

Or:

```python
None
```

---

This is the same function we reviewed in:

```python
banner.py
```

---

# Building the Model

```python
ScanResult(
```

---

Here we enter the most important part of the file.

---

The collected information:

```python
port
service
banner
```

---

is placed inside the model.

---

# The First Value

```python
port=port
```

---

Example:

```python
22
```

---

# The Second Value

```python
service=service
```

---

Example:

```python
"ssh"
```

---

# The Third Value

```python
banner=banner
```

---

Example:

```python
"OpenSSH"
```

---

Or:

```python
None
```

---

# The Final Result

```python
ScanResult(
    port=22,
    service="ssh",
    banner="OpenSSH"
)
```

---

# Adding to the List

```python
results.append(...)
```

---

This new object is added to the results list.

---

After the first iteration:

```python
[
    ScanResult(...)
]
```

---

After the second iteration:

```python
[
    ScanResult(...),
    ScanResult(...)
]
```

---

And so on.

---

# End of the Loop

When all ports have been processed:

```python
results
```

will contain all the information.

---

# Returning the Result

```python
return results
```

---

Example:

```python
[
    ScanResult(
        port=22,
        service="ssh",
        banner="OpenSSH"
    ),

    ScanResult(
        port=80,
        service="http",
        banner="Apache"
    ),

    ScanResult(
        port=443,
        service="https",
        banner=None
    )
]
```

---

# Why Is This File Important?

This file plays the role of:

```text
Orchestrator
```

---

Meaning it connects several different modules together.

---

Connections:

```text
scanner.py
      ↓

results.py

      ↓

services.py
      ↓

banner.py
      ↓

models.py
```

---

This file is the project's data-collection hub.

---

# The Design Pattern Used

This file is an example of:

```text
Data Transformation Pipeline
```

---

Input:

```python
[22, 80, 443]
```

---

Output:

```python
[
    ScanResult(...),
    ScanResult(...),
]
```

---

Meaning raw data is transformed into structured data.

---

This is exactly what happens in professional projects.

---

# An Important Architectural Note

Pay attention:

---

This file:

❌ Does not scan ports

❌ Does not detect services

❌ Does not grab Banners

❌ Does not save output

---

It is only:

```text
An information coordinator
```

---

This is exactly:

```text
Separation of Concerns
```

which is very important in software architecture.

---

# Summary

In this session, we learned:

✅ What the role of the `results.py` file is

✅ Why `build_scan_results` was created

✅ How Service Detection is performed

✅ How Banner Grabbing is performed

✅ How `ScanResult` is built

✅ How `append` works

✅ What a Data Transformation Pipeline is

✅ What an Orchestrator is

✅ What Separation of Concerns is

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
src/formatter.py
```

There we will learn:

- How to display the output nicely
- What Table Formatting is
- What String Formatting is
- How f-strings work
- Why the Banner is shortened
- Why the Formatter is one of the most important parts of user experience

