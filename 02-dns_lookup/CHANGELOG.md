# Changelog

All notable changes to this project are documented here.

## [1.0.0] - Initial Release

### Added

* DNS record lookup functionality.
* Support for the following DNS record types:

  * A
  * AAAA
  * MX
  * NS
  * TXT
  * CNAME
* Domain validation.
* DNS record type validation.
* Structured DNS result model using the `DNSRecord` dataclass.
* Human-readable terminal output.
* JSON export support.
* CSV export support.
* File-based logging.
* Command-line interface.
* Automated test suite using `pytest`.

### Improved

* Separation of validation, resolution, formatting, exporting, and logging responsibilities.
* Consistent structured output across terminal and export formats.
* Cleaner project architecture for maintainability and testing.

### Error Handling

* Graceful handling of:

  * Non-existent domains (`NXDOMAIN`)
  * Missing DNS records (`NoAnswer`)
  * DNS timeout conditions
  * Unavailable DNS servers

### Testing

* Comprehensive unit tests for:

  * Validation
  * Resolver
  * Models
  * Results
  * Formatter
  * Exporters
  * Logger
  * CLI

### Documentation

* Added complete project documentation.
* Added bilingual documentation structure (English and Persian).
* Documented architecture, usage, limitations, and future improvements.
