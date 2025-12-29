import sys

def fibonacci(n):
    """
    Calculates the n-th Fibonacci number.

    The Fibonacci sequence is defined as F(n) = F(n-1) + F(n-2),
    with F(0) = 0 and F(1) = 1.

    Args:
        n (int): The index of the Fibonacci number to calculate.
                 Must be a non-negative integer.

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is a negative integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
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
    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
            result = fibonacci(num)
            print(f"The {num}-th Fibonacci number is: {result}")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please provide a non-negative integer as an argument.")
        except TypeError as e:
            print(f"Error: {e}")
    else:
        print("Usage: python fibonacci.py <number>")
        print("\nDisplaying the first 15 Fibonacci numbers:")
        for i in range(15):
            try:
                print(f"F({i}) = {fibonacci(i)}")
            except (TypeError, ValueError) as e:
                print(f"Error calculating F({i}): {e}")