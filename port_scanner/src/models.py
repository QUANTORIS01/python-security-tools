from dataclasses import dataclass


@dataclass(frozen=True)
class ScanResult:
    """
    Represent the result of a scanned open port.
    """
    port: int
    service: str
    banner: str | None = None
