import socket


def validate_ip(ip: str) -> bool:
    """
    Validate IPv4 address.
    """
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def validate_port_range(start_port: int, end_port: int) -> bool:
    """
    Validate port range.
    """
    if not (0 <= start_port <= 65535):
        return False

    if not (0 <= end_port <= 65535):
        return False

    if start_port > end_port:
        return False

    return True