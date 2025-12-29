def fibonacci(n):
    """
    Calculates the nth Fibonacci number.

    The Fibonacci sequence starts with 0 and 1.
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

    Args:
        n (int): The index of the desired Fibonacci number (non-negative).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        TypeError: If the input n is not an integer.
        ValueError: If the input n is a negative integer.
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
    print("Fibonacci Sequence Generator")
    print("---------------------------\n")

    # Print the first 10 Fibonacci numbers
    print("First 10 Fibonacci numbers:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")

    # Example of calculating a specific Fibonacci number
    n_value = 15
    print(f"\nFibonacci({n_value}) = {fibonacci(n_value)}")

    # Example of handling invalid input
    try:
        print(f"\nFibonacci(-3) = {fibonacci(-3)}")
    except ValueError as e:
        print(f"\nError calculating F(-3): {e}")

    try:
        print(f"Fibonacci(5.5) = {fibonacci(5.5)}")
    except TypeError as e:
        print(f"Error calculating F(5.5): {e}")

    # You can also take user input
    # try:
    #     user_input = int(input("\nEnter a non-negative integer to find its Fibonacci number: "))
    #     print(f"Fibonacci({user_input}) = {fibonacci(user_input)}")
    # except ValueError:
    #     print("Invalid input. Please enter an integer.")
    # except Exception as e:
    #     print(f"An unexpected error occurred: {e}")