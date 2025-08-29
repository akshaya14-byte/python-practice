#checking voting eligibility
# age = int(input("Enter your age: "))
# if age < 0 or age > 100:
#     print("Invalid age.")
#
# elif age < 18:
#     print("You can register to vote once you turn 18.")
#
# elif age >= 18:
#     print("You are eligible to vote.")
# else: 
#     print("You are eligible to vote.")
    # git add .
    # git commit -m "updated"
    # git push origin main


# mark = int(input("Enter your mark: "))
#
# if mark < 0 or mark > 100:
#     print("Invalid mark.")
#
# elif mark >= 90 and mark <= 100:
#     print("Grade: A")
# elif mark >= 80 and mark < 90:
#     print("Grade: B")
# elif mark >= 70 and mark < 80:
#     print("Grade: c")
# elif mark >= 60 and mark < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")




Phy_mark = int(input("Enter your mark for Subject Phy: "))
Chem_mark = int(input("Enter your mark for Subject Chem: "))
Math_mark = int(input("Enter your mark for Subject Math: "))
Bot_mark = int(input("Enter your mark for Subject Bot: "))
Zoo_mark = int(input("Enter your mark for Subject Zoo: "))

avg_mark = (Phy_mark + Chem_mark + Math_mark + Bot_mark + Zoo_mark) / 5 
total_mark = Phy_mark + Chem_mark + Math_mark + Bot_mark + Zoo_mark
def get_grade(mark):
        if mark >= 90:
            return "A"
        elif mark >= 80:
            return "B"
        elif mark >= 70:
            return "C"
        elif mark >= 60:
            return "D"
        elif mark >= 40:
            return "E"
        else:
            return "F"
if Phy_mark < 35 or Chem_mark < 35 or Math_mark < 35 or Bot_mark < 35 or Zoo_mark < 35 or avg_mark < 40:
     
     print("Failed.Low average!!")

if avg_mark < 0 or avg_mark > 100 :
     print("Invalid mark.")

elif avg_mark >= 90 and avg_mark <= 100:
     print("Grade: A")
elif avg_mark >= 80 and avg_mark < 90:
     print("Grade: B") 
elif avg_mark >= 70 and avg_mark < 80:
     print("Grade: C")
elif avg_mark >= 60 and avg_mark < 70:
     print("Grade: D")
elif avg_mark <= 40:
     print("Fail")
else:
     print("Grade: F")

print(f"Physics: {Phy_mark} -> Grade {get_grade(Phy_mark)}")
print(f"Chemistry: {Chem_mark} -> Grade {get_grade(Chem_mark)}")
print(f"Math: {Math_mark} -> Grade {get_grade(Math_mark)}")
print(f"Botany: {Bot_mark} -> Grade {get_grade(Bot_mark)}")
print(f"Zoology: {Zoo_mark} -> Grade {get_grade(Zoo_mark)}")
print("Total mark is: ", total_mark)
print("Average mark is: ", avg_mark)

