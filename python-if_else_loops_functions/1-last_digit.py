#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
finalSrt = {
    'a': 'and is greater than 5',
    'b': 'and is 0',
    'c': 'and is less than 6 and not 0',
}
if number < 0:
    digit = -digit

print("Last digit of {} is {} ".format(number, digit), end="")
if digit > 5:
    print(finalSrt['a'])
elif digit == 0:
    print(finalSrt['b'])
else:
    print(finalSrt['c'])
