# Basic Calculator for +, -, *, /, %

limit = int(input("Enter the number of calculations: "))  # Limit for iterations

for count in range(limit):
    operator = input("Enter Calculate Operator (+, -, *, /, %): ")
    number1 = float(input("Enter First Value: "))
    number2 = float(input("Enter Second Value: "))
    result = None
    
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        if number2 != 0:
            result = number1 / number2
        else:
            print("Error: Division by zero is not allowed.")
            continue
    elif operator == "%":
        result = number1 % number2
    else:
        print("Sorry, your operation is wrong!")
        continue
    
    print(f"Calculated value is: {result}")

print("All calculations are complete.")
