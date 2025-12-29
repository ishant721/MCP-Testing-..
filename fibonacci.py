def fibonacci(n):
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
    print("--- Fibonacci Sequence Examples ---")
    
    # Print first 10 Fibonacci numbers
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")

    # Test with a larger number
    large_n = 20
    print(f"\nF({large_n}) = {fibonacci(large_n)}")

    # Test error handling for negative input
    try:
        print(f"\nAttempting F(-1): {fibonacci(-1)}")
    except ValueError as e:
        print(f"\nCaught error for F(-1): {e}")

    # Explicitly test F(0) and F(1) again
    print(f"\nF(0) = {fibonacci(0)}")
    print(f"F(1) = {fibonacci(1)}")