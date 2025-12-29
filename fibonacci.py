import sys

def generate_fibonacci_sequence(n_terms):
    """
    Generates a list of the first n_terms Fibonacci numbers.

    The sequence starts with F(0) = 0 and F(1) = 1.
    For example:
    generate_fibonacci_sequence(0) -> []
    generate_fibonacci_sequence(1) -> [0]
    generate_fibonacci_sequence(5) -> [0, 1, 1, 2, 3]
    """
    if not isinstance(n_terms, int):
        raise TypeError("Number of terms must be an integer.")
    if n_terms < 0:
        raise ValueError("Number of terms cannot be negative.")
    elif n_terms == 0:
        return []
    elif n_terms == 1:
        return [0]
    else:
        sequence = [0, 1]
        # Generate subsequent terms
        for _ in range(2, n_terms):
            next_fib = sequence[-1] + sequence[-2]
            sequence.append(next_fib)
        return sequence

def get_nth_fibonacci(n):
    """
    Calculates the n-th Fibonacci number (0-indexed).
    
    F(0) = 0
    F(1) = 1
    F(2) = 1
    F(3) = 2
    ...
    For example:
    get_nth_fibonacci(0) -> 0
    get_nth_fibonacci(1) -> 1
    get_nth_fibonacci(5) -> 5
    """
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")
    if n < 0:
        raise ValueError("Input 'n' cannot be negative.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        # Iterate n-1 times to reach the n-th Fibonacci number
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    # Default to generating 10 Fibonacci terms if no argument is provided
    default_terms = 10

    if len(sys.argv) > 1:
        try:
            num_input = int(sys.argv[1])
            if num_input < 0:
                raise ValueError("Number of terms cannot be negative.")
            default_terms = num_input
        except ValueError:
            print(f"Error: Invalid number of terms '{sys.argv[1]}' provided.")
            print("Usage: python fibonacci.py [number_of_terms]")
            print("       e.g., python fibonacci.py 15")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

    print(f"Generating the first {default_terms} Fibonacci numbers:")
    try:
        fib_sequence = generate_fibonacci_sequence(default_terms)
        print(fib_sequence)

    except Exception as e:
        print(f"Error generating sequence: {e}")
        sys.exit(1)