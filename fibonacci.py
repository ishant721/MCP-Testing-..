def fibonacci(n):
    """
    Calculates the nth Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to calculate (non-negative).

    Returns:
        int: The nth Fibonacci number. Returns 0 for n <= 0.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    print("Fibonacci sequence for n from 0 to 10:")
    for i in range(11):
        print(f"fibonacci({i}) = {fibonacci(i)}")

    print("\nCalculating specific Fibonacci numbers:")
    test_cases = [0, 1, 2, 5, 10, 15, -3]
    for n in test_cases:
        print(f"fibonacci({n}) = {fibonacci(n)}")