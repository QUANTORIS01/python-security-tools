import socket
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


def scan_port(ip: str, port: int, timeout: float = 0.5) -> bool:
    """
    Scan a single TCP port.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
        return result == 0
    except socket.error:
        return False


def scan_range(ip: str, start_port: int, end_port: int, timeout: float = 0.5, workers: int = 100) -> list[int]:
    """
    Scan a range of TCP ports.
    """
    open_ports = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(scan_port, ip, port, timeout): port for port in range(start_port, end_port + 1)
        }
        for future in as_completed(futures):
            port = futures[future]
            if future.result():
                open_ports.append(port)
    return sorted(open_ports)
