from tree import *


def test_succ_fcn():
    first_7 = [Fraction(1, 1), Fraction(1, 2), Fraction(2, 1), Fraction(1, 3), Fraction(3, 2), Fraction(2, 3),
               Fraction(3, 1)]

    gen_7 = [Fraction(1, 1)]
    for n in range(2, 8):
        gen_7 += [succ_fcn(gen_7[n - 2])]

    assert first_7 == gen_7

def test_generator_succ():
    start = 0
    end = 7
    gen_7 = list(itertools.islice(generator_succ(), start, end))
    print gen_7
    print len(gen_7)

test_succ_fcn()
test_generator_succ()
