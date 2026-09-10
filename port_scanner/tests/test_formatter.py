from src import format_scan_results, ScanResult


def test_format_scan_results():
    results = [
        ScanResult(
            port=22,
            service="ssh",
            banner="SSH-2.0-TestServer",
        ),
        ScanResult(
            port=80,
            service="http",
            banner="Apache/2.4.62",
        ),
    ]
    output = format_scan_results(results)

    assert "PORT" in output
    assert "STATUS" in output
    assert "SERVICE" in output
    assert "BANNER" in output

    assert "22" in output
    assert "ssh" in output
    assert "SSH-2.0-TestServer" in output

    assert "80" in output
    assert "http" in output
    assert "Apache/2.4.62" in output


def test_format_scan_results_with_missing_banner():
    results = [
        ScanResult(
            port=53,
            service="domain",
            banner=None,
        )
    ]

    output = format_scan_results(results)

    assert "53" in output
    assert "domain" in output
    assert "-" in output


def test_format_scan_results_with_empty_results():
    output = format_scan_results([])
    assert output == "No open ports found."


def test_format_scan_results_truncates_long_banner():
    long_banner = "A" * 100
    results = [
        ScanResult(
            port=80,
            service="http",
            banner=long_banner,
        )
    ]
    output = format_scan_results(results)

    assert "..." in output
    assert long_banner not in output
