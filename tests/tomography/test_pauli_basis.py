import unittest
import qiskit.ignis.tomography.basis.paulibasis as paulibasis
import numpy

class TestPauliBasis(unittest.TestCase):
    X = numpy.array([[0,1],[1,0]])
    Y = numpy.array([[0, -1j], [1j, 0]])
    Z = numpy.array([[1, 0], [0, -1]])

    def assertMatricesAlmostEqual(self, lhs, rhs, places = None):
        self.assertEqual(lhs.shape, rhs.shape, "Marix shapes differ: {} vs {}".format(lhs, rhs))
        n, m = lhs.shape
        for x in range(n):
            for y in range(m):
                self.assertAlmostEqual(lhs[x,y], rhs[x,y], places = places, msg="Matrices {} and {} differ on ({}, {})".format(lhs, rhs, x, y))


    def test_measurement_matrices(self):
        X0 = paulibasis.pauli_measurement_matrix("X", 0)
        X1 = paulibasis.pauli_measurement_matrix("X", 1)
        result_X = X0 - X1
        self.assertMatricesAlmostEqual(self.X, result_X)

        Y0 = paulibasis.pauli_measurement_matrix("Y", 0)
        Y1 = paulibasis.pauli_measurement_matrix("Y", 1)
        result_Y = Y0 - Y1
        self.assertMatricesAlmostEqual(self.Y, result_Y)

        Z0 = paulibasis.pauli_measurement_matrix("Z", 0)
        Z1 = paulibasis.pauli_measurement_matrix("Z", 1)
        result_Z = Z0 - Z1
        self.assertMatricesAlmostEqual(self.Z, result_Z)

    def test_preparation_matrices(self):
        X0 = paulibasis.pauli_preparation_matrix("Xp")
        X1 = paulibasis.pauli_preparation_matrix("Xm")
        result_X = X0 - X1
        self.assertMatricesAlmostEqual(self.X, result_X)

        Y0 = paulibasis.pauli_preparation_matrix("Yp")
        Y1 = paulibasis.pauli_preparation_matrix("Ym")
        result_Y = Y0 - Y1
        self.assertMatricesAlmostEqual(self.Y, result_Y)

        Z0 = paulibasis.pauli_preparation_matrix("Zp")
        Z1 = paulibasis.pauli_preparation_matrix("Zm")
        result_Z = Z0 - Z1
        self.assertMatricesAlmostEqual(self.Z, result_Z)


if __name__ == '__main__':
    unittest.main()