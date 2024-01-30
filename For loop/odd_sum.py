# Write a Python program to find the sum of all odd numbers from 1 to 50 using a for loop.
n=int(input("Enter the 1st range : "))
n2=int(input("Enter the 2nd range : "))
sum=0
for i in range(n,n2+1):
    if(i%2!=0):
        sum=sum+i
print("Sum of odd numbers in particular range : ",sum)

