# Beckett Pizza Plaza 4-for-3 Offer

print("Beckett Pizza Plaza 4-for-3 Offer")
print("=================================")

# Collect four pizza prices
pizza1 = pizza2 = pizza3 = pizza4 = 0.0

while True:
    try:
        pizza1 = float(input("Enter Price of Pizza #1: "))
        if pizza1 <= 0:
            print("Please enter a valid price!")
        else:
            break
    except ValueError:
        print("Please enter a valid price!")

while True:
    try:
        pizza2 = float(input("Enter Price of Pizza #2: "))
        if pizza2 <= 0:
            print("Please enter a valid price!")
        else:
            break
    except ValueError:
        print("Please enter a valid price!")

while True:
    try:
        pizza3 = float(input("Enter Price of Pizza #3: "))
        if pizza3 <= 0:
            print("Please enter a valid price!")
        else:
            break
    except ValueError:
        print("Please enter a valid price!")

while True:
    try:
        pizza4 = float(input("Enter Price of Pizza #4: "))
        if pizza4 <= 0:
            print("Please enter a valid price!")
        else:
            break
    except ValueError:
        print("Please enter a valid price!")

# Calculate total and discount
prices = [pizza1, pizza2, pizza3, pizza4]
total_price = sum(prices) - min(prices)
discount = round((min(prices) / sum(prices)) * 100)

# Show result
print(f"\nOrder Total is £{total_price:.2f}, a fabulous discount of {discount}%!")