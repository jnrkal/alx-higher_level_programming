#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = number % 10 if number >= 0 else (abs(number) % 10) * -1

if last_digit > 5:
    message = 'greater than 5'
elif last_digit < 6 and last_digit != 0:
    message = 'less than 6 and not 0'
else:
    message = '0'
print(f'Last digit of {number} is {last_digit} and is {message}')
