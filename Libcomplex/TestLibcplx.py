import Libcplx
import unittest
import math

class TestComplexFunctions(unittest.TestCase):

    def test_cplxsum(self):
        self.assertEqual(Libcplx.sum((1, 2), (3, 4)), (4, 6))
        self.assertEqual(Libcplx.sum((-1, -1), (1, 1)), (0, 0))

    def test_cplxrest(self):
        self.assertEqual(Libcplx.rest((5, 3), (2, 1)), (3, 2))
        self.assertEqual(Libcplx.rest((0, 0), (1, 1)), (-1, -1))

    def test_cplxmul(self):
        self.assertEqual(Libcplx.mul((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(Libcplx.mul((0, 1), (0, 1)), (-1, 0))

    def test_cplxdiv(self):
        self.assertAlmostEqual(Libcplx.div((1, 2), (3, 4))[0], 0.44, places=2)
        self.assertAlmostEqual(Libcplx.div((1, 2), (3, 4))[1], 0.08, places=2)

    def test_cplxmconj(self):
        self.assertEqual(Libcplx.conj((1, 2)), (1, -2))
        self.assertEqual(Libcplx.conj((3, -4)), (3, 4))

    def test_cplxmod(self):
        self.assertEqual(Libcplx.mod((3, 4)), 5)
        self.assertEqual(Libcplx.mod((0, 0)), 0)

    def test_cart_polar(self):
        r, theta = Libcplx.cart_polar((1, 0))
        self.assertAlmostEqual(r, 1.0, places=6)
        self.assertAlmostEqual(theta, 0.0, places=6)

    def test_polar_cart(self):
        a, b = Libcplx.polar_cart((1, math.pi/2))
        self.assertAlmostEqual(a, 0.0, places=6)
        self.assertAlmostEqual(b, 1.0, places=6)

    def test_cplxphase(self):
        self.assertAlmostEqual(Libcplx.phase((1, 1)), math.pi/4, places=6)
        self.assertAlmostEqual(Libcplx.phase((-1, 0)), math.pi, places=6)

if __name__ == '__main__':
    unittest.main()
