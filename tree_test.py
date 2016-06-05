from tree import *

first_7 = [Fraction(1, 1), Fraction(1, 2), Fraction(2, 1), Fraction(1, 3), Fraction(3, 2), Fraction(2, 3), Fraction(3, 1)]


def test_succ():
    gen_7 = [Fraction(1, 1)]
    for n in range(2, 8):
        gen_7 += [succ(gen_7[n - 2])]
    assert first_7 == gen_7


def test_entire_tree():
    start = 0
    stop = 7
    gen_7 = list(itertools.islice(entire_tree(), start, stop))
    assert first_7 == gen_7


def test_get_nth():
    assert first_7[6] == get_nth(7)

test_succ()
test_entire_tree()
test_get_nth()
