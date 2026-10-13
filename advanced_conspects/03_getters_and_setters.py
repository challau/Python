# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     @property
#     def first_name(self):
#         l =  self.name.split(" ")
#         return l[0]
#     @first_name.setter
#     def first_name(self,first):
#         l = self.name.split(" ")
#         new_name = f"{first} {l[1]}"
#         self.name = new_name

# e = Employee("jack Doe",3455)
# # e.projects = 6
# print(e.first_name)
# e.first_name= "John"
# print(e.name)



# In Python OOP, getters and setters are methods used to access and modify the values of an object's attributes.

# Let's understand with a simple example.
# 1. What is a getter?
# A getter is a method used to read or retrieve a value.

# 2. What is a setter?
# A setter is a method used to update or change a value.

class Student:
    def __init__(self, name):
        self._name = name

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, new_name):
        self._name = new_name


s = Student("Uday")

print(s.name)       # Getter
s.name = "Kumar"    # Setter
print(s.name)       # Getter


# getter — @property
# print(s.name)
# Reads the current value: "Uday".

# Setter — @name.setter
# s.name = "Kumar"
# Changes the value to "Kumar".