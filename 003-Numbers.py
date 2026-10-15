num = 3
print(type(num))  # int

num = 3.14
print(type(num))  # float

num = 5j  # j represents imaginary i
print(type(num))  # complex

print(3 + 5)  # 8
print(3 - 5)  # -2
print(3 * 5)  # 15
print(3 / 5)  # 0.6
print(3 // 2)  # 1
print(3**5)  # 243
print(3 % 5)  # 3

print(abs(-3.14))  # 3.14

print(round(3.768, 2))  # 3.77

# literally numbers?
num1 = "100"
num2 = "200"
print(num1 + num2)  # 100200 // not number

# string to integers // type casting
print(int(num1) + int(num2))  # 300
