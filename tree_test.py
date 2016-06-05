from tree import *
import timeit

given_first_7 = (Fraction(1, 1), Fraction(1, 2), Fraction(2, 1), Fraction(1, 3), Fraction(3, 2), Fraction(2, 3), Fraction(3, 1))


def test_succ():
    for n in range(len(given_first_7) - 1):
        assert succ(given_first_7[n]) == given_first_7[n + 1]


def test_entire_tree():
    start = 0
    stop = 7
    generated_first_7 = get_slice(start, stop)
    assert generated_first_7 == given_first_7


def test_get_nth():
    assert get_nth(3) == given_first_7[3]
    assert get_nth(6) == given_first_7[6]


def time_get_nth(n):
    """
    time how long it takes the accumulator to get the nth element
    :param n: positive int
    :return: float
    """
    start = timeit.default_timer()
    get_nth(n)
    stop = timeit.default_timer() - start
    return stop


def time_get_slice(n):
    """
    time how long it takes get_slice to get the nth element
    :param n: positive int
    :return: float
    """
    start = timeit.default_timer()
    get_slice(n-1, n)
    stop = timeit.default_timer() - start
    return stop


test_succ()
test_entire_tree()
test_get_nth()

print given_first_7
n = 2
print time_get_nth(n), get_nth(n)
print time_get_slice(n), get_slice(n, n + 1)[0]
# print time_get_nth(100000)
