# List can be used as Array
# however python has array module too, but it must be imported from NumPy library

courses = [
    "DSA",
    "Vector & Tensor",
    "Multi-variable Calculus",
    "ODE",
    "Statics",
    "Economics",
]

print(courses)  # whole list
print(len(courses))  # 6
print(courses[2])  # Multi-var calc
print(courses[len(courses) - 1])  # eco
print(courses[-1])  # eco // last item

print(courses[3:-1])  # ode, statics
print(courses[:2])  # dsa, vector
print(courses[-2:])  # statics, eco

# adding at end
courses.append("Python")
print(courses)  # added python at end

# adding at index
courses.insert(0, "JavaScript")
print(courses)  # added js at 0

artsCourses = ["Arts", "Human Relations"]
courses.insert(0, artsCourses)  # inserts the list inside the list (list inside list)
print(courses)  # [['Arts,'HR'],...]

courses.extend(artsCourses)  # adds the list's value at end
print(courses)

courses.remove("Statics")
print(courses)

popped = courses.pop()  # removes the last value
print(popped)  # HR

poppedArray = courses.pop(0)  # removes the first array that we were having
print(poppedArray)

courses.reverse()  # reverses the list

courses.sort()  # ascending order for char
print(courses)

nums = [4, 5, 6, 321, 3, 5, 745, 12]
nums.sort()  # ascending order
print(nums)

nums.sort(reverse=True)  # descending order
print(nums)

# all of these methods alters the original list

numbers = [3, 6, 21, 1, 3, 45, 6, 3, 56]
sortedNumbers = sorted(numbers)  # does not alters the original
print(sortedNumbers)
print(min(numbers))  # 1
print(max(numbers))  # 56
print(sum(numbers))  # 144

print(numbers.index(1))  # 3 // gives the index of 1

print(6 in numbers)  # true

print(9 in numbers)  # false

for item in numbers:  # gives all list values one by one in newline
    print(item)  # tabbing is must

for index, course in enumerate(numbers):  # gives access to the index
    print(index, course)

for index, course in enumerate(numbers, start=1):  # starts indexing from 1
    print(index, course)

# list to string
courses_str = ", ".join(courses)  # comma separated string from list
print(courses_str)

# string to list
new_list = courses_str.split(", ")
print(new_list)


#Empty Lists
empty_list = []
empty_list = list()
