from Fibonacci import fibonacci


def test1():
    assert fibonacci(2) == 1


def test2():
    assert fibonacci(10) == 55


def test3():
    assert fibonacci(18), 2584


def test4():
    assert fibonacci(22), 17711


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
