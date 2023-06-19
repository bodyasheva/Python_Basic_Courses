import math


class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        res_a = self.a * other.a
        res_b = self.b * other.b
        return Fraction(res_a, res_b)

    @staticmethod
    def fraction_operations(first_numer, first_den, second_numer, second_den):
        lcm = first_den * second_den
        res_a_first = first_numer * (lcm / first_den)
        res_a_second = second_numer * (lcm / second_den)
        res_b = lcm
        return res_a_first, res_a_second, res_b

    def __add__(self, other):
        res_a_first, res_a_second, res_b = self.fraction_operations(self.a, self.b, other.a, other.b)
        res_a = res_a_first + res_a_second
        return Fraction(int(res_a), int(res_b))

    def __sub__(self, other):
        res_a_first, res_a_second, res_b = self.fraction_operations(self.a, self.b, other.a, other.b)
        res_a = res_a_first - res_a_second
        return Fraction(int(res_a), int(res_b))

    def __eq__(self, other):
        res_a_first, res_a_second, res_b = self.fraction_operations(self.a, self.b, other.a, other.b)
        return res_a_first == res_a_second

    def __gt__(self, other):
        res_a_first, res_a_second, res_b = self.fraction_operations(self.a, self.b, other.a, other.b)
        return res_a_first > res_a_second

    def __lt__(self, other):
        res_a_first, res_a_second, res_b = self.fraction_operations(self.a, self.b, other.a, other.b)
        return res_a_first < res_a_second

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
