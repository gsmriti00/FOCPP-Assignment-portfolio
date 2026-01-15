print("===== Boolean Expressions =====")
# Relational operators
print(10 < 100)
print(100 != 100)
print(50 >= 50)

# Using a variable
age = 25
print(age < 18)
print(age < 21)
print(age < 31)

# String comparisons
print("a" < "b")
print("b" < "a")
print("John" < "Terry")
print("john" < "Terry")

# List comparisons
print([1,2,3] < [1,2,3])
print([1,2,2] < [1,2,3])

# Mixed types
print(5 < 10.2)
print(5 == "5")

print("\n===== Logical Operators =====")
age = 30
print(age >= 18 and age <= 65)
print(age < 18 or age > 65)
print(not age > 18)
print((age >= 18 and age <= 65) and (not age == 30))

# Chaining operators
weight = 150
height = 150
print(100 < weight < 200)
print(131 < height < 160)

print("\n===== Membership Testing =====")
names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
print("Eric" in names)
print("Mark" not in names)
message = "Hello there, my name is John"
print("nam" in message)
print("xyz" in message)

print("\n===== If Statements =====")
age = 25
if 18 <= age <= 30:
    print("you are still young!")

if age > 100:
    print("you are very old")
else:
    print("you are not very old - yet")

if age > 100:
    print("you are very old")
elif age > 80:
    print("you are fairly old")
elif age > 40:
    print("you are middle aged")
elif age > 30:
    print("you are young adult")
else:
    print("you are not very old - yet")

print("\n===== Non-Boolean Conditions =====")
total = 50
if total != 0:
    print("Total is non-zero")
else:
    print("Total is zero")

# Example name input (commented out so it doesn't stop the script)
# name = input("Enter your name: ")
# if name != "":
#     print("Your name is", name)
# else:
#     print("Name not entered")

print("\n===== Ternary Operator =====")
age = 25
print("you are an adult" if age >= 18 else "you are not an adult, yet!")

print("\n===== While Loop =====")
count = 5
while count > 0:
    print("Countdown is", count)
    count -= 1

print("\n===== For Loop over a List =====")
names = ["Alice", "Bob", "Charlie", "Diana"]
for name in names:
    print(name)

print("\n===== For Loop with range() =====")
for n in [2, 4, 6, 8, 10]:
    print(f"{n} to the power of {n} = {n**n}")

print("\n===== Break in a Loop =====")
numbers = [10, 20 , 30, 90, 200, 30, 22, 11]
total = 0
for num in numbers:
    if num > 100:
        break
    total += num
    print("Running total:", total)
else:
    print("all numbers processed")

print("\n===== Continue in a Loop =====")
grades = [20, 50, 43, 33, 90, 15]
pass_mark = 40
passes = 0
total = 0
for grade in grades:
    if grade < pass_mark:
        continue
    passes += 1
    total += grade
print("average pass mark was", total/passes)
