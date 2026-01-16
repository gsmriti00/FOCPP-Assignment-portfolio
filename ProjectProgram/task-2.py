# Task 2: Password Verification Program

print("Password Security Check")

# Prompt user to enter password
password = input("Enter your password: ")

# Check password length
if len(password) < 9:
    print("\nPassword too short.")
    exit()  # Exit the program if password is too short

# Ask for three random letters by their positions
# Note: positions are 1-based for the user, but 0-based in Python
positions = [4, 8, 3]  # Example positions (can be changed if needed)

for pos in positions:
    # Prompt user for the letter at the specified position
    try:
        letter = input(f"Enter letter at position {pos}: ")
        if letter == password[pos - 1]:
            print("Correct")
        else:
            print("Security check failed.")
            exit()  # Exit immediately if any letter is wrong
    except IndexError:
        # In case the user enters a position beyond password length
        print("Invalid position.")
        exit()

# If all letters are correct
print("Security check passed.")