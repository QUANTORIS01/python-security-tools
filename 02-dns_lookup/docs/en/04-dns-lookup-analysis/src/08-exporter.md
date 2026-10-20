[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/src/08-exporter.md)

# Chapter Four: DNS Lookup Project Code Analysis

## Lesson 8: Exporting to JSON Format in Python

### 1. Lesson Goal

In this lesson, we will learn:

- What JSON is and why it is used for data exchange.
- How the `json` module in Python converts data to JSON.
- How to create or open a file with `open()` and `with`.
- What role `encoding='utf-8'` and `indent=4` play.
- Why the export capability has been kept separate from the main DNS lookup logic.

### 2. Examining the `exporter.py` Code

The file content:

```python
import json


def export_json(data: dict, filename: str) -> None:
    """
    Export DNS results to a JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
```

This file defines a function named `export_json()` that takes two inputs:

- `data`: the data to be stored in the file.
- `filename`: the name or path of the target file.

The function's output type is specified with `-> None`; meaning the function is not intended to return a specific result, and its main task is storing data.

### 3. What Is JSON?

JSON stands for JavaScript Object Notation; a text format for displaying and exchanging structured data.

For example:

```json
{
    "domain": "example.com",
    "record_type": "A",
    "values": [
        "192.0.2.10",
        "192.0.2.11"
    ]
}
```

This sample displays the information of a hypothetical DNS lookup in a structured format.

JSON is supported in different languages and tools; that is why it is suitable for storing results and transferring them between programs.

### 4. Importing the `json` Module

```python
import json
```

The Python standard `json` module provides capabilities for converting Python data to JSON and converting JSON to Python data.

In this file, the `json.dump()` function is used; this function writes data directly to a file object.

### 5. Opening the File with `open()`

```python
with open(filename, 'w', encoding='utf-8') as file:
```

This line has several important parts.

**`filename`**

The name or path of the file in which the data is stored.

**`'w'`**

Opens the file in write mode. If the file does not exist, it is usually created; if it already exists, its previous content will be replaced.

Therefore, if the previous data is to be preserved, the behavior of this mode must be considered when designing the storage process.

**`encoding='utf-8'`**

Specifies the text encoding of the file. UTF-8 is suitable for storing text and characters of different languages, including Persian.

**`with`**

Using `with` causes the file to be properly closed after the managed block ends; even if an error occurs while executing the operation.

This pattern is very common and recommended for working with files in Python.

### 6. Writing Data with `json.dump()`

The main storage line:

```python
json.dump(data, file, indent=4)
```

The `json.dump()` function converts Python data to JSON format and writes it to the specified file.

Its two main arguments are:

- `data`: the data to be stored.
- `file`: the file object opened for writing.

The `indent=4` parameter causes the output to be formatted with four-space indentation. This makes the file easier for humans to read.

For example, compact JSON might look like this:

```json
{"domain":"example.com","record_type":"A","values":["192.0.2.10"]}
```

With proper indentation, the same data becomes more readable:

```json
{
    "domain": "example.com",
    "record_type": "A",
    "values": [
        "192.0.2.10"
    ]
}
```

The actual file content depends on the value passed to the `data` argument when calling `export_json()`.

### 7. What Types of Data Can Be Stored?

The `data` parameter in this function is specified with a type hint of type `dict`. This means a dictionary is declared as the expected input type.

The `json` module can convert standard convertible types, such as dictionaries, lists, strings, numbers, booleans, and `None`, to JSON equivalents.

But not every Python object is directly convertible to JSON. For example, if the data contains instances of the `DNSRecord` class, one should not assume that `json.dump()` can store them without extra conversion.

That is why data to be exported must be converted into a JSON-compatible structure.

### 8. How Export Relates to the Tool's Architecture

In the DNS Lookup architecture, each part has a separate responsibility:

- `resolver.py` performs the DNS request.
- `results.py` converts responses into `DNSRecord` objects.
- `formatter.py` formats results for display in the terminal.
- `exporter.py` stores JSON-compatible data in a file.

Keeping `exporter.py` separate allows the storage method to be changed without placing the DNS request execution logic in the same file.

Also, the `export_json()` function does not perform a DNS request itself; it only writes the data it receives to a file.

### 9. Error Behavior During Storage

The current function does not define custom management for file errors. Therefore, if the target path is not writable, the target folder does not exist, or the data is not convertible to JSON, the corresponding error can be propagated to the caller.

This does not necessarily mean the design is incomplete; error management should be done in proportion to each layer's responsibility and the program's needs. For example, the layer that executes the user's command can decide how to convert the storage error into an understandable message.

Another point is that `'w'` mode replaces the previous file content. Therefore, when using this function, the target file name and the expected storage behavior must be clear.

### 10. Practice Exercises

**Exercise 1 — Building JSON**

Create a simple dictionary containing a domain, a record type, and a list of values, and save it with `export_json()` to a file named `results.json`.

**Exercise 2 — The Difference Between `dump()` and `dumps()`**

In the official Python documentation, examine the difference between these two functions:

- `json.dump()`
- `json.dumps()`

Explain why `dump()` is used in the current file.

**Exercise 3 — Examining the Output File**

After saving the data, open the JSON file in a text editor. Check whether the four-space indentation has been applied or not.

**Exercise 4 — Write Mode Behavior**

Create a file with content, then run `export_json()` on the same file. Examine the result and explain what effect `'w'` mode has on the previous content.

### 11. Summary

In this lesson, we examined the `export_json()` function and became familiar with several important Python capabilities:

- The standard `json` module for converting data to JSON
- `open()` for opening a file
- `with` for managing the file's lifecycle
- `encoding='utf-8'` for text encoding
- `indent=4` for making the output more readable

This part of the tool enables saving results and, by keeping the file operation separate from the DNS logic, contributes to maintaining the project's orderly structure.
