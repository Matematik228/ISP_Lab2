import unittest
import task1
import numbers_gen


class Test(unittest.TestCase):
    def check(self):
        task1.external_sort()
        with open('sorted.txt', 'r') as inf:
            prev = None
            for line in inf.readlines():
                if prev is None:
                    prev = int(line)
                    continue
                now = int(line)
                self.assertTrue(prev <= now)
                prev = now

    def test_small_arr(self):
        numbers_gen.gen(1000, -1000, 1000)
        self.check()

    def test_big_arr(self):
        numbers_gen.gen(1000000, -1000000, 1000000)
        self.check()


if __name__ == '__main__':
    unittest.main()
