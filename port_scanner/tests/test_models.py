import pytest

from src import ScanResult


def test_scan_result_creation():
    result = ScanResult(port=22, service="ssh", banner="SSH-2.0-TestServer")
    assert result.port == 22
    assert result.service == "ssh"
    assert result.banner == "SSH-2.0-TestServer"


def test_scan_result_banner_defaults_to_none():
    result = ScanResult(port=80, service="http")
    assert result.banner is None


def test_scan_result_is_immutable():
    result = ScanResult(port=22, service="ssh")

    with pytest.raises(AttributeError):
        result.port = 80
