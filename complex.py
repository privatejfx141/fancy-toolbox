"""This module contains a basic implementaton of a complex number class.

Author: Jeffrey Li
Created: January 7, 2017
Modified: November 12, 2017
Software Engineering
University of Toronto
"""

from math import atan2
from fraction import Fraction

class Complex(object):
    """A class to represent complex numbers."""

    def __init__(self, real, imaginary):
        """(Complex, int or Fraction, int or Fraction) -> NoneType

        Creates a complex number with a real component and an imaginary scalar.
        """
        self._a = real
        self._b = imaginary

    def __abs__(self):
        return self.modulus()

    def __add__(self, other):
        if isinstance(other, Complex):
            new_a = self._a + other.real()
            new_b = self._b + other.imaginary()
            return Complex(new_a, new_b)
        else:
            return Complex(self._a + other, self._b)

    def __sub__(self, other):
        return self.__add__(-other)

    def __mul__(self, other):
        if isinstance(other, Complex):
            a1, a2 = self._a, other.real()
            b1, b2 = self._b, other.imaginary()
            return Complex(a1*a2 - b1*b2, a1*b2 + a2*b1)
        else:
            return Complex(self._a * other, self._b * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if isinstance(other, Complex):
            a, b = self._a, self._b
            c, d = other.real(), other.imaginary()
            denom = c**2 + d**2
            real = Fraction(a*c+b*d, denom).simplify()
            imag = Fraction(b*c-a*d, denom).simplify()
            return Complex(real, imag)
        return self

    def __floordiv__(self, other):
        return self.__div__(other)

    def __pow__(self, power):
        if power == 0:
            return 1
        elif power == 1:
            return self
        else:
            return self * self.__pow__(power - 1)

    def __eq__(self, other):
        if isinstance(other, Complex):
            return self._a == other.real() and self._b == other.imaginary()
        else:
            return self._a == other

    def __repr__(self):
        if self._a == 0 and self._b == 0:
            return "0"
        elif self._b != 0:
            imag = str(self._b) + 'i'
            # if imaginary value is positive, need to add plus sign
            if self._b > 0:
                imag = "+" + imag
            if self._a != 0:
                return str(self._a) + imag
            else:
                return imag
        else:
            return str(self._a)

    def real(self):
        """(Complex) -> int

        Returns the real component of this complex number.
        """
        return self._a

    def imaginary(self):
        """(Complex) -> int

        Returns the imaginary scalar of this complex number.
        """
        return self._b

    def conjugate(self):
        """(Complex) -> Complex

        Returns the conjugate of this complex number.
        """
        return Complex(self._a, -self._b)

    def modulus(self):
        """(Complex) -> float

        Returns the modulus (magnitude) of this complex number.
        """
        return (self._a**2 + self._b**2)**(1/2)

    def argument(self):
        """(Complex) -> float

        Returns the argument (angle) of this complex number.
        """
        return atan2(self._b, self._a)


if __name__ == "__main__":
    z = Complex(5, 7)
    w = Complex(3, -1)
    a = Complex(2, 0)
    print(z.real(), z.modulus(), z.conjugate())
    print(z, "x", w, "=", z*w)
    print(z // w)
    print(a.modulus())
    print(z.argument())
