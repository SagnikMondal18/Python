# Write a Python program to determine the largest of three numbers using if-else.
a=int(input("Enter the 1st number : "))
b=int(input("Enter the 2nd number : "))
c=int(input("Enter the 3rd number : "))

if a>b and a>c:
    print(a,"is larger number..")
elif a<b and c<b:
    print(b,"is larger number...")
else:
    print(c,"is larger number...")

