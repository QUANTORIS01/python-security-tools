from src import DNSRecord, format_dns_results


def test_format_dns_results():
    results = [
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
    output = format_dns_results(results)

    assert 'DOMAIN' in output
    assert 'TYPE' in output
    assert 'VALUE' in output

    assert 'google.com' in output
    assert '8.8.8.8' in output
    assert '8.8.4.4' in output


def test_format_dns_results_with_mx_record():
    results = [
        DNSRecord(
            domain='google.com',
            record_type='MX',
            value='smtp.google.com',
        )
    ]
    output = format_dns_results(results)
    assert 'MX' in output
    assert 'smtp.google.com' in output


def test_format_dns_results_empty():
    output = format_dns_results([])
    assert output == 'No DNS records found.'
