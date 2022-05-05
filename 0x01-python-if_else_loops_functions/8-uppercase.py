#!/usr/bin/python3

def is_char(c):
    return ord(c) >= 97 and ord(c) <= 122


def char_to_uppercase(c):
    if is_char(c):
        return chr(ord(c) - 32)
    else:
        return c


def uppercase(str):
    text = ""
    for i in str:
        text += char_to_uppercase(i)
    print(f"{text}")
