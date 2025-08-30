# or = at least one condition must be true


# temperature = int(input("Enter the temperature: "))
#
# is_raining = False
#
# if temperature > 30 or is_raining or temperature < 0:
#     print("The weather is not suitable.")
#
# else:
#     print("The weather is suitable.")

# Ans = both conditions must be true


# temperature = int(input("Enter the temperature: "))
#
# is_sunny = False
#
# if temperature >= 20 and is_sunny:
#     print("It is hot outside🥵.")
#
# elif temperature <= 0 and  is_sunny:
#     print("It is cold outside🥶.")
#
# elif temperature < 20 and  is_sunny:
#     print("The weather is moderate outside😌.")
#
# elif temperature >= 20 and not is_sunny:
#     print("It is hot and cloudy.")
#
# elif temperature <= 0 and not is_sunny:
#     print("It is cold and cloudy.")
#
# elif temperature < 20 and not is_sunny:
#     print("The weather is moderate and cloudy.")


#password strength
#true if any(char.upper() for char in password)
#true if any(int for int in password)
#true if any(char in "!@#$%^&*" for char in password)


# password = input("Enter your password: ")
#
# has_uppercase = any(char.isupper() for char in password)
# has_numbers = any(char.isdigit() for char in password)
# has_specialchar = any(char in "!@#$%^&*" for char in password)
#
# if has_uppercase and has_numbers and has_specialchar and len(password) >=8:
#     print("Strong password")
# else:
#     print("Weak password")
 

# Leap year checker:
# A year is a leap year if it is divisible by 4,
# except for years that are divisible by 100,
# unless they are also divisible by 400.
# year = int(input("Enter a year: "))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


#palindrome checker
# num = input("Enter a number: ")
# if num == num[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


#student grade checker

mrk_1 = int(input("Enter marks for subject 1: "))
mrk_2 = int(input("Enter marks for subject 2: "))
mrk_3 = int(input("Enter marks for subject 3: "))

if mrk_1 < 0 or mrk_2 < 0 or mrk_3 < 0 or mrk_1 > 100 or mrk_2 > 100 or mrk_3 > 100:
    print("Invalid marks")
else:
    avg_mrk = (mrk_1 + mrk_2 + mrk_3) / 3
    if avg_mrk >=75 and (mrk_1 >=35 and mrk_2 >=35 and mrk_3 >=35):
        print("Distinction")
    else:
        print("Not Distinction")
    print(f"The average mark is: {round(avg_mrk, 1)}")