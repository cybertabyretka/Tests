import unittest
from Fibonacci import fibonacci


class FibonacciTester(unittest.TestCase):
    def test1(self):
        self.assertEqual(fibonacci(2), 1)

    def test2(self):
        self.assertEqual(fibonacci(10), 55)

    def test3(self):
        self.assertEqual(fibonacci(18), 2584)

    def test4(self):
        self.assertEqual(fibonacci(22), 17711)


if __name__ == '__main__':
    unittest.main()