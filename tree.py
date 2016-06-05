import math
from fractions import Fraction
import itertools


def succ(x):
    """
    takes an element of the Calkin Wilf tree and returns the next element
    following a breadth first traversal
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
    takes a positive integer n and returns the nth element of the Calkin Wilf tree
    following a breadth first traversal
    :param n: int
    :return: Fraction
    """
    return get_slice(n - 1, n)[0]


def get_slice(start, stop):
    """
    return a finite sublist from the infinite generator
    :param start: int
    :param stop: int
    :return: list
    """
    return tuple(itertools.islice(entire_tree(), start, stop))
