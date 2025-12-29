def fibonacci(n):
    """
    Calculates the n-th Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to calculate (non-negative).

    Returns:
        int: The n-th Fibonacci number.

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
    print("Fibonacci Sequence Generator")
    try:
        num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
        if num_terms < 0:
            print("Please enter a non-negative integer.")
        else:
            print(f"Generating the first {num_terms} Fibonacci terms:")
            for i in range(num_terms):
                print(f"F({i}) = {fibonacci(i)}")
    except ValueError:
        print("Invalid input. Please enter an integer.")