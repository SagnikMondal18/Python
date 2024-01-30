# Write a Python program to remove duplicates from a list using a for loop.
l=[]
result=[]
n=int(input("Enter the list range : "))
for i in range(n):
    l.append(input("Value is = "))
print("All list value s are : ",l)

for i in l:
    if i not in result:
        result.append(i)
print("The final list of removing the duplicate values : ",result)



