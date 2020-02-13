"""Error handling and other utilities"""
import logging
import sys


class Error(Exception):
    def __init__(self, message: str):
        """Prints a usage message and exits"""
        logging.error(message)
        sys.exit(1)
