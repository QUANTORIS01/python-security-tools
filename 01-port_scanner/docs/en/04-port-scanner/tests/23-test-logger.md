[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/tests/23-test-logger.md)

# A Complete Review of the `test_logger.py` File

# Introduction

We have reached one of the most professional parts of the project.

---

So far, we have learned:

✅ Port scanning

✅ Service detection

✅ Banner retrieval

✅ Result building

✅ Output display

✅ JSON storage

✅ CSV storage

---

But one important feature still remained:

```text
Logging
```

---

If you remember, in the file:

```text
src/logger.py
```

we built the following function:

```python
setup_logger()
```

---

Its task was:

```text
Recording the program's events
in a log file
```

---

For example:

```text
Scan started
```

---

Or:

```text
Scan completed
```

---

were stored in the file:

```text
scan.log
```

---

Now we must make sure:

✅ The log file is created

✅ Messages are stored inside the file

✅ Duplicate Handlers are not created

✅ Tests do not affect each other

---

File content:

```python
import logging

import pytest

from src import setup_logger


def test_setup_logger_creates_log_file(tmp_path):
    log_file = tmp_path / "scan.log"
    logger = setup_logger(str(log_file))
    logger.info("Test message")
    for handler in logger.handlers:
        handler.flush()
    assert log_file.exists()


def test_setup_logger_writes_log_message(tmp_path):
    log_file = tmp_path / "scan.log"
    logger = setup_logger(str(log_file))
    logger.info("Test message")
    for handler in logger.handlers:
        handler.flush()
    content = log_file.read_text(encoding="utf-8")
    assert "Test message" in content
    for handler in logger.handlers:
        handler.close()
    logger.handlers.clear()


def test_setup_logger_does_not_duplicate_handlers(tmp_path):
    log_file = tmp_path / "scan.log"
    logger = setup_logger(str(log_file))
    initial_handler_count = len(logger.handlers)
    setup_logger(str(log_file))
    assert len(logger.handlers) == initial_handler_count


@pytest.fixture(autouse=True)
def cleanup_logger():
    yield
    logger = logging.getLogger("port_scanner")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)
```

---

# Imports

```python
import logging

import pytest

from src import setup_logger
```

---

# The First Import

```python
import logging
```

---

For accessing the project's Logger.

---

# The Second Import

```python
import pytest
```

---

For Fixtures.

---

# The Third Import

```python
from src import setup_logger
```

---

The function that is going to be tested.

---

# What Is the Goal of This File?

Checking three main things:

```text
Creating the log file
```

---

```text
Recording messages
```

---

```text
Managing Handlers
```

---

# The First Test

```python
def test_setup_logger_creates_log_file(
    tmp_path
):
```

---

Goal:

```text
Checking that the log file is created
```

---

# Building the File Path

```python
log_file =
    tmp_path / "scan.log"
```

---

For example:

```text
/tmp/.../scan.log
```

---

# Creating the Logger

```python
logger =
    setup_logger(
        str(log_file)
    )
```

---

If you remember:

```python
setup_logger()
```

created a:

```python
FileHandler
```

---

# Recording a Message

```python
logger.info(
    "Test message"
)
```

---

At this moment, the message must be stored in the file.

---

# Why Is Flush Necessary?

```python
for handler in logger.handlers:
    handler.flush()
```

---

A very important point.

---

The Logging system usually does not write data directly to disk.

---

Rather, it keeps it in a:

```text
Buffer
```

---

That is why, before the test:

```python
flush()
```

is called.

---

To make sure:

```text
All the data has been written to the file.
```

---

# Checking the File

```python
assert log_file.exists()
```

---

If the file has been created:

```text
PASS
```

---

# What Does This Test Prove?

This test guarantees:

```text
The FileHandler
has been created correctly.
```

---

# The Second Test

```python
def test_setup_logger_writes_log_message(
    tmp_path
):
```

---

Goal:

```text
Checking the content of the log file
```

---

The previous test only checked the file's existence.

---

But:

```text
The file's existence alone is not enough.
```

---

The file might be created but:

```text
Empty.
```

---

That is why this test was added.

---

# Creating the Logger

```python
logger =
    setup_logger(...)
```

---

# Recording a Message

```pythonlogger.info(
    "Test message"
)
```

---

# Flush

```python
handler.flush()
```

---

So that the message is actually written to disk.

---

# Reading the File

```python
content =
    log_file.read_text(
        encoding="utf-8"
    )
```

---

Now the entire file content is in:

```python
content
```

---

# Checking the Content

```python
assert "Test message" in content
```

---

If the message is inside the file:

```text
PASS
```

---

# Why Is This Test Important?

Because it verifies:

```text
The Logger does not just create a file
but actually writes data.
```

---

# Closing the Handlers

```python
for handler in logger.handlers:
    handler.close()
```

