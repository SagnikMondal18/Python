# Write a Python program to determine if a given number is a perfect square using if-else.
        #1 type of solution
n=int(input("Enter a number : "))
for i in range(1,n):
    if (i*i>n):
        print("The number is not perfact square..")
        break
    if (i*i==n):
        print("The number is perfact square..")
        break

