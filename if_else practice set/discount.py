# Create a Python program that calculates the discount amount based on the purchase amount using if-else.
amt=int(input("Enter your amount : "))
if(amt>100):
    if amt <=2000:
        discnt=amt*0.03
        print("discount is : ",discnt)
        print("Total cost : ",amt-discnt)
    elif amt<=5000:
        discnt=amt*0.05
        print("discount is : ",discnt)
        print("Total cost : ",amt-discnt)
    elif amt<=10000:
        discnt=amt*0.09
        print("discount is : ",discnt)
        print("Total cost : ",amt-discnt)
    elif amt<=15000:
        discnt=amt*0.11
        print("discount is : ",discnt)
        print("Total cost : ",amt-discnt)
    elif amt<=25000:
        discnt=amt*0.13
        print("discount is : ",discnt)
        print("Total cost : ",amt-discnt)
    else :
        discnt=amt*0.15
        print("discount is : ",discnt)
        print("Total cost : ",amt-discnt)

else :
    print(" You will get discount on minimum purchase of Rs.100...")
