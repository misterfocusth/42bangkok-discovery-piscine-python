#!/usr/bin/env python3

def add_one(n):
    n = n + 1
    return n

if __name__ == "__main__":
    x = 5
    print("Before calling add_one:", x)
    x = add_one(x)
    print("After calling add_one:", x)
