"""Write data in epub file"""
from bs4 import BeautifulSoup
from ebooklib import epub
from feedparser.util import FeedParserDict
import io
import logging
import os
from pathlib import Path
from PIL import Image
import urllib.request

from scripts import utils


def create_epub_file(arguments, feed, limit):
    """Try to create epub file and write it"""
    path = arguments.output_path if check_path(arguments.output_path) else get_default_path()
    try:
        epub_data = process_output_to_epub(feed, limit)
        epub.write_epub(path, epub_data, {})
    except Exception as e:
        raise utils.Error(str(e))
    else:
        print("Epub file", path, "was successfully created")


def check_path(path: str) -> bool:
    """Check if passed dir exists and filename has right extension"""
    return path and os.path.exists(os.path.dirname(path)) and os.path.basename(path).endswith(".epub")


def get_default_path() -> str:
    """Get home directory if path is not specified"""
    print("Path is invalid or not specified. Creating news.epub file in home directory", str(Path.home()))
    return os.path.join(str(Path.home()), "news.epub")


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
