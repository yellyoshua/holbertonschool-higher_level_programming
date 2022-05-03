#!/usr/bin/python3
import sys


def fizzbuzz():
    for i in range(0, 100):
        sys.stdout.write(" ")
        if ((i % 3) == 0):
            sys.stdout.write('Fizz')
        if ((i % 5) == 0):
            sys.stdout.write('Buzz')
