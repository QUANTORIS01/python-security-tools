from dataclasses import dataclass


@dataclass(frozen=True)
class DNSRecord:
    """
    Represent a DNS record.
    """
    domain: str
    record_type: str
    value: str
