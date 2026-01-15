# Ask user for a number
number = input("Enter a number: ")

# Convert the input to an integer
number = int(number)

# Print the number entered
print("The number entered was", number)

# Check if even or odd
if (number % 2) == 0:
    print("That is an even number")
else:
    print("That is an odd number")

# Check divisibility by 10
if number % 10 == 0:
    print("The number is divisible by 10")
else:
    print("The number is NOT divisible by 10")
