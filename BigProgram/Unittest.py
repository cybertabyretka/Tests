from Stack import Stack
import unittest


STACK = Stack(*[i for i in range(10**6)])


class StackTester(unittest.TestCase):
    def test_pop(self):
        self.assertEqual(STACK.pop(), 10**6 - 1)
        self.assertEqual(STACK.size(), 10**6 - 1)

    def test_push(self):
        STACK.push(8)
        STACK.push(9)
        self.assertEqual(STACK.peek(), 9)
        self.assertEqual(STACK.is_empty(), False)

    def test_clear(self):
        STACK.clear()
        self.assertEqual(STACK.is_empty(), True)


if __name__ == '__main__':
    unittest.main()
