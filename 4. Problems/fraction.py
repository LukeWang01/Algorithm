class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd_no_rec(a, b)
        self.a /= x
        self.b /= x

    def lcm(self, a, b):
        x = self.gcd_no_rec(a, b)
        return a * b / x

    @staticmethod
    def gcd_no_rec(a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    def __add__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        denominator = self.lcm(b, d)
        numerator = a * (denominator / b) + c * (denominator /d)
        return Fraction(numerator, denominator)

    def __str__(self):
        return f"{int(self.a)}/{int(self.b)}"


f1 = Fraction(30, 16)
f2 = Fraction(30, 54)
print(f1 + f2)

