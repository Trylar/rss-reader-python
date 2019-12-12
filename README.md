# rss-reader-python

rss_reader is a tool to receive rss data and print it in console in readable form.

Usage
-----

    rss_reader.py [-h] [-v] [--json] [--verbose] [--limit LIMIT] source

Only required argument is url source string, others are optional: 

    -h, --help     show this help message and exit
    -v, --version  show version and exit
    --json         show content in json format
    --verbose      show verbose status messages
    --limit LIMIT  news limit
    --date DATE    date for cached news in format YYYYMMDD

If ``limit`` is not provided, tool outputs all content.

If ``json`` argument is provided, tool returns data as json object with following structure:

    {
        "title": string,
        "entries": [
            {
                "title": string,
                "author": string,
                "link": string,
                "published": string,
                "summary": string,
                "comments": string,
                "links": [
                    {
                        "rel": string,
                        "type": string,
                        "href": string
                    }
                ]
            },
            ...
        ]
    }

If ```date``` argument is provided, news for this day are seeked in cache file. If there is no news, error is returned.
All other arguments work with this ```date``` argument as expected.

To run tool as command line utility:

* clone repository
* open command line from project folder
* run ```python setup.py sdist```
* run ```python setup.py install```

Now utility can be called from console like

    rss-reader [-h] [-v] [--json] [--verbose] [--limit LIMIT] source