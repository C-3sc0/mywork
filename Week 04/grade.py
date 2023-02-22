#program that reads in a student's % mark and prints out corresponding the grade (checking if the % is valid)
#under 40% --> Fail
#between 40% and 49% --> pass
#between 50% and 59% --> Merit 2
#between 60% and 69% --> Merit 1
#over 70% --> ditinction


grade = float(input("Enter the %:"))
if grade <= 40:
    print("Fail")
elif grade <= 49:
    print("Pass")
elif grade <= 59:
    print("Merit 2")
elif grade <= 69:
    print("Merit 1")
else:
    print("Distinction")

