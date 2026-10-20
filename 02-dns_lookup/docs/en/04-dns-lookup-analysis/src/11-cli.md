[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/src/11-cli.md)

# Lesson 11: Designing a Command-Line Interface with argparse

**File under review:** `src/cli.py`

## 1. Lesson Goal

In this lesson, we will learn how to build a command-line interface using `argparse` and connect the different components of a program through the main function.

The `cli.py` file is the coordinating point of the DNS Lookup tool's execution. Its main tasks are:

- Receiving the domain and record type from the command line
- Validating inputs
- Setting up the logger
- Executing the DNS lookup
- Managing the timeout error
- Displaying results in the terminal
- Preparing data for JSON and CSV output
- Announcing the success of output storage

In this project's architecture, each part has a specific task, and `cli.py` coordinates their execution.

## 2. The Complete File Code

```python 
import argparse
import sys

from src import (
    validate_domain,
    validate_record_type,
    build_dns_results,
    format_dns_results,
    export_json,
    export_csv,
    setup_logger,
)

from .exception import DNSTimeoutError


def create_parser() -> argparse.ArgumentParser:
    """
    Create command-line argument parser.
    """
    parser = argparse.ArgumentParser(description='DNS Lookup Tool')
    parser.add_argument('domain', type=str, help='Target domain name')
    parser.add_argument('record_type', type=str, help='DNS record type')
    parser.add_argument('--json', dest='json_file', type=str, help='Export results to JSON')
    parser.add_argument('--csv', dest='csv_file', type=str, help='Export results to CSV')
    return parser


def main() -> None:
    """
    Run DNS lookup CLI.
    """
    parser = create_parser()
    args = parser.parse_args()
    if not validate_domain(args.domain):
        print(f'❌ Invalid domain: {args.domain}')
        sys.exit(1)
    if not validate_record_type(args.record_type):
        print(f'❌ Invalid record type: {args.record_type}')
        sys.exit(1)
    logger = setup_logger('dns.log')
    logger.info('Lookup started domain=%s type=%s', args.domain, args.record_type)
    try:
        results = build_dns_results(args.domain, args.record_type)
    except DNSTimeoutError:
        print('❌ DNS query timed out.')
        sys.exit(1)
    logger.info('Lookup completed records=%s', len(results))
    print(format_dns_results(results))
    export_data = {
        'domain': args.domain,
        'record_type': args.record_type,
        'records': [{
            'domain': result.domain,
            'record_type': result.record_type,
            'value': result.value,
        } for result in results]
    }
    if args.json_file:
        export_json(export_data, args.json_file)
        print(f'Results exported to {args.json_file}')
    if args.csv_file:
        export_csv(export_data, args.csv_file)
        print(f'Results exported to {args.csv_file}')


if __name__ == '__main__':
    main()
```

## 3. Importing Modules

```python
import argparse
import sys
```

### The `argparse` Module

The `argparse` module is from Python's standard library and is used to build command-line interfaces. With it, mandatory inputs, optional options, descriptions, and the program's execution help can be defined.

### The `sys` Module

In this file, `sys.exit(1)` is used to end the program's execution with a non-zero exit code. Usually, exit code `0` indicates a successful end and a non-zero code indicates an error or unsuccessful end.

## 4. Importing the Project's Internal Components

```python
from src import (
    validate_domain,
    validate_record_type,
    build_dns_results,
    format_dns_results,
    export_json,
    export_csv,
    setup_logger,
)

from .exception import DNSTimeoutError
```

These imports show that `cli.py` does not implement the main logic of each operation itself; rather, it uses functions and classes that have been defined earlier in different parts of the project.

| Name | Responsibility |
|---|---|
| `validate_domain` | Examining the domain format |
| `validate_record_type` | Examining support for the record type |
| `build_dns_results` | Executing the lookup and building structured results |
| `format_dns_results` | Preparing the tabular text for the terminal |
| `export_json` | Storing data in JSON |
| `export_csv` | Storing data in CSV |
| `setup_logger` | Preparing the logger |
| `DNSTimeoutError` | Identifying the project's custom timeout error |

