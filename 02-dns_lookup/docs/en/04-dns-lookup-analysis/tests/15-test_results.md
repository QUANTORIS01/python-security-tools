[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/tests/15-test_results.md)

# 15. Test Writing for Building DNS Results in Python

## Lesson Goal

In this lesson, we examine the `tests/test_results.py` file to learn how to test the `build_dns_results()` function using `pytest`.

Main topics:

- Testing functions that depend on other functions
- Using `monkeypatch` to simulate the output of a function
- Examining the creation of `DNSRecord` objects
- Testing single, multiple, and empty results
- Comparing Python lists and objects with `assert`

## The Complete Test File Code

```python
from src import DNSRecord, build_dns_results


def test_build_dns_results(monkeypatch):
    monkeypatch.setattr('src.results.lookup_record', lambda domain, record_type: ['8.8.8.8'])
    results = build_dns_results('google.com', 'A')
    assert results == [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        )
    ]


def test_build_dns_results_multiple_records(monkeypatch):
    monkeypatch.setattr('src.results.lookup_record', lambda domain, record_type: ['8.8.8.8', '8.8.4.4'])
    results = build_dns_results('google.com', 'A')
    assert results == [
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


def test_build_dns_results_empty(monkeypatch):
    monkeypatch.setattr('src.results.lookup_record', lambda domain, record_type: [])
    results = build_dns_results('google.com', 'A')
    assert results == []
```

## 1. Importing the Required Components

```python
from src import DNSRecord, build_dns_results
```

In this file, two components from the project are imported:

- `DNSRecord`: the data model that holds the information of each DNS record.
- `build_dns_results`: the function that converts the Resolver's output into a set of `DNSRecord` objects.

The behavior of the function under test in the `src/results.py` file is as follows:

```python
def build_dns_results(domain: str, record_type: str) -> list[DNSRecord]:
    values = lookup_record(domain, record_type)
    return [
        DNSRecord(
            domain=domain,
            record_type=record_type,
            value=value,
        )
        for value in values
    ]
```

This function first calls `lookup_record()` and then, for each received value, creates a `DNSRecord` object.

## 2. Why Should We Simulate the Function's Dependency?

The `build_dns_results()` function depends on the `lookup_record()` function. If a real Resolver is executed during the test, the test might depend on the network and the DNS servers' responses.

But the goal of this file is to test the process of building results itself; not to test network communication.

Therefore, we simulate the output of `lookup_record()` so that we can precisely specify what data the function receives.

For this purpose, `monkeypatch` is used.

## 3. Testing the Construction of a Single Result

The test code:

```python
def test_build_dns_results(monkeypatch):
    monkeypatch.setattr(
        'src.results.lookup_record',
        lambda domain, record_type: ['8.8.8.8']
    )

    results = build_dns_results('google.com', 'A')

    assert results == [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        )
    ]
```

### First Step: Replacing the Dependent Function

```python
monkeypatch.setattr(
    'src.results.lookup_record',
    lambda domain, record_type: ['8.8.8.8']
)
```

This statement temporarily replaces the name `lookup_record` in the `src.results` module's namespace with a simple function.

The substitute function, upon receiving the domain and record type, always returns this list:

```python
['8.8.8.8']
```

An important point is that the replacement path is `src.results.lookup_record`; that is, the same name that the `build_dns_results()` function uses in the `src.results` module.

### Second Step: Executing the Function Under Test

```python
results = build_dns_results('google.com', 'A')
```

The function receives the domain `google.com` and the record type `A`. Then it converts the simulated value into a `DNSRecord` object.

### Third Step: Examining the Result

```python
assert results == [
    DNSRecord(
        domain='google.com',
        record_type='A',
        value='8.8.8.8',
    )
]
```

This statement checks that the output contains exactly one object with three expected values:

| Field | Expected Value |
|---|---|
| `domain` | `google.com` |
| `record_type` | `A` |
| `value` | `8.8.8.8` |

