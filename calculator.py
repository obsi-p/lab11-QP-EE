"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
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

def multiply(a, b): return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot Divide by Zero")
    return b/a

def logarithm(a, b):
    if a<= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid Input")
    return math.log(b,a)

def exponent(a, b): return a ** b


