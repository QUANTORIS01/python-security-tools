import socket


def grab_banner(ip: str, port: int, timeout: float = 1.0) -> str | None:
    """
    Attempt to retrieve a TCP service banner.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((ip, port))
            banner = sock.recv(1024)
        return banner.decode("utf-8", errors="ignore").strip() or None
    except (socket.timeout, socket.error):
        return None
