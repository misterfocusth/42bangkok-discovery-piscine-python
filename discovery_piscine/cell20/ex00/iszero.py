#!/usr/bin/env python3

try:
    num = int(input(""))
    if (num == 0):
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except:
    print("Error: invalid input.")
