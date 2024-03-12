def rc1(ord):
    if ord == 0:
        return 0
    return int(9 * rc1(ord - 1) + 10**(ord - 1) - 1)
