[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/src/09-csv_exporter.md)

# Lesson 9: CSV Export in Python

**File under review:** `src/csv_exporter.py`

## 1. Lesson Goal

In this lesson, we will learn how to save DNS Lookup data in a CSV file using Python's standard `csv` module.

In the DNS Lookup project, we have two methods for saving results:

- **JSON:** suitable for storing structured data and exchanging data between programs.
- **CSV:** suitable for tabular data that can be examined in spreadsheet software or data analysis tools.

## 2. The Complete File Code

```python
import csv


def export_csv(data: dict, filename: str) -> None:
    """
    Export DNS results to a CSV file.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['domain', 'record_type', 'value'])
        for item in data['records']:
            writer.writerow([item['domain'], item['record_type'], item['value']])
```

## 3. Importing the `csv` Module

```python
import csv
```

The `csv` module is part of Python's standard library; therefore, we do not need to install a separate library to use it.

This module provides capabilities for reading and writing CSV files.

CSV stands for *Comma-Separated Values*. In this format, data is stored in rows and columns, and values are usually separated by commas.

## 4. Defining the `export_csv` Function

```python
def export_csv(data: dict, filename: str) -> None:
```

This function takes two inputs:

- `data`: a dictionary containing the data to be stored.
- `filename`: the name or path of the output file.

The `dict` type indicates that we expect the `data` input to be a dictionary. The `str` type also specifies that the file name is received as a string.

The expression `-> None` indicates that the function is not designed to return a value; its task is to write information to a file.

Note: These type hints alone do not check the input types at runtime.

## 5. Opening the File for Writing

```python
with open(filename, 'w', newline='', encoding='utf-8') as file:
```

This line brings together several important Python concepts.

### `open()`

The `open()` function opens the file.

### `'w'` Mode

The letter `w` stands for *write*; meaning the file is opened for writing.

If the file does not exist, it is usually created. If it already exists, its previous content is erased and writing starts from the beginning.

Therefore, if the previous content needs to be preserved, another method must be used.

### `newline=''`

When working with the `csv` module, using `newline=''` is the recommended approach. This setting allows the CSV module to manage line endings itself and prevents extra blank lines in some environments.

### `encoding='utf-8'`

This option specifies the file's encoding. UTF-8 is suitable for storing text and supporting a wide range of characters.

### Why Do We Use `with`?

The `with` structure ensures that the file is properly closed after the work ends, even if an error occurs while writing.

This method is safer and more readable than manually opening and closing the file.

## 6. Creating a CSV Writer

```python
writer = csv.writer(file)
```

The `csv.writer()` function creates a writer object that can write data in CSV format inside the file.

After this line, the `writer` variable is a tool for writing rows to the file.

Instead of building CSV ourselves by concatenating strings and adding commas, we use the standard module. This approach also helps manage values that themselves contain commas or special characters.

## 7. Writing the Column Headers Row

```python
writer.writerow(['domain', 'record_type', 'value'])
```

The `writerow()` method writes a row to the file.

In this project, the first row contains three headers:

| domain | record_type | value |
|---|---|---|
| Domain name | DNS record type | Record value |

These headers specify the output structure and make reading the data easier.

## 8. Iterating Over Records and Writing Data

```python
for item in data['records']:
    writer.writerow([item['domain'], item['record_type'], item['value']])
```

In this part, the function accesses the `records` key in the `data` dictionary and iterates over its items.

In each loop iteration:

1. A record is placed in the `item` variable.
2. The domain value is read from `item['domain']`.
3. The record type is read from `item['record_type']`.
4. The record value is read from `item['value']`.
5. These three values are written to a new row with `writer.writerow()`.

### A Sample Input

Suppose `data` has the following structure:

```python
data = {
    'records': [
        {
            'domain': 'example.com',
            'record_type': 'A',
            'value': '93.184.216.34',
        },
        {
            'domain': 'example.com',
            'record_type': 'AAAA',
            'value': '2606:2800:220:1:248:1893:25c8:1946',
        },
    ]
}
```

And the function is called with:

```python
export_csv(data, 'dns_results.csv')
```

The CSV file will have roughly the following content:

```csv
domain,record_type,value
example.com,A,93.184.216.34
example.com,AAAA,2606:2800:220:1:248:1893:25c8:1946
```

This example only shows the shape of the output data; the DNS values in it are samples.

## 9. How This File Relates to the Project Design

In the DNS Lookup project's architecture, the `csv_exporter.py` file is responsible for converting the prepared data into a CSV file.

This separation has an important advantage: the DNS lookup logic, the result structuring, and the output storage each have a specific responsibility.

Also, this function receives the prepared data instead of performing a DNS lookup. As a result, the export logic can be examined and tested independently of network operations.

The `export_csv()` function expects the input structure to include a `records` key, and each record to have three keys: `domain`, `record_type`, and `value`. This data contract must be respected when calling the function.

## 10. Technical Notes and Opportunities for Improvement

The current code produces a simple and specific CSV output. For future developments, the following can be considered:

- **Input structure validation:** If `records` or one of the expected keys does not exist, the function will receive an error. Input errors can be managed if needed.
- **File error management:** An invalid path or lack of write permission can cause an error. The way to manage these errors should be consistent with the project's error policy.
- **Support for large files:** If the data volume increases, iterating and writing row by row helps avoid having to convert all records into a large string at once.
- **Compatibility with spreadsheet software:** In some regional settings, the expected separator might be different. If needed, the separator can be set in `csv.writer()`.

These items are suggestions for development, not a sign that the current implementation is inefficient.

## 11. Practice Exercises

### Exercise 1: Examining the Output

Pass the sample dictionary from this lesson to the function and examine the generated CSV file.

- How many data rows are in the file?
- In which row are the column headers located?

### Exercise 2: Adding a Record

Add a new record with type `MX` to the `records` list and check whether the function saves it in the file too.

### Exercise 3: Examining Write Mode

Create a CSV file and put some text in it. Then run the function with the same file name.

Check what effect using `'w'` mode has on the previous file content.

### Exercise 4: Examining Invalid Input

Run the function with a dictionary that does not have the `records` key.

- What error occurs?
- How can the data structure be examined before writing the file?

## 12. Summary

In this lesson, we became familiar with the main components of CSV export in Python:

- `csv.writer()` for creating a CSV writer
- `writerow()` for writing each row
- `open()` for opening a file
- `with` for managing the file's lifecycle
- `newline=''` for proper compatibility with the CSV module
- `encoding='utf-8'` for specifying text encoding

In the DNS Lookup project, this file has a specific responsibility: **it saves DNS data in a tabular form usable in other tools.**
