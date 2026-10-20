[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/tests/14-test_resolver.md)

# 14. Test Writing for DNS Resolver in Python

## Lesson Goal

In this lesson, we examine the `tests/test_resolver.py` file to learn how to test the behavior of the `lookup_record()` function without sending real requests to DNS servers.

Main topics of this lesson:

- Familiarity with `monkeypatch` in `pytest`
- Simulating DNS responses with simple classes
- Testing single and multiple responses
- Testing DNS error management
- Examining the difference between DNS errors and Timeout errors
- Writing tests that are independent of the network and the Internet

## The Complete Test File Code

```python
import dns.resolver
import pytest

from src import lookup_record
from src.exception import DNSTimeoutError


def test_lookup_a_record(monkeypatch):
    class FakeAnswer:
        def __str__(self):
            return '1.1.1.1'

    monkeypatch.setattr('dns.resolver.resolve', lambda *args, **kwargs: [FakeAnswer()])
    result = lookup_record('example.com', 'A')
    assert result == ['1.1.1.1']


def test_lookup_multiple_records(monkeypatch):
    class FakeAnswer:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return self.value

    monkeypatch.setattr(
        'dns.resolver.resolve', lambda *args, **kwargs: [FakeAnswer('1.1.1.1'), FakeAnswer('8.8.8.8')]
    )
    result = lookup_record('example.com', 'A')
    assert result == ['1.1.1.1', '8.8.8.8']


def test_lookup_nonexistent_domain(monkeypatch):
    def fake_resolve(*args, **kwargs):
        raise dns.resolver.NXDOMAIN

    monkeypatch.setattr('dns.resolver.resolve', fake_resolve)
    result = lookup_record('does-not-exist.com', 'A')
    assert result == []


def test_lookup_record_handles_no_answer(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.NoAnswer

    monkeypatch.setattr(dns.resolver, 'resolve', fake_resolve)
    assert lookup_record('example.com', 'TXT') == []


def test_lookup_record_handles_nxdomain(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.NXDOMAIN

    monkeypatch.setattr(dns.resolver, 'resolve', fake_resolve)
    assert lookup_record('invalid.test', 'A') == []


def test_lookup_record_handles_timeout(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.LifetimeTimeout

    monkeypatch.setattr(dns.resolver, 'resolve', fake_resolve)
    with pytest.raises(DNSTimeoutError):
        lookup_record('google.com', 'MX')
```

## 1. Importing the Libraries

```python
import dns.resolver
import pytest

from src import lookup_record
from src.exception import DNSTimeoutError
```

Each of these imports has a specific role:

- `dns.resolver`: access to the types of responses and exceptions of the `dnspython` library.
- `pytest`: providing testing tools, including `monkeypatch` and `pytest.raises`.
- `lookup_record`: the main function to be tested.
- `DNSTimeoutError`: the project's custom exception for indicating the end of the DNS request timeout.

These tests, instead of re-examining the function's implementation, examine its observable behavior.

## 2. The Concept of Mock and Monkeypatch

When running a real DNS Lookup, the result depends on the network, the DNS server, and the domain's state. These dependencies can cause tests to be slow, unstable, or dependent on the Internet.

To avoid this problem, the tests use **simulation of dependency behavior**.

In `pytest`, the `monkeypatch` tool provides the ability to temporarily replace a function or attribute.

For example:

```python
monkeypatch.setattr(
    'dns.resolver.resolve',
    lambda *args, **kwargs: []
)
```

This statement replaces the `dns.resolver.resolve` function during the test with a function that returns an empty list.

As a result, when `lookup_record()` is executed, no real DNS request is sent; rather, the result determined by the test is returned.

After the test ends, `pytest` automatically reverts the change made.

**Note:** The term Mock generally refers to experimental substitutes. In this file, `monkeypatch` is used to install these substitutes.

## 3. Testing the Retrieval of a Single DNS Record

The test code:

