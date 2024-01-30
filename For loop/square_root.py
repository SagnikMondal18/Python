# Create a Python program that calculates the square root of a number using a for loop.


        #<---Solutin-1(using Math module)--->
import math
num=int(input("Enter  any number : "))
sr=math.sqrt(num)
print("Square root of given number is : ",sr)

# any number square:-

# n=int(input("Enter  any number : "))
# sq=n**2
# print("Square of",n,"is :",sq)




        #<---Solution-2--->

num=int(input("Enter  any number : "))
sr=num**(0.5)
print("Square root of",num,"is : ",sr)
