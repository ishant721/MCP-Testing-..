def fibonacci(n):
    """
    Calculates the nth Fibonacci number.

    The Fibonacci sequence starts with 0 and 1, and each subsequent number
    is the sum of the two preceding ones.
    (e.g., 0, 1, 1, 2, 3, 5, 8, ...)

    Args:
        n (int): The index of the Fibonacci number to calculate.
                 Must be a non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is a negative integer.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")
    if n < 0:
        raise ValueError("Fibonacci sequence is defined for non-negative integers only.")
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
    print("--- Fibonacci Number Calculator ---")
    try:
        user_input = input("Enter a non-negative integer 'n' to find the nth Fibonacci number: ")
        n_term = int(user_input)

        fib_result = fibonacci(n_term)
        print(f"The {n_term}th Fibonacci number is: {fib_result}")

        print("\n--- First 10 Fibonacci Numbers ---")
        for i in range(10):
            print(f"F({i}) = {fibonacci(i)}")

    except ValueError:
        print("Error: Invalid input. Please enter an integer.")
    except TypeError as e:
        print(f"Error: {e}")