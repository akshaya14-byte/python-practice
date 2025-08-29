#python calculator
import math 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, **, sqrt, sin, cos, tan, log): ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '**':
    result = num1 ** num2
elif operator == 'sqrt':
    choice = input("Calculate sqrt of which number? (1/2): ")
    if choice == '1':
        result = math.sqrt(num1)
    elif choice == '2':
        result = math.sqrt(num2)
        #sin function
elif operator == 'sin':
    choice = input("Calculate sin of which number? (1/2): ")
    if choice == '1':
        result = math.sin(math.radians(num1))
    elif choice == '2':
        result = math.sin(math.radians(num2))
        #cos function
elif operator == 'cos':
    choice = input("Calculate cos of which number? (1/2): ")
    if choice == '1':
        result = math.cos(math.radians(num1))
    elif choice == '2':
        result = math.cos(math.radians(num2))
        #tan function
elif operator == 'tan':
    choice = input("Calculate tan of which number? (1/2): ")
    if choice == '1':
        result = math.tan(math.radians(num1))
    elif choice == '2':
        result = math.tan(math.radians(num2))
        #log function
elif operator == 'log':
    choice = input("Calculate log of which number? (1/2): ")
    if choice == '1':
        if num1 > 0:
            result = math.log(num1)
        else:
            result = "Log value of negative quantities is undefined!"
    elif choice == '2':
        if num2 > 0:
            result = math.log(num2)
        else:
            result = "Log value of negative quantities is undefined!"
    else:
        result = "Log value of negative quantities is undefined!"
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Division by zero error"
else:
    result = "Invalid operator"
print(result)
