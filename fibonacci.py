def fibonacci_sequence(n):
    """
    Generates a list of Fibonacci numbers up to the n-th term.

    Args:
        n (int): The number of terms to generate.

    Returns:
        list: A list containing the first n Fibonacci numbers.
              Returns an empty list if n <= 0.
              Returns [0] if n == 1.
              Returns [0, 1] if n == 2.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_fib = sequence[-1] + sequence[-2]
            sequence.append(next_fib)
        return sequence

if __name__ == "__main__":
    # Example usage:
    print("Fibonacci sequence up to 0 terms:", fibonacci_sequence(0))
    print("Fibonacci sequence up to 1 term:", fibonacci_sequence(1))
    print("Fibonacci sequence up to 2 terms:", fibonacci_sequence(2))
    print("Fibonacci sequence up to 10 terms:", fibonacci_sequence(10))
    print("Fibonacci sequence up to 15 terms:", fibonacci_sequence(15))

    # You can prompt the user for input
    try:
        num_terms = int(input("\nEnter the number of Fibonacci terms to generate: "))
        if num_terms < 0:
            print("Please enter a non-negative integer.")
        else:
            print(f"Fibonacci sequence up to {num_terms} terms: {fibonacci_sequence(num_terms)}")
    except ValueError:
        print("Invalid input. Please enter an integer.")