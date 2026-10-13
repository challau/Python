
'''
class Employee:
    company = "HP"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    # Instance method (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # static method does not need a self
    @staticmethod
    def sum(a,b):
        return a + b

    # class Methods
    @classmethod
    def print_company(cls):
        print(cls.company)
    
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company
        

e1 = Employee("Jack", 3455)
e2 = Employee("Jill", 34553)
# # print(Employee.company)
# e1.print_info()
# e2.print_info()

# print(e2.sum(5, 23))
print(Employee.company)
e1.change_company("Acer")
print(Employee.company)

'''

class Student:
    school = "DSU"  # Class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 1. Instance method
    def show(self):
        print(self.name, self.age)

    # 2. Class method
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # 3. Static method
    @staticmethod
    def is_adult(age):
        return age >= 18


s1 = Student("Uday", 20)

# Instance method
s1.show()

# Class method
Student.change_school("ABC College")
print(Student.school)

# Static method
print(Student.is_adult(20))
