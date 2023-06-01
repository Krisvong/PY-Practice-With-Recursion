# Write code for algorithm 3 below

# Write a function that returns the nth elements in the Fibonacci Sequence.
def fibonacci(n):
    if n <= 0:
        return None  # Return None for non-positive values of n
    elif n == 1:
        return 0  # Base case: the first Fibonacci number is 0
    elif n == 2:
        return 1  # Base case: the second Fibonacci number is 1
    else:
        # Recursive case: calculate the n-th Fibonacci number by summing the (n-1)-th and (n-2)-th Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# test 
result = fibonacci(8)
print(result)



#bonus iteration
def fibonacci(n):
    if n <= 0:
        return None  # Return None for non-positive values of n
    elif n == 1:
        return 0  # Base case: the first Fibonacci number is 0
    elif n == 2:
        return 1  # Base case: the second Fibonacci number is 1

    # Initialize variables to store the previous two Fibonacci numbers
    fib_n_minus_2 = 0
    fib_n_minus_1 = 1

    # Calculate the n-th Fibonacci number iteratively
    for _ in range(3, n + 1):
        fib_current = fib_n_minus_1 + fib_n_minus_2
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = fib_current

    return fib_n_minus_1

# test 
result = fibonacci(8)
print(result)


