
# recursive:
def fibnacci(n):
    if n == 1 or n==2:
        return 1
    else:
        return fibnacci(n - 1) + fibnacci(n - 2)


print(fibnacci(10))


# subproblem + repeat
def fibnacci_no_recursion(n):
    tmp = [0, 1, 1]
    if n > 2:
        for i in range(n-2):
            num = tmp[-2] + tmp[-1]
            tmp.append(num)
    return tmp[n]




