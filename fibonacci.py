def fibonacci(n):
    """
    Calculates the nth Fibonacci number.

    The Fibonacci sequence starts with F(0) = 0 and F(1) = 1.
    For n > 1, F(n) = F(n-1) + F(n-2).

    Args:
        n (int): The non-negative integer index of the desired Fibonacci number.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        # Loop from the 2nd number up to the nth number (inclusive)
        # F(2) is calculated in the first iteration of the loop
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    print("--- Fibonacci Number Examples ---")

    # Test cases with expected results
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (20, 6765) # F(20)
    ]

    for n, expected in test_cases:
        try:
            result = fibonacci(n)
            status = "✅" if result == expected else "❌"
            print(f"F({n:2}) = {result:<5} (Expected: {expected:<5}) {status}")
        except ValueError as e:
            print(f"F({n:2}) = Error: {e}")
        except Exception as e:
            print(f"F({n:2}) = An unexpected error occurred: {e}")

    print("\n--- Testing invalid inputs ---")
    invalid_inputs = [-1, 3.5, "abc", None]

    for invalid_n in invalid_inputs:
        try:
            fibonacci(invalid_n)
            print(f"F({invalid_n}) = No error raised for invalid input. ❌")
        except ValueError as e:
            print(f"F({invalid_n}) = Error: {e} ✅")
        except Exception as e:
            print(f"F({invalid_n}) = An unexpected error occurred: {e} ❌")