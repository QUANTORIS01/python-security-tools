import socket

from src import grab_banner


def test_grab_banner_returns_banner(monkeypatch):
    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass

        def settimeout(self, timeout):
            self.timeout = timeout

        def connect(self, address):
            self.address = address

        def recv(self, size):
            return b"SSH-2.0-TestServer\r\n"

    monkeypatch.setattr(socket, "socket", lambda *args, **kwargs: FakeSocket())
    result = grab_banner("127.0.0.1", 22)
    assert result == "SSH-2.0-TestServer"


def test_grab_banner_returns_none_on_connection_error(monkeypatch):
    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass

        def settimeout(self, timeout):
            pass

        def connect(self, address):
            raise socket.error("Connection failed")

    monkeypatch.setattr(socket, "socket", lambda *args, **kwargs: FakeSocket())
    result = grab_banner("127.0.0.1", 9999)
    assert result is None


def test_grab_banner_returns_none_for_empty_response(monkeypatch):
    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass

        def settimeout(self, timeout):
            pass

        def connect(self, address):
            pass

        def recv(self, size):
            return b""

    monkeypatch.setattr(socket, "socket", lambda *args, **kwargs: FakeSocket())
    result = grab_banner("127.0.0.1", 80)
    assert result is None


def test_grab_banner_sets_timeout(monkeypatch):
    captured = {}

    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            pass

        def settimeout(self, timeout):
            captured["timeout"] = timeout

        def connect(self, address):
            pass

        def recv(self, size):
            return b"Test Banner"

    monkeypatch.setattr(socket, "socket", lambda *args, **kwargs: FakeSocket())
    grab_banner("127.0.0.1", 80, timeout=2.5)
    assert captured["timeout"] == 2.5
