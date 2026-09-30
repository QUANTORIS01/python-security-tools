from src import (
    validate_ip,
    validate_port_range,
    validate_timeout,
    validate_workers,
)


def test_valid_ip():
    assert validate_ip("127.0.0.1")


def test_invalid_ip():
    assert not validate_ip("999.999.999.999")


def test_valid_port_range():
    assert validate_port_range(1, 1000)


def test_invalid_port_range():
    assert not validate_port_range(5000, 1000)


def test_valid_timeout():
    assert validate_timeout(0.5)
    assert validate_timeout(1.0)


def test_invalid_timeout():
    assert not validate_timeout(0)
    assert not validate_timeout(-1)


def test_valid_workers():
    assert validate_workers(1)
    assert validate_workers(100)


def test_invalid_workers():
    assert not validate_workers(0)
    assert not validate_workers(-5)


def test_valid_timeout_boundary():
    assert validate_timeout(0.001)


def test_valid_workers_boundary():
    assert validate_workers(1)
