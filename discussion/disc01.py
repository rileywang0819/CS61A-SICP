"""
LINK: https://cs61a.org/disc/disc01/
"""
# Q1: Case Conundrum
# （1）What is the result of evaluating the following code?
def special_case():
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x

special_case()  # 12

# （2）What is the result of evaluating this piece of code?
def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x

just_in_case()  # 19

# (3) How about this piece of code?
def case_in_point():
    x = 10
    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x

case_in_point() # 12


# Q2: Jacket Weather?
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    return temp < 60 or raining


# Q3: Square So Slow
# What is the result of evaluating the following code?
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0

square(so_slow(5))  # Infinite Loop


# Q4: Is Prime?
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k = k + 1
    return True


# Q5: Fizzbuzz
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    "*** YOUR CODE HERE ***"
    k = 1
    while k <= n:
        if k % 3 == 0 and k % 5 == 0:
            print('fizzbuzz')
        elif k % 3 == 0:
            print('fizz')
        elif k % 5 == 0:
            print('buzz')
        else:
            print(k)
        k = k + 1


# Q6: Unique Digits
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    count, k = 0, 0
    while k < 10:
        if has_digit(n, k):
            count = count + 1
        k = k + 1
    return count

def has_digit(n, k):
    """Returns whether K is a digit in N.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    "*** YOUR CODE HERE ***"
    while n > 0:
        if n % 10 == k:
            return True
        n = n // 10
    return False
