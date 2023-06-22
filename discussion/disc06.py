"""
LINK: https://inst.eecs.berkeley.edu/~cs61a/sp23/disc/disc06/
"""

from disc05 import is_leaf, branches, label

""" Mutability """
# Q1: WWPD: Mutability
"""
(1.1)
x = [1, 2, 3]
y = x
x += [4]
x   # [1, 2, 3, 4]
# y is pointing to the same list as x now, which got mutated
y   # [1, 2, 3, 4]   
"""
"""
(1.2)
x = [1, 2, 3]
y = x
x = x + [4]     # create NEW list, assigns it to x!
x   # [1, 2, 3, 4]
y   # [1, 2, 3]
"""
"""
s1 = [1, 2, 3]
s2 = s1
s1 is s2    # True
"""
"""
s2.extend([5, 6])
s1[4]   # 6
"""
"""
s1.append([-1, 0, 1])
s2[5]   # [-1, 0, 1]
"""
"""
s3 = s2[:]
s3.insert(3, s2.pop(3))
len(s1)     # 5
"""
"""
s1[4] is s3[6]      # True
s3[s2[4][1]]        # 1
s1[:3] is s2[:3]    # False
s1[:3] == s2[:3]    # True
"""
"""
s1[4].append(2)
s3[6][3]    # 2
"""


""" Iterators """
# Q2: Add This Many
def add_this_many(x, el, s):
    """ Adds el to the end of list s the number of times x occurs in s.
    Make sure to modify the original list using list mutation techniques.

    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    "*** YOUR CODE HERE ***"
    count_x = 0
    for item in s:
        if item == x:
            count_x += 1
    s.extend([el for _ in range(count_x)])


# Q3: WWPD: Iterators
"""
s = "cs61a"
s_iter = iter(s)
next(s_iter)    # 'c'
next(s_iter)    # 's'
list(s_iter)    # ['6', '1', 'a']
"""
"""
s = [[1, 2, 3, 4]]
i = iter(s)
j = iter(next(i))
next(j)     # 1
"""
"""
s.append(5)
next(i)     # 5
"""
"""
next(j)     # 2
list(j)     # [3, 4]
next(i)     # StopIteration
"""


""" Generators """
# Q4: WWPD: Generators
def infinite_generator(n):
    """
    >>> next(infinite_generator)
    TypeError
    >>> gen_obj = infinite_generator(1)
    >>> next(gen_obj)
    1
    >>> next(gen_obj)
    2
    >>> list(gen_obj)
    Infinite Loop
    """
    yield n
    while True:
        n += 1
        yield n

def rev_str(s):
    """
    >>> hey = rev_str("hey")
    >>> next(hey)
    'h'
    >>> next(hey)
    'e'
    >>> next(hey)
    'h'
    >>> list(hey)
    ['y', 'e', 'h']
    """
    for i in range(len(s)):
        yield from s[i::-1]

def add_prefix(s, pre):
    """
    >>> school = add_prefix("schooler", ["pre", "middle", "high"])
    >>> next(school)
    'preschooler'
    >>> list(map(lambda x: x[:-2], school))
    ['middleschool', 'highschool']
    """
    if not pre:
        return 
    yield pre[0] + s
    yield from add_prefix(s, pre[1:])


# Q5: Filter-Iter
def filter_iter(iterable, f):
    """
    Implement a generator function that only yields elements of iterable
    for which f returns True.

    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    "*** YOUR CODE HERE ***"
    yield from [item for item in iterable if f(item)]


# Q6: Primes Generator
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order. Implement this function
    using a for loop and yield statement.

    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    "*** YOUR CODE HERE ***"
    for num in range(n, 1, -1):
        if is_prime(num):
            yield num

def primes_gen2(n):
    """Generates primes in decreasing order. Now implement this function
    using yield from.

    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n < 2:
        return
    if is_prime(n):
        yield n
    yield from primes_gen2(n - 1)


# Q7: Generate Preorder
def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    branch_entries = []
    for b in branches(t):
        branch_entries += preorder(b)
    return [label(t)] + branch_entries

def generate_preorder(t):
    """Yield the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> gen = generate_preorder(numbers)
    >>> next(gen)
    1
    >>> list(gen)
    [2, 3, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    yield label(t)
    for b in branches(t):
        yield from generate_preorder(b)


# (Optional) Mystery Reverse Environment Diagram
def mystery(p, q):
    p[1].extend(q)
    q.append(p[1:])

p = [2, 3]
q = [4, [p]]
mystery(q, p)
