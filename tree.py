import math
from fractions import Fraction
import itertools
import matplotlib.pyplot as plt


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
    returns true if number is a power of 2
    :param number: int
    :return: Bool
    """
    return (number != 0) and (number & (number - 1) == 0)


def new_level(number):
    """
    returns true if number is the sum of all powers of 2
    less than some arbitrary number
    ie following a breadth first traversal
    this node is the first of a new level
    :param number: int
    :return: Bool
    """
    return (number != 0) and (number & (number + 1) == 0)


def display_slice(start, stop):
    """
    print a sublist of the tree
    :param start: positive int
    :param stop: positive int greater than start
    :return: string
    """
    display = ""
    position = 1
    for node in get_slice(start, stop):
        display += str(node) + ", "
        if new_level(position):
            display += "\n"
        position += 1
    display += "\n"
    return display


def get_position(node):
    """
    given a rational number, find where it occurs in the tree
    :param node: Fraction
    :return: positive int
    """
    position = 1
    while node.denominator != 1:
        node = succ(node)
        position += 1
    position = 2**node.numerator - position - 1
    return position


def plot_distribution(n):
    """
    plot the distribution of the first n elements over the reals
    :param n: positive int
    :return:
    """
    x = get_slice(0, n)
    # y = [1 - Fraction(1 * position, n) for position in range(1, len(x) + 1)]
    # y = [0 for position in range(1, len(x) + 1)]
    y = [position for position in range(1, len(x) + 1)]
    plt.plot(x, y, "o")
    # plt.axis([0, int(math.floor(math.log(n, 2))) + 1, 0, 1.1])
    plt.axis([0, int(math.floor(math.log(n, 2))) + 1, -1, n + 1])
    plt.show()
