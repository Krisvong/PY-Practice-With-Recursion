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


# Bonus iteration
def is_palindrome(string):
    # Convert the string to lowercase and remove whitespace
    string = string.lower().replace(" ", "")

    # Initialize two pointers: one at the beginning and one at the end of the string
    start = 0
    end = len(string) - 1

    # Iterate until the pointers meet in the middle
    while start < end:
        # Compare characters at the start and end positions
        if string[start] != string[end]:
            return False  # Characters are not equal, so it's not a palindrome

        # Move the pointers towards the middle
        start += 1
        end -= 1

    return True  # All characters have been compared and are equal, so it's a palindrome

result = is_palindrome("racecar")
print(result) #True

result = is_palindrome("Hello, World!")
print(result) #False
