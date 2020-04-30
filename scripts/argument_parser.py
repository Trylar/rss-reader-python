"""Handle command line arguments"""
import argparse

from scripts.version import __version__ as version


def parse_args(args: list) -> argparse.Namespace:
    """Create argument parser, parse arguments and return them"""
    arg_parser = create_arg_parser(desc="Get rss source and show it's content")
    arg_parser.add_argument("source", action="store", help="rss source")
    arg_parser.add_argument("-v", "--version", action="version", help="show version and exit", version=version)
    arg_parser.add_argument("--json", action="store_true", help="show content in json format", default=False)
    arg_parser.add_argument("--verbose", action="store_true", help="show verbose status messages", default=False)
    arg_parser.add_argument("--limit", action="store", help="news limit")
    arg_parser.add_argument("--date", action="store", help="date for cached news in format YYYYMMDD")
    arg_parser.add_argument("--to-epub", action="store_true", help="save data in epub file", default=False)
    arg_parser.add_argument("--output-path", action="store", help="path to the new file for saving")
    arg_parser.add_argument("--colorize", action="store_true", help="colorize output", default=False)
    return arg_parser.parse_args(args)


def create_arg_parser(desc: str) -> argparse.ArgumentParser:
    """Create object for parsing arguments from command line"""
    return argparse.ArgumentParser(description=desc)
