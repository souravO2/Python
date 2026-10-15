# A set is a collection which is unordered, unchangeable*,unindexed and do not allow duplicate values.
# Set items are unchangeable, but you can remove items and add new items

courses = {"History", "Math", "Physics", "CompSci", "Math"}

print(
    courses
)  # {'Math', 'Physics', 'CompSci', 'History'} // the order of value changes on each execution and removes the duplicates

print("Math" in courses)  # true // set does this quickly

art_courses = {"Arts", "Math", "Design"}

print(courses.intersection(art_courses))  # {'Math'}

print(courses.difference(art_courses))  # {'History', 'CompSci', 'Physics'}

print(courses.union(art_courses))  # union of both courses but no duplicate

# Empty Sets
empty_list = {}  # This creates an empty dict/object
empty_list = set()
