# Write code for algorithm 4 below

# 4. Write a function that calculates the value of 'a' to the power of 'b'.For example if a=2 and b=4, then power(2,4) would be calculating 2^4=2*2*2*2 so the result would be 16.
def power(a, b):
    if b == 0:
        return 1 # Any number raised to the power of 0 is 1
    elif b > 0:
        return a * power(a, b - 1) #Multiply 'a' by the result of 'a' raised to the power of (b - 1)
    else:
        return 1 / (a * power(a, -b - 1)) # Calculate the reciprocal by dividing 1 by the product of 'a' and the result of 'a' raised to the power of (-b - 1)
    
# test
result = power(2, 4)
print(result)

#bonus iteration
def power(a, b):
    if b == 0:
        return 1  # Base case: Any number raised to the power of 0 is 1

    result = 1  # Initialize the result to 1

    if b > 0:  # If the exponent is positive
        for _ in range(b):  # Multiply 'a' by itself 'b' times
            result *= a
    else:  # If the exponent is negative
        for _ in range(abs(b)):  # Divide 1 by 'a' 'abs(b)' times to calculate the reciprocal
            result /= a

    return result  # Return the calculated result

# test
result = power(2, 4)
print(result)