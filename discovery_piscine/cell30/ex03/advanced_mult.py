#!/usr/bin/env python3

def main():
    for i in range(0, 11):
        print(f"Table de {i}:", end=" ")
        for j in range(0, 11):
            result = i * j
            print(f"{result}", end=" ")
        print()

main()
