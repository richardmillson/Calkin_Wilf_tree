import math
from fractions import Fraction
import itertools


def succ_fcn(x):
    """
    takes an element of the Calkin Wilf tree and returns the next element
    following a breadth first traversal
    """
    x_int = Fraction(math.floor(x))
    x_nonint = Fraction(x.numerator - x_int * x.denominator, x.denominator)
    return Fraction(1 / (x_int + 1 - x_nonint))


def generator_succ():
    """
    a generator for the entire Calkin Wilf tree
    """
    x = Fraction(1, 1)
    yield x
    while True:
        x_int = Fraction(math.floor(x))
        x_nonint = Fraction(x.numerator - x_int * x.denominator, x.denominator)
        x = Fraction(1 / (x_int + 1 - x_nonint))
        yield x


def get_nth(n):
    """
    takes a natural number n and returns the nth element of the Calkin Wilf tree
    following a breadth first traversal
    """
    node = Fraction(1, 1)
    for i in range(1, n + 1):
        node = succ_fcn(node)
    return node
