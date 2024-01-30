# Write a Python program to determine the roots of a quadratic equation using if-else.
import cmath
a=int(input("Enter the value : "))
b=int(input("Enter the value : "))
c=int(input("Enter the value : "))

dis=(b**2)-(4*a*c)

s1=((-b)-cmath.sqrt(dis))/(2*a)
s2=((-b)+cmath.sqrt(dis))/(2*a)

if dis>0:
    print("Two distnict real roots..")
elif dis==0:
    print("Two real equal roots..")
elif dis<0:
    print("Two complex roots")
print(f"The solution are {s1} and {s2}")