---

Then:

```python
logger.handlers.clear()
```

---

Why?

---

Because:

```python
Logger
```

in Python behaves:

```text
Singleton-like
```

---

Meaning:

```python
logging.getLogger(
    "port_scanner"
)
```

---

always returns the same previous Logger.

---

If Handlers are not closed:

```text
The following tests will run into problems.
```

---

# The Third Test

```python
def test_setup_logger_does_not_duplicate_handlers(
    tmp_path
):
```

---

The most important test of the file.

---

Goal:

```text
Preventing duplicate Handlers
```

---

If you remember, in:

```python
logger.py
```

we had:

```python
for handler in logger.handlers:
```

---

Then:

```python
if isinstance(
    handler,
    logging.FileHandler
):
```

---

And:

```python
if handler.baseFilename == filename:
    return logger
```

---

This part was written to prevent:

```text
Duplicate Handler
```

---

# What Is the Problem?

Suppose this happens:

```python
setup_logger("scan.log")
```

---

Then again:

```python
setup_logger("scan.log")
```

---

If we do not control it:

```text
Two FileHandlers
```

will be created.

---

Result:

```text
Each message
is written twice.
```

---

For example:

```text
Scan started
Scan started
```

---

Which is a very common bug in Logging.

---

# Creating the Logger

```python
logger =
    setup_logger(...)
```

---

# Counting the Handlers

```python
initial_handler_count =
    len(logger.handlers)
```

---

For example:

```python
1
```

---

# Calling Again

```python
setup_logger(...)
```

---

If the code is correct:

```text
No new Handler is created.
```

---

# Checking

```python
assert len(
    logger.handlers
) == initial_handler_count
```

---

If the number does not change:

```text
PASS
```

---

This test guarantees:

```text
The project's Logger
does not suffer from Handler Duplication.
```

---

# The Final Fixture

Now we reach the most professional part of the file.

---

```python
@pytest.fixture(
    autouse=True
)
```

---

# What Is a Fixture?

In pytest:

```text
Code that runs before or after a test.
```

---

# `autouse=True`

Meaning:

```text
It does not need to be called manually.
```

---

Before and after each test:

```python
cleanup_logger()
```

is executed.

---

# The Fixture Structure

```python
def cleanup_logger():
```

---

# The First Part

```python
yield
```

---

Meaning:

```text
First, run the test.
```

---

After the test ends:

```text
The code after yield
runs.
```

---

# Getting the Logger

```python
logger =
    logging.getLogger(
        "port_scanner"
    )
```

---

The same project Logger.

---

# The Cleanup Loop

```python
for handler in logger.handlers[:]:
```

---

Pay attention:

```python
[:]
```

---

creates a copy of the list.

---

Why?

---

Because:

```python
removeHandler()
```

is simultaneously removing elements.

---

# Closing the Handler

```python
handler.close()
```

---

It closes the file.

---

# Removing the Handler

```python
logger.removeHandler(
    handler
)
```

---

It is completely removed from the Logger.

---

# Why Is This Fixture Important?

Without this Fixture:

```text
The first test
```

↓

```text
creates a Handler
```

↓

```text
The second test
```

↓

```text
sees the same Handler
```

↓

```text
Incorrect results
```

---

But this Fixture guarantees:

```text
Each test
has a completely clean
and independent environment.
```

---

# Professional Concepts We Learned in This File

✅ FileHandler

✅ Buffer

✅ Flush

✅ Log File Testing

✅ Handler Management

✅ Duplicate Handler Prevention

✅ Fixture

✅ `autouse=True`

✅ `yield` Fixture

✅ Test Isolation

---

# pytest Output

If everything is correct:

```bash
pytest
```

---

Output:

```text
==== 3 passed ====
```

---

# Summary

In this session, we learned:

✅ How to test the Logger

✅ How to check the log file

✅ How to validate log content

✅ What a Handler is

✅ What a Duplicate Handler is

✅ What a Fixture is

✅ What `autouse=True` does

✅ What Test Isolation is

✅ Why cleanup after tests matters

---

# The Current Status of the Project

Test files reviewed:

```text
test_validator.py
test_scanner.py
test_services.py
test_exporter.py
test_cli.py
test_banner.py
test_models.py
test_results.py
test_formatter.py
test_csv_exporter.py
test_logger.py
```

---

We are almost at the last steps of the project walkthrough chapter.

---

# What Will We Learn in the Next Session?

If there is any other file left in the folder:

```text
tests/
```

we will review it.

---

Otherwise, we will enter:

```text
The final project summary session
```

and we will review the entire Port Scanner architecture from beginning to end:

```text
CLI
↓
Validation
↓
Scanner
↓
Services
↓
Banner
↓
Results
↓
Formatter
↓
Exporter
↓
Logger
```
