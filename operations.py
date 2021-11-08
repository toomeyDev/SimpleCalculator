"""
Module for handling central operations used to calculate values
when using the calculator.
"""

def addition(addend1: int, addend2: int):
    result_sum = addend1 + addend2
    return result_sum
    
def subtraction(minuend: int, subtrahend: int):
    result_difference = minuend - subtrahend
    return result_difference
    
def multiplication(multiplicand: int, multiplier: int):
    result_product = multiplicand * multiplier
    return result_product
    
def division(dividend: int, divisor: int):
    result_quotient = int(dividend / divisor)
    result_remainder = int(dividend % divisor)
    return result_quotient
