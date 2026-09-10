import socket


def detect_service(port: int) -> str:
    """
    Detect the registered TCP service for a port.
    """
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"
