#checking voting eligibility
age = int(input("Enter your age: "))
if age < 0 or age > 100:
    print("Invalid age.")

elif age < 18:
    print("You can register to vote once you turn 18.")

elif age >= 18:
    print("You are eligible to vote.")
else: 
    print("You are eligible to vote.")
    # git add .
    # git commit -m "Your commit message"
    # git push origin main
