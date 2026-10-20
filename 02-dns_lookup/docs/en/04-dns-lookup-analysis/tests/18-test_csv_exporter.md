[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/tests/18-test_csv_exporter.md)

# 18. Test Writing for CSV Export in Python

## Lesson Goal

In this lesson, we examine the `tests/test_csv_exporter.py` file to learn how to test CSV output with `pytest`.

Main topics:

- Using `tmp_path` to create a temporary file
- Examining the creation of a CSV file
- Reading the file with `csv.reader()`
- Converting CSV rows into Python lists
- Examining the column headers, values, and row order
- The difference between testing CSV output and testing JSON output

## The Complete Test File Code

```python
import csv

from src import export_csv


def test_export_csv_creates_file(tmp_path):
    output_file = (tmp_path / 'results.csv')
    data = {
        'records': [{
            'domain': 'google.com',
            'record_type': 'A',
            'value': '8.8.8.8',
        }]
    }
    export_csv(data, str(output_file))
    assert output_file.exists()


def test_export_csv_content(tmp_path):
    output_file = (tmp_path / 'results.csv')
    data = {
        'records': [{
            'domain': 'google.com',
            'record_type': 'A',
            'value': '8.8.8.8',
        }, {
            'domain': 'google.com',
            'record_type': 'MX',
            'value': 'smtp.google.com',
        }]
    }
    export_csv(data, str(output_file))
    with open(output_file, 'r', newline='', encoding='utf-8') as file:
        rows = list(csv.reader(file))
    assert rows == [[
        'domain',
        'record_type',
        'value',
    ], [
        'google.com',
        'A',
        '8.8.8.8',
    ], [
        'google.com',
        'MX',
        'smtp.google.com',
    ], ]
```

## 1. Importing the Libraries

```python
import csv

from src import export_csv
```

Two components are used in this file:

- `csv`: Python's standard library for reading and writing CSV files.
- `export_csv`: the project function that stores data in CSV format.

The `export_csv()` function is in the `src/csv_exporter.py` file and uses `csv.writer()` to write data.

## 2. First Test: Examining File Creation

The test code:

```python
def test_export_csv_creates_file(tmp_path):
    output_file = tmp_path / 'results.csv'

    data = {
        'records': [{
            'domain': 'google.com',
            'record_type': 'A',
            'value': '8.8.8.8',
        }]
    }

    export_csv(data, str(output_file))

    assert output_file.exists()
```

### First Step: Specifying the File Path

```python
output_file = tmp_path / 'results.csv'
```

`tmp_path` is a ready-made fixture in `pytest` that provides a temporary folder path.

By combining it with the name `results.csv`, the test file path is created. Converting the path to a string with `str(output_file)` also prepares it for sending to the exporter function.

### Second Step: Building the Input Data

```python
data = {
    'records': [{
        'domain': 'google.com',
        'record_type': 'A',
        'value': '8.8.8.8',
    }]
}
```

The input structure includes the `records` key whose value is a list of dictionaries.

Each dictionary holds the information of a DNS record:

- `domain`: the domain name
- `record_type`: the record type
- `value`: the record value

This structure is compatible with how the data is read in `export_csv()`.

### Third Step: Executing the Function and Examining the File

```python
export_csv(data, str(output_file))

assert output_file.exists()
```

The function stores the data in the file and then `exists()` checks that the file has been created.

This test only examines the file's existence; to ensure the correctness of the CSV content, we need the second test.

## 3. Second Test: Examining the CSV Content

The test code:

```python
def test_export_csv_content(tmp_path):
    output_file = tmp_path / 'results.csv'

    data = {
        'records': [
            {
                'domain': 'google.com',
                'record_type': 'A',
                'value': '8.8.8.8',
            },
            {
                'domain': 'google.com',
                'record_type': 'MX',
                'value': 'smtp.google.com',
            },
        ]
    }

    export_csv(data, str(output_file))

    with open(
        output_file,
        'r',
        newline='',
        encoding='utf-8'
    ) as file:
        rows = list(csv.reader(file))

    assert rows == [
        ['domain', 'record_type', 'value'],
        ['google.com', 'A', '8.8.8.8'],
        ['google.com', 'MX', 'smtp.google.com'],
    ]
```

This test creates the file, then reads it again and compares all rows with the expected value.

### First Step: Writing Two Records

In this test, there are two different records:

