# largest among three number
a=int(input("Enter the 1st number : "))
b=int(input("Enter the 2nd number : "))
c=int(input("Enter the 3rd number : "))

if a>b:
    if a>c:
        print(a,"is large number..")
    else:
        print(c,"is larger number...")

else:
    if a<b:
        print(b,"is larger number...")
    else:
        print(c,"is larger number...")




