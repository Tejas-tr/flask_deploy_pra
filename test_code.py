# file name should start with 'test' else pytest wont consider this as testing file
import pytest
import numpy as np
from new_func import a,b, add_num, sub_num, multi_num, divide_num

print(add_num(a,b), a)
print(b)


# function should start with 'test' to include in pytest
def test_a_functionality():
    a = 20
    b = 2
    assert add_num(a,b) == 22 

def test_b_functionality():
    a = 20
    b = 2
    assert sub_num(a,b) == 18, 'value failed'
    assert multi_num(a,b) == 40, 'value failed'
    # here 'value failed' statment will shown in result if above statement is failed
# run 'pytest .' in terminal to get whether these functions are passed for failed

def add_number():
    a,b = 2 , 1
    assert add_num(a,b) == 3

def test_random():
    a, b = np.random.randint(1,100,2)
    assert add_num(a,b) == a + b, 'addition failed'
    assert sub_num(a,b) == a -b, 'subtraction failed'
    assert multi_num(a,b) == a*b, 'multiplication failed'
    assert divide_num(a,b) ==  a/b, 'divsion failed'