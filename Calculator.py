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
    num1 = float(input("Type first number: "))
    op = input("Choose an operator ('+', '-', '*', '/')\n: ")
    num2 = float(input("Type second number: "))
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        print("Invalid an operator")
        return main()
    print(f"{num1} {op} {num2} = {result}")
main()