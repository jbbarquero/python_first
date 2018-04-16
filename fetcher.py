import sys
from urllib.request import urlopen


def fetch_words(url):
    with urlopen(url) as content:
        fetched_words = []
        for line in content:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                fetched_words.append(word)
    return fetched_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
