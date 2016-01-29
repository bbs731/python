def remove_shared(L1, L2):
    """(list, list) -> NoneType
    Remove element from L1 that in both L1 and L2
    """

    for v in L2:
        if v in L1:
            L1.remove(v)

if __name__ == '__main__':
    import doctest
    doctest.testmod()