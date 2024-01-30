#Write a Python program to reverse a list using a for loop.
lst=[]
lr=int(input("Enter the list range : "))
for i in range(lr):
    lst.append(int(input("Enter the list value : ")))
    rev=lst[ : :-1]
print('Reverse list is = ',rev)

