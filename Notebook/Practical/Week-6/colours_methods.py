colours = ["red", "green", "yellow", "blue", "red"]

print("Index of blue:", colours.index("blue"))
print("Count of red:", colours.count("red"))

copy_colours = colours.copy()
colours.append("black")

print("Original:", colours)
print("Copy:", copy_colours)
