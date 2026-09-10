import logging

import pytest

from src import setup_logger


def test_setup_logger_creates_log_file(tmp_path):
    log_file = tmp_path / "scan.log"
    logger = setup_logger(str(log_file))
    logger.info("Test message")
    for handler in logger.handlers:
        handler.flush()
    assert log_file.exists()


def test_setup_logger_writes_log_message(tmp_path):
    log_file = tmp_path / "scan.log"
    logger = setup_logger(str(log_file))
    logger.info("Test message")
    for handler in logger.handlers:
        handler.flush()
    content = log_file.read_text(encoding="utf-8")
    assert "Test message" in content
    for handler in logger.handlers:
        handler.close()
    logger.handlers.clear()


def test_setup_logger_does_not_duplicate_handlers(tmp_path):
    log_file = tmp_path / "scan.log"
    logger = setup_logger(str(log_file))
    initial_handler_count = len(logger.handlers)
    setup_logger(str(log_file))
    assert len(logger.handlers) == initial_handler_count


@pytest.fixture(autouse=True)
def cleanup_logger():
    yield
    logger = logging.getLogger("port_scanner")
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)
