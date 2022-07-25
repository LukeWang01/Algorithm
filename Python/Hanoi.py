def hanoi(n, a, b, c):
    # n blocks from a via b to c
    if n > 0:
        hanoi(n-1, a, c, b)
        print(f"moving from {a} to {c}")
        hanoi(n-1, b, a, c)


hanoi(3, 'a', 'b', 'c')
# n = 2*(n-1) + 1
# around to 2^n

