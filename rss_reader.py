"""Utility to print RSS in console in readable format"""
# !/usr/bin/env python
import argparse
from bs4 import BeautifulSoup
import colorama
import datetime
from ebooklib import epub
import feedparser
from feedparser.util import FeedParserDict
import html2text
import io
import json
from typing import List, Dict, Optional
from dateutil.parser import parse as parse_date, ParserError
import logging
import os
from pathlib import Path
import pickle
from PIL import Image
import sys
import urllib.request

VERSION = "0.5"
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


def process_images(images, book):
    """Download images by url to local file and add to epub book"""
    for img in images:
        src = str(hash(img.get("src"))) + ".jpg"
        urllib.request.urlretrieve(img.get("src"), src)
        img["src"] = src
        try:
            image = Image.open(src)
            image_rgb = image.convert("RGB")
            image_stream = io.BytesIO()
            image_rgb.save(image_stream, 'jpeg')
            image_content = image_stream.getvalue()
            image_item = epub.EpubItem(uid=str(hash(src)), file_name=src, media_type='image/jpeg',
                                       content=image_content)
            book.add_item(image_item)
        except Exception:
            pass
        try:
            os.remove(src)
        except Exception:
            pass


def create_title(title: str) -> str:
    """Add title to news"""
    return "<h3>" + title + "</h3>"


def create_link(link: str) -> str:
    """Add link to news on external resource"""
    return "<br><a href='" + link + "'>Link</a>"


def process_output_to_epub(feed: FeedParserDict, limit: int) -> epub.EpubBook:
    """Form epub structure for epub file"""
    logging.debug("Starting format html for epub file")
    book = epub.EpubBook()
    book.set_identifier('rss news')
    book.set_title(feed.get("feed", {}).get("title"))
    book.set_language('en')

    book.spine = ['nav']
    book.toc = []
    for news in feed.get("entries")[:limit]:
        chapter = epub.EpubHtml(title=news.get("title"), file_name=str(hash(news.get("title"))) + '.xhtml')
        content = BeautifulSoup(create_title(news.get("title")) + news.get("summary") + create_link(news.get("link")),
                                "lxml")
        images = content.find_all('img')
        process_images(images, book)
        chapter.set_content(str(content))
        book.add_item(chapter)
        book.spine.append(chapter)
        book.toc.append(chapter)

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)
    logging.debug("Structure for epub file created")
    return book


def parse_args(args):
    """Create argument parser, parse arguments and return them"""
    arg_parser = create_arg_parser("Get rss source and show it's content")
    arg_parser.add_argument("source", action="store", help="rss source")
    arg_parser.add_argument("-v", "--version", action="version", help="show version and exit", version=VERSION)
    arg_parser.add_argument("--json", action="store_true", help="show content in json format", default=False)
    arg_parser.add_argument("--verbose", action="store_true", help="show verbose status messages", default=False)
    arg_parser.add_argument("--limit", action="store", help="news limit", default=-1)
    arg_parser.add_argument("--date", action="store", help="date for cached news in format YYYYMMDD")
    arg_parser.add_argument("--to-epub", action="store_true", help="save data in epub file", default=False)
    arg_parser.add_argument("--output-path", action="store", help="path to the new file for saving")
    arg_parser.add_argument("--colorize", action="store_true", help="colorize output", default=False)
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


def check_path(path: str) -> bool:
    """Check if passed dir exists and filename has right extension"""
    return path and os.path.exists(os.path.dirname(path)) and os.path.basename(path).endswith(".epub")


def get_default_path() -> str:
    """Get home directory if path is not specified"""
    print("Path is invalid or not specified. Creating news.epub file in home directory", str(Path.home()))
    return os.path.join(str(Path.home()), "news.epub")


def random_color(data):
    colors = [colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE,
              colorama.Fore.MAGENTA, colorama.Fore.CYAN, colorama.Fore.WHITE]
    return colors[hash(data) % 7]


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
    if arguments.output_path and not arguments.to_epub:
        print("Argument --output-path will be ignored")
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
            raise error("unexpected error while parsing, check rss source: " + str(e))
        else:
            if feed.get("bozo"):
                raise error("argument --source: invalid rss source")
            if feed.get("status") != 200:
                raise error(format_summary(feed.get("feed", {}).get("summary")) or "invalid rss source")
        with open(CACHE_FILE, "ab") as cache_file:
            pickle.dump(feed, cache_file)
    logging.debug("Data parsed")

    if json_arg:
        if arguments.to_epub:
            print("Argument --to-epub will be ignored")
        result = process_json(feed, limit)
        print(json.dumps(result, indent=4))
    else:
        if arguments.to_epub:
            path = arguments.output_path if check_path(arguments.output_path) else get_default_path()
            try:
                epub_data = process_output_to_epub(feed, limit)
                epub.write_epub(path, epub_data, {})
            except Exception as e:
                raise error(str(e))
            else:
                print("Epub file", path, "was successfully created")
        else:
            result = process_formatted_output(feed, limit)
            if arguments.colorize:
                colorama.init()
                [print(random_color(chunk) + chunk) for chunk in result if chunk]
                colorama.deinit()
            else:
                [print(chunk) for chunk in result if chunk]
    logging.debug("Work is done")


def main():
    run(sys.argv)
