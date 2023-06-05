"""
LINK: https://cs61a.org/disc/disc04/
"""
# Q1: Count Stair Ways
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.

    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    # base case 1: means that the action we took leads to our goal of reaching the top
    if n == 0:
        return 1
    # base case 2: means that the action we took leads overstep --> invalid action
    if n < 0:
        return 0
    # the number of different ways to go up the last (n - 1) stairs
    take_one_step = count_stair_ways(n - 1)   
    # the number of different ways to go up the last (n - 2) stairs 
    take_two_step = count_stair_ways(n - 2)
    return take_one_step + take_two_step


# Q2: Count K
def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.

    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 1
    if n < 0:
        return 0
    count, i = 0, 1
    while i <= k:
        count += count_k(n - i, k)
        i += 1
    return count


# Q3: WWPD: Lists
# What would Python display?
a = [1, 5, 4, [2, 3], 3]
print(a[0], a[-1])  # 1 3
len(a)      # 5
2 in a      # False
a[3][0]     #2


# Q4: Even weighted
def even_weighted_loop(s):
    """Return a new list that keeps only the even-indexed elements 
    of s and multiplies them by their corresponding index.

    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted_loop(x)
    [0, 6, 20]
    """
    "*** YOUR CODE HERE ***"
    return [i * s[i] for i in range(len(s)) if i % 2 == 0]


# Q5: Max Product
def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.

    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:])) 


# Q6: WWPD: Dictionaries
# What would Python display?
pokemon = {'pikachu': 25, 'dragonair': 148}
pokemon     # {'pikachu': 25, 'dragonair': 148}
'mewtwo' in pokemon     # False
len(pokemon)        # 2
pokemon['mew'] = pokemon['pikachu']
pokemon[25] = 'pikachu'
pokemon     # {'pikachu': 25, 'dragonair': 148, 'mew': 25, 25: 'pikachu'}
pokemon['mewtwo'] = pokemon['mew'] * 2
pokemon     # {'pikachu': 25, 'dragonair': 148, 'mew': 25, 25: 'pikachu', 'mewtwo': 50}
pokemon[['firetype', 'flying']] = 146       # Error, unhashable type