```python
def test_lookup_a_record(monkeypatch):
    class FakeAnswer:
        def __str__(self):
            return '1.1.1.1'

    monkeypatch.setattr(
        'dns.resolver.resolve',
        lambda *args, **kwargs: [FakeAnswer()]
    )

    result = lookup_record('example.com', 'A')

    assert result == ['1.1.1.1']
```

### Step-by-Step Examination

**Step one: Creating a test response**

```python
class FakeAnswer:
    def __str__(self):
        return '1.1.1.1'
```

The `FakeAnswer` class creates a simple and fabricated response.

The special method `__str__()` specifies that when the object is converted to a string, the value `'1.1.1.1'` should be returned.

This is important because the `lookup_record()` function in the project's implementation uses `str(answer)`.

**Step two: Replacing the DNS function**

```python
monkeypatch.setattr(
    'dns.resolver.resolve',
    lambda *args, **kwargs: [FakeAnswer()]
)
```

The main DNS function is replaced with a test function that returns a fabricated response.

**Step three: Executing the function under test**

```python
result = lookup_record('example.com', 'A')
```

The `lookup_record()` function goes through the same path it would in normal execution, but instead of the network, it encounters the fabricated response.

**Step four: Examining the result**

```python
assert result == ['1.1.1.1']
```

This assertion checks that the function's output is exactly equal to the expected list.

## 4. Testing Multiple DNS Records

The test code:

```python
def test_lookup_multiple_records(monkeypatch):
    class FakeAnswer:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return self.value

    monkeypatch.setattr(
        'dns.resolver.resolve',
        lambda *args, **kwargs: [
            FakeAnswer('1.1.1.1'),
            FakeAnswer('8.8.8.8')
        ]
    )

    result = lookup_record('example.com', 'A')

    assert result == ['1.1.1.1', '8.8.8.8']
```

In this test, the `FakeAnswer` class is a bit more flexible:

```python
def __init__(self, value):
    self.value = value
```

The response value is determined when creating the object. The `__str__()` method also returns the same value as a string.

Therefore, several different responses can be created:

```python
FakeAnswer('1.1.1.1')
FakeAnswer('8.8.8.8')
```

This test checks that `lookup_record()` converts all responses to strings and returns them in the form of a list.

**Why is this test important?**

A DNS Query does not necessarily have only one response. For example, a domain can have several A records. Therefore, the function must be able to process a set of responses, not just the first response.

## 5. Testing a Domain That Does Not Exist

The test code:

```python
def test_lookup_nonexistent_domain(monkeypatch):
    def fake_resolve(*args, **kwargs):
        raise dns.resolver.NXDOMAIN

    monkeypatch.setattr(
        'dns.resolver.resolve',
        fake_resolve
    )

    result = lookup_record('does-not-exist.com', 'A')

    assert result == []
```

Here, the substitute function, instead of returning a response, raises the `dns.resolver.NXDOMAIN` exception.

`NXDOMAIN` indicates that the requested domain name does not exist in DNS.

According to the implementation of `src/resolver.py`, this exception is managed and the function returns an empty list:

```python
except (
    dns.resolver.NXDOMAIN,
    dns.resolver.NoAnswer,
    dns.resolver.NoNameservers
):
    return []
```

Therefore, the test examines that the domain's non-existence, instead of stopping the program with an unmanaged exception, is converted into a usable result.

## 6. Testing the Absence of a Response for the Requested Record Type

The test code:

```python
def test_lookup_record_handles_no_answer(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.NoAnswer

    monkeypatch.setattr(
        dns.resolver,
        'resolve',
        fake_resolve
    )

    assert lookup_record('example.com', 'TXT') == []
```

This case is different from `NXDOMAIN`.

- `NXDOMAIN`: the domain name does not exist in DNS.
- `NoAnswer`: for the performed query, the expected response is not available.

In the above test, the substitute function raises the `NoAnswer` exception and the test examines that the output of `lookup_record()` is an empty list.

Here, another form of `monkeypatch.setattr()` is used:

```python
monkeypatch.setattr(
    dns.resolver,
    'resolve',
    fake_resolve
)
```

