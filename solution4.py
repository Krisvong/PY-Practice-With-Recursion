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