def fibonacci(n):
    """
    Calculates the nth Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to calculate.
                 n must be a non-negative integer.

    Returns:
        int: The nth Fibonacci number.
             Returns 0 for n=0, 1 for n=1 and n=2.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def print_fibonacci_sequence(count):
    """
    Prints the first 'count' Fibonacci numbers.

    Args:
        count (int): The number of Fibonacci numbers to print.
                     count must be a non-negative integer.
    """
    if not isinstance(count, int) or count < 0:
        raise ValueError("Count must be a non-negative integer.")

    if count == 0:
        print("Fibonacci sequence (0 numbers): []")
        return
    
    sequence = [0] if count > 0 else []
    if count > 1:
        sequence.append(1)
    
    a, b = 0, 1
    for _ in range(2, count):
        a, b = b, a + b
        sequence.append(b)
    
    print(f"Fibonacci sequence ({count} numbers): {sequence}")


if __name__ == "__main__":
    print("--- Calculating nth Fibonacci number ---")
    try:
        print(f"Fibonacci(0): {fibonacci(0)}")
        print(f"Fibonacci(1): {fibonacci(1)}")
        print(f"Fibonacci(2): {fibonacci(2)}")
        print(f"Fibonacci(3): {fibonacci(3)}")
        print(f"Fibonacci(5): {fibonacci(5)}")
        print(f"Fibonacci(10): {fibonacci(10)}")
        print(f"Fibonacci(20): {fibonacci(20)}")
    except ValueError as e:
        print(f"Error: {e}")

    print("\n--- Printing Fibonacci sequence ---")
    try:
        print_fibonacci_sequence(0)
        print_fibonacci_sequence(1)
        print_fibonacci_sequence(2)
        print_fibonacci_sequence(5)
        print_fibonacci_sequence(10)
    except ValueError as e:
        print(f"Error: {e}")

    # Example of invalid input handling:
    # try:
    #     fibonacci(-1)
    # except ValueError as e:
    #     print(f"\nCaught expected error for Fibonacci(-1): {e}")

    # try:
    #     print_fibonacci_sequence(-1)
    # except ValueError as e:
    #     print(f"Caught expected error for print_fibonacci_sequence(-1): {e}")

    # You can uncomment the following block to allow user input
    # try:
    #     num_str = input("\nEnter a non-negative integer 'n' to calculate Fibonacci(n) and its sequence: ")
    #     n = int(num_str)
    #     print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
    #     print_fibonacci_sequence(n)
    # except ValueError:
    #     print("Invalid input. Please enter a non-negative integer.")