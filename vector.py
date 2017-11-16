"""This module contains a basic list implementation of a vector.

Author: Jeffrey Li
Created: January 7, 2017
Modified: November 12, 2017
Software Engineering
University of Toronto
"""

from math import acos, sqrt

class Vector(object):
    """A class to represent a vector in Euclidean n-space."""

    @staticmethod
    def zero(dimension):
        """(int) -> Vector

        Returns a zero vector in the given dimension.
        """
        values = [0] * dimension
        return Vector(*values)

    def __init__(self, *values):
        self._v = list(values)
        self._n = len(values)

    def __hash__(self):
        return hash(tuple(self._v))

    def __len__(self):
        return self._n

    def __iter__(self):
        return iter(self._v)

    def __repr__(self):
        return "V{}".format(str(self._v))

    def __abs__(self):
        return self.norm()

    def __add__(self, other):
        values = [self._v[i] + other.get(i+1) for i in range(self._n)]
        return Vector(*values)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.dot_product(other)
        else:
            values = [self._v[i] * other for i in range(self._n)]
            return Vector(*values)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        return self.__add__(other.__mul__(-1))

    def __pow__(self, other):
        return self.cross_product(other)

    def __eq__(self, other):
        if isinstance(other, Vector):
            if self.dimension() == other.dimension():
                for i in range(self._n):
                    if self._v[i] != other.get(i+1):
                        return False
                return True
        return False

    def get(self, position, by_index=False):
        """(Vector, int[, bool]) -> int

        Returns the value in this vector at the given position.

        REQ: if by_index:
                0 <= position <= self.dimension() - 1
             otherwise:
                1 <= position <= self.dimension()
        """
        if by_index:
            return self._v[position]
        else:
            return self._v[position-1]

    def dimension(self):
        """(Vector) -> int

        Returns the number of dimensions of this vector.
        """
        return self._n

    def cardinality(self):
        """(Vector) -> int

        Returns the number of non-zero elements in this vector.
        """
        return self._n - self._n.count(0)

    def norm(self):
        """(Vector) -> float

        Returns the norm or magnitude of this vector.
        """
        squared = 0
        for value in self._v:
            squared += value ** 2
        return sqrt(squared)

    def unit(self):
        """(Vector) -> Vector

        Returns the unit vector parallel to this vector.
        """
        unit_values = list()
        norm = self.norm()
        for value in self._v:
            unit_values.append(value / norm)
        return Vector(*unit_values)

    def dot_product(self, other):
        """(Vector, Vector) -> int

        Returns the dot product of the two vectors.

        REQ: self.dimension() == other.dimension()
        """
        if self._n != other.dimension():
            raise ValueError("dimensions of both vectors must be equal")
        result = 0
        for i in range(self._n):
            result += self._v[i] * other.get(i+1)
        return result

    def angle(self, other):
        """(Vector, Vector) -> float

        Returns the angle between the two vectors.

        REQ: self.dimension() == other.dimension()
        """
        dot_prod = self.dot_product(other)
        norm_prod = self.norm() * other.norm()
        return acos(dot_prod / norm_prod)

    def cross_product(self, other):
        """(Vector, Vector) -> Vector

        Returns the cross product of the two vectors.

        REQ: self.dimension() == other.dimension() == 3
        """
        a1, a2, a3 = self._v
        b1, b2, b3 = other.get(1), other.get(2), other.get(3)
        n1 = a2 * b3 - a3 * b2
        n2 = a3 * b1 - a1 * b3
        n3 = a1 * b2 - a2 * b1
        return Vector(n1, n2, n3)

    def is_zero(self):
        """(Vector) -> bool

        Returns True iff this vector is the zero vector.
        """
        for value in self._v:
            if value != 0:
                return False
        return True


def examples():
    """() -> NoneType

    Displays examples of vector operations.
    """
    vect_v = Vector(8, -5, 7)
    vect_u = Vector(12, 6, -19)

    print("\nEuclidean vector v:")
    print(vect_v)

    # single vector operations
    print("\n> Unary vector operations:")
    print("-" * 40)
    print("\nScalar multiplication v*2:")
    print(vect_v * 2)
    print("\nNorm |v|:")
    print(vect_v.norm())
    print("\nUnit vector v/|v|:")
    print(vect_v.unit())

    # binary vector operations
    print("\n> Binary vector operations:")
    print("-" * 40)
    print("\nEuclidean vector u:")
    print(vect_u)
    print("\nVector addition v+u:")
    print(vect_v + vect_u)
    print("\nDot product v*u:")
    print(vect_v * vect_u)
    print("\nAngle arccos((v*u)/(|v|*|u|)):")
    print(vect_v.angle(vect_u), "radians")
    print("\nCross product vxu:")
    print(vect_v.cross_product(vect_u))

if __name__ == "__main__":
    examples()
