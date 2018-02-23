from math import floor

def sawtooth(T,x):
    while x > T:
        x = x - T
    while x < 0:
        x = x + T
    return x

def triangle(T,x):
    return abs(sawtooth(T,x)-T/2)

def square(T,x):
    while x > T :
        x = x - T
    while x < 0:
        x = x + T
    if  x<=T/2 and x>=0:
        return 1
    else:
        return 0
