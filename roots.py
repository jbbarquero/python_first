"""More exceptions treatment"""


def sqrt(x):
    """Compute square roots using the method of Heron of Alexandria

    Args:
        x: the number for which the square root is to be computed.

    Returns:
        The square root of x.
    """
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    """Calculate some square roots."""
    print(sqrt(9))
    print(sqrt(2))
    try:
        print(sqrt(-1))
    except ZeroDivisionError:
        print("Cannot copute square root of a negative number.")

    print("End main.")


if __name__ == '__main__':
    main()