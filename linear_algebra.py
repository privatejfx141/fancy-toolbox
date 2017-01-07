from math import sqrt, acos, degrees


class Vector(object):
    '''A class to represent a vector in Euclidean n-space.'''

    def __init__(self, *elements):
        '''(Vector, tuple of int/float) -> NoneType

        Create a vector in Euclidean n-space.
        '''
        self._vector = elements

    def __len__(self):
        '''(Vector) -> int

        See cardinality().
        '''
        return self.cardinality()

    def __add__(self, other):
        '''(Vector, Vector) -> Vector

        Return the sum of the two vectors.
        '''
        # Get the pointer to the shortest vector.
        if self._tuplelen() < other._tuplelen():
            short, long = self, other
        else:
            short, long = other, self
        # Loop and add both vector entries.
        new_entries = list()
        for i in range(long._tuplelen()):
            si, li = 0, long._vector[i]
            # If counter is still in range of short vector,
            # get the short vector's entries.
            if i < short._tuplelen():
                si = short._vector[i]
            new_entries.append(si + li)
        # Return the vector sum.
        return Vector(*new_entries)

    def __sub__(self, other):
        '''(Vector, Vector) -> Vector

        Return the difference of the two vectors.
        '''
        return self + (-1 * other)

    def __mul__(self, other):
        '''(Vector, Vector or int/float) -> Vector or float

        In the following cases:
        - If other is a vector, return the dot product.
        - If other is a scalar, return the scaled vector.
        '''
        # If other is numeric, return scaled vector.
        if type(other) in (int, float):
            scalar = other
            scaled_entries = (scalar * entry for entry in self._vector)
            return Vector(*scaled_entries)
        # If other is vector, return dot product.
        if type(other) is Vector:
            return self.dot_product(other)

    def __rmul__(self, other):
        '''(Vector, int/float) -> Vector

        Return the reverse product. See __mul__().
        '''
        return self * other

    def __pow__(self, other):
        '''(Vector, Vector) -> Vector

        Return the cross product. See cross_product().
        '''
        return self.cross_product(other)

    def __floordiv__(self, other):
        '''(Vector, Vector) -> bool

        See parallel().
        '''
        return self.parallel(other)

    def __repr__(self):
        '''(Vector) -> str

        Return the official string list representation of this vector.
        '''
        return str(self)

    def __str__(self):
        '''(Vector) -> str

        Return the informal string list representation of this vector.
        '''
        return str(list(self._vector))

    def _set_tuple(self, vector):
        '''(Vector, tuple of int/float) -> NoneType

        Set the tuple representation of this vector.
        '''
        self._vector = vector

    def _get_tuple(self):
        '''(Vector) -> tuple

        Return the tuple representation of this vector.
        '''
        return self._vector

    def _tuplelen(self):
        '''(Vector) -> int

        Return the length of the tuple representation of this vector.
        '''
        return len(self._vector)

    def norm(self):
        '''(Vector) -> float

        Return the norm, or magnitude, of this vector.
        '''
        squared = (entry**2 for entry in self._vector)
        return sqrt(sum(squared))

    def dot_product(self, other):
        '''(Vector, Vector) -> float

        Return the dot product of the two vectors.
        '''
        # Get the pointer to the shortest and longest vectors.
        if self._tuplelen() < other._tuplelen():
            short, long = self, other
        else:
            short, long = other, self
        # Loop and add both vector entries.
        dot_prod = 0
        for i in range(long._tuplelen()):
            si, li = 0, long._vector[i]
            # If counter is still in range of short vector,
            # get the short vector's entries.
            if i < short._tuplelen():
                si = short._vector[i]
            dot_prod += si * li
        # Return the vector sum.
        return dot_prod

    def angle(self, other):
        '''(Vector, Vector) -> float

        Return the angle between the two vectors in degrees.
        '''
        costheta = (self * other) / (self.norm() * other.norm())
        theta = acos(costheta)
        return degrees(theta)

    def cross_product(self, other):
        '''(Vector, Vector) -> Vector

        Return the cross product of the two vectors.
        '''
        return NotImplemented

    def cardinality(self):
        '''(Vector) -> int

        Return the cardinality of this vector; the number of non-zero
        elements in the vector.
        '''
        return self._tuplelen() - self._vector.count(0)

    def parallel(self, other):
        '''(Vector, Vector) -> bool

        Return True if both vectors are parallel.
        '''
        return NotImplemented

    def unit_vector(self):
        '''(Vector) -> Vector

        Return the normalized vector; maintains direction but norm is 1.
        '''
        norm = self.norm()
        normalized = self * (1 / norm)
        return normalized


if __name__ == '__main__':
    v1 = Vector(1, 2, 2, 4, 6)
    v2 = Vector(3, 4, 0, 1)
    
    u = Vector(-1, 3, 4)
    v = Vector(2, 1, -1)
    w = Vector(-2, -1, 3)
