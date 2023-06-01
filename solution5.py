# Write code for algorithm 5 below

# 5. Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.

def is_palindrome(string):
    # Convert the string to lowercase and remove whitespace
    string = string.lower().replace(" ", "")

    # Check if the string is equal to its reverse
    if string == string[::-1]:
        return True #It is a palindrome
    else:
        return False #It is not a palindrome
    
# test
result = is_palindrome("racecar")
print(result) #True

result = is_palindrome("Hello, World!")
print(result) #False