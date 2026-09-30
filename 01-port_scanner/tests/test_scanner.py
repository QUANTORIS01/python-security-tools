import socket
import threading

from src import scan_port, scan_range


def create_test_server():
    """
    Create a temporary TCP server on localhost.
    Returns the server socket, port number, and server thread.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 0))
    server.listen(1)
    port = server.getsockname()[1]

    def accept_connection():
        try:
            connection, _ = server.accept()
            connection.close()
        except OSError:
            pass

    thread = threading.Thread(target=accept_connection, daemon=True)
    thread.start()
    return server, port, thread


def test_scan_open_port():
    """
    Scanner should detect an open TCP port.
    """
    server, port, _ = create_test_server()
    try:
        result = scan_port("127.0.0.1", port)
        assert result is True
    finally:
        server.close()


def test_scan_closed_port():
    """
    Scanner should return False for a closed port.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 0))
    port = server.getsockname()[1]
    server.close()
    result = scan_port("127.0.0.1", port)
    assert result is False


def test_scan_single_port_range():
    """
    Scanner should correctly scan a single-port range.
    """
    server, port, _ = create_test_server()
    try:
        result = scan_range("127.0.0.1", port, port)
        assert result == [port]
    finally:
        server.close()


def test_scan_range_returns_sorted_ports():
    """
    Open ports should be returned in sorted order.
    """
    server1, port1, _ = create_test_server()
    server2, port2, _ = create_test_server()
    try:
        start_port = min(port1, port2)
        end_port = max(port1, port2)
        result = scan_range("127.0.0.1", start_port, end_port)
        assert result == sorted([port1, port2])
    finally:
        server1.close()
        server2.close()


def test_scan_with_custom_timeout():
    """
    Scanner should accept a custom timeout.
    """
    server, port, _ = create_test_server()
    try:
        result = scan_port("127.0.0.1", port, timeout=1.0)
        assert result is True
    finally:
        server.close()


def test_scan_with_different_worker_count():
    """
    Scanner should work with different worker counts.
    """
    server, port, _ = create_test_server()
    try:
        result = scan_range("127.0.0.1", port, port, workers=1)
        assert result == [port]
    finally:
        server.close()
