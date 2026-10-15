import sys

sys.path.append("path of the file")  # imports from anywhere, not recommended , use python path env variable

import Modules as mm  # imports the whole file
from Modules import find_index, test

courses = ["History", "Math", "Physics", "CompSci"]

index = mm.find_index(courses, "Math")  # 1
index = find_index(courses, "Physics")
print(index)  # 2
print(test)

print(sys.path)  # gives the path/ directory of the file in client system
