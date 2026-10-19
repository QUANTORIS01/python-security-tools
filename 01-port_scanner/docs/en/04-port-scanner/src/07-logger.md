[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/src/07-logger.md)

# A Complete Review of the `logger.py` File

# Introduction

In the previous session, we reviewed the file:

```text
src/csv_exporter.py
```

We learned:

- What CSV is
- What the difference between CSV and JSON is
- How `csv.writer` works
- What a Header is
- What `newline=""` is
- Why CSV output is suitable for Excel

---

But an important question:

If the user runs the program and later wants to know:

- When was the scan performed?
- Which IP was scanned?
- Which ports were found?
- Did an error occur?

What should we do?

---

If we only use:

```python
print()
```

Once the terminal is closed, everything is lost.

---

That is why professional software uses:

```text
Logging
```

---

The file:

```text
src/logger.py
```

is responsible for exactly this.

---

# File Content

```python
import logging


def setup_logger(filename: str) -> logging.Logger:
    """
    Configure and return a file logger.
    """
    logger = logging.getLogger("port_scanner")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            if handler.baseFilename == filename:
                return logger

    handler = logging.FileHandler(
        filename,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
```

---

# What Is the Goal of This File?

Goal:

```text
Create and configure the project's logging system
```

---

# What Is Logging?

Logging means:

```text
Recording important events of the program
```

---

Example:

```text
[10:30] Scan Started
[10:30] Target: 127.0.0.1
[10:31] Port 80 Open
[10:31] Port 443 Open
[10:32] Scan Finished
```

---

This information is saved to a file.

---

# Why Is Logging Important?

Almost all professional software in the world produces logs.

---

Example:

- Linux
- Windows
- Apache
- Nginx
- Docker
- Kubernetes
- Nmap
- Wireshark

---

Without logs:

```text
Troubleshooting is almost impossible.
```

---

# Import

```python
import logging
```

---

This module is one of the most powerful standard libraries in Python.

---

Task:

```text
Managing logs
```

---

# The Function Definition

```python
def setup_logger(
    filename: str
) -> logging.Logger:
```

---

## Input

```python
filename
```

---

Example:

```python
"scan.log"
```

---

## Output

```python
logging.Logger
```

---

Meaning:

```text
A Logger ready to use
```

---

# The Docstring

```python
"""
Configure and return a file logger.
"""
```

---

Meaning:

```text
Configure and return a file logger.
```

---

# Creating the Logger

```python
logger = logging.getLogger(
    "port_scanner"
)
```

---

# What Is `getLogger`?

This function creates a Logger or, if one has already been created, returns the same one.

---

Logger name:

```python
"port_scanner"
```

---

It is like the Logger's unique identifier.

---

It can be imagined as:

```text
Logger Name = Port Scanner
```

---

# Setting the Log Level

```python
logger.setLevel(
    logging.INFO
)
```

---

The Logging system has several different levels.

---

# DEBUG

```python
logging.DEBUG
```

---

For very detailed information.

---

Example:

```text
Socket Created
```

---

# INFO

```python
logging.INFO
```

---

For general information.

---

Example:

```text
Scan Started
```

---

# WARNING

```python
logging.WARNING
```

---

Warnings.

---

Example:

```text
Slow Response
```

---

# ERROR

```python
logging.ERROR
```

---

Errors.

---

Example:

```text
Connection Failed
```

---

# CRITICAL

```python
logging.CRITICAL
```

---

Very severe errors.

---

Example:

```text
Database Corrupted
```

---

In our project:

```python
logging.INFO
```

has been chosen.

---

Meaning:

```text
INFO and higher are recorded.
```

---

# Preventing Log Propagation

```python
logger.propagate = False
```

---

This line is very important.

---

If it is not:

```python
False
```

Then logs might be recorded:

```text
Twice
Three times
Multiple times
```

---

Especially when the project grows.

---

This line prevents that.

---

# Checking the Existing Handlers

```python
for handler in logger.handlers:
```

---

Each Logger can have several Handlers.

---

Example:

```text
FileHandler
ConsoleHandler
NetworkHandler
...
```

---

This loop checks all the Handlers.

---

# Checking the Handler Type

```python
if isinstance(
    handler,
    logging.FileHandler
):
```

---

Meaning:

```text
Is this Handler of type FileHandler?
```

---

# What Is a FileHandler?

A Handler that saves logs to a file.

---

# Checking the File

```python
if handler.baseFilename == filename:
```

---

Meaning:

```text
Has this same file already been registered?
```

---

Example:

```python
scan.log
```

---

If it already exists:

---

```python
return logger
```

---

The function returns the same Logger as before.

---

# Why Is This Important?

If this part did not exist:

---

Every time:

```python
setup_logger()
```

was called,

a new FileHandler would be created.

---

The result:

```text
Duplicated logs
```

---

Example:

```text
Scan Started
Scan Started
Scan Started
```

---

This is one of the best parts of the project's design.

---

# Creating the FileHandler

```python
handler = logging.FileHandler(
    filename,
    encoding="utf-8"
)
```

---

Here the log file is created.

---

Example:

```text
scan.log
```

---

All messages will be stored inside this file.

---

# UTF-8

```python
encoding="utf-8"
```

---

For support of:

```text
Persian
Arabic
English
```

---

# Creating the Formatter

```python
formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(message)s"
)
```

---

The Formatter defines the appearance of the logs.

---

# `asctime`

```python
%(asctime)s
```

---

The time the log was recorded.

---

Example:

```text
2025-07-01 12:30:15
```

---

# `levelname`

```python
%(levelname)s
```

---

The log level.

---

Example:

```text
INFO
WARNING
ERROR
```

---

# `message`

```python
%(message)s
```

---

The message text.

---

Example:

```text
Scan Started
```

---

# A Real Output Sample

```text
2025-07-01 12:30:15 INFO Scan Started
```

---

# Connecting the Formatter to the Handler

```python
handler.setFormatter(
    formatter
)
```

---

From this moment:

All logs are stored with this format.

---

# Connecting the Handler to the Logger

```python
logger.addHandler(
    handler
)
```

---

Meaning:

```text
Connect this file to the Logger.
```

---

From this moment, the Logger can write to the file.

---

# Returning the Logger

```python
return logger
```

---

Finally, the ready-to-use Logger is delivered to other parts of the program.

---

# Sample Usage

```python
logger = setup_logger(
    "scan.log"
)
```

---

Then:

```python
logger.info(
    "Scan Started"
)
```

---

The file:

```text
scan.log
```

---

will contain:

```text
2025-07-01 12:30:15 INFO Scan Started
```

---

# An Important Design Note

This file has only one job:

```text
Configuring Logging
```

---

It does not perform:

❌ Port scanning

❌ Service detection

❌ Banner grabbing

❌ Saving JSON

❌ Saving CSV

---

This is exactly the:

```text
Single Responsibility Principle
```

---

# Summary

In this session, we learned:

✅ What Logging is

✅ Why logging is important

✅ What a Logger is

✅ What a Handler is

✅ What a FileHandler is

✅ What a Formatter is

✅ What INFO is

✅ What `propagate` is

✅ What `addHandler` is

✅ What the structure of a professional log file looks like

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
src/banner.py
```

There we will learn:

- What Banner Grabbing is
- Why hackers and network administrators use it
- What the difference between a Banner and a Service is
- How a Socket receives data
- What `recv` is
- What `decode` is
- How Timeout works in Banner Grabbing

