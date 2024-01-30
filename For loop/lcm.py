# Write a Python program to find the LCM (Least Common Multiple) of two numbers using a for loop.
a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
c=max(a,b)
for i in range(1,c+1):
    if(a%i==0 and b%i==0):
        gcd=i
lcm=(a*b)//gcd       
print(f"LCM of {a} and {b} is : {lcm}")




