# Write a Python program to find the GCD (Greatest Common Divisor) of two numbers using a for loop.
n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
num=min(n1,n2)
print(num)
for n in range(1,num+1):
    if(n1%n==0 and n2%n==0):
        gcd=n
print(f"GCD of {n1} and {n2} is : {gcd}")


