#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return

    text = sys.argv[1]

    result = ''.join([c for c in text if c == 'z'])

    if result:
        print(result.lower())
    else:
        print("none")

if __name__ == "__main__":
    main()
