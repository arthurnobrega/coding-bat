"""
http://codingbat.com/prob/p124676

Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num)
computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False

"""


def near_hundred(n):
    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    return False


if __name__ == '__main__':
    assert near_hundred(90) == True
    assert near_hundred(100) == True
    assert near_hundred(110) == True

    assert near_hundred(89) == False
    assert near_hundred(50) == False
    assert near_hundred(0) == False

    assert near_hundred(190) == True
    assert near_hundred(200) == True
    assert near_hundred(210) == True
