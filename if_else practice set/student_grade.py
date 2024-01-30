markes=int(input("Enter student markes : "))
if(90<=markes):
    print("Grade 'O'")
elif (89>=markes and 80<=markes):
    print("Grade 'E'")
elif(79>=markes and 70<=markes):
    print("Grade 'A'")
elif(69>=markes and 60<=markes):
    print("Grade 'B'")
elif(59>=markes and 40<=markes):
    print("Grade 'C'")
elif 40>markes:
    print("FAIL")