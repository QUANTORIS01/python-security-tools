class DNSLookupError(Exception):
    pass


class DNSTimeoutError(DNSLookupError):
    pass
