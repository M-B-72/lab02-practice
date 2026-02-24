
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0

def subtract(a, b):
    return a - b

def max_of_three(a, b, c):
    max = a

    if b > max:
        max = b
    if c > max:
        max = c
    return max

def is_palindrome(s):
    if s[0:] == s[::-1]:
        return True
    else:
        return False
    
def find_min(numbers):
    min = numbers[0]

    for i in range(len(numbers)):
        if numbers[i] > min:
            min = numbers[i]

    return min

def remove_duplicates(items):
    return list(set(items))




