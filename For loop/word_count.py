# Create a Python program that counts the number of words in a sentence using a for loop.

s=input("Please enter a sentance : ")
l=s.split()
count=0
for i in l:
    count=count+1
print(count)
