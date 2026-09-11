# TCP Port Scanner

A lightweight TCP port scanner written in Python, designed for learning, experimentation, and practical security automation.

The project focuses on clean Python architecture, testability, structured scan results, service detection, banner grabbing, logging, and JSON/CSV export.

> **Disclaimer:** Use this tool only against systems you own or have explicit permission to test.

---

## Features

* TCP port scanning
* Configurable port range
* Configurable connection timeout
* Configurable worker count for concurrent scanning
* IPv4 validation
* TCP service name detection
* Generic TCP banner grabbing
* Structured scan results using Python dataclasses
* Human-readable terminal output
* JSON export
* CSV export
* File-based logging
* Automated test suite with `pytest`

---

## Project Structure

```text
port_scanner/
├── README.md
├── requirements.txt
├── CHANGELOG.md
├── docs/
│   ├── en.md
│   └── fa.md
├── reports/
├── src/
│   ├── __init__.py
│   ├── scanner.py
│   ├── validator.py
│   ├── services.py
│   ├── exporter.py
│   ├── csv_exporter.py
│   ├── logger.py
│   ├── banner.py
│   ├── models.py
│   ├── results.py
│   ├── formatter.py
│   └── cli.py
└── tests/
    ├── __init__.py
    ├── test_scanner.py
    ├── test_validator.py
    ├── test_cli.py
    ├── test_services.py
    ├── test_exporter.py
    ├── test_csv_exporter.py
    ├── test_logger.py
    ├── test_banner.py
    ├── test_models.py
    ├── test_results.py
    └── test_formatter.py
```

---

## Architecture

The scanner separates the main responsibilities into small modules:

```text
CLI
 │
 ├── Validation
 │
 ├── Port Scanner
 │      │
 │      └── Open Ports
 │
 └── Result Builder
        │
        ├── Service Detection
        ├── Banner Grabbing
        └── ScanResult
                │
                ├── Terminal Formatter
                ├── JSON Export
                └── CSV Export

Logger
 └── Scan lifecycle events
```

This separation keeps scanning, result processing, formatting, exporting, and logging independent and easier to test.

---

## Requirements

* Python 3.10+
* `pytest` for running tests

No third-party package is required by the scanner itself.

---

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/QUANTORIS01/python-security-tools.git
cd python-security-tools/port_scanner
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the development dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the scanner with:

```bash
python -m src.cli <IP> <START_PORT> <END_PORT>
```

For example:

```bash
python -m src.cli 127.0.0.1 1 1000
```

Example output:

```text
🔍 Scanning 127.0.0.1
Port range: 1-1000
Timeout: 0.5s
Workers: 100

----------------------------------------------------------------------
PORT     STATUS   SERVICE          BANNER
----------------------------------------------------------------------
53       OPEN     domain           -
135      OPEN     epmap            -
445      OPEN     microsoft-ds     -
----------------------------------------------------------------------

Scan completed in 6.75s
Open ports found: 3
```

The exact output depends on the target system and currently running services.

---

## Command-Line Options

### Timeout

Set the TCP connection timeout:

```bash
python -m src.cli 127.0.0.1 1 1000 --timeout 1.0
```

Default:

```text
0.5 seconds
```

### Workers

Set the number of concurrent workers:

```bash
python -m src.cli 127.0.0.1 1 1000 --workers 50
```

Default:

```text
100 workers
```

### JSON Export

Export scan results to JSON:

```bash
python -m src.cli 127.0.0.1 1 1000 --json results.json
```

### CSV Export

Export scan results to CSV:

```bash
python -m src.cli 127.0.0.1 1 1000 --csv results.csv
```

Both export formats can be used together:

```bash
python -m src.cli 127.0.0.1 1 1000 --json results.json --csv results.csv
```

---

## Service Detection

For each open TCP port, the scanner attempts to resolve the port to its registered TCP service name using Python's standard library.

For example:

```text
53   → domain
135  → epmap
445  → microsoft-ds
```

This represents the service associated with the port in the local service database. It should not be interpreted as definitive identification of the software actually running on the remote host.

---

## Banner Grabbing

The scanner also attempts to retrieve a generic TCP service banner from open ports.

Example:

```text
22   OPEN   ssh   SSH-2.0-TestServer
```

Banner grabbing is intentionally generic at this stage. Some protocols send an initial banner immediately after connection, while others require a protocol-specific request before returning useful information.

Therefore, an empty banner does not necessarily mean that the service is unavailable or unidentified.

Protocol-aware probing is planned for a future version.

---

## Scan Results

Open ports are represented using the `ScanResult` dataclass:

```python
ScanResult(
    port=22,
    service="ssh",
    banner="SSH-2.0-TestServer",
)
```

The model keeps scan data structured and provides a common representation for terminal output and export formats.

`ScanResult` is immutable to prevent accidental modification after creation.

---

## JSON Output

Example:

```json
{
    "target": "127.0.0.1",
    "start_port": 1,
    "end_port": 1000,
    "open_ports": [
        {
            "port": 22,
            "service": "ssh",
            "banner": "SSH-2.0-TestServer"
        }
    ]
}
```

---

## CSV Output

Example:

```csv
port,service,banner
22,ssh,SSH-2.0-TestServer
80,http,Apache/2.4.62
```

---

## Logging

The scanner records important scan lifecycle events in a log file.

Current logging includes events such as:

```text
Scan started
Scan completed
```

The default log file is:

```text
scan.log
```

---

## Testing

The project uses `pytest` for automated testing.

Run the complete test suite with:

```bash
python -m pytest -v
```

The current test suite covers:

* Scanner behavior
* Input validation
* CLI behavior
* Service detection
* JSON export
* CSV export
* Logging
* Banner grabbing
* Scan result models
* Result orchestration
* Terminal formatting

---

## Design Goals

This project is intentionally built as a learning-oriented security tool rather than as a replacement for mature security scanners.

The main goals are:

1. Practice Python networking with `socket`
2. Understand concurrent execution with `ThreadPoolExecutor`
3. Build testable modules with clear responsibilities
4. Work with structured data
5. Separate application logic from presentation and export
6. Practice defensive error handling
7. Maintain an open-source-style development workflow

---

## Current Limitations

The current implementation has several intentional limitations:

* IPv4 scanning only
* TCP scanning only
* Generic banner grabbing
* No protocol-specific probes
* No UDP scanning
* No IPv6 support
* No advanced service/version fingerprinting
* No stealth or evasion functionality

These limitations provide clear areas for future development without unnecessarily complicating the current implementation.

---

## Roadmap

Planned improvements include:

* [ ] Protocol-aware banner probing
* [ ] More robust service identification
* [ ] Improved IPv4 validation
* [ ] Additional result/report formats
* [ ] Better CLI help and usability
* [ ] Expanded documentation and examples
* [ ] Additional integration tests

---

## License

This project is licensed under the MIT License.
