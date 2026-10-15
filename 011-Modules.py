import random  # standard library
import math
import datetime
import calendar
import os  # operating system module

# import antigravity # python joke, opens https://xkcd.com/353/ webpage

courses = ["History", "Math", "Physics", "CompSci"]

random_course = random.choice(courses)

print(random_course)  # pick random from courses everytime

print(math.radians(90))  # 1.57 / degree to radian / pi/2
print(math.sin(math.radians(90)))  # 1.0

today = datetime.date.today()
print(today)  # date / year-month-day

print(calendar.isleap(2020))  # true
print(calendar.isleap(2026))  # false

print(os.getcwd())  # current working directory

# dunder -> double underscore __
print(os.__file__)  # location of the file in my file system
