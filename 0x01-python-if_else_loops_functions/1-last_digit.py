#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0 :
    last_digit = number % 10
if number < 0 :
    last_digit = ((number * -1) % 10) * -1
if number > 5 :
    str = f"last_digit of {number} is {last_digit} and its greater than 5"
elif last_digit < 6 and last_digit != 0 :
    str = f"last_digit of {number} is {last_digit} and its less than 6 and not 0"
elif last_digit == 0 :
    str = f"last_digit of {number} is {last_digit} and is 0"
print(str)
