import re

SUPPORTED_RECORD_TYPES = {
    'A',
    'AAAA',
    'MX',
    'NS',
    'TXT',
    'CNAME',
}


def validate_domain(domain: str) -> bool:
    """
    Validate a domain name.
    """
    pattern = (
        r'^(?!-)'
        r'(?:[A-Za-z0-9-]{1,63}\.)+'
        r'[A-Za-z]{2,63}$'
    )
    return bool(re.fullmatch(pattern, domain))


def validate_timeout(timeout: float) -> bool:
    """
    Validate DNS query timeout.
    """
    return timeout > 0


def validate_record_type(record_type: str) -> bool:
    """
    Validate DNS record type.
    """
    return record_type.upper() in SUPPORTED_RECORD_TYPES
