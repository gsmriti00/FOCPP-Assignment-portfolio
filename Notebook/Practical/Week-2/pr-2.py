# ---------------------------
# Task: Working with Variables
# ---------------------------
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

# Task: Calculate average
total = 98.2
count = 5
average = total / count
print("Average is", average)

# ---------------------------
# Task: Data-types
# ---------------------------
print(type(False))
print(type(1000))
print(type(100.111))
print(type("Hello"))
print(type(True))
print(type(100 / 5))
print(type(100 // 5))
print("ABC" * 10)

# ---------------------------
# Task: Built-in functions
# ---------------------------
name = input("Enter your name: ")
print("Hello there,", name)
print("Length of your name is", len(name))

# Input numeric values
age = int(input("Enter your age: "))
print("In one year, your age will be", age + 1)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Product of the two numbers is", num1 * num2)

# ---------------------------
# Task: Quotes and escape sequences
# ---------------------------
comment = 'I would have "thought" you knew better!'
print(comment)
print("This text includes characters such as '\\' '\"' and \"'\".\n")
print("\tThis is a new line that starts with a tab")
print("\t\tThis new line starts with two tabs")

# Triple quotes example
print("""This text spans three lines,
and includes both single ('),
and double quotes (").""")

# ---------------------------
# Task: Indexing and Slicing
# ---------------------------
surname = "Palin"
print("Third letter of surname:", surname[2])
# print(surname[9]) # will give error
print("Second to last letter:", surname[-2])
print("All except first letter:", surname[1:])
print("All except last letter:", surname[:-1])
print("Last three letters:", surname[-3:])

# ---------------------------
# Task: Lists
# ---------------------------
primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print("First four primes:", primes[:4])

names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
names[0:0] = ["Tim", "Bill"]
names.append("Brian")
names += ["Jacob"]
nums = [1, 2, 3] * 5
print("Names:", names)
print("Nums:", nums)
