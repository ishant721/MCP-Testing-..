def fibonacci_sequence(n):
    """
    Generates the first n Fibonacci numbers.

    Args:
        n (int): The number of terms to generate.

    Returns:
        list: A list containing the first n Fibonacci numbers.
              Returns an empty list if n is less than or equal to 0.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_list = [0, 1]
        while len(fib_list) < n:
            next_fib = fib_list[-1] + fib_list[-2]
            fib_list.append(next_fib)
        return fib_list

def get_nth_fibonacci(n):
    """
    Calculates the nth Fibonacci number (0-indexed).

    Args:
        n (int): The index of the Fibonacci number to retrieve.

    Returns:
        int: The nth Fibonacci number.
             Returns None if n is negative.
    """
    if n < 0:
        return None
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
    # Demonstrate generating a sequence
    num_terms = 15
    fib_series = fibonacci_sequence(num_terms)
    print(f"Fibonacci sequence up to {num_terms} terms: {fib_series}")

    # Demonstrate getting the nth Fibonacci number
    index_to_get = 10
    nth_fib = get_nth_fibonacci(index_to_get)
    if nth_fib is not None:
        print(f"The {index_to_get}th Fibonacci number (0-indexed) is: {nth_fib}")
    else:
        print(f"Invalid input for get_nth_fibonacci: {index_to_get}")

    index_to_get = 0
    nth_fib = get_nth_fibonacci(index_to_get)
    if nth_fib is not None:
        print(f"The {index_to_get}th Fibonacci number (0-indexed) is: {nth_fib}")

    index_to_get = 1
    nth_fib = get_nth_fibonacci(index_to_get)
    if nth_fib is not None:
        print(f"The {index_to_get}st Fibonacci number (0-indexed) is: {nth_fib}")

    index_to_get = -5
    nth_fib = get_nth_fibonacci(index_to_get)
    if nth_fib is not None:
        print(f"The {index_to_get}th Fibonacci number (0-indexed) is: {nth_fib}")
    else:
        print(f"Invalid input for get_nth_fibonacci: {index_to_get}")