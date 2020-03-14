import unittest
from task3 import Vector


class Test(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1, 2, 3)
        self.v2 = Vector(2, 3, 4)
        self.v3 = Vector(3, 4)

    def test_addition(self):
        self.v1 += self.v2
        self.assertEqual(self.v1, Vector(3, 5, 7))
        self.assertEqual(self.v2 + Vector(1, 1, 1), Vector(3, 4, 5))

    def test_error(self):
        self.assertEqual(abs(self.v3), 6)

    def test_hard(self):
        self.v1 *= 0
        self.assertEqual(self.v1, Vector(0, 0, 0))
        self.v2 -= self.v1
        self.assertEqual(self.v2, Vector(2, 3, 4))
        self.assertEqual(Vector(1, 2) * Vector(3, 3), 9)
        self.v3 *= -1
        self.assertEqual(self.v3 - Vector(1, 1), Vector(-4, -5))
        self.assertEqual(abs(self.v1 * self.v2), 0)
        self.assertEqual(abs(self.v1 * 0), 0)
        self.assertFalse(self.v1 == self.v3)
        self.assertEqual(str(self.v3), '{-3, -4}')


if __name__ == '__main__':
    unittest.main()
