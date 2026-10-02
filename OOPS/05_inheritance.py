# inheritance 
"""
inheritance is like a family tree A child class (or subclass). This allows you to create new classes that are specialized versions of existing classes without rewriting all the code
"""
'''
class Animal: # Parent class (superclass)
     def __init__(self, name):
         self.name = name
         def speak(self):
            print("Generic animal sound")

class Dog(Animal): # Dog inherits from Animal (Dog is a subclass of Animal)
        def speak(self): # We *override* the speak method (more on this later)
          print("Woof!")

class Cat(Animal): # Cat also inherits from Animal
       def speak(self):
          print("Meow!")
# Create objects:
my_dog = Dog("Rover")
my_cat = Cat("Fluffy")
# They both have a 'name' attribute (inherited from Animal):
print(my_dog.name) # Output: Rover
print(my_cat.name) # Output: Fluffy
# They both have a 'speak' method, but it behaves differently:
my_dog.speak() # Output: Woof!
my_cat.speak() # Output: Meow!

'''

class Animal: # parent class (super class)
    location = "Australia"
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Genetric animal sound")
class Dog(Animal): # this is how inheritance is done in python
    def speak(self):
        print("Woff!")

# a = Animal("Dog")
# a.speak()

d = Dog("Bruno")
d.speak()
print(d.location)



# super() : inside a child super() let you call methods from the parent class this is useful when you want to extend the parent's behaviour instead of completely replacing it's especially important when initializing the parent class's part of a child object


class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("speaking now..... ")
class Dog(Animal):
    def speak(self):
        super().speak()# we are the using the speak function of the parent class
        print("Woof!")
# a = Animal("Dog")
# a.speak()

d = Dog("Bruno")
d.speak()
