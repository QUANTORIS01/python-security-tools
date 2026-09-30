from src import grab_banner, ScanResult, detect_service


def build_scan_results(ip: str, open_ports: list[int], timeout: float = 1.0) -> list[ScanResult]:
    """
    Build structured scan results for open ports.
    """
    results = []
    for port in open_ports:
        service = detect_service(port)
        banner = grab_banner(ip, port, timeout=timeout)
        results.append(
            ScanResult(
                port=port,
                service=service,
                banner=banner,
            )
        )
    return results
