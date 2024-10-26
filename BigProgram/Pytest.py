from Stack import Stack


STACK = Stack(*[i for i in range(10**6)])


def test_pop():
    assert STACK.pop() == 10**6 - 1
    assert STACK.size() == 10**6 - 1


def test_push():
    STACK.push(8)
    STACK.push(9)
    assert STACK.peek() == 9
    assert STACK.is_empty() is False


def test_clear():
    STACK.clear()
    assert STACK.is_empty() is True
