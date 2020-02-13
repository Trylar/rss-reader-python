"""Work with cache"""
import datetime
from dateutil.parser import parse as parse_date
import os
import pickle
from typing import Dict, List

from scripts import utils

CACHE_FILE = "../rss-reader-cache"


def write_to_cache(feed):
    """Write data to cache"""
    with open(CACHE_FILE, "ab") as cache_file:
        pickle.dump(feed, cache_file)


def load_cache(cache_file):
    """Load cache from file until EOF"""
    cache = []
    while True:
        try:
            cache.append(pickle.load(cache_file))
        except EOFError:
            break
    return cache


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
                raise utils.Error("empty cache")
    else:
        raise utils.Error("empty cache")
    return feed


def get_news(feed_news: List, cached_news: List, date: datetime) -> List:
    """Get news with corresponding date from cached_news, deleting duplicates"""
    return [news for news in cached_news if same_day(news.published, date) and news not in feed_news]


def same_day(news_date: str, arg_date: datetime):
    """Check if news_date is the same day as arg_date"""
    return parse_date(news_date).date() == arg_date.date()
