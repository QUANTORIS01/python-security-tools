[🇮🇷 فارسی](/01-port_scanner/docs/fa/04-port-scanner/tests/16-test-exporter.md)

# A Complete Review of the `test_exporter.py` File

# Introduction

So far in the testing section, we have learned how to:

✅ Test validation functions

✅ Test network scanning functions

✅ Test service detection

---

But now we enter a different type of test.

---

So far, most of our functions' outputs were:

```python
True
False
list
str
```

---

But this time, we are facing something different:

```text
A file
```

---

Meaning we must check:

```text
Was the file really created?
```

and

```text
Was the file's content stored correctly?
```

---

This is exactly what:

```text
test_exporter.py
```

does.

---

# The Goal of the File

Goal:

```text
Testing export_json()
```

---

If you remember, in:

```text
src/exporter.py
```

we had:

```python
def export_json(
    data: dict,
    filename: str
):
```

---

The task was:

```text
Saving data to a JSON file
```

---

Now we must make sure:

```python
export_json()
```

really works correctly.

---

# File Content

```python
import json

from src import export_json


def test_export_json_creates_file(tmp_path):
    output_file = tmp_path / "results.json"
    data = {
        "target": "127.0.0.1",
        "open_ports": [80, 443]
    }
    export_json(data, str(output_file))
    assert output_file.exists()


def test_export_json_content(tmp_path):
    output_file = tmp_path / "results.json"
    data = {
        "target": "127.0.0.1",
        "open_ports": [80, 443]
    }
    export_json(data, str(output_file))

    with open(output_file, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
    assert loaded_data == data
```

---

# The First Import

```python
import json
```

---

Why?

---

Because later we want to read the created file.

---

To read JSON, we use:

```python
json.load()
```

---

# The Second Import

```python
from src import export_json
```

---

The function that is going to be tested.

---

# The First Test

```python
def test_export_json_creates_file(
    tmp_path
):
```

---

Goal:

```text
Checking that the file is created
```

---

# What Is `tmp_path`?

One of pytest's wonderful features.

---

Pytest automatically:

```python
tmp_path
```

injects into the function.

---

This path is:

```text
A temporary directory
```

---

Example:

```text
C:\Temp\pytest-1234\
```

---

Or:

```text
/tmp/pytest/
```

---

After the test ends:

```text
It is automatically deleted.
```

---

# Why Do We Use `tmp_path`?

Suppose we create a real file:

```python
results.json
```

---

Problems:

❌ Extra files remain on the system

❌ Tests affect each other

❌ The project gets cluttered

---

That is why:

```python
tmp_path
```

is the professional way to test files.

---

# Building the File Path

```python
output_file =
    tmp_path / "results.json"
```

---

Output:

```text
/tmp/pytest/results.json
```

---

Or something similar.

---

# Building the Test Data

```python
data = {
    "target": "127.0.0.1",
    "open_ports": [80, 443]
}
```

---

The data that is going to be saved.

---

# Running the Function

```python
export_json(
    data,
    str(output_file)
)
```

---

Flow:

```python
data
```

↓

```python
export_json()
```

↓

```python
results.json
```

---

# Checking the File's Existence

```python
assert output_file.exists()
```

---

The method:

```python
exists()
```

checks:

```text
Does the file exist?
```

---

If the file was created:

```python
True
```

---

If it was not created:

```python
False
```

---

As a result:

```python
assert
```

fails the test.

---

# The Goal of the First Test

Just checking:

```text
That the file is created
```

---

Not its content.

---

# The Second Test

```python
def test_export_json_content(
    tmp_path
):
```

---

This test is more important.

---

Why?

---

Because the file's existence alone is not enough.

---

The file might be created but:

```text
With the wrong data.
```

---

# Creating the File

Exactly like the previous test:

```python
output_file =
    tmp_path / "results.json"
```

---

And:

```python
data = {...}
```

---

And:

```python
export_json(...)
```

---

# Opening the File

```python
with open(
    output_file,
    "r",
    encoding="utf-8"
) as file:
```

---

The mode:

```python
"r"
```

means:

```text
Read Mode
```

---

# Reading the JSON

```python
loaded_data =
    json.load(file)
```

---

If the file contains:

```json
{
    "target": "127.0.0.1",
    "open_ports": [80, 443]
}
```

---

The output is:

```python
{
    "target": "127.0.0.1",
    "open_ports": [80, 443]
}
```

---

Meaning it is converted back into a Dictionary.

---

# Comparing the Data

```python
assert loaded_data == data
```

---

The most important line of the file.

---

If:

```python
loaded_data
```

equals:

```python
data
```

---

The test:

```text
PASS
```

---

If even a single value is different:

```text
FAIL
```

---

# Example

Suppose the function incorrectly saves:

```json
{
    "target": "127.0.0.1"
}
```

---

And forgets:

```python
open_ports
```

---

In this case:

```python
loaded_data == data
```

---

equals:

```python
False
```

---

And the test fails.

---

# What Type of Test Is This?

This file is an example of:

```text
File I/O Testing
```

---

# What Is File I/O?

I/O stands for:

```text
Input / Output
```

---

Meaning:

```text
Reading and writing data
```

---

Examples:

```python
open()
```

---

```python
read()
```

---

```python
write()
```

---

All are I/O.

---

# An Important Point

This file:

```text
Does not just create a file
```

---

Rather:

```text
It also verifies the correctness of the content.
```

---

This is exactly what is done in professional tests.

---

# What If We Did Not Have the Second Test?

Suppose:

```python
export_json()
```

produces an empty file.

---

The first test:

```text
PASS
```

---

Because the file exists.

---

But:

```text
The content is wrong.
```

---

That is why the second test is essential.

---

# pytest Output

If everything is correct:

```bash
pytest
```

---

Output:

```text
===== 2 passed =====
```

---

# Summary

In this session, we learned:

✅ Testing JSON files

✅ What `tmp_path` is

✅ What a Temporary Directory is

✅ What `exists()` is

✅ What File I/O Testing is

✅ What `json.load` is

✅ How to validate the file content

✅ The difference between testing file existence and testing file content

---

# What Will We Learn in the Next Session?

In the next session, we enter the file:

```text
tests/test_cli.py
```

---

This is one of the most important tests of the project.

---

There we will learn:

✅ What Monkeypatch is

✅ How to simulate CLI inputs

✅ How to test `sys.argv`

✅ How to check terminal output

✅ How Entry Point testing is done
