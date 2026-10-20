[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/tests/20-test_cli.md)

# Lesson 20: Testing the Command-Line Interface (CLI) with Pytest

## 1. Lesson Goal

In this lesson, we learn how to test a Python program's command-line interface without connecting to a real DNS server for each test or unintentionally affecting the project's auxiliary files.

By the end of this lesson, we can:

- Test command-line arguments.
- Examine invalid inputs.
- Replace program dependencies with `monkeypatch`.
- Test error management and the program's exit code.
- Distinguish between success testing and error testing.

## The Complete Test File Code

```python
import pytest

from src.cli import create_parser, main
from src import DNSRecord
from src.exception import DNSTimeoutError


class FakeLogger:
    def info(self, *args, **kwargs):
        pass


def test_create_parser():
    parser = create_parser()

    args = parser.parse_args(['google.com', 'A'])
    assert args.domain == 'google.com'
    assert args.record_type == 'A'


def test_main_invalid_domain(monkeypatch):
    monkeypatch.setattr('src.cli.setup_logger', lambda *args, **kwargs: FakeLogger())
    monkeypatch.setattr('sys.argv', ['cli.py', '!!!', 'A'])
    with pytest.raises(SystemExit):
        main()


def test_main_invalid_record_type(monkeypatch):
    monkeypatch.setattr('src.cli.setup_logger', lambda *args, **kwargs: FakeLogger())
    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'BAD'])
    with pytest.raises(SystemExit):
        main()


def test_main_valid_arguments(monkeypatch):
    monkeypatch.setattr('src.cli.setup_logger', lambda *args, **kwargs: FakeLogger())
    monkeypatch.setattr('src.cli.build_dns_results', lambda *args, **kwargs: [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        )
    ])

    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'A'])
    main()


def test_main_handles_timeout(monkeypatch):
    monkeypatch.setattr('src.cli.setup_logger', lambda *args, **kwargs: FakeLogger())
    monkeypatch.setattr('src.cli.build_dns_results', lambda *args, **kwargs: (_ for _ in ()).throw(DNSTimeoutError()))
    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'MX'])
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 1
```

## 2. Importing Dependencies

```python
import pytest

from src.cli import create_parser, main
from src import DNSRecord
from src.exception import DNSTimeoutError
```

Each import has a specific role:

- `pytest`: the tool for executing tests and examining the expected behavior.
- `create_parser`: the function for building the command-line argument parser.
- `main`: the main execution function of the DNS Lookup tool.
- `DNSRecord`: the data model used for simulating the DNS lookup result.
- `DNSTimeoutError`: the project's custom exception for the end of the DNS request timeout.

Architectural note: These tests go directly to the CLI's main function; therefore, they can examine the interaction between input validation, operation execution, report recording, and error management.

## 3. Building the Test Logger

```python
class FakeLogger:
    def info(self, *args, **kwargs):
        pass
```

In the main implementation, the `setup_logger` function returns a real Logger that records messages to a file. But most CLI tests do not need to examine the content of the report file.

That is why we have created a simple test Logger.

### Why Do We Use `FakeLogger`?

The `info` method is called in the main code to record messages such as the start and end of the lookup. The `FakeLogger` class has the same method, but does nothing.

This replacement has several advantages:

- Tests do not depend on creating a report file.
- The CLI behavior can be examined more independently.
- The test's focus remains on the main subject.

The `pass` method means that executing the function intentionally does nothing.

## 4. Testing the Parser Construction

```python
def test_create_parser():
    parser = create_parser()

    args = parser.parse_args(['google.com', 'A'])
    assert args.domain == 'google.com'
    assert args.record_type == 'A'
```

This test examines that `create_parser` correctly receives and interprets positional arguments.

Consider the following command:

```bash
python -m src.cli google.com A
```

In this command:

- `google.com` is the target domain.
- `A` is the DNS record type.

In the test, instead of running the actual command in the terminal, these two values are given directly to `parse_args`.

Then with `assert` we examine that the extracted values are correct.

**Note:** This test examines the parser directly; we have not executed the `main` function yet.

