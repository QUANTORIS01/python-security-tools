import pytest

from src.cli import create_parser, main
from src import DNSRecord
from src.exception import DNSTimeoutError


class FakeLogger:
    def info(self, *args, **kwargs):
        pass


def test_create_parser():
    parser = create_parser()

    args = parser.parse_args(['google.com', 'A'])
    assert args.domain == 'google.com'
    assert args.record_type == 'A'


def test_main_invalid_domain(monkeypatch):
    monkeypatch.setattr('src.cli.setup_logger', lambda *args, **kwargs: FakeLogger())
    monkeypatch.setattr('sys.argv', ['cli.py', '!!!', 'A'])
    with pytest.raises(SystemExit):
        main()


def test_main_invalid_record_type(monkeypatch):
    monkeypatch.setattr('src.cli.setup_logger', lambda *args, **kwargs: FakeLogger())
    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'BAD'])
    with pytest.raises(SystemExit):
        main()


def test_main_valid_arguments(monkeypatch):
    monkeypatch.setattr('src.cli.setup_logger', lambda *args, **kwargs: FakeLogger())
    monkeypatch.setattr('src.cli.build_dns_results', lambda *args, **kwargs: [
        DNSRecord(
            domain='google.com',
            record_type='A',
            value='8.8.8.8',
        )
    ])

    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'A'])
    main()


def test_main_handles_timeout(monkeypatch):
    monkeypatch.setattr('src.cli.setup_logger', lambda *args, **kwargs: FakeLogger())
    monkeypatch.setattr('src.cli.build_dns_results', lambda *args, **kwargs: (_ for _ in ()).throw(DNSTimeoutError()))
    monkeypatch.setattr('sys.argv', ['cli.py', 'google.com', 'MX'])
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 1
