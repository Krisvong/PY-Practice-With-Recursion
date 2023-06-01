# Write code for algorithm 1 below
# Code a solution for the following algorithms using direct recursion.

# 1. Write a program that takes a positive number as an argument and prints the numbers from n to zero.
def print_numbers(n):
    if n < 0:
        return  # Base case: return if n is less than 0
    print(n)  # Print the current value of n
    print_numbers(n - 1)  # Recursive call: print numbers from (n-1) to 0

#test 
print_numbers(5)