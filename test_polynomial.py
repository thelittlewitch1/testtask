import unittest
import polynomial as p


class TestPolynomial(unittest.TestCase):
    def setUp(self):
        self.pol1 = p.Polinomial((1, -1, 3))
        self.pol2 = p.Polinomial((2, -1, 4, 3))
        self.pol3 = p.Polinomial((3, 2.5, 4, 0.5))

    def test_init(self):
        p0 = p.Polinomial(1)
        self.assertEqual(p0.coeffs, [1])
        p1 = p.Polinomial(self.pol1)
        self.assertEqual(p1.coeffs, self.pol1.coeffs)
        p2 = p.Polinomial((1,2,3))
        self.assertEqual(p2.coeffs, [1,2,3])
        p3 = p.Polinomial([1,2,3])
        self.assertEqual(p3.coeffs, [1,2,3])
        with self.assertRaises(ValueError):
            p5 = p.Polinomial('')
            p6 = p.Polinomial('ab')

    def test_eq(self):
        self.assertTrue(self.pol1 == p.Polinomial((1, -1, 3)))
        self.assertFalse(self.pol1 == self.pol2)

    def test_repr(self):
        self.assertEqual(repr(self.pol1), 'Polynomial([1, -1, 3])')

    def test_atr(self):
        self.assertEqual(self.pol1.coeffs, [1, -1, 3])
        self.pol1.coeffs = [1, -1, 4]
        self.assertEqual(self.pol1.coeffs, [1, -1, 4])
        with self.assertRaises(AttributeError):
            a = self.pol1.a

    def test_add_const(self):
        self.assertEqual(self.pol1 + 3, p.Polinomial((1, -1, 6)))
        self.assertEqual(3 + self.pol1, p.Polinomial((1, -1, 6)))
        self.assertEqual(self.pol1 + 5.5, p.Polinomial((1, -1, 8.5)))
        self.assertEqual(5.5 + self.pol1, p.Polinomial((1, -1, 8.5)))

    def test_add_polyn(self):
        self.assertEqual(self.pol1 + self.pol2, p.Polinomial((2, 0, 3, 6)))
        self.assertEqual(self.pol2 + self.pol3, p.Polinomial((5, 1.5, 8, 3.5)))

    def test_add_fail(self):
        with self.assertRaises(ValueError):
            p0 = self.pol1 + 'ab'
            p1 = self.pol1 + (1, 2)

    def test_str(self):
        self.assertEqual(str(self.pol1), 'x^2 - x + 3')
        self.assertEqual(str(self.pol3), '3x^3 + 2.5x^2 + 4x + 0.5')
        self.assertEqual(str(p.Polinomial((1,0,0))), 'x^2')

    def test_mul_const(self):
        self.assertEqual(self.pol1 * 2, p.Polinomial((2, -2, 6)))
        self.assertEqual(self.pol1 * 0.5, p.Polinomial((1 * 0.5, -1 * 0.5, 3 * 0.5)))
        self.assertEqual(self.pol3 * 2, p.Polinomial((6, 5.0, 8, 1.0)))
        self.assertEqual(self.pol3 * 0.5, p.Polinomial((1.5, 1.25, 2.0, 0.25)))
        self.assertEqual(2 * self.pol1, p.Polinomial((2, -2, 6)))
        self.assertEqual(0.5 * self.pol1, p.Polinomial((1 * 0.5, -1 * 0.5, 3 * 0.5)))
        self.assertEqual(2 * self.pol3, p.Polinomial((6, 5.0, 8, 1.0)))
        self.assertEqual(0.5 * self.pol3, p.Polinomial((1.5, 1.25, 2.0, 0.25)))

    def test_mul_polyn(self):
        self.assertEqual(self.pol1*self.pol2, p.Polinomial((2, -3, 11, -4, 9, 9)))
        self.assertEqual(self.pol1*self.pol1, p.Polinomial((1, -2, 7, -6, 9)))
        self.assertEqual(self.pol2*self.pol3, p.Polinomial((6, 2.0, 17.5, 16.0, 23.0, 14.0, 1.5)))

    def test_mul_fail(self):
        with self.assertRaises(ValueError):
            p0 = self.pol1 * 'ab'
            p1 = self.pol1 * (1, 2)

    def test_sub_const(self):
        self.assertEqual(self.pol1 - 3, p.Polinomial((1, -1, 0)))
        self.assertEqual(3 - self.pol1, p.Polinomial((-1, 1, 0)))
        self.assertEqual(self.pol1 - 5.5, p.Polinomial((1, -1, -2.5)))
        self.assertEqual(5.5 - self.pol1, p.Polinomial((-1, 1, 2.5)))

    def test_sub_polyn(self):
        self.assertEqual(self.pol1 - self.pol2, p.Polinomial((-2, 2, -5, 0)))
        self.assertEqual(self.pol2 - self.pol1, p.Polinomial((2, -2, 5, 0)))
        self.assertEqual(self.pol2 - self.pol3, p.Polinomial((-1, -3.5, 0, 2.5)))





if __name__ == '__main__':
    unittest.main()
