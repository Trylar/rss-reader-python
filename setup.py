from setuptools import setup, find_packages

from scripts.version import __version__ as version

setup(
    name="rss-reader",
    version=version,
    packages=find_packages(),
    entry_points={"console_scripts": ["rss-reader=rss_reader.rss_reader:main"]},
    install_requires=["argparse==1.4.0", "bs4==0.0.1", "colorama==0.4.3", "ebooklib==0.17.1", "feedparser==6.0.0b1",
                      "html2text==2019.9.26", "pillow==9.0.1", "python-dateutil==2.8.1"],
    package_data={"": ["*.md", "*.rst"], },

    author="Olga Akhmetova",
    author_email="o.f.akhmetova@gmail.com",
    description="Utility to print RSS in console in readable format",
    keywords="RSS console",
    url="https://github.com/Trylar/rss-reader-python",
    python_requires=">=3.7.4",
)
