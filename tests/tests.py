import feedparser
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

from rss_reader import rss_reader
from scripts import process_data, argument_parser, format_output
from tests import tests_data


class TestRunner(unittest.TestCase):
    def test_format_title(self):
        self.assertEqual(format_output.format_title("title"), "\n-----\ntitle\n-----\n")

    def test_format_title_empty(self):
        self.assertEqual(format_output.format_title(""), None)

    def test_format_title_none(self):
        self.assertEqual(format_output.format_title(None), None)

    def test_format_fields_zero(self):
        feed = {"author": "Rowling", "book": "Harry Potter"}
        self.assertEqual(format_output.format_fields(feed), [])

    def test_format_fields_one(self):
        news = {"author": "Rowling", "book": "Harry Potter"}
        self.assertEqual(format_output.format_fields(news, "author"), ["Author: Rowling"])

    def test_format_fields_two(self):
        feed = {"author": "Rowling", "book": "Harry Potter"}
        self.assertEqual(format_output.format_fields(feed, "author", "book"),
                         ["Author: Rowling", "Book: Harry Potter"])

    def test_format_date_default_title(self):
        self.assertEqual(format_output.format_date("Thu, 05 Dec 2019 14:34:13 +0300"),
                         "Published: Thursday, 05 December 2019 14:34:13")

    def test_format_date_title(self):
        self.assertEqual(format_output.format_date("Thu, 05 Dec 2019 14:34:13 +0300", "Date"),
                         "Date: Thursday, 05 December 2019 14:34:13")

    def test_format_summary_text(self):
        self.assertEqual(format_output.format_summary("News description"), "\nNews description\n")

    def test_format_summary_html(self):
        self.assertEqual(format_output.format_summary("<p>News description<p>"), "\nNews description\n")

    def test_format_links_default_title(self):
        links = [{"href": "https://xkcd.com/353/"}]
        self.assertEqual(format_output.format_links(links), ["Links:", "https://xkcd.com/353/"])

    def test_format_links_same_links(self):
        links = [{"href": "https://xkcd.com/353/"}, {"href": "https://xkcd.com/1987/"},
                 {"href": "https://xkcd.com/353/"}]
        self.assertEqual(format_output.format_links(links),
                         ["Links:", "https://xkcd.com/353/", "https://xkcd.com/1987/"])

    def test_add_title(self):
        self.assertEqual(format_output.add_title("Batman", "superhero"), "Superhero: Batman")

    def test_wrap_string_default(self):
        self.assertEqual(format_output.wrap_string("Batman"), "\nBatman\n")

    def test_wrap_string_wrapper(self):
        self.assertEqual(format_output.wrap_string("Batman", "***"), "***\nBatman\n***")

    def test_wrap_string_wrappers(self):
        self.assertEqual(format_output.wrap_string("Batman", "***", "^^^"), "^^^\n***\nBatman\n***\n^^^")

    def test_process_json(self):
        feed = tests_data.feed
        json = tests_data.json
        self.assertEqual(process_data.process_json(feed, 2), json)

    def test_process_formatted_output(self):
        feed = tests_data.feed
        output = tests_data.output
        self.assertEqual(process_data.process_formatted_output(feed, 2), output)

    def test_process_json_empty(self):
        empty_feed = tests_data.empty_feed
        self.assertEqual(process_data.process_json(empty_feed, 2), {'entries': [], 'title': None})

    def test_process_formatted_output_empty(self):
        empty_feed = tests_data.empty_feed
        self.assertEqual(process_data.process_formatted_output(empty_feed, 2), [None])

    def test_parse_args(self):
        arguments = argument_parser.parse_args(["https://stackoverflow.com/feeds/", "--limit", "2"])
        self.assertEqual(arguments.source, "https://stackoverflow.com/feeds/")
        self.assertEqual(arguments.limit, "2")
        self.assertFalse(arguments.json)

    @patch.object(feedparser, "parse")
    def test_run(self, mock_parse):
        args = ["rss_reader.py", "https://stackoverflow.com/feeds/", "--limit", "2"]
        mock_parse.return_value = tests_data.feed
        output = tests_data.printed_output
        stream = StringIO()
        with redirect_stdout(stream):
            rss_reader.run(args)
            self.assertEqual(stream.getvalue(), output)


if __name__ == '__main__':
    unittest.main()
