import math
from fractions import Fraction


def succ_fcn(x):
    """
    takes an element of the Calkin Wilf tree and returns the next element
    following a breadth first traversal
    """
    print float(x), Fraction(x % 1)
    return Fraction(1 / (math.floor(x) + 1 - (x % 1)))


def get_nth(n):
    """
    takes a natural number n and returns the nth element of the Calkin Wilf tree
    following a breadth first traversal
    """
    node = Fraction(1, 1)
    for i in range(1, n + 1):
        node = succ_fcn(node)
    return node
