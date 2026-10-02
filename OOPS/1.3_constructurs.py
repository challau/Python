class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary # create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")

e1 = Employee(3400,"Jhon Doe", 4)
print(e1.get_salary())
e1.get_info()








# class     → blueprint
# object    → actual thing created from blueprint
# self      → current object

# __init__  → sets initial data when object is created
# method    → function that belongs to a class





# 3. The Constructor: Setting Things Up ( __init__ )
# The __init__ method is special. It’s called the constructor. It’s automatically run
# whenever you create a new object from a class.
# What’s it for? The constructor’s job is to 

# initialize the object’s attributes – to give
# them their starting values. It sets up the initial state of the object.

# You can also set default values for parameters in the constructor, making them
# optional when creating an object:
class Dog:
    def __init__(self, name, breed): # The constructor
       self.name = name # Setting the name attribute
       self.breed = breed # Setting the breed attribute
# When we do this:
my_dog = Dog("Fido", "Poodle") # The __init__ method is automatically called
# It's like we're saying:
# 1. Create a new Dog object.
# 2. Run the __init__ method on this new object:
# - Set my_dog.name to "Fido"
# - Set my_dog.breed to "Poodle"

class Dog:
      def __init__(self, name="Unknown", breed="Mixed"):
       self.name = name
       self.breed = breed
dog1 = Dog() # name will be "Unknown", breed will be "Mixed"
dog2 = Dog("Rex") # name will be "Rex", breed will be "Mixed"
dog3 = Dog("Bella", "Labrador") # name will be "Bella", breed will be