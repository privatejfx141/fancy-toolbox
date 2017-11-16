"""This module contains a list of list implementation of a complex matrix.

Author: Jeffrey Li
Created: January 7, 2017
Modified: November 15, 2017
Software Engineering
University of Toronto
"""

from matrix import Matrix

class ComplexMatrix(Matrix):
    """A class to represent a complex matrix."""

    def __init__(self, *rows):
        """(Matrix, tuple of list of complex) -> NoneType

        Creates a matrix with complex elements.
        """
        Matrix.__init__(self, *rows)

    def conjugate(self):
        """(ComplexMatrix) -> ComplexMatrix

        Returns the conjugate of this matrix.
        """
        conj_mtx = list()
        for row in self._m:
            conj_row = list()
            for value in row:
                conj_row.append(value.conjugate())
            conj_mtx.append(conj_row)
        return ComplexMatrix(*conj_mtx)

    def hermitian_adjoint(self):
        """(ComplexMatrix) -> ComplexMatrix

        Returns the Hermitian adjoint A* of this matrix.
        """
        return self.conjugate().transpose()

    def is_unitary(self):
        """(ComplexMatrix) -> bool

        Returns True if this matrix is unitary, i.e.
            (U*)U = I <=> U^-1 = U
        """
        herm_adj = self.hermitian_adjoint()
        prod = self * herm_adj
        identity = ComplexMatrix.identity(prod.rows())
        return prod == identity

    def is_hermitian(self):
        """(ComplexMatrix) -> bool

        Returns True iff this matrix is Hermitian, i.e.
            A* = A
        """
        herm_adj = self.hermitian_adjoint()
        return self == herm_adj

    def is_normal(self):
        """(ComplexMatrix) -> bool

        Returns True iff this matrix is normal, i.e.
            A(A*) = (A*)A
        """
        if not self.is_square():
            raise ValueError("matrix must be a square matrix")
        herm_adj = self.hermitian_adjoint()
        return self*herm_adj == herm_adj*self


def examples():
    """() -> NoneType

    Displays examples of complex matrix operations.
    """
    mtx_a = ComplexMatrix(
        [complex(1, 1), complex(0, -1), 0],
        [2, complex(3, -2), complex(0, 1)]
    )

    print("\nMatrix A:")
    print(mtx_a)

    # single matrix operations
    print("\n> Single complex matrix operations")
    print("-" * 40)
    print("\nComplex conjugate:")
    print(mtx_a.conjugate())
    print("\nHermitian adjoint A*:")
    print(mtx_a.hermitian_adjoint())


if __name__ == "__main__":
    examples()
