# Operator Overloading: Making Operators Work
# with Your Objects

# Python lets you define how standard operators (like + , - , == ) behave when
# used with objects of your own classes. This is done using special methods called
# “magic methods” (or “dunder methods” because they have double underscores
# before and after the name).

class Point:
    def __init__(self, x, y):
      self.x = x 
      self.y = y
    def __add__(self, other):  # Overloading the + operator
         return Point(self.x + other.x, self.y + other.y) #other' refers to the object on the *right* side of the +
    def __str__(self):     # String representation (for print() and str())
     return f"({self.x}, {self.y})"
    def __eq__(self, other):   # Overloading == operator
      return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2 # This now works! It calls p1.__add__(p2)
print(p3) # Output: (4, 6) (This uses the __str__ method)
print(p1 == p2) # Output: False (This uses the __eq__ method)

