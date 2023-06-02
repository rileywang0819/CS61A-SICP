"""
LINK: https://cs61a.org/disc/disc03/
"""
# Q1: Warm Up: Recursive Multiplication
def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.

    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if m == 1:
        return n
    if n == 1:
        return m
    return multiply(m - 1, n) + n


# Q3: Find the Bug
# Answer: this function will be infite when n is odd
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)
# Answer: this function will be infite when n is odd
# Fix it!
def skip_mul_fix(n):
    if n == 1 or n == 2:
        return n
    else:
        return n * skip_mul_fix(n - 2)


# Q4: Is Prime
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    assert n > 1, 'N should be greater than 1.'
    def helper(i):
        if i == n:      # better answer: if i > (n ** 0.5):
            return True
        if n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)
        

# Q5: Recursive Hailstone
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return 
    the number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)


# Q6: Merge Numbers
def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif (n1 % 10) < (n2 % 10):
        return 10 * merge(n1 // 10, n2) + (n1 % 10) 
    else:
        return 10 * merge(n1, n2 // 10) + (n2 % 10)
