# Write code for algorithm 2 below

# 2. Write a function that prints the natural numbers from 1 to n.
def print_natural_numbers(n):
    if n <= 0:
        return  # Base case: return if n is less than or equal to 0
    print_natural_numbers(n - 1)  # Recursive call: print natural numbers from (n-1) to 1
    print(n)  # Print the current value of n

#test 
print_natural_numbers(5)