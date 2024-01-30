# Write a Python program to count the number of vowels in a given string using a for loop.
name=input('Enter a string : ')
vow=0
con=0
for i in name:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vow=vow+1
for i in name:
    if (i!='a' or i!='e' or i!='i' or i!='o' or i!='u' or i!='A' or i!='E' or i!='I' or i!='O' or i!='U' and i!=' '):
        con=con+1
print('Number of vowel is = ',vow)
print('Number of consonent is = ',con-vow)
