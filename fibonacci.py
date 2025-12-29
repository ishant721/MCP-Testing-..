def fibonacci(n):
    """
    Calculates the n-th Fibonacci number.

    The Fibonacci sequence starts with F(0) = 0, F(1) = 1,
    and F(n) = F(n-1) + F(n-2) for n > 1.

    Args:
        n (int): The index of the Fibonacci number to calculate.
                 Must be a non-negative integer.

    Returns:
        int or str: The n-th Fibonacci number, or an error message
                    if the input is invalid.
    """
    if not isinstance(n, int):
        return "Input must be an integer."
    if n < 0:
        return "Input must be a non-negative integer."
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
    print("--- Fibonacci Sequence ---")
    
    # Print the first 15 Fibonacci numbers
    print("\nFirst 15 Fibonacci numbers:")
    for i in range(15):
        print(f"F({i}) = {fibonacci(i)}")

    # Example of getting a specific Fibonacci number
    print("\n--- Specific Fibonacci Numbers ---")
    test_cases = [7, 10, 20, 0, 1, -5, 3.5]
    for num in test_cases:
        result = fibonacci(num)
        print(f"The Fibonacci number at index {num} is: {result}")

    # You can also get user input for a specific number
    # try:
    #     user_input = int(input("\nEnter a non-negative integer to find its Fibonacci number: "))
    #     fib_result = fibonacci(user_input)
    #     print(f"The F({user_input}) is: {fib_result}")
    # except ValueError:
    #     print("Invalid input. Please enter an integer.")