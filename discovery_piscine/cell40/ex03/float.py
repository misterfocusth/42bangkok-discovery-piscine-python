#!/usr/bin/env python3

def main():
    num = input("Give me a number: ")

    try:
        if (num.endswith(".00")):
            print("This number is an integer.")
        else:
            int(num)
            print("This number is an integer.")
    except ValueError:
        try:
            float(num)
            print("This number is a decimal.")
        except ValueError:
            return "not a number"

main()
