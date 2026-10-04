import dns.resolver

from .exception import DNSTimeoutError


def lookup_record(domain: str, record_type: str) -> list[str]:
    """
    Lookup DNS records.
    """
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(answer) for answer in answers]
    except dns.resolver.LifetimeTimeout as exc:
        raise DNSTimeoutError('DNS query timed out') from exc
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers):
        return []
