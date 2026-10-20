[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/src/10-logger.md)

# Lesson 10: Event Logging and Log Management in Python

**File under review:** `src/logger.py`

## 1. Lesson Goal

In this lesson, we will learn how to create an event logging system for a program using Python's standard `logging` module.

Logs can be useful for recording important program events, examining errors, and troubleshooting the tool's behavior. In a network tool like DNS Lookup, proper event logging helps examine problems such as operational errors or failed requests; however, this function alone does not record events, but prepares the logger for use in other parts of the program.

## 2. The Complete File Code

```python
import logging


def setup_logger(filename: str) -> logging.Logger:
    """
    Configure and return a file logger.
    """
    logger = logging.getLogger('dns_lookup')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            if handler.baseFilename == filename:
                return logger
    handler = logging.FileHandler(filename, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
```

## 3. Importing the `logging` Module

```python
import logging
```

The `logging` module is part of Python's standard library and is used to record program messages.

Log messages can have different levels; for example:

| Level | Use |
|---|---|
| `DEBUG` | Detailed information for troubleshooting |
| `INFO` | Normal and important program events |
| `WARNING` | Unusual conditions that do not necessarily stop the program's execution |
| `ERROR` | Errors that have caused an operation to fail |
| `CRITICAL` | Very serious problems |

Choosing the appropriate level makes the recorded messages appropriate to the program's needs.

## 4. Defining the `setup_logger` Function

```python
def setup_logger(filename: str) -> logging.Logger:
```

This function receives the name or path of the log file and returns an object of type `logging.Logger`.

- `filename: str` specifies that the expected input is a string.
- `-> logging.Logger` indicates the type of the output object.

This function is designed to configure the logger; logging messages is usually done after receiving the logger and with methods like `logger.info()` or `logger.error()`.

## 5. Getting the Logger with a Specific Name

```python
logger = logging.getLogger('dns_lookup')
```

The `logging.getLogger()` function receives a logger with a specific name.

In this project, the logger's name is `dns_lookup`. Calling `getLogger()` again with the same name, in the same Python execution environment, usually returns the same logger object; meaning a completely new logger is not created each time.

This feature is useful for a program whose several parts use a shared logger.

## 6. Setting the Message Recording Level

```python
logger.setLevel(logging.INFO)
```

This line sets the logger's level to `INFO`.

As a result, messages with the `INFO` level and higher levels such as `WARNING`, `ERROR`, and `CRITICAL` pass through the logger's level filter. `DEBUG` messages are usually not recorded with this setting.

An important point is that the logger level and the handler level are two separate settings. In this code, the logger level is explicitly set, but no independent level is set for the handler; therefore, the handler level follows its default setting.

## 7. Preventing Propagation of Messages to the Parent Logger

```python
logger.propagate = False
```

By default, messages of a named logger can be propagated to parent loggers after passing through their own handlers.

Setting `propagate = False` stops this propagation.

Why is this useful?

If a logger has both its own dedicated handler and its messages are propagated to parent handlers, a message might be displayed or recorded more than once.

This setting helps control the message propagation path; especially when the program wants to keep the log output in a specific file.

## 8. Examining the Existing Handlers

```python
for handler in logger.handlers:
    if isinstance(handler, logging.FileHandler):
        if handler.baseFilename == filename:
            return logger
```

This part is one of the important points of our implementation.

### `logger.handlers`

Each logger can have one or more handlers. A handler specifies where the log message is sent; for example, to a file or console.

### `isinstance()`

```python
isinstance(handler, logging.FileHandler)
```

This expression checks whether the current handler is of type `logging.FileHandler`.

`FileHandler` is a type of handler that writes log messages to a file.

### `handler.baseFilename`

This attribute specifies the file path associated with the `FileHandler`.

Our code compares the existing handler's path with `filename`. If a `FileHandler` for the same path already exists, the function immediately returns the same logger:

```python
return logger
```

As a result, for the same logger and the same file path, a duplicate handler is not added.

### Why Is This Examination Important?

Suppose the function is called multiple times with the same name:

```python
logger = setup_logger('dns_lookup.log')
logger = setup_logger('dns_lookup.log')
```

Without examining the existing handlers, each call might add a new handler. In such a situation, a message might be written multiple times in one file.

Our current logic controls this duplication for file handlers with the same path.

