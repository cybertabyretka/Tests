from Stack import Stack


STACK = Stack()


def stack_tests():
    STACK.push(1)
    STACK.push(5)
    assert STACK.size() == 2
    assert STACK.peek() == 5
    STACK.push(13)
    assert STACK.pop() == 13
    assert STACK.size() == 2
    assert STACK.peek() == 5
    print('ALL TESTS PASSED')


if __name__ == '__main__':
    stack_tests()