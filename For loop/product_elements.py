#Write a Python program to find the product of all elements in a list using a for loop.
n=int(input("Enter your range = "))
lst=[]
for i in range(n):
    lst.append(int(input("Enter the value = ")))

mul=1
for i in lst:
    mul=mul*i
print("The product of all list number is = ",mul)

