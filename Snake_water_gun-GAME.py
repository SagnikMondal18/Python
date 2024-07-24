import random

# water=-1 , snake=1 , gun=0

name=input("Enter name : ")
print(f"Welcome,{name}")
while(1):
    yes_no=input("You want to play 'SNAKE , WATER , GUN' game? yes/no: ")
    if(yes_no.lower()=="yes".lower()):
        computer= random.choice([0, 1, -1])
        youstr=input("enter your choise (w,s,g) : ")
        if(youstr.lower()=="w".lower() or youstr.lower()=="s".lower() or youstr.lower()=="g".lower()):
            youdict={"s".lower():1,"w".lower():-1,"g".lower():0}
            you=youdict[youstr.lower()]
            dictgame={1:"snake",-1:"water",0:"gun"}

            print(f"\nYou choise {dictgame[you]} \nComputer chose {dictgame[computer]}\n")

            if(computer==you):
                print(f"MATCH  is DRAW,\nThank you")
            else:
                if(computer==1 and you==-1):
                    print(f"You Lost!!\nOops better luck next time")

                elif(computer==1 and you==0):
                    print(f"You Win..\nThank you")   

                elif(computer==-1 and you==1):
                    print(f"You Win..\nThank you")   

                elif(computer==-1 and you==0):
                    print(f"You Lost!!\nOops better luck next time")   

                elif(computer==0 and you==-1):
                    print(f"You Win..\nThank you")   

                elif(computer==0 and you==1):
                    print(f"You Lost!!\nOops better luck next time")  

        else:
            print(f"Somthing gone wrong!!!")

    else:
        print("Exit!!")
        exit()