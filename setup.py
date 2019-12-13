from setuptools import setup

setup(
    name="rss-reader",
    version="0.52",
    scripts=['rss_reader.py'],
    entry_points={"console_scripts": ["rss-reader=rss_reader:main"]},
    install_requires=["argparse", "bs4", "colorama", "ebooklib", "feedparser", "html2text", "pillow",
                      "python-dateutil", "typing"],
    package_data={
        '': ['*.md', '*.rst'],
    },

    author="Olga Akhmetova",
    author_email="o.f.akhmetova@gmail.com",
    description="Utility to print RSS in console in readable format",
    keywords="RSS console",
    url="https://github.com/Trylar/rss-reader-python",
)
