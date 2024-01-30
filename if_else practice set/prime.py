# Write a Python program to determine if a given number is prime or not using if-else
import math
n=int(input("Enter the value : "))
for i in range(2,int(math.sqrt(n))+1,1):
    if(n%i==0):
        print(n,"is not Prime number...")
        break
else:
    print(n,"is Prime number...")

