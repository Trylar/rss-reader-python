"""Utility to print RSS in console in readable format"""
# !/usr/bin/env python
import argparse
import datetime
import feedparser
from feedparser.util import FeedParserDict
import html2text
import json
from typing import List, Dict, Optional
from dateutil.parser import parse as parse_date, ParserError
import logging
import os
import pickle
import sys

VERSION = "0.3"
CACHE_FILE = "cache"


def format_title(title: str) -> Optional[str]:
    """Format header to readability"""
    return wrap_string(title, "-" * len(title), "") if title else None


def format_fields(news: FeedParserDict, *fields: str) -> List[Optional[str]]:
    """Format fields of news for output"""
    return [add_title(news.get(field), field) for field in fields if field in news]


def format_date(field_value: str, title: str = "Published") -> Optional[str]:
    """Format date to convenient form"""
    try:
        return add_title(parse_date(field_value).strftime("%A, %d %B %Y %H:%M:%S"), title) if field_value else None
    except ParserError:
        return None


def format_summary(summary: str) -> Optional[str]:
    """Format news summary. If it's in html format, format nicely according to tags, otherwise just addЫ line breaks"""
    return wrap_string(html2text.html2text(summary).strip()) if summary else None


def format_links(links: List[FeedParserDict], title: str = "Links:") -> List[str]:
    """Format links"""
    return [title] + [link.get("href") for num, link in enumerate(links) if
                      (link not in links[:num])] if links else ["No links"]


def add_title(field, title: str) -> str:
    """Add title to field"""
    return "{}: {}".format(title.capitalize(), field)


def wrap_string(string: str, wrapper: str = "", *wrappers: str) -> str:
    """Wrap string with other strings for nice output.
    "wrapper" parameter stands alone for default value"""
    return "\n".join(wrappers[::-1] + (wrapper, string, wrapper) + wrappers) if string else None


def create_arg_parser(desc: str) -> argparse.ArgumentParser:
    """Create object for parsing arguments from command line"""
    return argparse.ArgumentParser(description=desc)


def error(message: str) -> None:
    """Prints a usage message and exits"""
    logging.error(message)
    sys.exit(1)


def process_json(feed: FeedParserDict, limit: int) -> Dict:
    """Form object for converting to json"""
    logging.debug("Starting create JSON object...")
    result = {"title": feed.get("feed", {}).get("title"), "entries": []}
    keys = ["title", "author", "link", "published", "summary", "comments", "links"]
    for news in feed.get("entries")[:limit]:
        result["entries"].append({key: news[key] for key in keys if key in news})
    logging.debug("JSON created")
    return result


def process_formatted_output(feed: FeedParserDict, limit: int) -> List[Optional[str]]:
    """Form readable output for console"""
    logging.debug("Starting format output")
    result = [wrap_string(feed.get("feed", {}).get("title"))]
    for news in feed.get("entries")[:limit]:
        result.append(format_title(news.get("title")))
        result.extend(format_fields(news, "author", "link"))
        result.append(format_date(news.get("published")))
        result.append(format_summary(news.get("summary")))
        result.extend(format_fields(news, "comments"))
        result.extend(format_links(news.get("links")))
    logging.debug("Output formatted")
    return result


def parse_args(args):
    """Create argument parser, parse arguments and return them"""
    arg_parser = create_arg_parser("Get rss source and show it's content")
    arg_parser.add_argument("source", action="store", help="rss source")
    arg_parser.add_argument("-v", "--version", action="version", help="show version and exit", version=VERSION)
    arg_parser.add_argument("--json", action="store_true", help="show content in json format", default=False)
    arg_parser.add_argument("--verbose", action="store_true", help="show verbose status messages", default=False)
    arg_parser.add_argument("--limit", action="store", help="news limit", default=-1)
    arg_parser.add_argument("--date", action="store", help="date for cached news in format YYYYMMDD")
    return arg_parser.parse_args(args)


def parse_feeds(source: str) -> FeedParserDict:
    """Parse url source"""
    return feedparser.parse(source)


def load_cache(cache_file):
    """Load cache from file until EOF"""
    cache = []
    while True:
        try:
            cache.append(pickle.load(cache_file))
        except EOFError:
            break
    return cache


def same_day(news_date: str, arg_date: datetime):
    """Check if news_date is the same day as arg_date"""
    return parse_date(news_date).date() == arg_date.date()


def get_news(feed_news: List, cached_news: List, date: datetime) -> List:
    """Get news with corresponding date from cached_news, deleting duplicates"""
    return [news for news in cached_news if same_day(news.published, date) and news not in feed_news]


def get_feed_from_cache(source, date) -> Dict:
    """Get feed for url source from cache"""
    if os.path.exists(CACHE_FILE) and os.stat(CACHE_FILE).st_size:
        with open(CACHE_FILE, "rb") as cache_file:
            cache = load_cache(cache_file)
            feed = {}
            for cached_feed in cache:
                if cached_feed.get("href") == source:
                    if not feed:
                        feed = {"feed": cached_feed.get("feed"), "entries": []}
                    feed.get("entries").extend(get_news(feed.get("entries"), cached_feed.get("entries"), date))
            if not feed or not feed.get("entries"):
                raise error("empty cache")
    else:
        raise error("empty cache")
    return feed


def run(argv) -> None:
    """Main function. Parses arguments and prints result in desired form.
    Argument "argv" is added for testing"""
    arguments = parse_args(argv[1:])
    if arguments.verbose:
        logging.basicConfig(level=logging.DEBUG)
    logging.debug("Reading arguments...")
    source, json_arg = arguments.source, arguments.json
    try:
        limit = int(arguments.limit)
    except Exception:
        raise error("argument --limit: expected number")
    logging.debug("Arguments parsed")

    logging.debug("Parsing data...")
    if arguments.date:
        try:
            date = datetime.datetime.strptime(len(arguments.date) == 8 and arguments.date, '%Y%m%d')
        except Exception:
            raise error("date has incorrect format, should be YYYYMMDD")
        feed = get_feed_from_cache(source, date)
    else:
        try:
            feed = parse_feeds(source)
        except Exception as e:
            raise error("unexpected error while parsing" + str(e))
        else:
            if feed.get("bozo"):
                raise error("argument --source: invalid rss source")
            if feed.get("status") != 200:
                raise error(format_summary(feed.get("feed", {}).get("summary")) or "invalid rss source")
        with open(CACHE_FILE, "ab") as cache_file:
            pickle.dump(feed, cache_file)
    logging.debug("Data parsed")

    if json_arg:
        result = process_json(feed, limit)
        print(json.dumps(result, indent=4))
    else:
        result = process_formatted_output(feed, limit)
        [print(chunk) for chunk in result if chunk]
    logging.debug("Work is done")


def main():
    run(sys.argv)
