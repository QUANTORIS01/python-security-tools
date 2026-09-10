import pytest

from src.cli import create_parser, main


def test_create_parser():
    parser = create_parser()
    args = parser.parse_args(["127.0.0.1", "1", "1000"])
    assert args.ip == "127.0.0.1"
    assert args.start_port == 1
    assert args.end_port == 1000
    assert args.timeout == 0.5
    assert args.workers == 100


def test_main_with_valid_arguments(monkeypatch, capsys):
    def fake_scan_range(ip, start_port, end_port, timeout, workers):
        return [22, 80, 443]

    monkeypatch.setattr("src.cli.scan_range", fake_scan_range)
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "1000"])
    main()
    captured = capsys.readouterr()
    assert "ssh" in captured.out
    assert "http" in captured.out
    assert "https" in captured.out

    assert "22" in captured.out
    assert "80" in captured.out
    assert "443" in captured.out


def test_main_with_invalid_ip(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["cli.py", "999.999.999.999", "1", "1000"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Invalid IP address" in captured.out


def test_main_with_invalid_port_range(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "5000", "1000"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Invalid port range" in captured.out


def test_main_with_invalid_timeout(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "1000", "--timeout", "0"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Timeout must be greater than 0" in captured.out


def test_main_with_invalid_workers(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "1000", "--workers", "0"])
    with pytest.raises(SystemExit) as exc_info:
        main()
    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Workers must be greater than 0" in captured.out


def test_main_shows_service_names(monkeypatch, capsys):
    monkeypatch.setattr("src.cli.scan_range", lambda *args, **kwargs: [80, 443])
    monkeypatch.setattr("src.cli.detect_service", lambda port: {80: "http", 443: "https"}[port])
    monkeypatch.setattr("sys.argv", ["cli.py", "127.0.0.1", "1", "1000"])
    main()
    captured = capsys.readouterr()
    assert "http" in captured.out
    assert "https" in captured.out
