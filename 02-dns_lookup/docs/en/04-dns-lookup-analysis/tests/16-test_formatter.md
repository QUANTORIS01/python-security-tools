[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/tests/16-test_formatter.md)

# 16. Test Writing for DNS Output Formatting in Python

## Lesson Goal

In this lesson, we examine the `tests/test_formatter.py` file to learn how to test the text output of a function with `pytest`.

Main topics:

- Testing functions that produce strings
- Examining the presence of text with `in`
- Building test data with `DNSRecord`
- Testing different DNS records
- Examining the function's behavior when receiving an empty list
- The difference between testing output content and testing its exact format

## The Complete Test File Code

```python
from src import DNSRecord, format_dns_results


def test_format_dns_results():
    results = [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        ),
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.4.4',
        ),
    ]
    output = format_dns_results(results)

    assert 'DOMAIN' in output
    assert 'TYPE' in output
    assert 'VALUE' in output

    assert 'google.com' in output
    assert '8.8.8.8' in output
    assert '8.8.4.4' in output


def test_format_dns_results_with_mx_record():
    results = [
        DNSRecord(
            domain='google.com',
            record_type='MX',
            value='smtp.google.com',
        )
    ]
    output = format_dns_results(results)
    assert 'MX' in output
    assert 'smtp.google.com' in output


def test_format_dns_results_empty():
    output = format_dns_results([])
    assert output == 'No DNS records found.'
```

## 1. Importing the Required Components

```python
from src import DNSRecord, format_dns_results
```

In this file, two components from the project are used:

- `DNSRecord`: the data model that holds the information of a DNS record.
- `format_dns_results`: the function that converts a list of records into text suitable for display in the terminal.

The `format_dns_results()` function is defined in the `src/formatter.py` file. This function builds a text table for non-empty results and returns a specific message for an empty result.

## 2. Testing the Formatting of Multiple Records

The test code:

```python
def test_format_dns_results():
    results = [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        ),
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.4.4',
        ),
    ]

    output = format_dns_results(results)

    assert 'DOMAIN' in output
    assert 'TYPE' in output
    assert 'VALUE' in output

    assert 'google.com' in output
    assert '8.8.8.8' in output
    assert '8.8.4.4' in output
```

### First Step: Building Test Data

In this part, two `DNSRecord` objects are created. Both relate to the domain `google.com` and the record type `A`, but their IP values are different.

This data is created directly in the test; therefore, running this test does not require the Internet or a real DNS request.

### Second Step: Executing the Formatting Function

```python
output = format_dns_results(results)
```

The function receives the list of records and places the text output in the `output` variable.

For example, the output might look like this:

```text
DOMAIN                         TYPE     VALUE
----------------------------------------------------------------------
google.com                     A        8.8.8.8
google.com                     A        8.8.4.4
```

The exact spacing and the column arrangement come from the formatted strings in the function's implementation.

### Third Step: Examining the Column Headers

```python
assert 'DOMAIN' in output
assert 'TYPE' in output
assert 'VALUE' in output
```

The `in` operator checks whether one string exists in another string.

For example:

```python
assert 'DOMAIN' in output
```

If the header `DOMAIN` is not present in the output, the test fails.

### Fourth Step: Examining the Record Data

```python
assert 'google.com' in output
assert '8.8.8.8' in output
assert '8.8.4.4' in output
```

These assertions check that the domain name and both IP values are present in the output.

**Note:** This test examines the presence of data, not the exact column order, number of spaces, or the complete table structure. Therefore, some changes in the output's appearance might occur and the test would still pass.

## 3. Testing the Formatting of an MX Record

The test code:

```python
def test_format_dns_results_with_mx_record():
    results = [
        DNSRecord(
            domain='google.com',
            record_type='MX',
            value='smtp.google.com',
        )
    ]

    output = format_dns_results(results)

    assert 'MX' in output
    assert 'smtp.google.com' in output
```

This test checks that formatting does not work only for `A` records and can also display data with the `MX` record type.

MX records are used to specify a domain's email-receiving servers. In this test, the value `smtp.google.com` is only sample data for testing the formatting.

The two final assertions check that the record type and its value are present in the output.

This test also shows that the formatting function receives the data from the `DNSRecord` fields and is not limited to a specific record type for displaying them.

## 4. Testing the Empty Result

The test code:

```python
def test_format_dns_results_empty():
    output = format_dns_results([])
    assert output == 'No DNS records found.'
```

In this case, the function receives an empty list:

```python
[]
```

The output is expected to be exactly equal to the following string:

```text
No DNS records found.
```

Unlike the previous tests, here the `==` operator is used:

```python
assert output == 'No DNS records found.'
```

This comparison examines the complete equality of the two strings; therefore, the presence of extra spaces or newlines in the output could also cause the test to fail.

This behavior differs from the previous tests:

- `in`: checks that part of the text exists in the output.
- `==`: checks that the complete output value equals the expected value.

## 5. How the Tests Relate to the Formatter File

The `format_dns_results()` function has two main paths.

### First Path: Empty List

If no records exist, the function returns the following message:

```python
'No DNS records found.'
```

The `test_format_dns_results_empty()` test examines this behavior precisely.

### Second Path: List with Records

If the list is not empty, the function:

1. Builds the column headers `DOMAIN`, `TYPE`, and `VALUE`.
2. Adds a separator line.
3. For each record, produces a text line.
4. Converts the lines into a string with `'\n'.join(lines)`.

The first and second tests examine that the expected content is present in this string.

## 6. Do the Tests Fully Examine the Table's Appearance?

In the current state, the tests focus on **the presence of important content**. This method is flexible against minor formatting changes.

However, if the goal is to also guarantee the exact spacing and column order, a separate test can be written for the complete output.

For example, a complementary test could check that the output is exactly equal to an expected string. Such a test should also consider the separator line, spaces, and newlines.

This is useful when the appearance of the terminal output is part of the program's contract and an unwanted change in the table's appearance is not acceptable.

## 7. Running the Tests

To run only the Formatter tests:

```powershell
pytest tests/test_formatter.py
```

To view the test names and the result of each:

```powershell
pytest -v tests/test_formatter.py
```

To run all the project's tests:

```powershell
pytest
```

## 8. Suggested Exercises

1. Add a test that examines the presence of an `AAAA` record in the output.

2. Write a test that passes multiple different domains to the function and examines the presence of all domains in the output.

3. Explain why the empty-result test uses `==`, but the column header test uses `in`.

4. Examine if one of the column headers changes from `VALUE` to `DATA`, which test would fail and why.

5. Design a complementary test that compares the complete table output with an expected string. What is its advantage and what cost does it create in terms of test maintenance?

## Summary

In this lesson, we learned that:

- Test data can be created directly by constructing `DNSRecord` objects.
- The `in` operator is suitable for examining the presence of a specific part of the output.
- The `==` operator examines the complete equality of the output.
- The current tests examine the column headers and record values.
- The Formatter function provides a specific message for an empty list.
- Testing the output content and testing the exact table format have two different goals.

