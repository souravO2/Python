name = "saifur rahman sourav"
print(name.title())
print(name.lower())
print(name.upper())

multiline = """This 
is a multiline text"""
print(multiline)

print(len(name))  # 20
print(name[0])  # s
print(name[0:6])  # ending is exclusive

print(name.count("s"))  # 2

print(name.find("rahman"))  # 7
print(name.find("r"))  # 5, the first r

# replace replaces but doesnt change the main string
print(name.replace("sourav", "aknda"))  # saifur rahman aknda
print(name)  # saifur rahman sourav

# concatenation
greeting = "Hello"
whom = "sourav"

noSpace = greeting + whom
print(noSpace)  # Hellosourav (no space)

space = greeting + " " + whom
print(space)  # Hello sourav

# best way
formatting = f"{greeting} {whom.title()}"  # prev : "{} {}".format(greeting,whom)
print(formatting)  # Hello Sourav


# print without a new line
print("Hello World!", end=" ")
print("This will be printed on the same line.")
