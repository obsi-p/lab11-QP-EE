
import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(a)
    except TypeError:
        raise ValueError("Inputs must be a number")

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise ValueError("Inputs must be a number")

def add(a, b): return a + b

def subtract(a, b): return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("invalid logarithm input")
    return math.log(b, a)

def exp(a, b):
    return a ** b