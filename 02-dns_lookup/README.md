# DNS Lookup Tool

A lightweight DNS lookup utility written in Python for learning, experimentation, automation, and security-related workflows.

The project focuses on clean architecture, structured DNS results, automated testing, logging, and export capabilities while remaining simple enough to study and extend.

> **Disclaimer:** This tool is intended for educational, administrative, and authorized security purposes only.

---

## Documentation

This project includes bilingual documentation:

* English Documentation
* Persian Documentation

The Persian learning track includes:

* Python Fundamentals
* Networking Fundamentals
* DNS Fundamentals
* Cybersecurity Fundamentals
* Step-by-step source code analysis

---

## Features

* DNS record lookup
* Support for A records
* Support for AAAA records
* Support for MX records
* Support for NS records
* Support for TXT records
* Support for CNAME records
* Domain validation
* DNS record type validation
* Structured DNS results using Python dataclasses
* Human-readable terminal output
* JSON export
* CSV export
* File-based logging
* Automated testing with pytest

---

## Project Structure

```text
dns_lookup/

├── README.md
├── CHANGELOG.md
├── requirements.txt
│
├── docs/
│   ├── en/
│   └── fa/
│
│
├── src/
│   ├── __init__.py
│   ├── validator.py
│   ├── resolver.py
│   ├── models.py
│   ├── results.py
│   ├── formatter.py
│   ├── exporter.py
│   ├── csv_exporter.py
│   ├── logger.py
│   └── cli.py
│
└── tests/
```

---

## Architecture

```text
CLI
 │
 ├── Validation
 │
 ├── Resolver
 │
 └── Result Builder
        │
        └── DNSRecord
                │
                ├── Formatter
                ├── JSON Export
                └── CSV Export

Logger
 └── Lookup lifecycle events
```

---

## Requirements

* Python 3.10+
* pytest (for testing)

Dependencies:

* dnspython

Install:

```bash
pip install -r requirements.txt
```

---

## Usage

Lookup an A record:

```bash
python -m src.cli google.com A
```

Lookup an MX record:

```bash
python -m src.cli google.com MX
```

Lookup a TXT record:

```bash
python -m src.cli google.com TXT
```

---

## Exporting Results

JSON:

```bash
python -m src.cli google.com A --json result.json
```

CSV:

```bash
python -m src.cli google.com A --csv result.csv
```

Both:

```bash
python -m src.cli google.com A --json result.json --csv result.csv
```

---

## Logging

Lookup events are written to:

```text
dns.log
```

Current events include:

* Lookup started
* Lookup completed

---

## Testing

Run the full test suite:

```bash
python -m pytest -v
```

---

## Design Goals

1. Learn DNS fundamentals.
2. Practice Python networking libraries.
3. Build maintainable software.
4. Work with structured data models.
5. Practice automated testing.
6. Create reusable security-oriented utilities.

---

## Current Limitations

* Uses the system DNS configuration.
* No custom DNS server selection.
* No DNSSEC validation.
* No reverse lookup support.
* No bulk lookup functionality.

---

## Roadmap

Planned improvements:

* Custom DNS server selection
* Reverse DNS lookups
* Bulk domain processing
* DNSSEC inspection
* Additional export formats
* Extended reporting

---

## License

This project is licensed under the MIT License.
