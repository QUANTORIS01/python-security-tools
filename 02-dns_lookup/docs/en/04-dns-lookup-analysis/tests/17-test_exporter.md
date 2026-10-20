[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/tests/17-test_exporter.md)

# 17. Test Writing for JSON Export in Python

## Lesson Goal

In this lesson, we examine the `tests/test_exporter.py` file to learn how to test file-writing operations with `pytest`.

Main topics:

- Working with temporary files in tests
- Familiarity with the `tmp_path` fixture
- Examining the creation of a file
- Reading JSON with `json.load()`
- Comparing the original data with the stored data
- Writing tests that are not dependent on the project's actual files

## The Complete Test File Code

```python
import json

from src import export_json


def test_export_json_creates_file(tmp_path):
    output_file = (tmp_path / 'results.json')
    data = {
        'domain': 'google.com',
        'records': ['8.8.8.8'],
    }
    export_json(data, str(output_file))
    assert output_file.exists()


def test_export_json_content(tmp_path):
    output_file = (tmp_path / 'results.json')
    data = {
        'domain': 'google.com',
        'records': ['8.8.8.8', '8.8.4.4'],
    }
    export_json(data, str(output_file))
    with open(output_file, 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)
    assert loaded_data == data
```

## 1. Importing the Libraries

```python
import json

from src import export_json
```

Two items are used in this file:

- `json`: for reading JSON data from a file.
- `export_json`: the project function that stores data in a JSON file.

The `export_json()` function is defined in the `src/exporter.py` file and uses `json.dump()` to write data.

## 2. Familiarity with `tmp_path`

Both tests of this file receive the `tmp_path` argument:

```python
def test_export_json_creates_file(tmp_path):
    ...
```

`tmp_path` is a ready-made fixture in `pytest` that provides the path of a temporary folder dedicated to each test.

Using this path, a test file can be created without changing the project files or the main working directory.

For example:

```python
output_file = tmp_path / 'results.json'
```

The `/` operator here is used to combine the folder path and the file name. The result is a path object of type `pathlib.Path`.

Next:

```python
str(output_file)
```

converts the path into a string so that it can be given to the `export_json()` function.

This approach allows tests to have their own temporary files and not depend on fixed paths on the system.

## 3. First Test: Examining File Creation

The test code:

```python
def test_export_json_creates_file(tmp_path):
    output_file = tmp_path / 'results.json'

    data = {
        'domain': 'google.com',
        'records': ['8.8.8.8'],
    }

    export_json(data, str(output_file))

    assert output_file.exists()
```

### First Step: Specifying the Output Path

```python
output_file = tmp_path / 'results.json'
```

The output file path with the name `results.json` is created in the temporary folder.

### Second Step: Preparing the Data

```python
data = {
    'domain': 'google.com',
    'records': ['8.8.8.8'],
}
```

A simple dictionary is prepared for testing. This data includes the domain name and a list of record values.

This structure is only test data for this specific test; the test does not examine whether this dictionary necessarily has all the fields required for the program's final output.

### Third Step: Executing the Storage Function

```python
export_json(data, str(output_file))
```

The function receives the data and the destination path and writes the file.

### Fourth Step: Examining the File's Existence

```python
assert output_file.exists()
```

The `exists()` method checks whether the target path exists.

If the file has not been created, this expression's value will be `False` and the test will fail.

**Note:** This test only examines the file's existence; it does not by itself prove that the file's content is valid or equal to the input data. This responsibility belongs to the second test.

## 4. Second Test: Examining the JSON Content

The test code:

```python
def test_export_json_content(tmp_path):
    output_file = tmp_path / 'results.json'

    data = {
        'domain': 'google.com',
        'records': ['8.8.8.8', '8.8.4.4'],
    }

    export_json(data, str(output_file))

    with open(output_file, 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)

    assert loaded_data == data
```

This test, in addition to creating the file, examines that the data is stored correctly and can be read back.

### First Step: Storing the Data

Like the first test, a dictionary is prepared and written to the file with `export_json()`. This time, there are two values in the `records` list.

### Second Step: Opening the File for Reading

```python
with open(output_file, 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)
```

In this part:

- `open()` opens the file.
- `'r'` means the file is opened for reading.
- `encoding='utf-8'` specifies the text encoding.
- `with` ensures that the file is properly closed after the block ends.
- `json.load(file)` reads the JSON content and converts it into Python data structures.

For example, a JSON object is converted into a Python dictionary and a JSON array is converted into a Python list.

### Third Step: Comparing the Data

```python
assert loaded_data == data
```

This assertion checks that the data read from the file equals the initial dictionary.

As a result, the test examines items such as preserving the keys, the values, and the order of list elements within the framework of comparing Python structures. The order of dictionary keys is not determining for dictionary equality, but the order of list elements matters.

If the file is not valid and `json.load()` cannot parse it, the test will also stop with an error.

## 5. How the Tests Relate to `src/exporter.py`

The project function's implementation is as follows:

```python
import json


def export_json(data: dict, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
```

This function uses two main operations:

- `open(..., 'w')`: opens the file for writing. If the file already exists, its previous content is replaced.
- `json.dump(data, file, indent=4)`: converts the data to JSON format and writes it to the file. The `indent=4` value makes the output more readable with four-space indentation.

The current tests examine that the file is created and the written data equals the initial data. They do not independently examine the `indent` value or the exact way the JSON is spaced.

## 6. Why Is a Temporary File Better Than a Fixed File?

If a test always creates a file in a fixed path like `results.json` in the project folder, it might:

- Overwrite the project's actual file.
- Conflict with simultaneous test execution.
- Depend on the state left over from a previous run.

Using `tmp_path` reduces these problems, because each test receives its own temporary path.

## 7. Running the Tests

To run the JSON exporter tests:

```powershell
pytest tests/test_exporter.py
```

To view the result of each test:

```powershell
pytest -v tests/test_exporter.py
```

To run the entire test suite:

```powershell
pytest
```

## 8. Suggested Exercises

1. Add a test that stores a dictionary containing multiple keys and multiple lists, then examines the equality of the read data.

2. Design a test that writes twice to the same file path and examines the behavior of `'w'` mode.

3. Explain why `json.load()` is used for reading from a file, but `json.loads()` is used for receiving a JSON string.

4. Examine what behavior `json.load()` shows if the file is empty or contains invalid JSON.

5. Explain why examining the file's existence and examining the file's content in two separate tests can be useful.

## Summary

In this lesson, we learned that:

- `tmp_path` provides a temporary path for test files.
- `Path.exists()` checks a file's existence.
- `json.load()` converts JSON content from a file into Python structures.
- Comparing the read data with the initial data examines the correctness of the storage.
- File-writing tests should be independent of the project's actual files.

