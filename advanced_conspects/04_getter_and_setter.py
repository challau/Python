class Student:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Age must be positive!")


s = Student(20)

print(s.age)  # 20
s.age = -5    # Invalid
print(s.age)  # 20