In this form, instead of providing the path name as a string, the `dns.resolver` object itself and the attribute name `'resolve'` are provided separately.

Both methods can be used to replace this function.

## 7. Testing the NXDOMAIN Error Again

The test code:

```python
def test_lookup_record_handles_nxdomain(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.NXDOMAIN

    monkeypatch.setattr(
        dns.resolver,
        'resolve',
        fake_resolve
    )

    assert lookup_record('invalid.test', 'A') == []
```

This test also examines the same `NXDOMAIN` behavior; with the difference that the test name and the domain used are different.

From the perspective of behavior coverage, the previous test `test_lookup_nonexistent_domain` also examines this same main case. The existence of both tests can help with readability and more explicit naming of the scenarios, but both target the same main line for managing `NXDOMAIN`.

This point shows that **the number of tests alone is not a complete measure of quality**; it matters what independent behavior each test examines.

## 8. Testing Timeout and the Project's Custom Exception

The test code:

```python
def test_lookup_record_handles_timeout(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.LifetimeTimeout

    monkeypatch.setattr(
        dns.resolver,
        'resolve',
        fake_resolve
    )

    with pytest.raises(DNSTimeoutError):
        lookup_record('google.com', 'MX')
```

This test examines the most important behavioral difference in error management.

In the project, the `lookup_record()` function behaves like this when `dns.resolver.LifetimeTimeout` occurs:

```python
except dns.resolver.LifetimeTimeout as exc:
    raise DNSTimeoutError('DNS query timed out') from exc
```

Meaning the `dnspython` library's error is converted into the project's custom exception.

### Why Do We Use `pytest.raises()`?

```python
with pytest.raises(DNSTimeoutError):
    lookup_record('google.com', 'MX')
```

This statement checks that executing the code inside the `with` block raises the `DNSTimeoutError` exception.

If the function returns without this exception or raises another exception, the test will not be successful.

Also note that the test only examines the exception type; it does not examine the error message text or the exception chain.

### Why Is Timeout Different from an Empty Response?

In the project's current design:

- The absence of the domain, the absence of a response, or the unavailability of name servers leads to an empty list.
- The end of the DNS request timeout leads to the `DNSTimeoutError` exception.

This decision allows the caller to distinguish between "no response was found" and "the request did not complete within the specified time."

## 9. How the Tests Relate to the Project Architecture

The simple behavior flow is as follows:

1. `lookup_record()` performs the DNS request through `dns.resolver.resolve()`.
2. Successful responses are converted to strings.
3. Some DNS errors are converted to an empty list.
4. The Timeout error is converted to `DNSTimeoutError`.
5. The `test_resolver.py` file examines these behaviors without needing to send a real DNS request.

This separation is valuable; because the program logic can be tested independently of the Internet's state.

## 10. Running the Tests

To run only the Resolver tests:

```powershell
pytest tests/test_resolver.py
```

To run all the project's tests:

```powershell
pytest
```

To view the details of each test:

```powershell
pytest -v tests/test_resolver.py
```

## 11. Suggested Exercises

1. Add a test that when `dns.resolver.resolve()` returns an empty list, the output of `lookup_record()` is also an empty list.

2. Write a test that simulates the `dns.resolver.NoNameservers` exception and examines the empty output.

3. In the Timeout test, in addition to the exception type, also examine the `DNS query timed out` message.

4. Design a test that examines that `lookup_record()` with two fabricated responses returns both values in the same order received.

5. Explain why using `monkeypatch` makes the tests less dependent on the Internet and the DNS servers' state.

## Summary

In this lesson, we learned that:

- `monkeypatch` is used to temporarily replace dependencies in tests.
- Simple classes like `FakeAnswer` can produce fabricated but controllable responses.
- Successful tests examine the processing of one response and multiple responses.
- The `NXDOMAIN` and `NoAnswer` errors are converted to an empty list in the current design.
- The Timeout error is converted to the custom `DNSTimeoutError` exception.
- Tests independent of the network have faster and more repeatable execution.