This separation makes the command-line interface responsible for coordinating operations, leaving each task's details in its own part.

## 5. Building the Parser with `create_parser()`

```python
def create_parser() -> argparse.ArgumentParser:
    """
    Create command-line argument parser.
    """
    parser = argparse.ArgumentParser(description='DNS Lookup Tool')
```

The `create_parser()` function creates and configures the parser object.

`ArgumentParser` is responsible for interpreting the arguments entered when running the program.

The `description` parameter specifies a short description for the program. This description is visible in the help displayed with the `--help` option.

Separating the parser construction in an independent function makes the code more orderly and allows testing the argument settings.

## 6. Defining Mandatory Arguments

```python
parser.add_argument(
    'domain',
    type=str,
    help='Target domain name'
)
parser.add_argument(
    'record_type',
    type=str,
    help='DNS record type'
)
```

In `argparse`, arguments defined without an option prefix are mandatory by default.

Therefore, the user must specify the domain and record type when running the program.

For example:

```bash
python -m src.cli example.com A
```

In this command:

- `example.com` is the value of the `domain` argument.
- `A` is the value of the `record_type` argument.

The `type=str` parameter specifies that the argument value should be converted to a string. Since command-line arguments are usually received as strings, this here mostly serves to explicitly document the expected type.

The `help` parameter also specifies the argument's description for the command-line help.

## 7. Defining Optional JSON and CSV Options

```python
parser.add_argument(
    '--json',
    dest='json_file',
    type=str,
    help='Export results to JSON'
)
parser.add_argument(
    '--csv',
    dest='csv_file',
    type=str,
    help='Export results to CSV'
)
```

These two options allow the user to specify the format in which the results should be stored.

### The `--json` Option

Usage example:

```bash
python -m src.cli example.com A --json results.json
```

The file name `results.json` is received as the value of the `--json` option.

### The `--csv` Option

Usage example:

```bash
python -m src.cli example.com A --csv results.csv
```

In this case, the file `results.csv` is specified as the CSV output destination.

### The Role of `dest`

The `dest` parameter specifies the name of the attribute in which the argument's value will be stored.

As a result:

- The value of `--json` is placed in `args.json_file`.
- The value of `--csv` is placed in `args.csv_file`.

If the user does not enter one of these options, the corresponding value will usually be `None`.

This design makes output storage optional, and the user can receive only the terminal output or choose one or both formats.

## 8. Returning the Parser

```python
return parser
```

The `create_parser()` function returns the parser after defining all the arguments.

Next, the `main()` function uses this same object to process the actual command-line input.

## 9. The Program's Entry Point: The `main()` Function

```python
def main() -> None:
    """
    Run DNS lookup CLI.
    """
    parser = create_parser()
    args = parser.parse_args()
```

In this part, the main execution of the command-line interface begins.

First, the parser is created; then `parse_args()` reads the entered arguments and places the result in the `args` object.

After processing, the values can be used by accessing the object's attributes:

```python
args.domain
args.record_type
args.json_file
args.csv_file
```

For example, if the command is:

```bash
python -m src.cli example.com A --json results.json
```

The main values of `args` will be like this:

| Attribute | Value |
|---|---|
| `args.domain` | `example.com` |
| `args.record_type` | `A` |
| `args.json_file` | `results.json` |
| `args.csv_file` | `None` |

An important point is that `argparse` examines the structure of the command-line input; but the semantic validation of the domain and record type is still delegated to the project's dedicated functions.

## 10. Domain Validation

```python
if not validate_domain(args.domain):
    print(f'❌ Invalid domain: {args.domain}')
    sys.exit(1)
```

In this part, the domain value is given to the `validate_domain()` function.

If the function returns `False`, the `not` condition is met; an error message is displayed and the program terminates with exit code `1`.

This check is performed before the DNS operation begins. As a result, input that is not compatible with the project's current validation rules does not reach the lookup stage.

The following expression also uses an f-string:

