"""This module contains a nested list implementation of a matrix.

Author: Jeffrey Li
Created: January 7, 2017
Modified: November 12, 2017
Software Engineering
University of Toronto
"""

from vector import Vector

class Matrix(object):
    """A class to represent a matrix."""

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
        self._rows = len(rows)
        self._cols = len(rows[0])
        self._m = list()
        for row in rows:
            self._m.append(list(row))

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
        if not self.same_dimensions(other):
            raise ValueError("matrices must have the same dimensions")
        sum_m = list()
        for row_pos in range(self._rows):
            row1 = self.row_vector(row_pos+1)
            row2 = other.row_vector(row_pos+1)
            sum_m.append(row1 + row2)
        return Matrix(*sum_m)

    def __mul__(self, other):
        prod_m = list()
        # matrix multiplication
        if isinstance(other, Matrix):
            if not self.opposite_dimensions(other):
                raise ValueError("matrices must have opposite dimensions")
            row_vectors_a = [Vector(*row) for row in self._m]
            col_vectors_b = [other.column_vector(i+1) for i in range(self._rows)]
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

    def __sub__(self, other):
        return self.__add__(other.__mul__(-1))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, power):
        prod_m = self
        for i in range(power):
            prod_m = prod_m.__mul__(self)
        return prod_m

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
        This is to check if both matrices are suitable for matrix addition.
        """
        return self._rows == other.rows() and self._cols == other.columns()

    def opposite_dimensions(self, other):
        """(Matrix, Matrix) -> bool

        Returns True iff both matrices have opposite dimensions.
        This is to check if both matrices are suitable for matrix multiplication.
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

        Returns the modified matrix that is the given row added to this matrix.

        REQ: len(row) == self.cols()
        REQ: 1 <= pos <= self.rows()
        """
        if len(row) != self._cols:
            raise ValueError("incorrect number of values for row")
        new_m = self._m.copy()
        if pos:
            new_m.insert(pos-1, row)
        else:
            new_m.append(row)
        return Matrix(*new_m)

    def add_column(self, col, pos=None):
        """(Matrix, list or Vector[, int]) -> Matrix

        Returns the modified matrix that is the given column added to this matrix.

        REQ: len(col) == self.rows()
        REQ: 1 <= pos <= self.columns()
        """
        if len(col) != self._rows:
            raise ValueError("incorrect number of values for column")
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

        Returns the modified matrix that is the row removed from this matrix.

        REQ: 1 <= pos <= self.rows()
        """
        new_m = self._m.copy()
        new_m.pop(pos-1)
        return Matrix(*new_m)

    def remove_column(self, pos):
        """(Matrix, list or Vector[, int]) -> Matrix

        Returns the modified matrix that is the column removed from this matrix.

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
        row_vectors = [Vector(*row) for row in self._m]
        row_vectors[pos-1] = row_vectors[pos-1] * mult
        return Matrix(*row_vectors)

    def row_add_multiple(self, pos1, pos2, mult2):
        """(Matrix, int, int, Number) -> Matrix

        Returns the matrix with the given row multiple addition operation.

        REQ: 1 <= pos1, pos2 <= self.rows()
        """
        row_vectors = [Vector(*row) for row in self._m]
        adder = row_vectors[pos2-1] * mult2
        row_vectors[pos1-1] = row_vectors[pos1-1] + adder
        return Matrix(*row_vectors)

    # <!-- row echelon form operations -->

    def reduced_row_echelon_form(self):
        """(Matrix) -> Matrix

        Returns the reduced row echelon form that is row equivalent
        to this matrix.

        Credits: https://rosettacode.org/wiki/Reduced_row_echelon_form
        """
        result = self
        lead = 0
        for r in range(self._rows):
            if lead >= self._cols:
                return result
            i = r
            while result.get(i, lead, True) == 0:
                i += 1
                if i == self._rows:
                    i = r
                    lead += 1
                    if self._cols == lead:
                        # return the matrix in RREF
                        return result
            result = result.row_interchange(i+1, r+1)
            lv = result.get(r, lead, True)
            result = result.row_multiply(r+1, 1/float(lv))
            for i in range(self._rows):
                if i != r:
                    lv = result.get(i, lead, True)
                    result = result.row_add_multiple(i+1, r+1, -lv)
            lead += 1
        return result

    def rank(self):
        """(Matrix) -> int

        Returns the rank of this matrix.
        """
        return self._cols - self.nullity()

    def nullity(self):
        """(Matrix) -> int

        Returns the nullity of this matrix.
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
        """
        if not self.is_square():
            raise ValueError("matrix must be a square matrix")
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
        """
        det = self.determinant()
        if det == 0:
            raise ValueError("matrix is not invertible")
        return self.adjugate() * (1/det)

    # <!-- boolean operations -->

    def is_square(self):
        """(Matrix) -> bool

        Returns True iff this matrix is a square matrix.
        This is used to check if the determinant can be calculated.
        """
        return self._rows == self._cols

    def is_singular(self):
        """(Matrix) -> bool

        Returns True iff this matrix is singular (not invertible).
        """
        if not self.is_square():
            raise ValueError("matrix must be a square matrix")
        return self.determinant() == 0

    # <!-- complex operations -->

    def solve_for_x(self, vector_b):
        """(Matrix, Vector) -> Vector

        Returns the vector x given the vector b, such that the equation is satisfied:
            Ax = b

        REQ: len(vector_b) == self.rows()
        """
        if self._rows != vector_b.dimension():
            raise ValueError("vector must have same dimensions as this matrix's rows")
        augmented = self.add_column(vector_b)
        rref = augmented.reduced_row_echelon_form()
        return rref.column_vector(self._cols+1)


if __name__ == "__main__":
    matrix_a = Matrix([1, 1, 1], [0, 2, 5], [2, 5, -1])
    vector_b = Vector(6, -4, 27)
    vector_x = matrix_a.solve_for_x(vector_b)
    inverse_a = matrix_a.inverse()

    print(inverse_a * vector_b)
    print(vector_x)
    print(Matrix([2, 6], [1, 3]).determinant())
