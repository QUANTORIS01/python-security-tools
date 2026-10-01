from src import DNSRecord, build_dns_results


def test_build_dns_results(monkeypatch):
    monkeypatch.setattr('src.results.lookup_record', lambda domain, record_type: ['8.8.8.8'])
    results = build_dns_results('google.com', 'A')
    assert results == [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        )
    ]


def test_build_dns_results_multiple_records(monkeypatch):
    monkeypatch.setattr('src.results.lookup_record', lambda domain, record_type: ['8.8.8.8', '8.8.4.4'])
    results = build_dns_results('google.com', 'A')
    assert results == [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        ),
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.4.4',
        ),
    ]


def test_build_dns_results_empty(monkeypatch):
    monkeypatch.setattr('src.results.lookup_record', lambda domain, record_type: [])
    results = build_dns_results('google.com', 'A')
    assert results == []
