# Write a Python program to find the common elements between two lists using a for loop
l1=[]
l2=[]
l3=[]
n=int(input("Enter first list range : "))
for i in range(1,n+1):
    l1.append(int(input("Enter value = ")))

n1=int(input("Enter second list range : "))
for j in range(1,n1+1):
    l2.append(int(input("Enter value = ")))

for i in l1:
    if i in l2:
        l3.append(i)
print("Common elements : ",l3)