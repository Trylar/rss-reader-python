#!/usr/bin/env python
"""Utility to print RSS in console in readable format"""
import datetime
import json
import logging
import sys

from scripts import *


def run(argv):
    """Main function. Parses arguments and prints result in desired form.
    Argument "argv" is added for testing"""
    arguments = argument_parser.parse_args(argv[1:])
    if arguments.verbose:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug("Reading arguments...")
    if arguments.limit:
        try:
            limit = int(arguments.limit)
            if limit < 0:
                raise Exception
        except Exception:
            raise utils.Error("argument --limit: expected non-negative number")
    else:
        limit = -1
    if arguments.output_path and not arguments.to_epub:
        print("Argument --output-path will be ignored")
    logging.debug("Arguments parsed")

    logging.debug("Parsing data...")
    if arguments.date:
        try:
            date = datetime.datetime.strptime(len(arguments.date) == 8 and arguments.date, '%Y%m%d')
        except Exception:
            raise utils.Error("date has incorrect format, should be YYYYMMDD")
        feed = cache.get_feed_from_cache(arguments.source, date)
    else:
        try:
            feed = feed_parser.parse_feeds(arguments.source)
        except Exception as e:
            raise utils.Error("unexpected error while parsing, check rss source: " + str(e))
        else:
            if feed.get("bozo"):
                raise utils.Error("argument --source: invalid rss source")
            if feed.get("status") != 200:
                raise utils.Error(
                    format_output.format_summary(feed.get("feed", {}).get("summary")) or "invalid rss source")
        cache.write_to_cache(feed)
    logging.debug("Data parsed")

    if arguments.json:
        if arguments.to_epub:
            print("Argument --to-epub will be ignored")
        result = process_data.process_json(feed, limit)
        print(json.dumps(result, indent=4))
    else:
        if arguments.to_epub:
            epub.create_epub_file(arguments, feed, limit)
        else:
            result = process_data.process_formatted_output(feed, limit)
            if arguments.colorize:
                color.color_print(result)
            else:
                [print(chunk) for chunk in result if chunk]
    logging.debug("Work is done")


def main():
    run(sys.argv)


if __name__ == '__main__':
    main()
