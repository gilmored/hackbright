"""CLI application for a prefix-notation calculator."""

from arithmetic import *


# Replace this with your code

while True:
    user_input = input("Enter your equation > ")
    tokens = user_input.split(" ")
   

    if len(tokens) < 2:
        print('not an equation')
        break
    elif len(tokens) > 3:
        print('too many inputs')
        break
    elif len(tokens) < 3:
        num2 =  "0"
    else:
         num2 = tokens[2]


    num1 = tokens[1]
    operator = tokens [0]
    result = None


    if operator == "+":
        result = add(float(num1), float(num2))
        print(result)

    elif operator == "-":
        result = subtract(float(num1), float(num2))
        print(result)

    elif operator == "x":
        result = multiply(float(num1), float(num2))
        print(result)
        
    elif operator == "/":
        result = divide(float(num1), float(num2))
        print(result)
    
    elif operator == "square":
        result = square(float(num1))
        print(result)

    elif operator == "cube":
        result = cube(float(num1))
        print(result)

    elif operator == "pow":
        result = pow(float(num1), float(num2))
        print(result)

    elif operator == "mod":
        result = mod(float(num1), float(num2))
        print(result)