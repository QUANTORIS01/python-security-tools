import pytest

from src import DNSRecord


def test_dns_record_creation():
    record = DNSRecord(domain='google.com', record_type='A', value='8.8.8.8')
    assert record.domain == 'google.com'
    assert record.record_type == 'A'
    assert record.value == '8.8.8.8'


def test_dns_record_is_immutable():
    record = DNSRecord(domain='google.com', record_type='A', value='8.8.8.8')

    with pytest.raises(AttributeError):
        record.value = '1.1.1.1'


def test_dns_record_with_mx_record():
    record = DNSRecord(domain='google.com', record_type='MX', value='smtp.google.com')
    assert record.record_type == 'MX'
