# Create a Python program that checks if a string is a palindrome using a for loop.
str=input("Enter a string : ")
store=(str[::-1])
if (store==str):
    print("String is palondrome")
else:
    print("String is not palindrome")


