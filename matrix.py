"""This module contains a nested list implementation of a matrix.

Author: Jeffrey Li
Created: January 7, 2017
Modified: November 12, 2017
Software Engineering
University of Toronto
"""

from fraction import Fraction
from vector import Vector


class MatrixDimensionError(Exception):
    """An exception for invalid matrix dimensions."""


class SingularMatrixError(Exception):
    """An exception for invalid singular matrix operations."""


class Matrix(object):
    """A class to represent a matrix."""

    @staticmethod
    def _pivot_position(vector):
        for pos in range(vector.dimension(), 0, -1):
            if vector.get(pos) != 0:
                return pos
        return vector.dimension()

    @staticmethod
    def zero(rows, columns=None):
        """(int[, int]) -> Matrix

        Returns a zero matrix with the given dimensions.
        """
        if not columns:
            columns = rows
        zero_m = list()
        for i in range(rows):
            zero_m.append([0] * columns)
        return Matrix(*zero_m)

    @staticmethod
    def identity(rows):
        """(int) -> Matrix

        Returns an identity matrix with the given dimensions.
        """
        identity_m = list()
        for i in range(rows):
            identity_m.append([0]*i + [1] + [0]*(rows-i-1))
        return Matrix(*identity_m)

    def __init__(self, *rows):
        """(Matrix, tuple of iterable) -> NoneType

        Creates a matrix with the given elements in the iterables.
        """
        self._rows = len(rows)
        self._cols = len(rows[0])
        self._m = list()
        for row in rows:
            self._m.append(list(row))

    def __hash__(self):
        row_vector_hashes = list()
        for row_vector in self:
            row_vector_hashes.append(hash(row_vector))
        return hash(tuple(row_vector_hashes))

    def __repr__(self):
        str_m = str(self._m)[1:-1]
        return "M({})".format(str_m)

    def __str__(self):
        str_m = list()
        for row in self._m:
            str_row = list(map(str, row))
            str_m.append(" ".join(str_row))
        return "\n".join(str_m)

    def __iter__(self):
        row_vectors_list = list()
        for row in self._m:
            row_vectors_list.append(Vector(*row))
        return iter(row_vectors_list)

    def __abs__(self):
        return self.determinant()

    def __add__(self, other):
        """(Matrix, Matrix) -> Matrix

        Returns the sum of the two matrices.

        REQ: self.dimensions == other.dimensions
        """
        if not self.same_dimensions(other):
            err_msg = "matrices must have the same dimensions"
            raise MatrixDimensionError(err_msg)
        sum_m = list()
        for row_pos in range(self._rows):
            row1 = self.row_vector(row_pos+1)
            row2 = other.row_vector(row_pos+1)
            sum_m.append(row1 + row2)
        return Matrix(*sum_m)

    def __mul__(self, other):
        """(Matrix, Matrix or Scalar) -> Matrix or Vector

        Returns a product of this matrix with another value.
        If other is a...
          Matrix: returns matrix, result of matrix multiplication.
          Vector: returns vector, result of matrix-vector multiplication.
          Scalar (int, float): returns matrix, result of scalar multiplication.

        REQ: if other is matrix, self.rows == other.columns
        REQ: if other is vector, self.rows == other.dimension
        """
        prod_m = list()
        # matrix multiplication
        if isinstance(other, Matrix):
            if not self._rows == other.columns():
                err_msg = "matrices must have opposite dimensions"
                raise MatrixDimensionError(err_msg)
            row_vectors_a = [Vector(*row) for row in self._m]
            col_vectors_b = [other.column_vector(
                i+1) for i in range(other.columns())]
            for row_vector in row_vectors_a:
                prod_row = list()
                for col_vector in col_vectors_b:
                    prod_row.append(row_vector * col_vector)
                prod_m.append(prod_row)
        # matrix-vector multiplication
        elif isinstance(other, Vector):
            prod_v = prod_m
            for row_vector in self:
                prod_v.append(row_vector * other)
            return Vector(*prod_v)
        # scalar multiplication
        else:
            for row in self._m:
                row_vector = Vector(*row)
                prod_m.append(row_vector * other)
        return Matrix(*prod_m)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        return self.__add__(other.__neg__())

    def __pow__(self, power):
        prod_m = self
        for i in range(power):
            prod_m = prod_m.__mul__(self)
        return prod_m

    def __neg__(self):
        return self.__mul__(-1)

    def __eq__(self, other):
        if isinstance(other, Matrix):
            if self.same_dimensions(other):
                for i in range(self._rows):
                    if self.row_vector(i+1) != other.row_vector(i+1):
                        return False
                return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    # <!-- basic operations -->

    def rows(self):
        """(Matrix) -> int

        Returns the number of rows in this matrix.
        """
        return self._rows

    def columns(self):
        """(Matrix) -> int

        Returns the number of columns in this matrix.
        """
        return self._cols

    def dimensions(self):
        """(Matrix) -> int, int

        Returns the dimensions of this matrix.
        """
        return self._rows, self._cols

    def same_dimensions(self, other):
        """(Matrix, Matrix) -> bool

        Returns True iff both matrices have the same dimension.
        This is to check if this matrix is suitable for matrix addition with
        the other given matrix.
        """
        return self._rows == other.rows() and self._cols == other.columns()

    def opposite_dimensions(self, other):
        """(Matrix, Matrix) -> bool

        Returns True iff both matrices have opposite dimensions.
        This is to check if this matrix is suitable for matrix multiplication
        with the other given matrix.
        """
        return self._rows == other.columns() and self._cols == other.rows()

    def get(self, row_pos, col_pos, by_index=False):
        """(Matrix, int, int[, bool]) -> Number

        Returns the number at the given row and column position in this matrix.

        REQ: 1 <= row_pos <= self.rows()
        REQ: 1 <= col_pos <= self.columns()
        """
        if by_index:
            return self._m[row_pos][col_pos]
        else:
            return self._m[row_pos-1][col_pos-1]

    def row_vector(self, position):
        """(Matrix, int) -> Vector

        Returns the row vector at the given row position.

        REQ: 1 <= position <= self.rows()
        """
        return Vector(*self._m[position-1])

    def column_vector(self, position):
        """(Matrix, int) -> Vector

        Returns the column vector at the given column position.

        REQ: 1 <= position <= self.columns()
        """
        col_values = list()
        for row in self._m:
            col_values.append(row[position-1])
        return Vector(*col_values)

    def transpose(self):
        """(Matrix) -> Matrix

        Returns the transpose of this matrix.
        """
        col_vectors = list()
        for cindex in range(self._cols):
            col_vectors.append(self.column_vector(cindex+1))
        return Matrix(*col_vectors)

    # <!-- matrix modifiers -->

    def add_row(self, row, pos=None):
        """(Matrix, list or Vector[, int]) -> Matrix

        Returns the modified matrix that is the given row added to this matrix
        at the row position (if given).

        REQ: len(row) == self.cols()
        REQ: 1 <= pos <= self.rows()
        """
        if len(row) != self._cols:
            raise MatrixDimensionError("incorrect number of values for row")
        new_m = self._m.copy()
        if pos:
            new_m.insert(pos-1, row)
        else:
            new_m.append(row)
        return Matrix(*new_m)

    def add_column(self, col, pos=None):
        """(Matrix, list or Vector[, int]) -> Matrix

        Returns the modified matrix that is the given column added to this
        matrix at the column position (if given).

        REQ: len(col) == self.rows()
        REQ: 1 <= pos <= self.columns()
        """
        if len(col) != self._rows:
            raise MatrixDimensionError("incorrect number of values for column")
        new_m = [row.copy() for row in self._m]
        if pos:
            for i, value in enumerate(col):
                new_m[i] = new_m[i][:pos-1] + [value] + new_m[i][pos-1:]
        else:
            for i, value in enumerate(col):
                new_m[i] += [value]
        return Matrix(*new_m)

    def remove_row(self, pos):
        """(Matrix, list or Vector[, int]) -> Matrix

        Returns the modified matrix that is the row at the given row position
        removed from this matrix.

        REQ: 1 <= pos <= self.rows()
        """
        new_m = self._m.copy()
        new_m.pop(pos-1)
        return Matrix(*new_m)

    def remove_column(self, pos):
        """(Matrix, list or Vector[, int]) -> Matrix

        Returns the modified matrix that is the column at the given column
        position removed from this matrix.

        REQ: 1 <= pos <= self.columns()
        """
        new_m = [row.copy() for row in self._m]
        for i in range(self._rows):
            new_m[i] = new_m[i][:pos-1] + new_m[i][pos:]
        return Matrix(*new_m)

    # <!-- elementary row operations -->

    def row_interchange(self, pos1, pos2):
        """(Matrix, int, int) -> Matrix

        Returns the matrix with the given row interchange operation.

        REQ: 1 <= pos1, pos2 <= self.rows()
        """
        if pos1 == pos2:
            return self
        row_vectors = [row for row in self._m]
        temp = row_vectors[pos1-1]
        row_vectors[pos1-1] = row_vectors[pos2-1]
        row_vectors[pos2-1] = temp
        return Matrix(*row_vectors)

    def row_multiply(self, pos, mult):
        """(Matrix, int, Number) -> Matrix

        Returns the matrix with the given row multiplication operation.

        REQ: 1 <= pos <= self.rows()
        """
        if mult == 1:
            return self
        row_vectors = [Vector(*row) for row in self._m]
        row_vectors[pos-1] *= mult
        return Matrix(*row_vectors)

    def row_add_multiple(self, pos1, pos2, mult2):
        """(Matrix, int, int, Number) -> Matrix

        Returns the matrix with the given row multiple addition operation.

        REQ: 1 <= pos1, pos2 <= self.rows()
        """
        row_vectors = [Vector(*row) for row in self._m]
        row_vectors[pos1-1] += row_vectors[pos2-1] * mult2
        return Matrix(*row_vectors)

    # <!-- row echelon form operations -->

    def _rref(self, all_steps=False):
        steps = [self]
        result = self
        lead = 0
        for r in range(self._rows):
            if lead >= self._cols:
                return steps if all_steps else result
            i = r
            while result.get(i, lead, by_index=True) == 0:
                i += 1
                if i == self._rows:
                    i = r
                    lead += 1
                    if self._cols == lead:
                        # return the matrix in RREF
                        return steps if all_steps else result
            result = result.row_interchange(i+1, r+1)
            steps.append(result)
            lv = result.get(r, lead, by_index=True)
            result = result.row_multiply(r+1, Fraction(1, lv))
            steps.append(result)
            for i in range(self._rows):
                if i != r:
                    lv = result.get(i, lead, by_index=True)
                    result = result.row_add_multiple(i+1, r+1, -1*lv)
                    steps.append(result)
            lead += 1
        return result

    def reduced_row_echelon_form(self):
        """(Matrix) -> Matrix

        Returns the matrix in reduced row echelon form that is row equivalent
        to this matrix.

        Credits: https://rosettacode.org/wiki/Reduced_row_echelon_form
        """
        return self._rref(all_steps=False)

    def rref_all_steps(self):
        """(Matrix) -> list of Matrix

        Returns all the steps (row equivalent matrices) in reducing this matrix
        to reduced row echelon form.

        Credits: https://rosettacode.org/wiki/Reduced_row_echelon_form
        """
        rref_all_steps = self._rref(all_steps=True)
        rref_main_steps = [self]
        prev_step = self
        for step in rref_all_steps:
            if step != prev_step:
                rref_main_steps.append(step)
            prev_step = step
        return rref_main_steps

    def rank(self):
        """(Matrix) -> int

        Returns the rank of this matrix.
        The rank is calculated via the rank equation:
            rank(A) = columns(A) - nullity(A)
        """
        return self._cols - self.nullity()

    def nullity(self):
        """(Matrix) -> int

        Returns the nullity of this matrix.
        The nullity is calculated via the rank equation:
            nullity(A) = columns(A) - rank(A)
        """
        nullity = 0
        rref = self.reduced_row_echelon_form()
        for row_vector in rref:
            if row_vector.is_zero():
                nullity += 1
        return nullity

    # <!-- determinant operations -->

    def determinant(self):
        """(Matrix) -> Number

        Returns the determinant of this matrix.

        REQ: matrix must be a square
        """
        if not self.is_square():
            raise MatrixDimensionError("matrix must be a square matrix")
        det = 0
        if self._rows == 1:
            det = self.get(1, 1)
        elif self._rows == 2:
            det = self.get(1, 1)*self.get(2, 2) - self.get(1, 2)*self.get(2, 1)
        else:
            for cindex in range(self._cols):
                det += self.get(1, cindex+1) * self.cofactor(1, cindex+1)
        return det

    def minor(self, row_pos, col_pos):
        """(Matrix) -> Number

        Returns the minor at the given positions of this matrix.

        REQ: 1 <= row_pos <= self.rows()
        REQ: 1 <= col_pos <= self.columns()
        """
        return self.remove_row(row_pos).remove_column(col_pos).determinant()

    def cofactor(self, row_pos, col_pos):
        """(Matrix) -> Number

        Returns the cofactor at the given positions of this matrix.

        REQ: 1 <= row_pos <= self.rows()
        REQ: 1 <= col_pos <= self.columns()
        """
        return (-1)**(row_pos+col_pos) * self.minor(row_pos, col_pos)

    def adjugate(self):
        """(Matrix) -> Matrix

        Returns the adjugate of this matrix, where:
            adj(A) = cofactor(A)^T

        REQ: matrix must be a square
        """
        cofactor_mtx = list()
        for i in range(self._rows):
            cofactor_row = list()
            for j in range(self._cols):
                cofactor_row.append(self.cofactor(i+1, j+1))
            cofactor_mtx.append(cofactor_row)
        return Matrix(*cofactor_mtx).transpose()

    def inverse(self):
        """(Matrix) -> bool

        Returns the inverse of this matrix.

        REQ: matrix must be a square and not singular
        """
        det = self.determinant()
        if det == 0:
            raise SingularMatrixError("matrix is not invertible")
        return self.adjugate() * Fraction(1, det)

    # <!-- boolean operations -->

    def is_square(self):
        """(Matrix) -> bool

        Returns True iff this matrix is a square matrix.
        This is used to check if the determinant can be calculated.
        """
        return self._rows == self._cols

    def is_symmetric(self):
        """(Matrix) -> bool

        Returns True iff this matrix is symmetric, i.e.
            A == A^T
        """
        if self.is_square():
            return self == self.transpose()
        return False

    def is_singular(self):
        """(Matrix) -> bool

        Returns True iff this matrix is singular (not invertible).
        """
        if not self.is_square():
            raise MatrixDimensionError("matrix must be a square matrix")
        return self.determinant() == 0

    # <!-- complex operations -->

    def solve_for_x(self, vector_b):
        """(Matrix, Vector) -> Vector

        Returns the vector x given the vector b, such that the following
        equation is satisfied:
            Ax = b

        REQ: len(vector_b) == self.rows()
        """
        if self._rows != vector_b.dimension():
            err_msg = "vector must have same dimensions as this matrix's rows"
            raise MatrixDimensionError(err_msg)
        augmented = self.add_column(vector_b)
        rref = augmented.reduced_row_echelon_form()
        return rref.column_vector(self._cols + 1)

    def row_space(self):
        """(Matrix) -> set of Vector

        Returns the basis of the row space of this matrix.
        """
        rref = self.reduced_row_echelon_form()
        row_space = {self.row_vector(
            i+1) for i, row_v in enumerate(rref) if not row_v.is_zero()}
        return row_space

    def column_space(self):
        """(Matrix) -> set of Vector

        Returns the basis of the column space of this matrix.
        """
        col_space = set()
        rref = self.reduced_row_echelon_form()
        column_vectors = [rref.column_vector(i+1) for i in range(self._cols)]
        prev_pivot_pos = -1
        for col_vector in column_vectors:
            pivot_pos = Matrix._pivot_position(col_vector)
            if pivot_pos != prev_pivot_pos:
                col_space.add(col_vector)
            prev_pivot_pos = pivot_pos
        return col_space


def examples():
    """() -> NoneType

    Displays examples of matrix operations.
    """
    mtx_a = Matrix([1, 1, 1], [0, 2, 5], [2, 5, -1])
    mtx_a_inverse = mtx_a.inverse()
    vtr_b = Vector(6, -4, 27)
    vtr_x = mtx_a.solve_for_x(vtr_b)

    print("\nMatrix A:")
    print(mtx_a)

    # single matrix operations
    print("\n> Single matrix operations")
    print("-" * 40)
    print("\nMatrix transpose A^T:")
    print(mtx_a.transpose())
    print("\nMatrix inverse A^(-1):")
    print(mtx_a_inverse)
    print("\nMatrix multiplication A^(-1)*A = I")
    print(mtx_a_inverse * mtx_a)
    print("\nReduced row echelon form H ~ A:")
    print(mtx_a.reduced_row_echelon_form())

    # solving for vector x
    print("\n> Ax = b, solving for x")
    print("-" * 40)
    print("\nVector b:")
    print(vtr_b)
    print("\nResult vector x:")
    print(vtr_x)

    print(
        # end of example
    )


if __name__ == "__main__":
    examples()
