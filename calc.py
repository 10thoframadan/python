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
  userInp = float(input("Type first number: "))
  op = input("Choose an operator (+, -, *, /): ")
  userInp1 = float(input("Type second number: "))
  
  if op == '+':
    result = userInp + userInp1

  elif op == '-':
    result = userInp - userInp1

  elif op == '*':
    result = userInp * userInp1

  elif op == '/':
    result = userInp / userInp1

  else:
    print("Invalid an operator")
    return main()

  print(f"{userInp} {op} {userInp} = {result}")
  main()

main()
