#!/usr/bin/env python3

def main():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = [x + 2 for x in original_array]

    print("Original array:", original_array)
    print("New array:", new_array)

if __name__ == "__main__":
    main()