```python
f'❌ Invalid domain: {args.domain}'
```

With the help of f-strings, the value entered by the user is placed in the error message.

## 11. Record Type Validation

```python
if not validate_record_type(args.record_type):
    print(f'❌ Invalid record type: {args.record_type}')
    sys.exit(1)
```

This condition examines the entered record type.

In the project, the `validate_record_type()` function compares the record type with the set of supported types. If the input type is not accepted, the program terminates before executing the lookup.

An important point is that the domain and record type are two independent checks. The validity of one does not guarantee the validity of the other.

## 12. Preparing the Logger and Recording the Start of the Operation

```python
logger = setup_logger('dns.log')
logger.info(
    'Lookup started domain=%s type=%s',
    args.domain,
    args.record_type
)
```

First, the logger is prepared using the `setup_logger()` function we examined in the previous lesson.

Then an `INFO` message is recorded that specifies the domain and requested record type.

In this call, the `%s` placeholders are for string values. The `logging` module places the subsequent values in these placeholders when preparing the message.

This method is common for recording messages and avoids manually building a string with f-strings before calling the logger.

By recording this message, the log file can show for which domain and which record type the lookup request was started.

## 13. Executing the DNS Lookup and Managing Timeout

```python
try:
    results = build_dns_results(
        args.domain,
        args.record_type
    )
except DNSTimeoutError:
    print('❌ DNS query timed out.')
    sys.exit(1)
```

In this part, the `build_dns_results()` function is called; the same function responsible for converting the received values into structured `DNSRecord` results.

Because the DNS operation might fail due to a timeout, the call is placed inside a `try` block.

If `DNSTimeoutError` occurs, the normal execution of this part does not continue; an error message is displayed and the program ends with exit code `1`.

### Why Is a Custom Error Used?

In the `exception.py` file, the `DNSTimeoutError` class is defined as a subclass of `DNSLookupError`. In the `resolver.py` file too, the DNS library's timeout is converted into this custom error.

Therefore, the command-line interface can manage a specific error from the project's own problem domain, instead of depending directly on the details of the DNS library's error.

In the current implementation, this block specifically catches `DNSTimeoutError`. Other unexpected errors in this part are not managed and can be propagated to the caller or cause an abnormal termination of execution.

## 14. Recording the End of the Operation

```python
logger.info('Lookup completed records=%s', len(results))
```

After the successful return of the `build_dns_results()` function, the number of results is recorded.

The `len()` function returns the number of elements in `results`.

If the lookup has no result and `results` is an empty list, the recorded value will be zero. This state does not necessarily mean a program error; the lookup might have been performed successfully, but there might be no records to display.

This message records the end of a successful operation, not merely the existence of one or more records.

## 15. Displaying Results in the Terminal

```python
print(format_dns_results(results))
```

In this part, the results are given to the `format_dns_results()` function.

This function, which we examined in the lesson about `formatter.py`, converts the list of `DNSRecord`s into a text string with a tabular format.

Then `print()` displays that string in the terminal.

With this design, `cli.py` is responsible for deciding when to display the results; but the details of column arrangement are in `formatter.py`.

## 16. Preparing Data for Export

```python
export_data = {
    'domain': args.domain,
    'record_type': args.record_type,
    'records': [{
        'domain': result.domain,
        'record_type': result.record_type,
        'value': result.value,
    } for result in results]
}
```

This part converts the structured results into a dictionary so that the export functions can use it.

The final structure contains three main keys:

- `domain`: the requested domain
- `record_type`: the requested record type
- `records`: a list of the found records

Each element inside `records` is a dictionary with the keys `domain`, `record_type`, and `value`.

### Understanding List Comprehension

The following part is a *list comprehension*:

```python
[
    {
        'domain': result.domain,
        'record_type': result.record_type,
        'value': result.value,
    }
    for result in results
]
```

This expression creates a dictionary for each `DNSRecord` object in `results` and places the dictionaries in a list.

For example, an object with the following values:

```python
DNSRecord(
    domain='example.com',
    record_type='A',
    value='93.184.216.34'
)
```

