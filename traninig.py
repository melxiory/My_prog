from fractions import Fraction
from math import factorial


def expand(x, digit):
    x = Fraction(f'{x}')
    value_1 = factorial_k = 1
    while True:
        if len(str(value_1.numerator)) >= digit:
            return [value_1.numerator, value_1.denominator]
        value_1 += Fraction(x ** factorial_k, factorial(factorial_k))
        factorial_k += 1

print(expand(1.6, 10))
print(expand(1, 2))
print(expand(2, 5))
print(expand(3, 10))
print(expand(1.5, 10))
print(expand(1.6, 10))
