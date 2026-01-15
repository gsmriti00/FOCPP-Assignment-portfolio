# -------------------------------------------

# Expressions
print(45 + 20)
print(10 + 20 - 15)
print(10 * 5)
print(100 / 33)
print(100 // 33)
print(10 ** 2)
print(10 % 3)

# Operator Precedence
print(10 + 5 * 2)
print(10 - 5 * 10 + 5)
print(5 * 10 ** 2)
print((10 + 5) * 2)
print(10 - 5 * (10 + 5))
print((5 * 10) ** 2)
print(12 + (5 * 2 + 3))
print(12 + (5 * (2 + 3)))

# Syntax & Runtime Error Examples
# Uncomment one at a time to see the error
# 10 +
# print("Ten divided by zero is", 10/0)

# -------------------------------------------
# Week 2 Lab: Variables, Data-types, Lists
# -------------------------------------------

# Working with Variables
total = 100
print("The total is", total)
total += 99
print("The total is now", total)
total -= 1
print("The total is", total)
total *= 4
print("The total is", total)
total /= 2
print("The total is", total)

# Calculate Average
total = 98.2
count = 5
average = total / count
print("Average is", average)

# Data-types
print(type(False))
print(type(1000))
print(type(100.111))
print(type("Hello"))
print(type(True))
print(type(100 / 5))
print(type(100 // 5))
print("ABC" * 10)

# Built-in functions
name = input("Enter your name: ")
print("Hello there,", name)
print("Length of your name is", len(name))

age = int(input("Enter your age: "))
print("In one year, your age will be", age + 1)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Product of the two numbers is", num1 * num2)

# Strings and Escape Sequences
comment = 'I would have "thought" you knew better!'
print(comment)
print("This text includes characters such as '\\' '\"' and \"'\".\n")
print("\tThis is a new line that starts with a tab")
print("\t\tThis new line starts with two tabs")

# Triple Quotes
print("""This text spans three lines,
and includes both single ('),
and double quotes (").""")

# Indexing and Slicing
surname = "Palin"
print("Third letter of surname:", surname[2])
print("Second to last letter:", surname[-2])
print("All except first letter:", surname[1:])
print("All except last letter:", surname[:-1])
print("Last three letters:", surname[-3:])

# Lists
primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print("First four primes:", primes[:4])

names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
names[0:0] = ["Tim", "Bill"]
names.append("Brian")
names += ["Jacob"]
nums = [1, 2, 3] * 5
print("Names:", names)
print("Nums:", nums)

# -------------------------------------------
