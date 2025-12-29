def fibonacci(n):
    """
    Calculates the n-th Fibonacci number.

    The Fibonacci sequence starts with F(0) = 0 and F(1) = 1.
    F(n) = F(n-1) + F(n-2) for n > 1.

    Args:
        n (int): The index of the Fibonacci number to calculate. Must be a non-negative integer.

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")
    if n < 0:
        raise ValueError("Input 'n' must be a non-negative integer.")
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
    print("Fibonacci sequence up to F(10):")
    for i in range(11):
        print(f"F({i}) = {fibonacci(i)}")

    print("\nTesting specific values:")
    print(f"F(7) = {fibonacci(7)}")
    print(f"F(0) = {fibonacci(0)}")
    print(f"F(1) = {fibonacci(1)}")
    print(f"F(20) = {fibonacci(20)}")

    # Example of error handling
    try:
        fibonacci(-5)
    except ValueError as e:
        print(f"\nError calculating F(-5): {e}")

    try:
        fibonacci(3.5)
    except TypeError as e:
        print(f"Error calculating F(3.5): {e}")

    try:
        fibonacci("abc")
    except TypeError as e:
        print(f"Error calculating F('abc'): {e}")