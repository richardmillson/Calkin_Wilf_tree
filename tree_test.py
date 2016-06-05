from tree import *

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
    assert get_nth(7) == given_first_7[6]


test_succ()
test_entire_tree()
test_get_nth()