## 5. Testing an Invalid Domain

```python
def test_main_invalid_domain(monkeypatch):
    monkeypatch.setattr(
        'src.cli.setup_logger',
        lambda *args, **kwargs: FakeLogger()
    )
    monkeypatch.setattr('sys.argv', ['cli.py', '!!!', 'A'])

    with pytest.raises(SystemExit):
        main()
```

This test examines that the program prevents normal execution from continuing when receiving an invalid domain.

### Temporarily Changing `sys.argv`

In actual execution, `argparse` receives the arguments from `sys.argv`. In the test, we change this value:

```python
monkeypatch.setattr('sys.argv', ['cli.py', '!!!', 'A'])
```

The list above means that the program name is `cli.py` and the user's arguments include `!!!` and `A`.

Since `!!!` is not a valid domain, the `main` function must execute the error path.

### Why `pytest.raises(SystemExit)`?

In the CLI code, an invalid input ends with `sys.exit(1)`. Python implements this operation by raising the `SystemExit` exception.

Therefore:

```python
with pytest.raises(SystemExit):
    main()
```

means we expect the execution of `main()` to result in `SystemExit`.

If such an exception is not raised, the test will fail.

### Why Do We Also Replace the Logger?

In the invalid domain path, the program does not pass the input before creating the Logger. However, replacing `setup_logger` in this test maintains the uniformity of the test environment and prevents the creation of a real Logger in case of future changes in the code's execution order.

## 6. Testing an Invalid Record Type

```python
def test_main_invalid_record_type(monkeypatch):
    monkeypatch.setattr(
        'src.cli.setup_logger',
        lambda *args, **kwargs: FakeLogger()
    )
    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'BAD'])

    with pytest.raises(SystemExit):
        main()
```

This test is similar to the previous test, but this time the domain is valid and the record type is invalid.

The value `BAD` is not in the set of supported record types; therefore, the `validate_record_type` function must reject it.

This test specifically examines that:

1. The program receives the input from the command line.
2. It validates the record type.
3. If the record type is invalid, it stops normal execution.

This is important; because domain validation alone is not enough. All inputs used in the DNS operation must be examined according to the program's rules.

## 7. Testing a Successful Execution with Valid Input

```python
def test_main_valid_arguments(monkeypatch):
    monkeypatch.setattr(
        'src.cli.setup_logger',
        lambda *args, **kwargs: FakeLogger()
    )
    monkeypatch.setattr(
        'src.cli.build_dns_results',
        lambda *args, **kwargs: [
            DNSRecord(
                domain='google.com',
                record_type='A',
                value='8.8.8.8',
            )
        ]
    )

    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'A'])
    main()
```

This test examines the program's successful execution path.

### Replacing the DNS Lookup Function

The important part of the test is:

```python
monkeypatch.setattr(
    'src.cli.build_dns_results',
    lambda *args, **kwargs: [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        )
    ]
)
```

In the main code, `build_dns_results` performs the DNS lookup operation and converts the results into `DNSRecord` objects.

But in the test, this function is replaced with a substitute function that always returns a specific result.

As a result, the test does not depend on the real DNS response to run.

### Why Do We Use `DNSRecord`?

Because the CLI's main function expects to receive the results with the project model's structure. The test object also has the same expected structure:

- `domain`: the target domain
- `record_type`: the record type
- `value`: the record value

In this way, the continuation of `main`'s execution can format the results and prepare them for output or export.

### Does This Test Examine the Printed Output?

No. This test only executes `main()` and expects the successful execution to end without an unexpected exception.

In this test, `capsys` is not used to examine the printed text, and the terminal output is not directly compared. Therefore, we should not conclude that the output text has also been fully validated in this same test.

## 8. Testing Timeout Management

```python
def test_main_handles_timeout(monkeypatch):
    monkeypatch.setattr(
        'src.cli.setup_logger',
        lambda *args, **kwargs: FakeLogger()
    )
    monkeypatch.setattr(
        'src.cli.build_dns_results',
        lambda *args, **kwargs: (
            _ for _ in ()
        ).throw(DNSTimeoutError())
    )
    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'MX'])

    with pytest.raises(SystemExit) as exc:
        main()

    assert exc.value.code == 1
```

