name = "saifur rahman sourav"
print("Hello World!")
print(f"This is {name.title()} signing in on python.")

message1 = "This is a message."
message2 = "This is also a message"
print(message1.upper(), end=" ")  # lowercase , uppercase , titlecase
print(message2.lower())  # the end makes the line in oneline

print("Languages:\nPython\nC\nJavaScript")  # new line \n

print("Languages:\n\tPython\n\tJavaScript")  # new line and a tab

fav_lang = "Python   "
print(
    fav_lang.strip()
)  # it trims the extra whitespace, it also has lstrip() , rstrip()

msg = "One of python's strength is it's diverse community."
print(msg)

print(
    'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
)

# type casting
x = str(3)  # x will be "3"
y = int(3.1)  # y will be 3
z = float(3)  # z will be 3.0

# type checking
x = str(3)
print(type(x))
y = int(3)
print(type(y))

# many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# one value in multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
