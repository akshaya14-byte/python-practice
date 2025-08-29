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

if avg_mark < 0 or avg_mark > 100:
     print("Invalid mark.")

elif avg_mark >= 90 and avg_mark <= 100:
     print("Grade: A")
elif avg_mark >= 80 and avg_mark < 90:
     print("Grade: B") 
elif avg_mark >= 70 and avg_mark < 80:
     print("Grade: c")
elif avg_mark >= 60 and avg_mark < 70:
     print("Grade: D")
else:
     print("Grade: F")
print("Total mark is: ", total_mark)
print("Average mark is: ", avg_mark)

