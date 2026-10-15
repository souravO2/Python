if True:
    print("Conditional was true.")

language = "Java"

if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
else:
    print("No Match")

# match is like switch of c
day = 2
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case _:
        print("Invalid day")

user = "Admin"
logged_in = False

if user == "Admin" and logged_in:  # its like &&
    print("Admin page.")  # bad creds
else:
    print("bad creds")

if not logged_in:
    print("Please Log In.")  # please log in
else:
    print("Welcome")

# difference in is and ==
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # true, it just cares about value
print(a is b)  # false, as they are not same memory
b = a
print(a is b)  # true, b points to a , so same memory

# False values - False, None, 0, “”, (), [], {}
