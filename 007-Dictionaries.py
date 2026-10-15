# its like js object

student = {
    "name": "Sourav",
    "roll": "04",
    "age": 25,
    "courses": ["Math", "CompSci"],
}

print(student)

print(student["name"])  # Sourav
print(student["courses"])  # ['Math', 'CompSci']

print(student["phone"])  # error
print(student.get("phone"))  # none
print(student.get("phone"), "Not Found")  # Not Found

student["location"] = "Sylhet"
print(student.get("location"))  # Sylhet

student["age"] = 21
print(student.get("age"))  # 21

student.update({"name": "Ornab", "age": 18, "phone": "0152323"})
print(student)
# {
#     "name": "Ornab",
#     "roll": "04",
#     "age": 18,
#     "courses": ["Math", "CompSci"],
#     "location": "Sylhet",
#     "phone": "0152323",
# }

del student["location"]  # deletes location
print(student)

popped = student.pop("roll")
print(popped)  # 04

print(len(student))  # 4

print(student.keys())  # dict_keys(['name', 'age', 'courses', 'phone'])
print(student.values())  # dict_values(['Ornab', 18, ['Math', 'CompSci'], '0152323'])
print(
    student.items()
)  # dict_items([('name', 'Ornab'), ('age', 18), ('courses', ['Math', 'CompSci']), ('phone', '0152323')])

# looping
for key in student:
    print(key)  # name age courses phone

for key,value in student.items():
  print(key,value) # key value pairs
  
