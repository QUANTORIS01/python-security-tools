[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/tests/21-conclusion.md)

# Chapter Four: Summary of Architecture and Analysis of the DNS Lookup Project

## 1. Goal of This Lesson

In the previous lessons, we examined the project's main files and its test files. In this lesson, the goal is to understand the relationship between the different parts instead of looking at each file separately.

By the end of this lesson, we can:

- Explain the project's overall architecture.
- Follow the path of data from the command line to the output.
- Identify each module's responsibility.
- Explain the role of automated tests in examining the program's behavior.
- Identify the architecture's strengths and opportunities for improvement.

## 2. The Project's Overall Structure

The program's main modules are in the `src` folder and their tests are kept in the `tests` folder.

```text
python-security-tools/
│
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── validator.py
│   ├── resolver.py
│   ├── exception.py
│   ├── models.py
│   ├── results.py
│   ├── formatter.py
│   ├── exporter.py
│   ├── csv_exporter.py
│   └── logger.py
│
└── tests/
    ├── test_cli.py
    ├── test_validator.py
    ├── test_resolver.py
    ├── test_models.py
    ├── test_results.py
    ├── test_formatter.py
    ├── test_exporter.py
    ├── test_csv_exporter.py
    └── test_logger.py
```

Each module has a specific responsibility. This separation helps ensure that a change in one part, as much as possible, does not require changing all other parts.

## 3. Each Module's Responsibility

| Module | Main Responsibility |
|---|---|
| `__init__.py` | Providing public access to some of the project's functions and classes |
| `cli.py` | Receiving arguments, executing the main program flow, and managing error paths |
| `validator.py` | Examining the validity of the domain, Timeout, and record type |
| `resolver.py` | Sending DNS requests and converting responses to strings |
| `exception.py` | Defining the project's custom exceptions |
| `models.py` | Defining the `DNSRecord` data model |
| `results.py` | Converting raw DNS values into `DNSRecord` objects |
| `formatter.py` | Converting structured results into text suitable for the terminal |
| `exporter.py` | Storing data in JSON format |
| `csv_exporter.py` | Storing records in CSV format |
| `logger.py` | Configuring event logging to a report file |

This design is an example of **separation of responsibilities**. For example, the `resolver.py` module is not responsible for building the output table, and `formatter.py` should not send network requests itself.

## 4. The Path of Data in the Program

Suppose we run the tool with this command:

```bash
python -m src.cli google.com A --json results.json --csv results.csv
```

In this example, the goal is to retrieve `A` records for the domain `google.com` and save the results in both JSON and CSV formats.

The general execution path is as follows:

```text
User input on the command line
          |
          v
      cli.py
  Receiving arguments
          |
          v
    validator.py
   Input validation
          |
          v
     resolver.py
    DNS request
          |
          v
      results.py
 Building DNSRecord results
          |
          v
     +----+----+
     |         |
     v         v
formatter.py  Exporting data
Terminal display        |
              +-------+-------+
              |               |
              v               v
        exporter.py  csv_exporter.py
                JSON          CSV
```

This diagram shows the program's typical execution path. If validation fails, the program stops before the DNS request. If the DNS request encounters a Timeout, the CLI manages the error and ends with exit code `1`.

### First Stage: Receiving Input

The `create_parser` function in `cli.py` uses `argparse` to define the positional arguments `domain` and `record_type` and the optional options `--json` and `--csv`.

### Second Stage: Validation

The `validate_domain` and `validate_record_type` functions examine that the inputs are compatible with the program's current rules.

This stage prevents invalid inputs from being sent to the network part; of course, the domain validation in this project is a string format check and does not by itself guarantee that the domain actually exists.

### Third Stage: DNS Request

The `lookup_record` function in `resolver.py` sends the request using `dns.resolver.resolve`.

The received responses are converted to strings. Some DNS errors like `NXDOMAIN` and `NoAnswer` are converted to an empty list in the current implementation, while Timeout is converted to `DNSTimeoutError`.

### Fourth Stage: Building the Data Model

The `build_dns_results` function in `results.py` converts the values received from the Resolver into `DNSRecord` objects.

This model has three main attributes:

- `domain`
- `record_type`
- `value`

As a result, the next parts of the program work with data that has a specific structure, not just scattered strings.

### Fifth Stage: Display and Export

The `format_dns_results` function formats the results for display in the terminal.

If the `--json` option is specified, the data is stored through `export_json`. If the `--csv` option is specified, the `export_csv` function writes it in CSV format.

Both exporters receive data with a dictionary structure that the CLI has built from the results.

## 5. Why Is the `DNSRecord` Model Important?

Imagine the Resolver returns several DNS values:

```python
values = ['8.8.8.8', '8.8.4.4']
```

These values alone do not specify which domain and what record type they belong to. The `DNSRecord` model keeps this information alongside each value.

```python
DNSRecord(
    domain='google.com',
    record_type='A',
    value='8.8.8.8',
)
```

Using `@dataclass(frozen=True)` makes the instance creation simple and its attributes cannot be changed after creation through normal assignment.

This structure is also useful in tests; because specific and predictable instances can be created and the outputs of functions can be compared with them.

