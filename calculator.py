"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    calculator_input = input("Please enter math function followed by the two numbers you would like to use (Please separate items by spaces): ")

    if calculator_input == "q":
        break
    else:
        calculator_input = calculator_input.split(" ") 
        num_1 = int(calculator_input[1])
        num_2 = int(calculator_input[2])
        if calculator_input[0] == '+':
            print(add(num_1, num_2))
        elif calculator_input[0] == '-':
            print(subtract(num_1, num_2))
        elif calculator_input[0] == '*':
            print(multiply(num_1, num_2))