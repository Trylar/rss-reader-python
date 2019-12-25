"""Format data for nice output"""
from dateutil.parser import parse as parse_date, ParserError
from feedparser.util import FeedParserDict
import html2text
from typing import List, Optional


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
