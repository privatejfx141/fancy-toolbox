"""This module contains a basic implementaton of a fraction class.

Author: Jeffrey Li
Created: January 7, 2017
Modified: November 12, 2017
Software Engineering
University of Toronto
"""

class Fraction(object):
    """A class to represent a fraction, rational number."""

    @staticmethod
    def _gcd(num1, num2):
        return num2 if (num1 % num2 == 0) else Fraction._gcd(num2, num1 % num2)

    @staticmethod
    def _lcm(num1, num2):
        return (num1 * num2) // Fraction._gcd(num1, num2)

    def __init__(self, numerator, denominator):
        """(Fraction, int or Fraction, int or Fraction) -> NoneType

        Creates a fraction with a numerator and denominator.

        REQ: denominator != 0
        """
        if denominator == 0:
            raise ValueError("denominator cannot be zero")
        if numerator < 0 and denominator < 0:
            self._n = abs(numerator)
            self._d = abs(denominator)
        elif numerator >= 0 and denominator < 0:
            self._n = -numerator
            self._d = abs(denominator)
        else:
            self._n = numerator
            self._d = denominator

    def __hash__(self):
        return (self._n, self._d, repr(self)).__hash__()

    @staticmethod
    def convert_int(integer, denominator=1):
        """(int[, int]) -> Fraction

        Converts the given integer to a fraction with the set denominator.

        REQ: denominator != 0
        """
        if denominator == 0:
            raise ValueError("denominator cannot be zero")
        return Fraction(integer * denominator, denominator)

    def __int__(self):
        return int(self.decimal())

    def __float__(self):
        return self.decimal()

    @staticmethod
    def convert_float(rational, simplify=True):
        """(float[, bool]) -> Fraction

        Converts the given float to a fraction.
        """
        num = rational
        den = 1
        if isinstance(rational, float):
            while not num.is_integer():
                num *= 10
                den *= 10
        result = Fraction(int(num), den)
        if simplify:
            result = result.simplify()
        return result

    def __lt__(self, other):
        if isinstance(other, Fraction):
            other_n = other.numerator()
            other_d = other.denominator()
            if self._d == other_d:
                return self._n < other_n
            else:
                return self._n * other_d < other_n * self._d
        else:
            return self._n < other * self._d

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __eq__(self, other):
        if isinstance(other, int):
            return self._n == other * self._d
        elif isinstance(other, Fraction):
            if self._d == other.denominator():
                return self._n == other.numerator()
            simp_self = self.simplify()
            simp_other = other.simplify()
            same_n = simp_self.numerator() == simp_other.numerator()
            same_d = simp_self.denominator() == simp_other.denominator()
            return same_n and same_d

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, Fraction):
            other_n = other.numerator()
            other_d = other.denominator()
            if self._d == other_d:
                return self._n > other_n
            else:
                return self._n * other_d > other_n * self._d
        else:
            return self._n > other * self._d

    def __abs__(self):
        if self._n > 0:
            return self
        else:
            return Fraction(abs(self._n), self._d)

    def __add__(self, other):
        new_n = num1 = self._n
        new_d = den1 = self._d
        if isinstance(other, Fraction):
            num2 = other.numerator()
            den2 = other.denominator()
            if den1 == den2:
                new_n = num1 + num2
            else:
                new_d = Fraction._lcm(den1, den2)
                new_n = num1 * (new_d // den1) + num2 * (new_d // den2)
        elif isinstance(other, int):
            if other == 0:
                return self
            else:
                new_n = num1 + other * den1
        if new_n == 0:
            return 0
        else:
            return Fraction(new_n, new_d).simplify()

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        new_n = self._n
        new_d = self._d
        if isinstance(other, Fraction):
            new_n = self._n * other.numerator()
            new_d = self._d * other.denominator()
        elif isinstance(other, int):
            if other == 1:
                return self
            else:
                new_n = self._n * other
        elif isinstance(other, float):
            return self.__mul__(Fraction.convert_float(other))
        return Fraction(new_n, new_d).simplify()

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if isinstance(other, Fraction):
            return self.__mul__(other.reciprocal())
        elif isinstance(other, int):
            return self.__mul__(Fraction(1, other))
        elif isinstance(other, float):
            return self.__mul__(Fraction.convert_float(other).reciprocal())

    def __rdiv__(self, other):
        return (self.reciprocal()).__mul__(other)

    def __floordiv__(self, other):
        return self.__div__(other)

    def __rfloordiv__(self, other):
        return self.__rdiv__(other)

    def __pow__(self, exp):
        if isinstance(exp, int):
            if exp == 0:
                return 1
            elif exp == 1:
                return self
            else:
                new_n = self._n ** exp
                new_d = self._d ** exp
                return Fraction(new_n, new_d)
        elif isinstance(exp, Fraction):
            return self.decimal() ** exp.decimal()
        else:
            return self.decimal() ** exp

    def __sub__(self, other):
        return self.__add__(other.__neg__())

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __neg__(self):
        return self.__mul__(-1)

    def __repr__(self):
        return "({}/{})".format(self._n, self._d)

    def numerator(self):
        """(Fraction) -> int

        Returns the numerator of this fraction.
        """
        return self._n

    def denominator(self):
        """(Fraction) -> int

        Returns the denominator of this fraction.
        """
        return self._d

    def decimal(self):
        """(Fraction) -> float

        Returns the float representation of this fraction.
        """
        simp_self = self.simplify()
        return simp_self.numerator() / simp_self.denominator()

    def reciprocal(self):
        """(Fraction) -> Fraction

        Returns the reciprocal of this fraction.
        """
        return Fraction(self._d, self._n)

    def simplify(self):
        """(Fraction) -> Fraction or int

        Simplifies this fraction to its most basic terms.
        """
        old_n = self.numerator()
        old_d = self.denominator()
        # if both numerator and denominator are fractions
        if isinstance(old_n, Fraction) and isinstance(old_d, Fraction):
            return (old_n * old_d.reciprocal()).simplify()
        # if only the numerator is a fraction
        elif isinstance(old_n, Fraction):
            new_n = old_n.numerator()
            new_d = old_n.denominator() * self._d
            return Fraction(new_n, new_d).simplify()
        # if only the denominator is a fraction
        elif isinstance(old_d, Fraction):
            multiplier = old_d.reciprocal()
            new_n = multiplier.numerator() * self._n
            new_d = multiplier.denominator()
            return Fraction(new_n, new_d).simplify()
        # otherwise, both numerator and denominators are integers
        else:
            # if denominator divides numerator, return int
            if old_n % old_d == 0:
                return old_n // old_d
            # if numerator divides denominator
            elif old_d % old_n == 0:
                return Fraction(1, old_d // old_n)
            # otherwise use GCD to simplify fraction
            else:
                gcd = Fraction._gcd(old_n, old_d)
                if gcd != 1:
                    return Fraction(old_n // gcd, old_d // gcd)
                else:
                    return self

    def is_improper(self):
        """(Fraction) -> bool

        Returns True iff this fraction is improper.
        """
        return self._n >= self._d

    def set_denominator(self, denominator):
        """(Fraction, int or Fraction):

        Fixes the denominator of this fraction to a specific value.

        REQ: denominator != 0
        """
        new_n = self._n * Fraction(denominator, self._d)
        return Fraction(new_n, denominator)


def examples():
    """() -> NoneType

    Displays examples of fraction operations.
    """
    frac_a = Fraction(2, 4)
    frac_b = Fraction(5, 7)
    frac_b_recip = frac_b.reciprocal()
    int_c = int(3)

    # single fraction operations
    print("\n> Unary fraction operations")
    print("-" * 40)
    print("\nFraction a:")
    print(frac_a)
    print("\nNegation -a:")
    print((-frac_a).set_denominator(4))
    print("\nDecimal value:")
    print(frac_a.decimal())
    print("\nReciprocal:")
    print(frac_a.reciprocal())
    print("\nSimplest terms:")
    print(frac_a.simplify())
    print("\nSet denominator = 7:")
    print(frac_a.set_denominator(7))

    # binary fraction operations
    print("\n> Binary fraction operations")
    print("-" * 40)
    print("\nFraction a:")
    print(frac_a)
    print("\nFraction b:")
    print(frac_b)
    print("\nFraction addition a + b:")
    print(frac_a, "+", frac_b, "=", frac_a + frac_b)
    print("\nFraction subtraction a - b:")
    print(frac_a, "-", frac_b, "=", frac_a - frac_b)
    print("\nFraction subtraction b - a:")
    print(frac_b, "-", frac_a, "=", frac_b - frac_a)
    print("\nFraction multiplication a * b:")
    print(frac_a, "x", frac_b, "=", frac_a * frac_b)
    print("\nFraction division a / b:")
    print(frac_a, "/", frac_b, "=", frac_a // frac_b)
    print("\nFraction division b / a:")
    print(frac_b, "/", frac_a, "=", frac_b // frac_a)

    # fraction-integer operations
    print("\n> Fraction-integer operations")
    print("-" * 40)
    print("\nFraction b:")
    print(frac_b)
    print("\nInteger c:")
    print(int_c)
    print("\nAddition b + c:")
    print(frac_b, "+", int_c, "=", frac_b + int_c)
    print("\nSubtraction b - c:")
    print(frac_b, "-", int_c, "=", frac_b - int_c)
    print("\nSubtraction c - b:")
    print(int_c, "-", frac_b, "=", int_c - frac_b)
    print("\nMultiplication b * c:")
    print(frac_b, "*", int_c, "=", frac_b * int_c)
    print("\nDivision b / c:")
    print(frac_b, "/", int_c, "=", frac_b // int_c)
    print("\nDivision c / b:")
    print(int_c, "/", frac_b, "=", int_c // frac_b)

    print(
        # end of examples
    )


if __name__ == '__main__':
    examples()
