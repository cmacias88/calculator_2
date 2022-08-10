"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

print("This is a calculator.")
print()
print("It does the following operations:") 
print("add(+)\nsubtract(-)\nmultiply(*)\ndivide(/)\nsquare(square)\ncube(cube)\npower(pow)\nmodulus(mod)\nquit(q)\n")
calculator_operations = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod','q']

def calculator_input_validation(calculator_input):
    while True:
        calculator_input = calculator_input.split(" ")
        if calculator_input[0] in calculator_operations:
            if len(calculator_input) > 1:
                if (len(calculator_input)==2 and calculator_input[1].isdigit()) or (len(calculator_input)==3 and calculator_input[1].isdigit() and calculator_input[2].isdigit()):
                    return calculator_input
                else:
                    print("Please enter numbers after your operation.")
                    calculator_input = input("> ")
            elif calculator_input[0]=='q':
                return calculator_input
            else:
                print("You have not input values to calculate.")
                calculator_input = input("> ")
        else:
            print("You have not entered a valid operation.")
            calculator_input = input("> ") 

while True:
    calculator_input = input("Please enter math function followed by the two numbers you would like to use (Please separate items by spaces): ")
    calculator_input = calculator_input_validation(calculator_input)
    if calculator_input[0] == "q":
        break
    else:
        num_1 = int(calculator_input[1])
        if len(calculator_input) > 2:
            num_2 = int(calculator_input[2]) 

        if calculator_input[0] == '+':
            print(add(num_1, num_2))
        elif calculator_input[0] == '-':
            print(subtract(num_1, num_2))
        elif calculator_input[0] == '*':
            print(multiply(num_1, num_2))
        elif calculator_input[0] == '/':
            print(divide(num_1, num_2))
        elif calculator_input[0] == 'square':
            print(square(num_1))
        elif calculator_input[0] == 'cube':
            print(cube(num_1))
        elif calculator_input[0] == 'pow':
            print(power(num_1, num_2))
        elif calculator_input[0] == 'mod':
            print(mod(num_1, num_2))
        
        