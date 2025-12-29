def get_fibonacci_n(n):
    """
    Calculates the nth Fibonacci number iteratively.
    The sequence starts with F(0)=0, F(1)=1.
    F(2)=1, F(3)=2, etc.
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

def generate_fibonacci_sequence(count):
    """
    Generates a list of the first 'count' Fibonacci numbers.
    The sequence starts with F(0)=0, F(1)=1.
    """
    if count < 0:
        raise ValueError("Count must be a non-negative integer.")
    
    if count == 0:
        return []
    elif count == 1:
        return [0]
    else:
        sequence = [0, 1]
        a, b = 0, 1
        for _ in range(2, count):
            next_fib = a + b
            sequence.append(next_fib)
            a, b = b, next_fib
        return sequence

if __name__ == "__main__":
    print("--- Fibonacci Numbers and Sequences ---")

    print("\nGetting specific Fibonacci numbers:")
    for i in range(13):
        try:
            fib_n = get_fibonacci_n(i)
            print(f"F({i}) = {fib_n}")
        except ValueError as e:
            print(f"Error for F({i}): {e}")

    print("\nGenerating Fibonacci sequences:")
    for count in [0, 1, 2, 5, 10, 15]:
        try:
            fib_seq = generate_fibonacci_sequence(count)
            print(f"First {count} terms: {fib_seq}")
        except ValueError as e:
            print(f"Error for count {count}: {e}")

    print("\nTesting error handling:")
    try:
        get_fibonacci_n(-5)
    except ValueError as e:
        print(f"Caught expected error for negative n: {e}")

    try:
        generate_fibonacci_sequence(-1)
    except ValueError as e:
        print(f"Caught expected error for negative count: {e}")