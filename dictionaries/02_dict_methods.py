# marks = {"harry": 34, "jack": 45, "lily": 94}

# print(marks.keys()) dict_keys(['harry', 'jack', 'lily'])
# print(marks.values()) dict_values([34, 45, 94])




student = {"name": "alice", "age": 21,"grade":"A"} 


print(student.keys()) #dict_keys(['name', 'age', 'grade'])
print(student.values()) #dict_values(['alice', 21, 'A'])
print(student.items()) #dict_items([('name', 'alice'), ('age', 21), ('grade', 'A')])

student.pop("age") # removes "age" key
print(student) #{'name': 'alice', 'grade': 'A'}
student.clear() # empties dictionary
print(student) # {}



