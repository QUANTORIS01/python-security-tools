[🇮🇷 فارسی](/02-dns_lookup/docs/fa/04-dns-lookup-analysis/src/01-__init__.md)

# Lesson 1: The `__init__.py` File and Package Structure in Python

## Package Initialization and Public Exports

## 1. Introduction

As Python programs grow, placing all the code in a single file makes maintenance and development difficult. That is why a program is usually divided into several modules, each with a specific responsibility.

For example, a DNS Lookup tool can have separate parts for validating inputs, sending DNS requests, processing results, formatting output, and logging reports.

Python provides facilities for organizing these parts in the form of **Modules** and **Packages**.

In this lesson, we will become familiar with the `__init__.py` file, the concept of relative import, and the role of this file in organizing the members of a package.

## 2. What Is the Difference Between a Module and a Package?

### Module

A module is usually a Python file with the `.py` extension that can contain functions, classes, variables, and executable statements.

For example, in the DNS Lookup project, there are modules with the following names:

- `validator.py`
- `resolver.py`
- `models.py`
- `formatter.py`
- `logger.py`

Each module holds part of the program's code.

### Package

A package is a way to organize related modules in a shared structure.

A simplified structure of the main part of the DNS Lookup project is as follows:

```text
src/
├── __init__.py
├── validator.py
├── resolver.py
├── models.py
├── results.py
├── formatter.py
├── exporter.py
├── csv_exporter.py
├── logger.py
└── exception.py
```

In this structure, each Python file is an independent module, and `__init__.py` can make accessing parts of these modules through the package easier.

This structure is a sample of division of responsibilities in the project; the details of each module's tasks are examined in the lessons related to that file.

## 3. What Is the `__init__.py` File?

The `__init__.py` file is used to initialize a regular Python package.

When a regular package is imported, the top-level code of this file is executed. This file can also import selected names from internal modules to make accessing them easier through the package path.

In the DNS Lookup project, the content of this file includes the following imports:

```python
from .validator import validate_domain, validate_timeout, validate_record_type
from .resolver import lookup_record
from .models import DNSRecord
from .results import build_dns_results
from .formatter import format_dns_results
from .exporter import export_json
from .csv_exporter import export_csv
from .logger import setup_logger
```

These lines do not create new definitions of functions or classes; rather, they import the names existing in other modules into the namespace of the `__init__.py` module.

As a result, these names can also be accessed through the package namespace.

## 4. Examining the Concept of Relative Import

In the above code, the module names start with a dot; for example:

```python
from .resolver import lookup_record
```

This dot indicates a **Relative Import**.

In this statement:

- `.` refers to the current package.
- `resolver` is the name of the internal module.
- `lookup_record` is the name imported from that module.

Therefore, this statement imports the name `lookup_record` from the `resolver` module into the current package's scope.

### The Difference from a Regular Import

In a regular import, you can write:

```python
import json
```

In this case, the standard `json` module is imported.

But in a relative import, the relationship between the modules inside a package is explicitly specified.

### Why Is Relative Import Useful?

Relative import helps make the dependency between the internal components of a package clear. It also avoids the need to write long paths or paths dependent on external naming in some project structures.

Of course, relative import depends on the package execution context. Running a file that uses relative import directly might cause an `ImportError`; because when Python runs a file directly, it does not necessarily have the package context available.

## 5. Examining the Names Imported in the Package

Below, we examine the names that have been imported in `__init__.py`.

### 5.1. Validation Functions

```python
from .validator import validate_domain, validate_timeout, validate_record_type
```

Three names are imported from the `validator` module:

- `validate_domain`
- `validate_timeout`
- `validate_record_type`

These names refer, respectively, to validating the domain, the Timeout, and the record type. But to determine the exact validation rules, error types, and acceptable values, the implementation of the `validator.py` module must be examined.

### 5.2. DNS Lookup Function

```python
from .resolver import lookup_record
```

The name `lookup_record` is imported from the `resolver` module.

This name refers to the DNS record lookup operation. How the Query is sent, how the Resolver is used, and how network errors are handled are determined in the module itself.

### 5.3. DNS Record Model

```python
from .models import DNSRecord
```

The name `DNSRecord` is imported from the `models` module.

Its name indicates that we are dealing with a model related to DNS records. The exact fields, class definition type, and how it is used must be examined in `models.py`.

### 5.4. Building and Formatting Results

