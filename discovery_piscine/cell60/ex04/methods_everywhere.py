#!/usr/bin/env python3
import sys

def shrink(s):
    return s[:8]

def enlarge(s):
    return s + "Z" * (8 - len(s))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("none")
    else:
        for arg in sys.argv[1:]:
            if len(arg) > 8:
                print(shrink(arg))
            elif len(arg) < 8:
                print(enlarge(arg))
            else:
                print(arg)
