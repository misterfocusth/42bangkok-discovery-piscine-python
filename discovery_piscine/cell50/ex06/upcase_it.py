#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) == 2:
        print(sys.argv[1].upper())
    else:
        print("none")

if __name__ == "__main__":
    main()
