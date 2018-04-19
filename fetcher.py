"""Retrieve and print words from a URL.

Usage:

python3 words.py <URL>

"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: the URL as UTF-8 text

        Returns:
            A list of strings with the words of the document.
    """
    with urlopen(url) as content:
        fetched_words = []
        for line in content:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                fetched_words.append(word)
    return fetched_words


def print_items(items):
    """Print items, one per line.

    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document provided by URL.

    Args:
        url: the URL of an UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename
