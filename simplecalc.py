#python calculator
import math 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, **, sqrt): ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '**':
    result = num1 ** num2
elif operator == 'sqrt':
    result = math.sqrt(num1 * num2)
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Division by zero error"
else:
    result = "Invalid operator"
print(result)
