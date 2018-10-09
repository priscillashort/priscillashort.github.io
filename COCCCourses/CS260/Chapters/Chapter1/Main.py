"""
    Main driver for display/testing...
"""

from Fraction import Fraction
from Fraction import gcd

print("...................")
x = Fraction(1,2)
y = Fraction(2,3)
print("x:", x)
print("y:", y)
print("x + y:", x + y)
print("x - y:", x - y)
print("x * y =", x * y)
print("x / y:", x / y)
print("x == y:", x == y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
print("x != y:", x != y)
x += y
print("x += y:", x)
print("repr(x):", repr(x))
print("...................")
a = Fraction(1,-2)
b = Fraction(-2,3)
print("a:", a)
print("b:", b)
print("a + b:", a + b)
print("a - b:", a - b)
print("a * b =", a * b)
print("a / b:", a / b)
print("a == b:", a == b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print("a != b:", a != b)
print("...................")
help(Fraction)
