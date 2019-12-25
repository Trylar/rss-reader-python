# rss-reader-python

rss_reader is a tool to receive rss data and print it in console in readable form.

Usage
-----

    usage: rss_runner.py [-h] [-v] [--json] [--verbose] [--limit LIMIT]
                         [--date DATE] [--to-epub] [--output-path OUTPUT_PATH]
                         [--colorize]
                         source

Only required argument is url source string, others are optional: 

    positional arguments:
      source                rss source
    
    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show version and exit
      --json                show content in json format
      --verbose             show verbose status messages
      --limit LIMIT         news limit
      --date DATE           date for cached news in format YYYYMMDD
      --to-epub             save data in epub file
      --output-path OUTPUT_PATH
                            path to the new file for saving
      --colorize            colorize output

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

```limit``` should be non-negative number, if not provided, tool outputs all content.

If ```date``` argument is provided, news for this day are seeked in cache file. If there is no news, error is returned.
All other arguments work with this ```date``` argument as expected.

If ```to-epub```  argument is provided, news will be converted and saved in .epub file. Optional argument
```output-path``` allows to specify path for file. If it is invalid or is not specified, file wiil be saved in current directory. If ```to-epub```
argument is missing, ```output-path``` will be ignored. If ```json``` argument is present, ```to-epub``` will be ignored.

Argument ```colorize```, if present, colorizes output in console in different random colors. Not working with ```json``` argument. 

To run tool as command line utility:

* clone repository
* open command line from project folder
* run ```python setup.py build```
* run ```python setup.py install```

Now utility can be called from console like

    rss-reader [-h] [-v] [--json] [--verbose] [--limit LIMIT]
               [--date DATE] [--to-epub] [--output-path OUTPUT_PATH]
               [--colorize]
               source