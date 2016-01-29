def reverse(s):
    """ (str) -> str
    Return a reversed version of s

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'

    """
    rev = ''
    for ch in s:
        rev = ch + rev
    return rev


def is_palindrome_v1(s):
    """
    :param s: str
    :return: bool
    Return True if an only if s is palindrome.

    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome_v1('dented')
    False

    """
    return s == reverse(s)


if __name__ == '__main__':
    import doctest
    doctest.testmod()