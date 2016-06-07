import math
from fractions import Fraction
import itertools

# TODO given a rational number, find its location in the tree
# TODO visually display the tree
# TODO look at the distribution of elements over the reals


def succ(x):
    """
    takes an element of the Calkin Wilf tree and returns the next element
    following a breadth first traversal
    :param x: Fraction
    :return: Fraction
    """
    x_int = Fraction(math.floor(x))
    x_nonint = Fraction(x.numerator - x_int * x.denominator, x.denominator)
    return Fraction(1 / (x_int + 1 - x_nonint))


def entire_tree():
    """
    a generator for the entire Calkin Wilf tree
    :return: generator of Fraction
    """
    x = Fraction(1, 1)
    yield x
    while True:
        x = succ(x)
        yield x


def get_nth(n):
    """
    returns the nth element of the tree following a breadth first traversal
    :param n: positive int
    :return: Fraction
    """
    return get_slice(n, n + 1)[0]


def get_slice(start, stop):
    """
    return a finite sublist from the infinite generator
    :param start: positive int
    :param stop: positive int greater than start
    :return: tuple
    """
    return tuple(itertools.islice(entire_tree(), start, stop))


def is_power_of_two(number):
    """
    returns true if num is a power of 2
    :param number: int
    :return: Bool
    """
    return (number != 0) and (number & (number - 1) == 0)


def display_slice(start, stop):
    """
    print a sublist of the tree
    :param start: positive int
    :param stop: positive int greater than start
    :return: string
    """
    display = ""
    position = 0
    for node in get_slice(start, stop):
        display += str(node) + ","
        if position % 2 == 0:
            display += "\n"
        position += 1
    display += "\n"
    return display
