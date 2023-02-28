t = [100, 50, 20, 5, 1]


def greedy_change(n, t):

    res = [0 for i in range(len(t))]

    for i, money in enumerate(t):
        res[i] = n // money
        n = n % money

    return res, n
