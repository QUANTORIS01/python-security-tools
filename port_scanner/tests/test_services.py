from src import detect_service


def test_detect_known_ssh_service():
    assert detect_service(22) == "ssh"


def test_detect_known_http_service():
    assert detect_service(80) == "http"


def test_detect_known_https_service():
    assert detect_service(443) == "https"


def test_detect_unknown_service():
    assert detect_service(65000) == "unknown"
