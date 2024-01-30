#Write a Python program to find the largest number in a list using a for loop.
        #1 type (using min & max function)
        
# n=int(input("Enter the list range = "))
# lst=[]
# for i in range(n):
#     lst.append(int(input("Enter value = ")))

# print("Maximum number of a list = ",max(lst))
# print("Minimum number of a list = ",min(lst))



        #2 type 

n=int(input("Enter the list range = "))
lst=[]
for i in range(n):
    lst.append(int(input("Enter value = ")))
    lrg=lst[0]
    sml=lst[0]
for i in lst:
    if(lrg<i):
        lrg=i
    if(sml>i):
        sml=i
print("Maximum number is : ",lrg)
print("Minimum number is : ",sml)



