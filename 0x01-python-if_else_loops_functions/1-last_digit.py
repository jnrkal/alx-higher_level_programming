#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
digit = abs(number) % 10

if number < 0:
    digit = -digit

comparison = "greater than 5" if digit > 5 else "less than 6 and not 0" if digit != 0 else "0"

print("Last digit of {} is {} and is {}".format(number, digit, comparison))