## 6. Error Management in the Project Architecture

The project uses custom exceptions to display DNS errors better.

```python
class DNSLookupError(Exception):
    pass


class DNSTimeoutError(DNSLookupError):
    pass
```

`DNSTimeoutError` inherits from `DNSLookupError`. This structure enables categorizing errors related to DNS.

In the Resolver, the Timeout error is converted to a custom exception. Then the CLI catches it, prints the appropriate message, and ends with a non-zero exit code.

This division of responsibilities causes the Resolver to manage the network error details and the CLI to decide how that error should be displayed to the user.

## 7. The Role of Tests in Ensuring the Program's Behavior

The project's tests do not just examine that the functions run without errors; they also examine the expected behavior of each part.

| Test File | Main Items Examined |
|---|---|
| `test_validator.py` | Domain, Timeout, and record type |
| `test_models.py` | `DNSRecord` construction and its immutability |
| `test_resolver.py` | DNS response, multiple records, empty response, and Timeout |
| `test_results.py` | Converting values to structured models |
| `test_formatter.py` | Output format and the no-results case |
| `test_exporter.py` | Creating the JSON file and the correctness of the stored data |
| `test_csv_exporter.py` | Creating the CSV file and the content of the rows |
| `test_logger.py` | Creating the report file, recording a message, and preventing duplicate Handlers |
| `test_cli.py` | Parser, invalid input, successful execution, and Timeout management |

### Three Important Techniques in the Tests

**1. `monkeypatch`**

Used to temporarily replace dependencies; such as replacing `sys.argv`, the Resolver function, or the Logger.

**2. `tmp_path`**

Used to create temporary paths in tests related to files. In this way, tests can create files and examine their content, without depending on the project's fixed files.

**3. `pytest.raises`**

Used to examine that the expected operation actually raises an exception; such as `SystemExit` in the CLI or the expected error when changing an attribute of an immutable model.

### Why Is Simulating Dependencies Useful?

The Resolver or CLI tests should not depend on the random response of a DNS server to examine their internal logic. By simulating responses, successful scenarios, empty responses, and errors can be tested in a controlled manner.

## 8. Strengths of the Current Design

Several valuable features are visible in the current architecture:

- **Separation of responsibilities:** Validation, DNS request, formatting, export, and logging are in separate modules.
- **A specific data model:** `DNSRecord` provides a shared structure for holding results.
- **Custom error management:** Timeout is converted in a way that the CLI can manage it specifically.
- **Testability:** The main dependencies can be replaced with `monkeypatch`.
- **Support for two output formats:** Data can be stored in JSON and CSV formats.
- **Event logging:** The Logger provides the ability to record the time and level of messages.

These features create a suitable foundation for gradual development of the project.

## 9. Opportunities for Technical Improvement

These items do not mean that the current design is unusable; rather, they are specific paths for strengthening the project in the future.

### 9.1. Making Domain Validation More Precise

The current regular expression checks the general domain format but does not cover all possible domain name rules. For example, it might accept a label ending with a hyphen.

In the next version, the validation rules can be made more precise and more boundary tests added.

### 9.2. Timeout Configuration Management

The `validate_timeout` function exists in the project, but the current Resolver does not receive the Timeout value as an argument and `dns.resolver.resolve` is also called without explicitly setting the Timeout.

If the user is to be able to set the wait time, this capability must also be implemented consistently in the command-line interface and the Resolver's call path.

### 9.3. Extending the CLI Test Coverage

The CLI tests examine important paths. If more coverage is needed, the following can also be tested:

- The exact text of the terminal output
- Executing the `--json` and `--csv` options through the CLI
- Behavior in case of file-writing operation failure
- Error messages and exit codes in different scenarios

### 9.4. Making Logger Management More Robust

The current Logger prevents adding a Handler again for the same path string. In the future, management of relative and absolute paths, and the behavior when using multiple different report files, can also be designed more precisely.

### 9.5. Improving the Delimitation of Module Dependencies

In several modules, imports are performed through `src`; for example, `results.py` and `formatter.py` import the `DNSRecord` class from `src`.

If the project is extended, dependencies can be organized so that internal modules import directly from the module that owns each definition as much as possible. This can make understanding dependencies and maintaining the package structure easier.

### 9.6. Documenting the Empty Response Behavior

The Resolver returns an empty list for several specific states, including the absence of the domain or the absence of a response. This choice is simple and practical; but if the program's consumer needs to distinguish between "the domain does not exist" and "there is no response for this record type," more information must be kept in the result model or the error layer.

## 10. Final Summary of the Chapter

In this chapter, we examined the project from two perspectives:

1. **The main code:** What is each module's task and how does it participate in the program's execution flow?

2. **Tests:** How can we automatically examine the expected behavior of the modules and the program's main paths?

The most important point is that a software tool is not just a collection of functions. A good architecture specifies how data moves, what responsibility each part has, where errors are managed, and how the program's behavior remains testable.

With the end of this chapter, we have examined a practical example of structuring, testing, and analyzing a Python network tool. The same method can be applied in other projects as well: first, understand the modules' responsibilities, then follow the path of data, examine behavior with tests, and finally prioritize improvement opportunities based on the project's actual needs.
