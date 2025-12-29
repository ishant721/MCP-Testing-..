def fibonacci(n):
    """
    Calculates the nth Fibonacci number.

    The Fibonacci sequence starts with 0 and 1,
    and each subsequent number is the sum of the two preceding ones.
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

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

    # Test cases for small numbers
    for i in range(11):
        print(f"fibonacci({i}) = {fibonacci(i)}")

    # Test case for a larger number
    print(f"\nfibonacci(20) = {fibonacci(20)}")

    # Test case for a slightly larger number
    print(f"fibonacci(30) = {fibonacci(30)}")

    # Test error handling
    try:
        fibonacci(-1)
    except ValueError as e:
        print(f"\nError handling test: {e}")