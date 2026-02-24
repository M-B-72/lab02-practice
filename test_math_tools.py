
from math_tools import add, multiply, is_even, subtract, max_of_three, is_palindrome, find_min, remove_duplicates

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("test_add: ALL PASSED")

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
    print("test_multiply: ALL PASSED")

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    print("test_is_even: ALL PASSED")


def test_subtract():
    assert subtract(7, 2) == 5
    assert subtract(3, 1) == 2
    assert subtract(11, 3) == 8
    print("test_subtract: ALL PASSED")

def test_max_of_three():
    assert max_of_three(7, 7, 7) == 7
    assert max_of_three(7, 2, 5) == 7
    assert max_of_three(9, 2, 7) == 9
    assert max_of_three(9, 11, 7) == 11
    assert max_of_three(2, 2, 1) == 2

    print("test_max_of_three: ALL PASSED")

def test_is_palindrome():
    assert is_palindrome('aza') == True
    assert is_palindrome('') == True
    assert is_palindrome('c') == True
    assert is_palindrome('a b a') == True
    assert is_palindrome('racecar') == True
    assert is_palindrome('bye') == False

    print("test_is_palindrome: ALL PASSED")


def test_find_min():
    assert find_min([0, 1, 2, 3, 4, 5]) == 5
    assert find_min([7, 1, 8, 3, 9, 5]) == 9

    print("test_find_min: ALL PASSED")

def test_remove_duplicates():

    assert remove_duplicates(['apple', 'apple', 'banana', 'banana' ]) == list(set(['apple', 'apple', 'banana', 'banana' ]))
    assert remove_duplicates([]) == list(set([])) 
    assert remove_duplicates(['zebra', 'apple', 'banana']) == list(set(['zebra', 'apple', 'banana']))
    assert remove_duplicates(['apple', 'apple', 'banana', 1, '1', 2]) == list(set(['apple', 'apple', 'banana', 1, '1', 2]))
    assert remove_duplicates([2, 2, 2]) == list(set([2, 2, 2]))
    assert remove_duplicates([1]) == list(set([1]))

    print("test_remove_duplicates: ALL PASSED")


# Run all tests
test_add()
test_multiply()
test_is_even()
test_subtract()
test_max_of_three()
test_is_palindrome()
test_find_min()
test_remove_duplicates()
print("--- All tests passed! ---")