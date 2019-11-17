import pytest
import calculator


def test_calc_int_add():
    temp=calculator.add(2,4)
    assert temp==6

def test_calc_int_substract():
    temp=calculator.subtract(4,2)
    assert temp==2
    
def test_calc_int_multiply():
    temp=calculator.multiply(4,2)
    assert temp==8
    
def test_calc_int_divide():
    temp=calculator.divide(10,5)
    assert temp==2
    
def test_calc_double_add():
    temp=calculator.add(2.3,4.6)
    assert temp==float(6.9)

def test_calc_double_substract():
    temp=calculator.subtract(4.73,2.21)
    assert temp==float(2.52)
    
def test_calc_double_multiply():
    temp=calculator.multiply(4.12,2.32)
    assert temp==round(float(9.5584),2)
    
def test_calc_double_divide():
    temp=calculator.divide(7,4.7)
    assert temp==round(float(1.48936170213),2)
    
def test_calc_op_add():
    temp=calculator.Calc('add',2.3,4.6)
    assert temp==float(6.9)

def test_calc_op_substract():
    temp=calculator.Calc('subtract',4.73,2.21)
    assert temp==float(2.52)
    
def test_calc_op_multiply():
    temp=calculator.Calc('multiply',4.12,2.32)
    assert temp==round(float(9.5584),2)
    
def test_calc_op_divide():
    temp=calculator.Calc('divide',7,4.7)
    assert temp==round(float(1.48936170213),2)
    
def test_calc_op_undef():
    temp=calculator.Calc('noname',7,4.7)
    assert temp=='Error'

def test_calc_undef_mult():
    temp=calculator.add('nonum','ahmet')
    assert temp=='Error'

def test_calc_undef_sub():
    temp=calculator.subtract('nonum','ahmet')
    assert temp=='Error'

def test_calc_undef_mult():
    temp=calculator.multiply('nonum','ahmet')
    assert temp=='Error'
    
def test_calc_undef_div():
    temp=calculator.divide('kemal','ahmet')
    assert temp=='Error'
    
def test_calc_undef_divide():
    temp=calculator.divide(10,0)
    assert temp=='Error'
