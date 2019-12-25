"""Error handling and other utilities"""
import logging
import sys


def error(message: str) -> None:
    """Prints a usage message and exits"""
    logging.error(message)
    sys.exit(1)
