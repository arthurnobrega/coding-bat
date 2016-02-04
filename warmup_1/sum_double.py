"""
http://codingbat.com/prob/p141905

Given two int values, return their sum. Unless the two values are the same,
then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""


def sum_double(a, b):
    result = a + b
    if a == b:
        result *= 2
    return result


if __name__ == '__main__':
    assert sum_double(1, 2) == 3
    assert sum_double(3, 2) == 5
    assert sum_double(2, 2) == 8

    assert sum_double(10, 10) == 40
