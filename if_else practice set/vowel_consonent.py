# Create a Python program that checks if a given character is a vowel or consonant using if-else.
ltr=(input("Enter a alphabte : "))
# if ('a'==ltr or 'e'==ltr or 'i'==ltr or 'o'==ltr or 'u'==ltr or 'A'==ltr or 'E'==ltr or 'I'==ltr or 'O'==ltr or 'U'==ltr):
#     print(ltr,"is vowel alphabate..")
# else:
#     print(ltr,"is consonent alphabate...")

if ltr in 'aeiouAEIOU':
    print("this is vowel...")
else:
    print("This is consonent...")