#!/usr/bin/env python3
import sys

def main():
    params = sys.argv[1:]

    if not params:
        print("none")
        return

    displayed = False
    for word in params:
        if not word.endswith("ism"):
            print(word + "ism")
            displayed = True

    if not displayed:
        print("none")

if __name__ == "__main__":
    main()
