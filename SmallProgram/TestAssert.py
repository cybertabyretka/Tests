from Fibonacci import fibonacci


def fibonacci_test():
    assert fibonacci(2) == 1
    assert fibonacci(10) == 55
    assert fibonacci(18) == 2584
    assert fibonacci(22) == 17711
    print('ALL TEST PASSED')


if __name__ == '__main__':
    fibonacci_test()