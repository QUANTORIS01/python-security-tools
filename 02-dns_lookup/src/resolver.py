import dns.resolver


def lookup_record(domain: str, record_type: str) -> list[str]:
    """
    Lookup DNS records.
    """
    answers = dns.resolver.resolve(domain, record_type)
    return [str(answer) for answer in answers]
