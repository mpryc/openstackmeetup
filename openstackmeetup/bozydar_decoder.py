#!/bin/python

def decode(code):
    result = ''
    length = len(code)
    for i in range(length/2):
        result += chr(int((code[2*i:2*i+2]),16))
    return result

code=raw_input()
print decode(code)
