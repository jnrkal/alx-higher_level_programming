#!/usr/bin/python3
# 9-print_last_digit.py
#prints the last digit of a number.

def print_last_digit(number):
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last
