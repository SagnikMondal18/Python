#Write a Python program that calculates the factorial of a number using a for loop.
        #Type 1
n=int(input("Enter the numnber : "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"Factorial of {n} is : ",fact)




        #Type 2
import math
n=int(input("Enter the numnber : "))
for i in range(1,n+1):
    fact=math.factorial(i)
print("The factorial is = ",fact)
