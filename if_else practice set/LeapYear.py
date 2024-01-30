# Create a Python program that checks if a given year is a leap year using both if-else and a function

def leapyear(year):
    if(year%4==0 and year%100!=0 or year%400==0):
        print("The year is leap Year..")
    else:
        print("The year is not leap Year..")


year=int(input("enter year : "))
leapyear(year)