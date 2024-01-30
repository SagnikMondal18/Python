#How do you iterate through a list using a for loop in Python?
a=[]
n=int(input('Enter the list range : '))
for i in range(n):
    a.append(int(input("Enter values = ")))
print("List value is : ")
for i in a:
    print(i)