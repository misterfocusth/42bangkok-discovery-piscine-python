#!/usr/bin/env python3

def main():
    num = int(input("Enter a number\n"))
    for i in range(0, 10):
        result = num * i
        print(f"{i} x {num} = {result}")

main()
