# ============================
# TASK 1: Import math and sqrt
# ============================
import math
print("TASK 1 -> sqrt(2401):", math.sqrt(2401))


# ==========================================
# TASK 2: Import only log2 and compute value
# ==========================================
from math import log2
print("TASK 2 -> log2(1024):", log2(1024))


# ============================
# TASK 3: displayTwice function
# ============================
def displayTwice(msg):
    print(msg)
    print(msg)

displayTwice("Hello from TASK 3")
displayTwice("Python practice")


# ===========================================
# TASK 4: displayTwice with docstring + help
# ===========================================
def displayTwice_doc(msg):
    """Prints the given message twice."""
    print(msg)
    print(msg)

print("TASK 4 -> docstring:", displayTwice_doc.__doc__)


# ============================
# TASK 5: findMax function
# ============================
def findMax(a, b):
    """Finds the maximum of two values."""
    if a > b:
        maximum = a
    else:
        maximum = b
    return maximum

print("TASK 5 examples:", findMax(3, 5), findMax(10, 2), findMax(-1, -7))


# ====================================================
# TASK 6: multiply function (square if 1 argument only)
# ====================================================
def multiply(a, b=None):
    if b is None:
        return a * a
    return a * b

print("TASK 6:", multiply(5, 3), multiply(7), multiply(4))


# ================================================
# TASK 7: someFunc with positional and keyword args
# ================================================
def someFunc(x, y, z):
    print("x is", x)
    print("y is", y)
    print("z is", z)

someFunc(1, 2, 3)
someFunc(y=2, z=3, x=1)
someFunc(1, z=99, y=4)


# ============================
# TASK 8: Printing with sep
# ============================
print("TASK 8 examples:")
print("A", "B", "C", sep="-")
print("2025", "12", "10", sep="/")
print("word1", "word2", "word3", sep="***")


# =======================================
# TASK 9: calcAve using variable arguments
# =======================================
def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

print("TASK 9 examples:", calcAve(10, 20), calcAve(1, 2, 3, 4, 5), calcAve(100, 200, 300))


# =====================================
# TASK 10: hypot lambda expression
# =====================================
hypot = lambda a, b: math.sqrt(a * a + b * b)

print("TASK 10 -> type(hypot):", type(hypot))
print("TASK 10 -> hypot(3,4):", hypot(3, 4))


# =======================================
# TASK 11: to_seconds lambda (no default)
# =======================================
to_seconds = lambda hours, minutes: hours * 3600 + minutes * 60

print("TASK 11 examples:", to_seconds(0, 2), to_seconds(2, 0), to_seconds(1, 30))


# ===========================================================
# TASK 12: to_seconds lambda with default parameter (minutes)
# ===========================================================
to_seconds = lambda hours, minutes=0: hours * 3600 + minutes * 60

print("TASK 12 examples:", to_seconds(1), to_seconds(2), to_seconds(1, 30))


# ==========================================
# TASK: Key terms (definitions dictionary)
# ==========================================
definitions = {
    "Module": "A Python file that groups related code (functions, classes, variables).",
    "Python Standard Library": "Built-in collection of modules provided with Python.",
    "Formal Parameters": "Variable names in a function definition.",
    "Actual Parameters": "Values passed to a function when calling a function.",
    "Default Arguments": "Parameters that have default values.",
    "Keyword Arguments": "Arguments supplied by name when calling a function.",
    "Lambda Expression": "A small anonymous one-line function using lambda."
}

for key, value in definitions.items():
    print(f"{key} -> {value}")