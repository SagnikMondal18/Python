#Create a Python program that calculates the BMI (Body Mass Index) of a person based on their weight and height using if-else.
h=float(input("Enter your hight : "))
w=int(input("enter your weight : "))
bmi=(w/(h**2)) 
print(bmi)
if bmi<18.5:
    print("Underweight..")
elif(bmi>=18.5 and bmi<25):
    print("Normal..")
elif(bmi>=25 and bmi<30):
    print('Overweight..')
else:
    print('Obesity..')    





