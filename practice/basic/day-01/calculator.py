# Write a program that takes two numbers and an operator (+, -, *, /) as input and 
# performs the corresponding operation.

def simple_calculator(n1,n2,operator):

  if operator == '+':
    return n1+n2
  elif operator == '-':
    return n1-n2
  elif operator == '*':
    return n1*n2
  elif operator == '/':
    if n2 == 0:
      return "Error: Division by Zero is not allowed"
    
    return n1/n2
  else:
    return "Invalida Operator, Please use +, -, * or /"

while True:
  try:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    operator = input("Enter opeartor (+ ,* , /, -): ")
    res = simple_calculator(n1, n2, operator)
    print(res)
  except ValueError:
    print("invalid Input")
