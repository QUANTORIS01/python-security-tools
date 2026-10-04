import dns.resolver
import pytest

from src import lookup_record
from src.exception import DNSTimeoutError


def test_lookup_a_record(monkeypatch):
    class FakeAnswer:
        def __str__(self):
            return '1.1.1.1'

    monkeypatch.setattr('dns.resolver.resolve', lambda *args, **kwargs: [FakeAnswer()])
    result = lookup_record('example.com', 'A')
    assert result == ['1.1.1.1']


def test_lookup_multiple_records(monkeypatch):
    class FakeAnswer:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return self.value

    monkeypatch.setattr(
        'dns.resolver.resolve', lambda *args, **kwargs: [FakeAnswer('1.1.1.1'), FakeAnswer('8.8.8.8')]
    )
    result = lookup_record('example.com', 'A')
    assert result == ['1.1.1.1', '8.8.8.8']


def test_lookup_nonexistent_domain(monkeypatch):
    def fake_resolve(*args, **kwargs):
        raise dns.resolver.NXDOMAIN

    monkeypatch.setattr('dns.resolver.resolve', fake_resolve)
    result = lookup_record('does-not-exist.com', 'A')
    assert result == []


def test_lookup_record_handles_no_answer(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.NoAnswer

    monkeypatch.setattr(dns.resolver, 'resolve', fake_resolve)
    assert lookup_record('example.com', 'TXT') == []


def test_lookup_record_handles_nxdomain(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.NXDOMAIN

    monkeypatch.setattr(dns.resolver, 'resolve', fake_resolve)
    assert lookup_record('invalid.test', 'A') == []


def test_lookup_record_handles_timeout(monkeypatch):
    def fake_resolve(domain, record_type):
        raise dns.resolver.LifetimeTimeout

    monkeypatch.setattr(dns.resolver, 'resolve', fake_resolve)
    with pytest.raises(DNSTimeoutError):
        lookup_record('google.com', 'MX')

