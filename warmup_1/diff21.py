"""
http://codingbat.com/prob/p197466

Given an int n, return the absolute difference between n and 21, except return
double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
"""


def diff21(n):
    diff = 21 - n

    if n > 21:
        return diff * -2

    return diff


if __name__ == '__main__':
    assert diff21(19) == 2
    assert diff21(10) == 11
    assert diff21(21) == 0
    assert diff21(22) == 2
    assert diff21(23) == 4
    assert diff21(24) == 6
    assert diff21(30) == 18
