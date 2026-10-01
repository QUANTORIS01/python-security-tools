from src import (
    validate_domain,
    validate_timeout,
    validate_record_type,
)


def test_valid_domain():
    assert validate_domain('google.com')


def test_valid_subdomain():
    assert validate_domain('mail.google.com')


def test_invalid_domain_without_tld():
    assert not validate_domain('google')


def test_invalid_domain_with_protocol():
    assert not validate_domain('https://google.com')


def test_invalid_domain_with_space():
    assert not validate_domain('google .com')


def test_valid_timeout():
    assert validate_timeout(1.0)


def test_valid_timeout_boundary():
    assert validate_timeout(0.001)


def test_invalid_timeout():
    assert not validate_timeout(0)


def test_invalid_negative_timeout():
    assert not validate_timeout(-1)


def test_valid_record_type_a():
    assert validate_record_type('A')


def test_valid_record_type_lowercase():
    assert validate_record_type('mx')


def test_valid_record_type_aaaa():
    assert validate_record_type('AAAA')


def test_invalid_record_type():
    assert not validate_record_type('FTP')


def test_invalid_empty_record_type():
    assert not validate_record_type('')
