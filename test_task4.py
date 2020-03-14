import unittest
import task4


class Test(unittest.TestCase):
    def test_small(self):
        self.assertEqual(task4.fib(5), 5)

    def test_big(self):
        self.assertEqual(task4.fib(100), 354224848179261915075)

    def test_error(self):
        self.assertEqual(task4.fib(-5), 0)


if __name__ == '__main__':
    unittest.main()
