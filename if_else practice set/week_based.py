# Write a Python program to determine the day of the week based on a user-provided number using if-else
num=int(input("enter the value : "))
if(num<7 and num!=0):
    if(num==1):
        print("Monday...")
    elif(num==2):
        print("Tuesday...")
    elif(num==3):
        print("Wednesday...")
    elif(num==4):
        print("Thursday...")
    elif(num==5):
        print("Friday...")
    elif(num==6):
        print("Saturday...")
    elif(num==7):
        print("Sunday...")
else:
    print("Invalid Number!!!!!!!!")
    