```python
from .results import build_dns_results
from .formatter import format_dns_results
```

These two names are imported from two different modules.

- `build_dns_results` is related to building DNS results.
- `format_dns_results` is related to formatting results.

The names give us an initial understanding of the purpose of these functions, but the exact input and output contract and how they relate to each other are determined only by examining the implementation.

### 5.5. Exporting Data

```python
from .exporter import export_json
from .csv_exporter import export_csv
```

These imports bring in two names:

- `export_json`
- `export_csv`

The names refer to capabilities related to JSON and CSV output. The storage method, the exact data format, and file error handling are determined in the corresponding modules.

### 5.6. Setting Up Logging

```python
from .logger import setup_logger
```

The name `setup_logger` is imported from the `logger` module.

This name refers to setting up or configuring Logging. The actual settings, message destinations, and possible effects of executing this function are determined in the `logger.py` module.

## 6. Does Importing a Module Cause Its Code to Run?

Yes. When a module is imported for the first time, its top-level statements are executed. This is not limited to functions that are called later.

For example, if a module creates a file or changes global program settings when imported, these side effects might occur at import time.

That is why, when designing reusable packages, it is better to avoid executing unnecessary operations at import time.

For example, sending a network request or creating a file should not happen merely because a module was imported.

In multi-module projects, this principle helps make the program's behavior predictable and simplifies testing.

## 7. Does `__init__.py` Define the Public Interface of the Package?

The `__init__.py` file can help simplify the public interface of a package.

Suppose a package named `dns_package` has a function `lookup_record` in the internal module `resolver`, and this name is also imported in the `__init__.py` file.

In such a structure, it might be possible to import the name from the package path:

```python
from dns_package import lookup_record
```

In contrast, without importing this name into the package namespace, you might need to use the module path:

```python
from dns_package.resolver import lookup_record
```

This example is hypothetical, and the name `dns_package` is used only to explain the concept; the actual import path depends on the package name and the project's execution structure.

The important point is that **being able to import a name does not necessarily mean it is officially guaranteed or supported as a public API**. Designing a public API also involves deciding about stable names, usage contracts, and compatibility of future versions.

If needed, the `__all__` variable can be used to specify the names considered in operations such as `from package import *`. However, using `__all__` is not mandatory for all packages.

## 8. Important Notes on Designing `__init__.py`

When designing this file, several points should be considered:

- Import only names that actually need easier access.
- Avoid creating circular dependencies between modules.
- Pay attention to the side effects of import.
- Avoid unnecessarily making the import process heavy.
- Design the package's public interface consciously.
- Distinguish between importing a name and calling its function.

For example, this statement:

```python
from .logger import setup_logger
```

imports the function name; but it does not by itself mean calling `setup_logger()`.

Calling the function occurs only when its execution statement is written or it is called in some other way from part of the code.

## 9. Common Errors

### First Error: Confusing Module and Package

A module is usually a Python file, but a package is used to organize modules.

### Second Error: Assuming Relative Import Works in Every Condition

Relative import depends on the package context, and running a file directly might not provide this context.

### Third Error: Assuming Importing a Function Executes It

Importing a name and calling a function are two different operations.

### Fourth Error: Importing All Internal Members Without Design

Importing many names can make the package interface larger and its dependencies more complex. It is better to expose only the names actually needed for using the package.

### Fifth Error: Ignoring the Side Effects of Import

Importing a module can execute its top-level code; therefore, we must be aware of unnecessary dependencies and expensive operations at import time.

## 10. Summary

In this lesson, we learned:

- Module and Package are two different concepts in organizing Python code.
- The `__init__.py` file plays a role in initializing regular packages.
- The dot in imports like `from .resolver import lookup_record` indicates a relative import.
- The imports in `__init__.py` bring names from internal modules.
- This file can simplify access to selected names and the design of the package's public API.
- Importing a module might execute its top-level statements.
- To understand the exact behavior of each function or class, the implementation of the corresponding module must be examined.

### Exercise

1. Explain the difference between Module and Package with an example.

2. In the following statement, what does the dot mean?

```python
from .resolver import lookup_record
```

3. Does importing `setup_logger` mean executing it? Why?

4. Why might running a file that uses relative import directly encounter an error?

5. State two reasons to avoid unnecessary operations when a module is imported.

6. Explain why importing a name in `__init__.py` alone does not guarantee that the name is a stable public API.

