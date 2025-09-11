def fibonacci(v):
    """
    Calculate the nth Fibonacci number.

    Args:
        v (int): The position in the Fibonacci sequence (must be a non-negative integer).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If v is a negative integer.

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(5)
        5
    """
    if v < 0:
        raise ValueError("Input must be a non-negative integer")
    elif v == 0:
        return 0
    elif v == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, v + 1):
            a, b = b, a + b
        return b