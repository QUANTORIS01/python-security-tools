from src import (
    validate_ip,
    validate_port_range
)


def test_valid_ip():
    assert validate_ip("127.0.0.1")


def test_invalid_ip():
    assert not validate_ip("999.999.999.999")


def test_valid_port_range():
    assert validate_port_range(1, 1000)


def test_invalid_port_range():
    assert not validate_port_range(5000, 1000)
