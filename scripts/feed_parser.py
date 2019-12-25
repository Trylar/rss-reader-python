import feedparser
from feedparser.util import FeedParserDict


def parse_feeds(source: str) -> FeedParserDict:
    """Parse url source"""
    return feedparser.parse(source)
