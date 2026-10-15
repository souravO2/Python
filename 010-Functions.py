def hello_func():
    pass  # means we are not doing anything inside the func for now and i dont want any error for that.

print(hello_func)  # type and location
print(hello_func())  # none, coz the func has nothing in it

def hello_func():
    print("Hello Function!")

hello_func()

for i in range(5):
    hello_func()  # prints 5 times

def name_func():
    return "Sourav"

print(name_func().upper())

# making a string length counter
def str_length(str):
    count = 0
    for c in str:
        count += 1
    return count

print(str_length("Test"))  # 4
print(str_length("Sourav"))  # 6

def greeting_func(greeting, name="You"):
    return f"{greeting}, {name}."

print(greeting_func("Hi", "Sourav"))  # Hello, Sourav.
print(greeting_func("Hello"))  # Hello, You.

# positional keyword arguments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info(
    "Math", "Arts", name="Sourav", age=21
)  # tuple & dict / ('Math', 'Arts') {'name': 'Sourav', 'age': 21}

courses = ["ODE", "ECO", "Calc"]
info = {"name": "John", "age": 33}

student_info(
    courses, info
)  # (['ODE', 'ECO', 'Calc'], {'name': 'John', 'age': 33}) {} // thats not what we want

student_info(*courses, **info)  # ('ODE', 'ECO', 'Calc') {'name': 'John', 'age': 33}

# examples
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    """return true for leap year, false for non-leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """return number of days in that month in that year"""
    if not 1 <= month <= 12:
        return "Invalid Month"
    if month == 2 and is_leap_year(year):
        print(f"February of {year} is 29 days as its leap year")
        return 29
    return month_days[month]

print(is_leap_year(2022))  # false
print(days_in_month(2020, 2))  # 29 . leap year
