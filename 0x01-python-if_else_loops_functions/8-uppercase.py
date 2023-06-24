#!/usr/bin/python3
# 8-uppercase.py
# prints a string in uppercase followed by a new line.


def uppercase(str):
    for char in string:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
            print(char, end="")
            print()
