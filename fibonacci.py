def fibonacci(n):
    """
    Calculates the nth Fibonacci number.

    The Fibonacci sequence starts with F(0) = 0 and F(1) = 1.
    F(n) = F(n-1) + F(n-2) for n > 1.

    Args:
        n (int): The index of the Fibonacci number to calculate (non-negative).

    Returns:
        int: The nth Fibonacci number. Returns 0 for negative input.
    """
    if n < 0:
        return 0  # Fibonacci numbers are typically defined for non-negative integers
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
    print("--- Fibonacci Sequence Examples ---")

    # Calculate and print the first 10 Fibonacci numbers
    print("\nFirst 10 Fibonacci numbers (F(0) to F(9)):")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")

    # Test with a specific positive number
    num_positive = 15
    print(f"\nThe {num_positive}th Fibonacci number (F({num_positive})): {fibonacci(num_positive)}")

    # Test with 0
    num_zero = 0
    print(f"The {num_zero}th Fibonacci number (F({num_zero})): {fibonacci(num_zero)}")

    # Test with 1
    num_one = 1
    print(f"The {num_one}st Fibonacci number (F({num_one})): {fibonacci(num_one)}")

    # Test with a negative number
    num_negative = -5
    print(f"The {num_negative}th Fibonacci number (F({num_negative})): {fibonacci(num_negative)} (usually 0 or error for negative input)")