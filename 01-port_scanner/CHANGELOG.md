[🇮🇷 فارسی](./CHANGELOG.fa.md)

# Changelog

All notable changes to this project are documented here.

## [Unreleased]

### Added

* TCP port scanning with configurable port ranges.
* IPv4 and port-range validation.
* Concurrent scanning using `ThreadPoolExecutor`.
* TCP service name detection.
* Generic TCP banner grabbing.
* Structured scan results using the `ScanResult` dataclass.
* Human-readable terminal result formatting.
* JSON export support.
* CSV export support.
* File-based logging.
* Automated tests for scanner components, CLI behavior, result processing, formatting, logging, and exporters.

### Improved

* Separated scan execution from result processing and presentation.
* Improved CLI validation and error handling.
* Added structured result processing for open ports.
* Added backward-compatible handling for missing banner values in CSV export.

### Testing

* Current test suite: 51 tests.
* All tests passing.

### Documentation

* Added project architecture and usage documentation.
* Documented current limitations and future roadmap.
