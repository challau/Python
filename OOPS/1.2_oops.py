# class : class is a blueprint or a template. Eg. form for an exam that contains name,age, eletives, father's name etc


# object : specific instance created from the template (class) . Eg. from which contains the data for john Doe

class Employee:
    company = "Hp"
    def get_salary(self): # self is important here because self is a way to refernece the object of the class which is being created
        print(self)
        return 3400


e1 = Employee() # an object of class employee is created here
print(e1.get_salary()) # Employee's get salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)