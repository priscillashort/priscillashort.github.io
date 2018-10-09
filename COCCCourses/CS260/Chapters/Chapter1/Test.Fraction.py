
"""
    Test code for Fraction class
"""

import unittest
from Fraction import Fraction


class TestFraction(unittest.TestCase):
    """
        Unit test class for Fraction class
    """

    def setUp(self):
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(2, 8)
        self.f3 = Fraction(1, 4)
        self.f4 = Fraction(-1, 5)
        self.f5 = Fraction(1, -6)
        self.f6 = Fraction(-1, -4)

    def tearDown(self):
        pass

    def test_init(self):
        fail = False

        try:
            f = Fraction(1, 0)
        except ValueError:
            fail = True

        self.assertTrue(fail)
        self.assertTrue(self.f6.num == 1)
        self.assertTrue(self.f6.den == 4)

    def test_init_type(self):
        fail = False

        try:
            f = Fraction(1.0, 3)
        except TypeError:
            fail = True

        self.assertTrue(fail)

    def test_str(self):
        self.assertEqual(str(self.f1), "1/2")
        self.assertEqual(str(self.f4), "-1/5")
        self.assertEqual(str(self.f6), "1/4")

    def test_add(self):
        self.assertEqual(self.f1 + self.f2, Fraction(3, 4))
        self.assertEqual(self.f3 + self.f6, Fraction(1, 2))
        self.assertEqual(self.f1 + self.f4, Fraction(3, 10))

    def test_sub(self):
        self.assertEqual(self.f1 - self.f2, Fraction(1, 4))
        self.assertEqual(self.f3 - self.f6, Fraction(0, 4))
        self.assertEqual(self.f1 - self.f4, Fraction(7, 10))

    def test_mul(self):
        self.assertEqual(self.f1 * self.f2, Fraction(1, 8))
        self.assertEqual(self.f3 * self.f4, Fraction(-1, 20))

    def test_truediv(self):
        self.assertEqual(self.f1 / self.f2, Fraction(2, 1))
        self.assertEqual(self.f3 / self.f4, Fraction(-5, 4))

    def test_eq(self):
        self.assertNotEqual(self.f1, self.f2)
        self.assertEqual(self.f2, self.f3)
        self.assertEqual(self.f2, self.f6)
        self.assertEqual(Fraction(-1, 2), Fraction(1, -2))
        self.assertEqual(Fraction(-1, -2), Fraction(1, 2))

    def test_lt(self):
        self.assertTrue(self.f2 < self.f1)
        self.assertTrue(self.f4 < self.f5)
        self.assertFalse(self.f6 < self.f3)
        self.assertTrue(Fraction(-1, 2) < Fraction(1, -4))
        self.assertTrue(Fraction(-1, -4) < Fraction(1, 2))

    def test_gt(self):
        self.assertTrue(self.f1 > self.f2)
        self.assertTrue(self.f5 > self.f4)
        self.assertFalse(self.f3 > self.f6)
        self.assertTrue(Fraction(-1, 4) > Fraction(1, -2))
        self.assertTrue(Fraction(-1, -2) > Fraction(1, 4))

    def test_le(self):
        self.assertTrue(self.f2 <= self.f1)
        self.assertTrue(self.f4 <= self.f5)
        self.assertTrue(self.f6 <= self.f3)
        self.assertTrue(Fraction(-1, 2) <= Fraction(1, -4))
        self.assertTrue(Fraction(-1, -4) <= Fraction(1, 2))

    def test_ge(self):
        self.assertTrue(self.f1 >= self.f2)
        self.assertTrue(self.f5 >= self.f4)
        self.assertTrue(self.f3 >= self.f6)
        self.assertTrue(Fraction(-1, 4) >= Fraction(1, -2))
        self.assertTrue(Fraction(-1, -2) >= Fraction(1, 4))

    def test_ne(self):
        self.assertNotEqual(self.f1, self.f2)
        self.assertEqual(self.f2, self.f3)
        self.assertEqual(self.f2, self.f6)
        self.assertEqual(Fraction(-1, 2), Fraction(1, -2))
        self.assertEqual(Fraction(-1, -2), Fraction(1, 2))

    def test_iadd(self):
        self.f1 += self.f2
        self.assertEqual(self.f1, Fraction(3, 4))
        self.f3 += self.f6
        self.assertEqual(self.f3, Fraction(1, 2))
        self.f1 += self.f4
        self.assertEqual(self.f1, Fraction(11, 20))
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(2, 8)
        self.f3 = Fraction(1, 4)
        self.f4 = Fraction(-1, 5)
        self.f6 = Fraction(-1, -4)
    


if __name__ == "__main__":
    unittest.main()
