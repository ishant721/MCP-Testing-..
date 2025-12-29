def fibonacci(n):
    """
    Calculates the n-th Fibonacci number.

    The Fibonacci sequence starts with 0, 1, 1, 2, 3, 5, ...
    - fibonacci(0) returns 0
    - fibonacci(1) returns 1
    - fibonacci(2) returns 1
    - fibonacci(3) returns 2

    Args:
        n (int): The non-negative index of the Fibonacci number to calculate.

    Returns:
        int: The n-th Fibonacci number. Returns -1 for invalid input (n < 0).
    """
    if n < 0:
        # Invalid input for a Fibonacci index
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def generate_fibonacci_sequence(count):
    """
    Generates a list of the first 'count' Fibonacci numbers.

    Args:
        count (int): The number of Fibonacci numbers to generate.
                     Must be a non-negative integer.

    Returns:
        list: A list containing the first 'count' Fibonacci numbers.
              Returns an empty list for count <= 0.
    """
    if count <= 0:
        return []
    elif count == 1:
        return [0]
    else:
        sequence = [0, 1]
        while len(sequence) < count:
            next_fib = sequence[-1] + sequence[-2]
            sequence.append(next_fib)
        return sequence

if __name__ == "__main__":
    print("--- Fibonacci Number Calculation ---")
    for i in range(15):
        print(f"fibonacci({i}) = {fibonacci(i)}")

    print("\n--- Testing Edge Cases ---")
    print(f"fibonacci(-1) = {fibonacci(-1)}") # Expected: -1
    print(f"fibonacci(0) = {fibonacci(0)}")   # Expected: 0
    print(f"fibonacci(1) = {fibonacci(1)}")   # Expected: 1

    print("\n--- Fibonacci Sequence Generation ---")
    print(f"First 0 numbers: {generate_fibonacci_sequence(0)}")
    print(f"First 1 number: {generate_fibonacci_sequence(1)}")
    print(f"First 5 numbers: {generate_fibonacci_sequence(5)}")
    print(f"First 10 numbers: {generate_fibonacci_sequence(10)}")
    print(f"First 20 numbers: {generate_fibonacci_sequence(20)}")