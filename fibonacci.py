def generate_fibonacci_sequence(n_terms):
    """
    Generates a list containing the first n_terms of the Fibonacci sequence.

    Args:
        n_terms (int): The number of terms to generate. Must be a non-negative integer.

    Returns:
        list: A list of Fibonacci numbers. Returns an empty list if n_terms <= 0.
    """
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
    else:
        sequence = [0, 1]
        while len(sequence) < n_terms:
            next_term = sequence[-1] + sequence[-2]
            sequence.append(next_term)
        return sequence

if __name__ == "__main__":
    try:
        num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
        if num_terms < 0:
            print("Please enter a non-negative integer.")
        else:
            fib_sequence = generate_fibonacci_sequence(num_terms)
            if fib_sequence:
                print(f"The first {num_terms} Fibonacci terms are:")
                print(fib_sequence)
            else:
                print(f"No Fibonacci sequence generated for {num_terms} terms.")
    except ValueError:
        print("Invalid input. Please enter an integer.")