# Create a Python program that identifies the type of a triangle (e.g., equilateral, isosceles, or scalene) based on input values using if-else.

a=int(input("Enter the one side value of triangle: "))
b=int(input("Enter the 2nd side value of triangle: "))
c=int(input("Enter the 3rd side value of triangle: "))
if (b+c>a)and(c+a>b)and(a+b>c):
    if(a==b)and(b==c)and(a==c):
        print("Eequilateral Triangle")

    elif((a==b)or(b==c)or(a==c)):
	     print("Isosceles Triangle")

    elif((a!=b)and(b!=c)and(a!=c)):
        print("Scalene Triangle")

else:
    print("Invalid Value...")