def fibonacci(n):
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
    print("Fibonacci Sequence:")
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")

    try:
        num = int(input("\nEnter a non-negative integer to find its Fibonacci number: "))
        result = fibonacci(num)
        print(f"The {num}th Fibonacci number is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")