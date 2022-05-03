#!/usr/bin/python3

def uppercase(str):
    # check if the string is empty
    if str == "":
        return ""
    # check if the first character is lowercase
    if str[0] >= 'a' and str[0] <= 'z':
        # convert the first character to uppercase
        str = chr(ord(str[0]) - ord('a') + ord('A')) + str[1:]
    # return the string
    return str
