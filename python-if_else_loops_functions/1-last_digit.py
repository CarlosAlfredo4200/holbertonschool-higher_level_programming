#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10

finalSrt = {
    'a': 'and is greater than 5',
    'b': 'and is 0',
    'c': 'and is less than 6 and not 0',
}
if lastDigit > 5:
    print("Last digit of {} is {} {} ".format(
        number, lastDigit, finalSrt['a']))
elif lastDigit == 0:
    print("Last digit of {} is {} {}".format(number, lastDigit, finalSrt['b']))
else:
    print("Last digit of {} is {} {}".format(number, lastDigit, finalSrt['c']))
