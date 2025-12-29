def fibonacci(n):
    """
    Calculates the nth Fibonacci number.

    The Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, ...
    (where F(0) = 0, F(1) = 1)

    Args:
        n (int): The index of the Fibonacci number to calculate.
                 Must be a non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    print("Fibonacci sequence examples:")
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")

    print(f"\nfibonacci(20) = {fibonacci(20)}")

    try:
        fibonacci(-1)
    except ValueError as e:
        print(f"\nCaught expected error for negative input: {e}")