- The `A` record with the value `8.8.8.8`
- The `MX` record with the value `smtp.google.com`

The existence of two records helps examine that the exporter stores all records, not just the first item.

### Second Step: Opening the File

```python
with open(
    output_file,
    'r',
    newline='',
    encoding='utf-8'
) as file:
    rows = list(csv.reader(file))
```

In this part:

- `'r'` opens the file for reading.
- `newline=''` is the recommended approach for opening a CSV file with the `csv` module so that newline management is performed correctly.
- `encoding='utf-8'` specifies the text encoding.
- `csv.reader(file)` reads the CSV rows.
- `list(...)` places all the read rows in a list.

For this sample data, the `rows` value should consist of three lists:

1. The column headers
2. The row for the `A` record
3. The row for the `MX` record

### Third Step: Examining All Rows

```python
assert rows == [
    ['domain', 'record_type', 'value'],
    ['google.com', 'A', '8.8.8.8'],
    ['google.com', 'MX', 'smtp.google.com'],
]
```

This assertion compares the entire read structure with the expected structure.

As a result, the following are examined at the same time:

- The column headers are correct.
- Each record's values are correctly written.
- The column order is preserved.
- Both records are present in the file.
- The row order is as expected.

This approach is more precise than examining the presence of a few strings in the file, because it examines the CSV structure as rows and columns.

## 4. How the Tests Relate to `src/csv_exporter.py`

The exporter's implementation in the project is like this:

```python
import csv


def export_csv(data: dict, filename: str) -> None:
    with open(
        filename,
        'w',
        newline='',
        encoding='utf-8'
    ) as file:
        writer = csv.writer(file)
        writer.writerow(['domain', 'record_type', 'value'])

        for item in data['records']:
            writer.writerow([
                item['domain'],
                item['record_type'],
                item['value'],
            ])
```

This function has several stages:

1. It opens the file for writing.
2. It creates a `csv.writer` object.
3. It writes the column headers with `writer.writerow()`.
4. It iterates over the records in `data['records']`.
5. For each record, it writes a CSV row.

The second test examines that the output of these stages, after re-reading the file, equals the expected data.

## 5. Why Is `csv.reader()` Better Than Examining the Raw Text?

CSV is a text format for displaying tabular data. If we read the file as raw text, we would have to manage separators, newlines, and special cases ourselves.

Using `csv.reader()` allows Python to parse rows and columns based on CSV rules.

For example, this output:

```text
domain,record_type,value
google.com,A,8.8.8.8
google.com,MX,smtp.google.com
```

is converted into a structure similar to this:

```python
[
    ['domain', 'record_type', 'value'],
    ['google.com', 'A', '8.8.8.8'],
    ['google.com', 'MX', 'smtp.google.com'],
]
```

This structure can be easily compared with `assert`.

## 6. The Difference Between CSV and JSON Testing

In the JSON tests, the file is converted into Python dictionaries and lists with `json.load()` and then compared with the initial data.

In the CSV tests, the file is converted into a list of rows with `csv.reader()`.

| Feature | JSON | CSV |
|---|---|---|
| Reading method in test | `json.load()` | `csv.reader()` |
| Typical structure | Dictionaries and lists | Rows and columns |
| Current content test | Comparing dictionaries | Comparing lists of rows |
| Column headers | Depends on the data structure | The first row of the file |

Both methods examine that the data can be recovered after storage and matches the expectation, but their output structure and reading tools differ.

## 7. Running the Tests

To run the CSV exporter tests:

```powershell
pytest tests/test_csv_exporter.py
```

To view the result of each test:

```powershell
pytest -v tests/test_csv_exporter.py
```

To run all the project's tests:

```powershell
pytest
```

## 8. Suggested Exercises

1. Add a test that has two records from two different domains and examines both in the output.

2. Write a test that examines only the column headers of the CSV file.

3. Explain why `list(csv.reader(file))` is used in this test.

4. Examine if the current test would fail if the column order of the output changed. Explain your reasoning.

5. Design a test for an empty list of records. Based on the current implementation, what row should the file contain?

## Summary

In this lesson, we learned that:

- `tmp_path` is used for creating temporary files in tests.
- `exists()` examines the creation of the file.
- `csv.reader()` converts CSV content into rows and columns usable in Python.
- Comparing the full `rows` examines the column headers, values, and row order.
- Testing file creation and testing its content are two different responsibilities.

