import logging


def setup_logger(filename: str) -> logging.Logger:
    """
    Configure and return a file logger.
    """
    logger = logging.getLogger("port_scanner")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            if handler.baseFilename == filename:
                return logger
    handler = logging.FileHandler(filename, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
