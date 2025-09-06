

# i = 1
# while i <= numbers:
#     print(i)
#     i += 1
#num = int(input("Enter a number: "))
# i = 2
# total = 0
#
# while i <= num and i % 2 == 0:
#     digit = num % 10
#     total += digit * i
#     num //= 10
#     i += 2
# num = int(input("Enter a number: "))


# palindrome = 0
# original_num = num
# while num > 0:
#     last_digit = num % 10
#     palindrome = palindrome * 10 + last_digit
#     num //= 10
# if original_num == palindrome:
#     print("The number is a palindrome")
# else:
#     print("The number is not a palindrome")


# num = int(input("Enter a number: "))
#
# i = 1
# count = 0
# while num > 0:
#     num //= 10
#     count += 1
# print(count)


#Print multiplication table of a given number
# num = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(f"{num} x {i} ={num * i} ")
#     i += 1


# num = int(input("Enter a number: "))
#
# sum  = 0
# while num > 0:
#     digit = num % 10
#     sum += digit
#     num //= 10
# print("sum:", sum)


#compound interest
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount must be greater than 0")

while rate <= 0:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("Rate of interest must be greater than 0")

while time <= 0:
    time = float(input("Enter the time (in years): "))
    if time <= 0:
        print("Time must be greater than 0")

amount = principle * (1 + rate / 100) ** time
print(f"The amount after {time} years is: {amount:.2f}")