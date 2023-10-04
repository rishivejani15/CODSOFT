#Calculator Project
logo = """
 _____________________
|  _________________  |
| |   Python Calc   | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

import os
import math

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

def modulo(n1, n2):
  return n1 % n2

def power(n1, n2):
  return n1 ** n2

def root(n1):
  return math.sqrt(n1)

def factorial(n1):
  return math.factorial(n1)

operations1 = {
  "!": factorial,
  "√": root
}

operations2 = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "%": modulo,
  "^": power
}

def calculator():
  print(logo)
  print("Enter 0 for Single Digit calculations")
  print("Enter 1 for Double Digit calculations")
  option = int(input("Choose: "))

  num1 = float(input("Enter the first number?: "))

  should_continue = True
 
  while should_continue:
    
    if(option == 0):
      for symbol in operations1:
        print(symbol)
      operation_symbol = input("Choose an operation: ")
      calculation_function = operations1[operation_symbol]
      answer = calculation_function(num1)
      print(f"\n{operation_symbol}{num1} = {answer}")
      
    elif(option == 1):
      for symbol in operations2:
        print(symbol)
      operation_symbol = input("Choose an operation: ")
      num2 = float(input("Enter the next number?: "))
      calculation_function = operations2[operation_symbol]
      answer = calculation_function(num1, num2)
      print(f"\n{num1} {operation_symbol} {num2} = {answer}")

    else:
      print("Invalid Choice")

    if input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      os.system('cls')
      calculator()

calculator()