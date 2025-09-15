#!/usr/bin/env python3
import math

def main():
    try:
        user_input = input("Give me a number: ")
        number = float(user_input)
        result = math.ceil(number)
        print(result)

    except ValueError:
        print("Invalid input, please enter a number.")

main()
