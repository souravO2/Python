nums = [1, 2, 3, 4, 5]

# for loop
for num in nums:
    print(num)

for num in nums:
    if num == 3:
        print("Found")
        break
    print(num)  # 1, 2, Found

for num in nums:
    if num == 3:
        print("Found")
        continue
    print(num)  # 1, 2, Found, 4, 5

# loop in loop
for num in nums:
    for letter in "abc":
        print(num, letter)  # 1 a, 1 b, 1 c...

for i in range(10):
    print(i)  # 0 to 9

for i in range(1, 11):
    print(i)  # 1 to 10

# while loop
x = 0

while x < 10:
    print(x)  # 0 to 9
    x += 1

x = 0
while x < 10:
    if x == 5:
        break
    print(x)  # 0 to 4
    x += 1

x = 10
while True:
    if x == 7:
        break
    print(x)  # 10 to 8
    x -= 1