**Technical note:** The comparison of `baseFilename` with `filename` is done directly. Different paths that point to the same file, such as relative and absolute paths, might not be exactly equal. If the program deals with various paths in the future, comparing normalized paths can be considered.

## 9. Creating the FileHandler

```python
handler = logging.FileHandler(filename, encoding='utf-8')
```

If a file handler with the target path is not found, a new `FileHandler` is created.

Two important arguments of this line are:

- `filename`: the path of the target file.
- `encoding='utf-8'`: the encoding used for writing text.

With UTF-8, text messages, including Persian texts, can be stored in the log file.

Note: `FileHandler` opens the file in append mode by default. Therefore, creating a new handler for an existing file usually does not erase its previous content; new messages are added to the end of the file.

## 10. Defining the Log Message Format

```python
formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(message)s'
)
```

`logging.Formatter` specifies the display format of each log message.

In this project, the format consists of three parts:

- `%(asctime)s`: the time the message was recorded.
- `%(levelname)s`: the message level, such as `INFO` or `ERROR`.
- `%(message)s`: the main message text.

For example, if a message with `INFO` level and text `DNS lookup completed` is recorded, the output might look like:

```text
2026-10-13 10:30:00,123 INFO DNS lookup completed
```

The exact time and format depend on the execution time and the formatter settings; this line is only a hypothetical sample of the output format.

The presence of time, level, and message text helps events be recognizable when examining the log file.

## 11. Attaching the Formatter to the Handler

```python
handler.setFormatter(formatter)
```

In this stage, the format we have defined is attached to the handler.

As a result, the messages the handler receives will be prepared with this format.

Separating the formatter from the handler has a specific design advantage: the message destination and the way it is formatted are two separate responsibilities.

## 12. Adding the Handler to the Logger

```python
logger.addHandler(handler)
```

Creating a handler alone is not enough; we must attach it to the logger.

With `addHandler()`, we specify that the logger should use this handler to send messages.

After this stage, messages that pass the level filter can be directed to the file through the handler.

## 13. Returning the Logger

```python
return logger
```

At the end, the function returns the configured logger.

Other parts of the program can receive this object and record their messages. For example:

```python
logger = setup_logger('dns_lookup.log')

logger.info('DNS lookup started')
logger.warning('No DNS records returned')
logger.error('DNS lookup failed')
```

This snippet is a sample of how to use the function; the message texts are chosen only to demonstrate the logger's behavior.

## 14. A Few Notes About the Actual Behavior of This Implementation

To understand the code precisely, we must distinguish between "preparing the logger" and "recording an event".

The `setup_logger()` function:

1. Gets the named logger.
2. Sets the message recording level.
3. Disables propagation to the parent logger.
4. Examines whether a file handler exists for the given path.
5. If needed, creates the handler and formatter and attaches them to the logger.
6. Returns the logger.

The function itself does not produce any log messages; recording messages requires calls like `logger.info()` or `logger.error()`.

Also, this function does not remove file handlers with different paths. If the logger already has a file handler for another path, the new handler might also be added to it. This behavior can be useful for recording to multiple files, but should be consciously considered when designing the logging policy.

## 15. Practice Exercises

### Exercise 1: Examining the Log Level

Create a logger with this function and record messages at `DEBUG`, `INFO`, and `ERROR` levels.

Check which messages pass the logger's level filter with the current setting.

### Exercise 2: Examining Duplicate Handler Prevention

Call the function twice with the same file name.

- Is a new file handler added on the second call?
- Which part of the code prevents this?

### Exercise 3: Examining Different Paths

Call the function with two different file names and then record a message.

Check, based on the handlers attached to the shared logger, in which files the message is recorded.

### Exercise 4: Changing the Format

Change the formatter's format so that the message level and its text are displayed with a clear separator.

Then record an `INFO` message and examine the output difference.

## 16. Summary

In this lesson, we became familiar with the important components of the `logging` module:

- `getLogger()` for getting a named logger
- `setLevel()` for specifying the minimum message level
- `propagate` for controlling message propagation to parent loggers
- `FileHandler` for writing messages to a file
- `Formatter` for specifying the output format
- `addHandler()` for attaching the message recording destination to the logger

In the DNS Lookup project, the `logger.py` file is responsible for preparing the event-logging infrastructure. Examining the existing handlers also helps prevent repeated calls to the function with the same path from creating duplicate file handlers.
