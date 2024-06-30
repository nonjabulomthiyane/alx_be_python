# match_case_calculator.py

# Prompt for user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation using match case
match operation:
    case '+':
        result = num1 + num2
        operation_symbol = 'plus'
    case '-':
        result = num1 - num2
        operation_symbol = 'minus'
    case '*':
        result = num1 * num2
        operation_symbol = 'multiplied by'
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
            exit()
        result = num1 / num2
        operation_symbol = 'divided by'
    case _:
         print(f"Invalid operation '{operation}'. Please choose from '+', '-', '*', '/'.")
