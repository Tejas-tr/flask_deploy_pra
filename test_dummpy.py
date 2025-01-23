# file name should start with 'test' else pytest wont consider this as testing file
import pytest
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
    assert sub_num(a,b) == 18
    assert multi_num(a,b) == 40
# run 'pytest .' in terminal to get whether these functions are passed for failed