Because `DNSRecord` is defined with `@dataclass`, the comparison of objects is performed based on the values of their fields. Therefore, there is no need to separately examine each field in this test.

## 4. Testing the Construction of Multiple Results

The test code:

```python
def test_build_dns_results_multiple_records(monkeypatch):
    monkeypatch.setattr(
        'src.results.lookup_record',
        lambda domain, record_type: ['8.8.8.8', '8.8.4.4']
    )

    results = build_dns_results('google.com', 'A')

    assert results == [
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
```

In this test, the substitute function returns two values:

```python
['8.8.8.8', '8.8.4.4']
```

The `build_dns_results()` function must create a separate object for each value.

The expected result includes two `DNSRecord` objects that both have the same domain and record type, but their `value` fields differ.

This test examines two properties:

1. For each received value, an object is created.
2. The order of results is preserved.

In the current implementation, this behavior is performed using list comprehension:

```python
return [
    DNSRecord(
        domain=domain,
        record_type=record_type,
        value=value,
    )
    for value in values
]
```

The expression `for value in values` causes the function to iterate over the values in order and create an object for each value.

## 5. Testing the Empty Result

The test code:

```python
def test_build_dns_results_empty(monkeypatch):
    monkeypatch.setattr(
        'src.results.lookup_record',
        lambda domain, record_type: []
    )

    results = build_dns_results('google.com', 'A')

    assert results == []
```

In this test, the simulated function returns no values.

Therefore, `values` will be an empty list:

```python
[]
```

When the list comprehension runs on an empty list, no object is created and the output will also be an empty list.

This test ensures that the function still provides a valid and predictable output in the absence of a DNS response.

## 6. How These Tests Relate to the Project Architecture

The data flow in this part of the project is as follows:

1. `lookup_record()` returns DNS values as strings.
2. `build_dns_results()` places each value in a `DNSRecord` object.
3. Other parts of the program can work with structured data instead of raw strings.

For example, the following raw value:

```python
'8.8.8.8'
```

after processing, is converted into an object with specific fields:

```python
DNSRecord(
    domain='google.com',
    record_type='A',
    value='8.8.8.8',
)
```

This separation causes the responsibility of receiving the DNS response to be separate from the responsibility of building the final data.

## 7. Why Are These Tests Useful?

These three tests cover the function's important cases:

| Test | Behavior Examined |
|---|---|
| `test_build_dns_results` | Building one record |
| `test_build_dns_results_multiple_records` | Building multiple records and preserving order |
| `test_build_dns_results_empty` | Handling an empty result |

Also, by simulating `lookup_record()`, the tests are independent of the real DNS request. As a result, changes in the network state should not change the result of these tests.

Of course, these tests alone do not guarantee the correctness of the real communication with DNS; that responsibility is examined in the Resolver tests.

## 8. Running the Tests

To run the tests of this file:

```powershell
pytest tests/test_results.py
```

To run the tests along with the name of each test:

```powershell
pytest -v tests/test_results.py
```

To run the entire test suite:

```powershell
pytest
```

## 9. Suggested Exercises

1. Add a test that runs `build_dns_results()` with the record type `MX` and examines the `record_type` value.

2. Write a test that receives three fabricated values and checks that the output contains exactly three `DNSRecord` objects.

3. Explain why in this file we simulate `lookup_record()`, but in the Resolver tests we run the `lookup_record()` function itself.

4. If the `build_dns_results()` function incorrectly processes only the first value, which current test would likely reveal this problem? Explain your reasoning.

5. Explain the difference between the `list[str]` and `list[DNSRecord]` outputs and state how using a data model helps the next parts of the program.

## Summary

In this lesson, we learned that:

- `monkeypatch` can replace a function's dependencies for testing.
- Tests should examine the behavior of the function in question separately from its dependent responsibilities.
- `build_dns_results()` converts each received string into a `DNSRecord` object.
- The multiple-record test examines the number and order of results.
- The empty-result test ensures that the function has a valid output even in the absence of data.

