# tuple is list that is immutable

list_1 = ["History", "Math", "Physics"]
list_2 = list_1

print(list_1)  # ['History', 'Math', 'Physics']
print(list_2)  # ['History', 'Math', 'Physics']

list_1[0] = "Chemistry"

print(list_1)  # ['Chemistry', 'Math', 'Physics']
print(list_2)  # changed to ['Chemistry', 'Math', 'Physics']

# immutable
tuple_1 = ("Drawing", "Arts", "Craft")
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = "Killing"  # tuple doesnt support assigning

print(tuple_1)  # will give error

# Empty Tuples
empty_list = ()
empty_list = tuple()
