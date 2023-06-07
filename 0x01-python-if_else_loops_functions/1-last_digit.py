#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = abs(number) % 10
if number < 0:
    rem = -rem
else:
    rem = rem

i = f"Last digit of {number} is {rem} "

if rem > 5:
    j = "and is greater than 5"
elif rem == 0:
    j = "and is 0"
else:
    j = "and is less than 6 and not 0"

print(i + j)
