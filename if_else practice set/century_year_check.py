# Create a Python program that checks if a given year is a century year or not using if-else.
y=int(input("Enter the year : "))
if y<=0:
    print("0 or negetive are not allow...")
elif (y<=100):
    print("Frist cetnuary")
elif(y%100==0):
    print(y//10,"Mountain")
else:
    print(y%100+1,"Century")