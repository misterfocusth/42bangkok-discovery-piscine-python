#!/usr/bin/env python3

def main():
    msg = input("")

    for char in msg:
        if char.islower():
            print(char.upper(), end="")
        elif char.isupper():
            print(char.lower(), end="")
        else:
            print(char, end="")
    print("")

main()
