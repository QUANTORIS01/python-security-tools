from src import ScanResult, build_scan_results


def test_build_scan_results(monkeypatch):
    def fake_detect_service(port):
        return "ssh"

    def fake_grab_banner(ip, port, timeout):
        return "SSH-2.0-TestServer"

    monkeypatch.setattr("src.results.detect_service", fake_detect_service)
    monkeypatch.setattr("src.results.grab_banner", fake_grab_banner)
    results = build_scan_results("127.0.0.1", [22], timeout=2.0)
    assert results == [
        ScanResult(
            port=22,
            service="ssh",
            banner="SSH-2.0-TestServer",
        )
    ]


def test_build_scan_results_with_multiple_ports(monkeypatch):
    def fake_detect_service(port):
        services = {22: "ssh", 80: "http"}
        return services[port]

    def fake_grab_banner(ip, port, timeout):
        banners = {22: "SSH-2.0-TestServer", 80: "HTTP/1.1 200 OK"}
        return banners[port]

    monkeypatch.setattr("src.results.detect_service", fake_detect_service)
    monkeypatch.setattr("src.results.grab_banner", fake_grab_banner)
    results = build_scan_results("127.0.0.1", [22, 80])
    assert results == [
        ScanResult(
            port=22,
            service="ssh",
            banner="SSH-2.0-TestServer",
        ),
        ScanResult(
            port=80,
            service="http",
            banner="HTTP/1.1 200 OK",
        ),
    ]


def test_build_scan_results_handles_missing_banner(monkeypatch):
    monkeypatch.setattr("src.results.detect_service", lambda port: "http")
    monkeypatch.setattr("src.results.grab_banner", lambda ip, port, timeout: None)
    results = build_scan_results("127.0.0.1", [80])
    assert results == [
        ScanResult(
            port=80,
            service="http",
            banner=None,
        )
    ]
