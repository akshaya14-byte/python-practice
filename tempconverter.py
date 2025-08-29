#temperature converter

unit = input("Enter the unit you want to convert from (C/F): ").upper()
temp = float(input("Enter the temperature: "))

if unit.upper() =='C':
    print(f"{temp}C is {round(temp * 9/5 + 32, 1)}F")
elif unit.upper() =='F':
    print(f"{temp}F is {round((temp - 32) * 5/9, 1)}C")
else:
    print("Invalid unit")
