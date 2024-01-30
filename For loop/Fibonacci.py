# Create a Python program that prints the Fibonacci sequence up to a specified limit using a for loop.
n=int(input('Enter the range element : '))
a,b=0,1
print("Fibonacci Series is : ")
for i in range(1,n+1):
    print(a)
    sum=a+b
    a=b
    b=sum

