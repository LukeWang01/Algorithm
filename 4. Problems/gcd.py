# gcd(a, b) = gcd(b, a mod b)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_no_rec(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

print(gcd(12,16))