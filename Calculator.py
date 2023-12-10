def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():

    first_number = float(input("Type first number: "))

    operator = input("Choose an operator (+ - * /): ")

    second_number = float(input("Type second number: "))

    if operator == "+":
        resulst = first_number + second_number

    elif operator == "-":
        result = first_number - second_number

    elif operator == "*":
        result = first_number * second_number

    elif operator == "/":
        result = first_number / second_number

    else:
        print("Invalid an operator")
        return main()

    print(f"{first_number} {operator} {second_number}")

main()