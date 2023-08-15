"""
LINK: https://inst.eecs.berkeley.edu/~cs61a/sp23/disc/disc08/
"""

# Q1: That's inheritance, init?
class Butterfly():
    def __init__(self, wings=2):
        self.wings = wings

class Monarch(Butterfly):
    def __init__(self):
        # _________________________________________
        self.colors = ['orange', 'black', 'white']

# super.__init__()  ... ×
# super().__init__()    ... √
# Butterfly.__init__()  ... ×
# Butterfly.__init__(self)  ... √

class MimicButterfly(Butterfly):
    def __init__(self, mimic_animal):
        super().__init__()
        self.mimic_animal = mimic_animal


# Q2: Shapes
import math
pi = math.pi

class Shape:
    """All geometric shapes will inherit from this Shape class."""
    def __init__(self, name):
        self.name = name

    def area(self):
        """Returns the area of a shape"""
        print("Override this method in ", type(self))

    def perimeter(self):
        """Returns the perimeter of a shape"""
        print("Override this function in ", type(self))

class Circle(Shape):
    """A circle is characterized by its radii"""
    def __init__(self, name, radius):
        "*** YOUR CODE HERE ***"
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        """Returns the perimeter of a circle (2πr)"""
        "*** YOUR CODE HERE ***"
        return 2 * pi * self.radius

    def area(self):
        """Returns the area of a circle (πr^2)"""
        "*** YOUR CODE HERE ***"
        return pi * self.radius ** 2

class RegPolygon(Shape):
    """A regular polygon is defined as a shape whose angles and side lengths are all the same.
    This means the perimeter is easy to calculate. 
    The area can also be done, but it's more inconvenient.
    """
    def __init__(self, name, num_sides, side_length):
        "*** YOUR CODE HERE ***"
        super().__init__(name)
        self.num_sides = num_sides
        self.side_length = side_length

    def perimeter(self):
        """Returns the perimeter of a regular polygon (the number of sides multiplied by side length)"""
        "*** YOUR CODE HERE ***"
        return self.num_sides * self.side_length

class Square(RegPolygon):
    def __init__(self, name, side_length):
        "*** YOUR CODE HERE ***"
        super().__init__(name)
        self.side_length = side_length

    def area(self):
        """Returns the area of a square (squared side length)"""
        "*** YOUR CODE HERE ***"
        return self.side_length ** 2

class Triangle(RegPolygon):
    """An equilateral triangle"""
    def __init__(self, name, side_length):
        "*** YOUR CODE HERE ***"
        super().__init__(name)
        self.side_length = side_length

    def area(self):
        """Returns the area of an equilateral triangle is (squared side length multiplied by the provided constant"""
        constant = math.sqrt(3)/4
        "*** YOUR CODE HERE ***"
        return self.side_length ** 2 * constant


# Q3: Cat
class Pet:
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner)
        self.lives = lives

    def talk(self):
        """Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        "*** YOUR CODE HERE ***"
        print(f'{self.name} says meow!')

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero,
        is_alive becomes False. If this is called after lives has
        reached zero, print 'This cat has no more lives to lose.'
        """
        "*** YOUR CODE HERE ***"
        self.lives -= 1
        if self.lives == 0:
            self.is_alive = False
        if self.lives <= 0:
            print('This cat has no more lives to lose.')

    def revive(self):
        """Revives a cat from the dead. The cat should now have 
        9 lives and is_alive should be true. Can only be called
        on a cat that is dead. If the cat isn't dead, print 
        'This cat still has lives to lose.'
        """
        if not self.is_alive:
            self.__init__(self.name, self.owner)
        else:
            print('This cat still has lives to lose.')

    def __repr__(self):
        "*** YOUR CODE HERE ***"
        return self.name + ', ' + str(self.lives) + ' lives'

    def __str__(self):
        "*** YOUR CODE HERE ***"
        return self.name

# Q4: NoisyCat
class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner, lives)

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        "*** YOUR CODE HERE ***"
        for _ in range(2):
            super().talk()
        

# Q5: WWPD: Repr-esentation
"""
Note: 
This is not the typical way repr is used, nor is this way of writing repr recommended.
This problem is mainly just to make sure you understand how repr and str work.
"""
class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
         return self.x

    def __str__(self):
         return self.x * 2

class B:
    def __init__(self):
         print('boo!')
         self.a = []

    def add_a(self, a):
         self.a.append(a)

    def __repr__(self):
         print(len(self.a))
         ret = ''
         for a in self.a:
             ret += str(a)
         return ret
    
# Given the above class definitions, what will the following lines output?
"""
>>> A('one')
one
>>> print(A('one'))
oneone
>>> repr(A('two'))
'two'
>>> b = B()
boo!
>>> b.add_a(A('a'))
>>> b.add_a(A('b'))
>>> b
2
'aabb'
"""


# Q6: Cat Representation
# (The rest of the Cat class is omitted here, but assume all methods from the Cat class above are implemented)
"""
>>> cat = Cat("Felix", "Kevin")
>>> cat
Felix, 9 lives
>>> cat.lose_life()
>>> cat
Felix, 8 lives
>>> print(cat)
Felix
"""
