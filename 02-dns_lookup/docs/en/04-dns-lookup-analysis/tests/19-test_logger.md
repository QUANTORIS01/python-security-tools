[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/tests/19-test_logger.md)

# 19. Test Writing for the Logging System in Python

## Lesson Goal

In this lesson, we examine the `tests/test_logger.py` file to learn how to test the program's event logging system.

Main topics:

- Familiarity with `logging` and `Logger`
- Examining the creation of the log file
- Reading and examining the recorded messages
- Preventing duplicate Handlers
- Using Fixtures in `pytest`
- Cleaning up resources after test execution
- Understanding the role of `flush()`, `close()`, and `removeHandler()`

## The Complete Test File Code

```python
import logging
import pytest

from src import setup_logger


def test_setup_logger_creates_log_file(tmp_path):
    log_file = (tmp_path / 'dns.log')
    logger = setup_logger(str(log_file))
    logger.info('Test message')
    for handler in logger.handlers:
        handler.flush()
    assert log_file.exists()


def test_setup_logger_writes_log_message(tmp_path):
    log_file = (tmp_path / 'dns.log')
    logger = setup_logger(str(log_file))
    logger.info('Test message')
    for handler in logger.handlers:
        handler.flush()
    content = log_file.read_text(encoding='utf-8')
    assert 'Test message' in content


def test_setup_logger_does_not_duplicate_handlers(tmp_path):
    log_file = (tmp_path / 'dns.log')
    logger = setup_logger(str(log_file))
    initial_count = len(logger.handlers)
    setup_logger(str(log_file))
    assert (len(logger.handlers) == initial_count)


@pytest.fixture(autouse=True)
def cleanup_logger():
    yield

    logger = logging.getLogger('dns_lookup')
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)
```

## 1. Importing the Libraries

```python
import logging
import pytest

from src import setup_logger
```

Each of these imports has a specific role:

- `logging`: Python's standard library for recording program messages.
- `pytest`: the tool for executing tests and defining Fixtures.
- `setup_logger`: the project function that configures the Logger.

The `setup_logger()` function is in the `src/logger.py` file. This function creates or retrieves a Logger named `dns_lookup`, sets the message recording level, and adds a `FileHandler` to it for writing to a file; unless a Handler with the target file path already exists.

## 2. First Test: Examining the Creation of the Log File

The test code:

```python
def test_setup_logger_creates_log_file(tmp_path):
    log_file = tmp_path / 'dns.log'
    logger = setup_logger(str(log_file))

    logger.info('Test message')

    for handler in logger.handlers:
        handler.flush()

    assert log_file.exists()
```

### First Step: Building the File Path

```python
log_file = tmp_path / 'dns.log'
```

`tmp_path` is a ready-made Fixture in `pytest` that provides a temporary folder path.

Using it, the `dns.log` file is created in the temporary path; therefore, the test does not depend on the project's actual log file.

### Second Step: Getting the Logger

```python
logger = setup_logger(str(log_file))
```

The `setup_logger()` function returns a configured Logger.

Converting `log_file` to a string with `str()` causes the file path to be sent in the form the function expects.

### Third Step: Recording a Message

```python
logger.info('Test message')
```

The `info()` method records a message with the `INFO` importance level.

In the project's settings, the Logger level is set to `logging.INFO`; therefore, this message is eligible for recording.

### Fourth Step: Ensuring the Data Is Written

```python
for handler in logger.handlers:
    handler.flush()
```

The `flush()` method asks the Handler to transfer the buffered data to the destination.

This helps ensure that the recorded messages have been written to the file before examining it.

### Fifth Step: Examining the File's Existence

```python
assert log_file.exists()
```

This assertion checks that the file path exists.

An important note: This test alone does not examine the file's content or the correctness of the recorded message; this responsibility belongs to the second test.

## 3. Second Test: Examining the Message Written to the File

The test code:

```python
def test_setup_logger_writes_log_message(tmp_path):
    log_file = tmp_path / 'dns.log'
    logger = setup_logger(str(log_file))

    logger.info('Test message')

    for handler in logger.handlers:
        handler.flush()

    content = log_file.read_text(encoding='utf-8')

    assert 'Test message' in content
```

This test, in addition to creating the file, examines that the recorded message actually exists in its content.

### Reading the File

```python
content = log_file.read_text(encoding='utf-8')
```

The `read_text()` method reads the file's content as a string.

Using `encoding='utf-8'` specifies the text encoding.

### Examining the Message

```python
assert 'Test message' in content
```

The `in` operator checks that the target text exists in the file's content.

The project's log file, in addition to the message, can also contain other information such as the recording time and the importance level. That is why the test only examines the presence of the message text, not the complete equality of the file content with a fixed string.

## 4. Third Test: Preventing Duplicate Handlers

The test code:

```python
def test_setup_logger_does_not_duplicate_handlers(tmp_path):
    log_file = tmp_path / 'dns.log'

    logger = setup_logger(str(log_file))
    initial_count = len(logger.handlers)

    setup_logger(str(log_file))

    assert len(logger.handlers) == initial_count
```

This test examines an important behavior of the `setup_logger()` function.

