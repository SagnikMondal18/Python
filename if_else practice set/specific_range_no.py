# Write a Python program to check if a number is within a specified range using if-else.

num=int(input("Enter your value : "))
r=range(1,num*2,2)
if num in r:
    print("The number is present in this range")
else:
    print("This number is not present in the range ")
