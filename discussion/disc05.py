"""
LINK: https://cs61a.org/disc/disc05/
"""

# Tree Data Abstraction Implementation #
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t):
    def helper(i, t):
        print("    " * i + str(label(t)))
        for b in branches(t):
            helper(i + 1, b)
    helper(0, t)
# Tree Data Abstraction Implementation #


# Q1: Tree Abstraction Barrier
# Consider a tree t = tree(1, [tree(2), tree(4)]).
# For each of the following expressions, answer these two questions:
# - What does the expression evaluate to?
# - Does the expression violate any abstraction barriers? 
#   If so, write an equivalent expression that does not violate abstraction barriers.
t = tree(1, [tree(2), tree(4)])
label(t)    # 1; no violation
t[0]        # 1; violated --> label(t)
label(branches[0])  # 2; no violation
is_leaf(t[1:][1])   # True; violated --> is_leaf(branches(t)[1])
[label(b) for b in branches(t)]     # [2, 4]; no violation
branches(tree(5, [t, tree(3)]))[0][0]   # 1; violated --> label(branches(tree(5, [t, tree(3)]))[0])


# Q2: Height
def height(t):
    """Return the height of a tree.
    The height of a tree is the length of the longest path from the root to a leaf.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return 0
    return 1 + max(height(b) for b in branches(t))


# Q3: Maximum Path Sum
def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return label(t)
    return label(t) + max(max_path_sum(b) for b in branches(t))


# Q4: Find Path
def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        path = find_path(b, x)
        if path is not None:
            return [label(t)] + path


# Q5: Perfectly Balanced
# Part A
def sum_tree(t):
    """
    Add all elements in a tree.

    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    "*** YOUR CODE HERE ***"
    # total = 0
    # for b in branches(t):
    #     total += sum_tree(b)
    # return label(t) + total
    return label(t) + sum(sum_tree(b) for b in branches(t))

# Part B
def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.

    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    "*** YOUR CODE HERE ***"
    # for b in branches(t):
    #     if sum_tree(b) != sum_tree(branches(t)[0]) or not balanced(b):
    #         return False
    # return True
    return False not in [sum_tree(branches(t)[0]) == sum_tree(b) and balanced(b) for b in branches(t)]


# Q6: Sprout Leaves
def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    # if is_leaf(t):
    #     return tree(label(t), [tree(leaf) for leaf in leaves])
    # new_branches = []
    # for b in branches(t):
    #     new_branches.append(sprout_leaves(b, leaves))
    # return tree(label(t), new_branches)
    if is_leaf(t):
        return tree(label(t), [tree(leaf) for leaf in leaves])
    return tree(label(t), [sprout_leaves(b, leaves) for b in branches(t)])


# Q7: Hailstone Tree
def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will reach N, with height H.

    >>> print_tree(hailstone_tree(1, 0))
    1
    >>> print_tree(hailstone_tree(1, 4))
    1
        2
            4
                8
                    16
    >>> print_tree(hailstone_tree(8, 3))
    8
        16
            32
                64
            5
                10
    """
    if h == 0:
        return tree(n)
    branches = [hailstone_tree(2 * n, h - 1)]
    if (n - 1) % 3 == 0 and (n - 1) > 3 and ((n - 1) // 3) % 2 == 1:
        branches += [hailstone_tree((n - 1) // 3, h - 1)]
    return tree(n, branches)
