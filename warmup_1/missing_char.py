"""
http://codingbat.com/prob/p190570

Given a non-empty string and an int n, return a new string where the char at
index n has been removed. The value of n will be a valid index of a char in
the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""


def missing_char(word, n):
    return word[:n] + word[n+1:]


if __name__ == '__main__':
    assert missing_char('kitten', 1) == 'ktten'
    assert missing_char('kitten', 0) == 'itten'
    assert missing_char('kitten', 4) == 'kittn'

    assert missing_char('dog', 0) == 'og'
    assert missing_char('dog', 1) == 'dg'
    assert missing_char('dog', 2) == 'do'
