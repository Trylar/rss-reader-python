from feedparser.util import FeedParserDict
import logging
from typing import Dict, List, Optional

from scripts import format_output


def process_formatted_output(feed: FeedParserDict, limit: int) -> List[Optional[str]]:
    """Form readable output for console"""
    logging.debug("Starting format output")
    result = [format_output.wrap_string(feed.get("feed", {}).get("title"))]
    for news in feed.get("entries")[:limit]:
        result.append(format_output.format_title(news.get("title")))
        result.extend(format_output.format_fields(news, "author", "link"))
        result.append(format_output.format_date(news.get("published")))
        result.append(format_output.format_summary(news.get("summary")))
        result.extend(format_output.format_fields(news, "comments"))
        result.extend(format_output.format_links(news.get("links")))
    logging.debug("Output formatted")
    return result


def process_json(feed: FeedParserDict, limit: int) -> Dict:
    """Form object for converting to json"""
    logging.debug("Starting create JSON object...")
    result = {"title": feed.get("feed", {}).get("title"), "entries": []}
    keys = ["title", "author", "link", "published", "summary", "comments", "links"]
    for news in feed.get("entries")[:limit]:
        result["entries"].append({key: news[key] for key in keys if key in news})
    logging.debug("JSON created")
    return result