### What Is the Problem with Duplicate Handlers?

In Python, calling `logging.getLogger('dns_lookup')` again usually returns the same named Logger object.

If each execution of `setup_logger()` adds a new Handler to it, a message might be recorded multiple times in the file.

To prevent this situation, the project implementation examines the existing Handlers:

```python
for handler in logger.handlers:
    if isinstance(handler, logging.FileHandler):
        if handler.baseFilename == filename:
            return logger
```

If a file Handler with the target path already exists, the function returns the same Logger and does not add another Handler.

### Why Do We Compare the Number of Handlers?

```python
initial_count = len(logger.handlers)
```

This line stores the number of current Handlers.

Then the function is called again:

```python
setup_logger(str(log_file))
```

At the end:

```python
assert len(logger.handlers) == initial_count
```

The test examines that the number of Handlers has not increased.

This test prevents unwanted changes in the Logger configuration; although it alone does not guarantee that all Handler details are correct or that messages are written exactly once.

## 5. The Cleanup Fixture: `cleanup_logger`

The final part of the test file:

```python
@pytest.fixture(autouse=True)
def cleanup_logger():
    yield

    logger = logging.getLogger('dns_lookup')
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)
```

This part is one of the most important parts of the test, because it cleans up the resources that the Logger has taken after each test.

### `@pytest.fixture`

A Fixture in `pytest` can provide setup or cleanup code to tests.

### `autouse=True`

This option causes the Fixture to be executed without needing to write its name in the arguments of each test.

Therefore, `cleanup_logger` is automatically applied to the tests of this set.

### The Role of `yield`

In a Fixture, the code before `yield` constitutes the setup stage and the code after it constitutes the stage after execution.

In this file, the code before `yield` does nothing. After each test ends, the Fixture's execution continues from `yield` and cleanup is performed.

### Getting the Logger

```python
logger = logging.getLogger('dns_lookup')
```

The same named Logger that the project function uses is retrieved.

### Why Is `logger.handlers[:]` Used?

```python
for handler in logger.handlers[:]:
```

The expression `logger.handlers[:]` creates a copy of the list of Handlers.

Next, the Handlers are removed from the main list. Iterating over the copy helps prevent problems with the loop when the main list is being changed.

### Closing and Removing the Handler

```python
handler.close()
logger.removeHandler(handler)
```

These two operations have different tasks:

- `close()` releases the Handler's resources, such as the opened file.
- `removeHandler()` detaches that Handler from the Logger.

If the Handlers are not cleaned up, subsequent tests might use the remaining Handlers or files might stay open longer than expected.

## 6. The Difference Between `flush()` and `close()`

These two methods both help with managing writing and resources, but they are not the same.

| Method | Task |
|---|---|
| `flush()` | Transferring buffered data to the destination |
| `close()` | Closing the Handler and releasing its resources |
| `removeHandler()` | Detaching the Handler from the Logger |

In the first two tests, `flush()` is used before reading the file.

In the cleanup Fixture, `close()` and `removeHandler()` are used to end the use of Handlers and detach them from the Logger.

## 7. How the Tests Relate to the Project Architecture

The `src/logger.py` file is responsible for configuring the Logger; but the `tests/test_logger.py` file examines its behavior from the outside.

These tests cover three important aspects:

1. **File creation:** The Logger can create its file destination.
2. **Message recording:** The recorded message is actually visible in the file.
3. **Reproducible configuration:** Calling the function again for the same path does not add a duplicate Handler.

The cleanup Fixture also helps tests release the Logger's shared resources after execution.

This is especially important in projects where several tests use one named Logger; because Loggers in the `logging` system are usually shared across different program calls.

## 8. A Technical Note About the File Path

The current implementation compares the Handler's file path with the input string:

```python
handler.baseFilename == filename
```

In some conditions, a relative path and an absolute path might point to the same file but have different strings. In that case, this comparison might not recognize the existing Handler.

This is not necessarily a problem in the current test that uses the `tmp_path` path, but it can be an opportunity for future improvement; for example, by normalizing the paths before comparison.

## 9. Running the Tests

To run the Logger tests:

```powershell
pytest tests/test_logger.py
```

To view the result of each test:

```powershell
pytest -v tests/test_logger.py
```

To run all the project's tests:

```powershell
pytest
```

## 10. Suggested Exercises

1. Add a test that examines that the recorded message includes the `INFO` level.

2. Design a test that configures the Logger twice for the same file and then examines that the test message has not been written twice in the file.

3. Explain why the third test compares the number of Handlers before and after calling again.

4. Examine what problem might arise when running several tests in a row if the cleanup Fixture did not exist.

5. Explain why `handler.close()` alone is not the same as `logger.removeHandler(handler)`.

## Summary

In this lesson, we learned that:

- `logging` is used for recording the program's events.
- `flush()` helps ensure that buffered messages are written before reading the file.
- Logger tests should examine both file creation and its content.
- Preventing duplicate Handlers prevents messages from being recorded multiple times.
- A Fixture with `autouse=True` can perform cleanup automatically.
- Closing a Handler and detaching it from the Logger are two different stages in resource management.

