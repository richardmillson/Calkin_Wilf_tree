import math


def succ_fcn(x):
    """
    takes an element of the Calkin Wilf tree and returns the next element
    following a breadth first traversal
    """
    return 1 / (math.floor(x) + 1 - (x % 1))
