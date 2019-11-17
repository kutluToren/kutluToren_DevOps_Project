# -*- coding: utf-8 -*-
   
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# This function adds two numbers 
def add(x, y):
    if (is_number(x) and is_number(y)):
        return round(x + y,2)
    else:
        return 'Error'

# This function subtracts two numbers 
def subtract(x, y):
    if (is_number(x) and is_number(y)):
        return round(x - y,2)
    else:
        return 'Error'
# This function multiplies two numbers
def multiply(x, y):
   if (is_number(x) and is_number(y)):
        return round(x * y,2)
   else:
        return 'Error'
# This function divides two numbers
def divide(x, y):
    if (is_number(x) and is_number(y) and y!=0 ):
        return round(x / y,2)
    else:
        return 'Error'
    
    
def Calc(op,val1,val2):
    if op=='add':
        return add(val1,val2)
    elif op=='subtract':
        return subtract(val1,val2)
    elif op=='multiply':
        return multiply(val1,val2)
    elif op=='divide':
        return divide(val1,val2)
    else:
        return 'Error'
    