is converted to this dictionary:

```python
{
    'domain': 'example.com',
    'record_type': 'A',
    'value': '93.184.216.34'
}
```

This conversion makes the data structure suitable for the current project's exporters; because both `export_json()` and `export_csv()` use the `export_data` dictionary.

## 17. Optional Storage in JSON

```python
if args.json_file:
    export_json(export_data, args.json_file)
    print(f'Results exported to {args.json_file}')
```

If the user has entered the `--json` option, `args.json_file` will usually be a non-empty string and the condition will be met.

Then:

1. The data is stored in the specified file with the `export_json()` function.
2. A message about the output path is displayed.

If the `--json` option is not used, this block does not run and the JSON file will not be created.

Note: The success message is printed after the export function returns. If storage fails with an unmanaged error, the program's execution does not reach this message.

## 18. Optional Storage in CSV

```python
if args.csv_file:
    export_csv(export_data, args.csv_file)
    print(f'Results exported to {args.csv_file}')
```

This part has a structure similar to the JSON output; except that it uses the `export_csv()` function.

The user can choose only CSV, only JSON, both, or neither.

Since the JSON and CSV conditions are independent, choosing both options causes both blocks to run.

## 19. The Overall Order of Program Execution

The execution flow of the `main()` function can be summarized as follows:

1. Building the parser and receiving arguments
2. Domain validation
3. Record type validation
4. Preparing the logger and recording the start of the request
5. Executing the DNS lookup and managing timeout
6. Recording the number of results
7. Displaying results in the terminal
8. Converting results into the `export_data` dictionary
9. Optional storage in JSON
10. Optional storage in CSV

This order matters; for example, if the domain validation fails, the program terminates before creating the logger and executing the DNS lookup.

## 20. The Program's Entry Point

```python
if __name__ == '__main__':
    main()
```

In Python, the special variable `__name__` specifies how a module has been executed.

When the file is executed directly as the main program, the value of `__name__` is `'__main__'` and the `main()` function is called.

But when the module is imported from another part of the program, this condition is usually not met; therefore, automatic execution of the command-line interface does not occur.

This pattern allows a file to both be executable and allow its functions to be imported from other modules.

For the project's current structure, a sample of running the module is as follows:

```bash
python -m src.cli example.com A
```

Using `-m` runs the module in the package structure format.

## 21. Practice Exercises

### Exercise 1: Examining the Help

Run the following command:

```bash
python -m src.cli --help
```

Examine how the descriptions of `domain`, `record_type`, `--json`, and `--csv` are displayed.

### Exercise 2: Invalid Input

Run the program with an invalid domain.

- Is the DNS operation performed?
- What message is displayed?
- What is the program's exit code?

### Exercise 3: Choosing the Output Format

Run the program in three modes:

1. Without an output option
2. Only with `--json`
3. With both `--json` and `--csv` options

Compare the behavior of each mode.

### Exercise 4: Examining the Timeout

Based on the `try/except` structure, explain which subsequent steps will not be executed if `build_dns_results()` raises a `DNSTimeoutError`.

### Exercise 5: Examining the Data Structure

Examine the `export_data` dictionary and explain why a new dictionary is created for each `DNSRecord` object.

## 22. Summary

The `cli.py` file is the connection point of the main DNS Lookup components. This file is responsible for coordinating input reception, validation, lookup, display, logging, and export.

The most important concepts of this lesson are:

- Building a command-line interface with `argparse`
- The difference between mandatory arguments and optional options
- Accessing values through `args`
- Using `sys.exit()` for ending with a specific exit code
- Managing custom errors with `try/except`
- Recording messages with `logging`
- Converting model objects into dictionaries with list comprehension
- Connecting independent components through the main function
- Using `if __name__ == '__main__'` to control the entry point

**Architectural outcome:** The validation logic, the DNS lookup, the formatting, and the storage are placed in separate parts, and `cli.py` manages their execution. This structure improves the tool's readability and maintainability and enables each part to be developed with minimal dependence on the other parts.