This test examines one of the CLI's most important error paths: when the DNS request encounters a Timeout.

### Simulating Timeout

The substitute function `build_dns_results`, instead of returning a result, raises the `DNSTimeoutError` exception.

The following expression might seem unusual at first glance:

```python
(_ for _ in ()).throw(DNSTimeoutError())
```

This expression uses an empty generator and raises the exception with `throw`. Its goal is to build a short substitute function for `monkeypatch` that, when called, throws an exception instead of returning a value.

This method is valid, although for greater readability an independent function can be defined:

```python
def raise_timeout(*args, **kwargs):
    raise DNSTimeoutError()
```

Then replace it:

```python
monkeypatch.setattr(
    'src.cli.build_dns_results',
    raise_timeout
)
```

Both methods have one goal in this scenario.

### Examining the Exit Code

In the CLI code, upon receiving `DNSTimeoutError`, an error message is printed and the program ends with `sys.exit(1)`.

In the test:

```python
with pytest.raises(SystemExit) as exc:
    main()
```

The `exc` object holds the information of the exception that occurred.

Then:

```python
assert exc.value.code == 1
```

examines that the exit code is exactly `1`; a value that usually indicates the program's termination due to an error.

This test does not only examine the existence of `SystemExit`; it also verifies the expected exit code.

## 9. An Important Concept: `monkeypatch`

In this file, `monkeypatch` is used to temporarily replace dependencies.

| Replaced Item | Goal |
|---|---|
| `sys.argv` | Simulating command-line arguments |
| `src.cli.setup_logger` | Preventing unnecessary dependence on the real Logger |
| `src.cli.build_dns_results` | Simulating a successful result or a DNS error |

The changes made with the standard `monkeypatch` fixture are reverted at the end of the test scope. This helps keep tests independent.

**Practical rule:** When we want to test the behavior of a function, it is usually better to simulate dependencies unrelated to that behavior, so that the test is faster, more predictable, and more independent.

## 10. Summary of CLI Tests

| Test Name | Behavior Examined |
|---|---|
| `test_create_parser` | Correct extraction of domain and record type arguments |
| `test_main_invalid_domain` | Stopping execution if the domain is invalid |
| `test_main_invalid_record_type` | Stopping execution if the record type is invalid |
| `test_main_valid_arguments` | Executing the successful path with a simulated result |
| `test_main_handles_timeout` | Managing Timeout and exit with code `1` |

These five tests cover important parts of the command-line interface's behavior: input reception, validation, successful execution, and management of a specific error.

Of course, this set does not examine all possible CLI behaviors. For example, there is no independent test in this same file for the exact output text, exporting JSON or CSV through the CLI, or the precise error message. These items can be considered as exercises or development opportunities if more coverage is needed.

## 11. Suggested Exercises

1. Write a function named `raise_timeout` and use it to replace `build_dns_results` in the Timeout test.

2. Using `capsys`, examine that the successful execution of the CLI prints the domain name and the record value in the output.

3. Add a test that examines that running the CLI with a valid domain and the record type `BAD` ends with exit code `1`.

4. Examine whether you can write an independent test for the message `DNS query timed out`; such that both the printed message and the program's exit code are examined.

## 12. Running the Tests

To run this file:

```bash
pytest tests/test_cli.py -v
```

To run all the project's tests:

```bash
pytest -v
```

Running all the tests helps ensure that a change in one part has not unintentionally broken the behavior of other parts.

## Lesson Outcome

With this file, we saw that testing the command-line interface is not limited to examining arguments; by replacing dependencies, the success path and error paths can also be examined without executing the actual DNS operation.

With this, the examination of the DNS Lookup project's test files comes to an end. The next step is to put together what we have learned and draw the project's overall architecture, so that it becomes clear what responsibility each module has and how data flows from the CLI input to displaying and exporting the result.
