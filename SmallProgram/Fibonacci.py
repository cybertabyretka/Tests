def fibonacci(n):
    """
    :param n: fibonacci number ordinal; n >= 0
    :return: fibonacci number
    >>> fibonacci(2)
    1
    >>> fibonacci(10)
    55
    >>> fibonacci(18)
    2584
    >>> fibonacci(22)
    17711
    """
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
