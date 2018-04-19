"""A module for demostrating exceptions."""

import sys


def convert(s):
    """Convert to an integer.

    Try this:

    >>> from exceptional import convert

    >>> convert(33)
    33
    >>> convert("hola")
    -1
    >>> convert([1, 2, 3])
    -1
    """
    x = -1
    try:
        x = int(s)
    except (ValueError, TypeError):
        pass
    return x


def convert2(s):
    """Convert to an integer."""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        return -1
