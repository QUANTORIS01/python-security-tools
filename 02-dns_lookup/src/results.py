from src import DNSRecord, lookup_record


def build_dns_results(domain: str, record_type: str) -> list[DNSRecord]:
    """
    Build structured DNS results.
    """
    values = lookup_record(domain, record_type)
    return [
        DNSRecord(
            domain=domain,
            record_type=record_type,
            value=value,
        )
        for value in values
    ]
