
# recursion, from top down

def cut_rod_recursion(p, n):
    if n == 0:
        res = 0

    else:
        res = 0
        for i in range(1, n + 1):
            res = max(res, p[i] + cut_rod_recursion(p, n - 1))

    return res

# with 4. Problems, from down to top, like dict, save the caculated value

def cut_rod_dp(p, n):
    r = [0]
    for i in range(1, n + 1):
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] + r[i - j])

        r.append(res)
    return r[n]


def cut_rod_dp_output(p, n):
    r = [0]
    s = [0]
    for i in range(1, n + 1):
        res_r = 0
        res_s = 0
        for j in range(1, i + 1):
            if res_r < (p[j] + res_r[i -j]):
                res_r = p[j] + res_r[i -j]
                res_s = j

        r.append(res_r)
        s.append(res_s)

    return res_r[n], s


def cut_rod_method(p, n):
    r, s = cut_rod_dp_output(p, n)
    solution = []

    # trace back
    while n > 0:
        solution.append(s[n])
        n -= s[n]

    return r, solution






