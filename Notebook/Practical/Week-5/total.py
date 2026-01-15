import sys

# If no extra arguments were passed (only program name)
if len(sys.argv) == 1:
    print("no arguments were provided")
else:
    count = len(sys.argv)
    total = 0.0
    num_args = count - 1  # exclude program name

    # Sum all numeric arguments
    while count > 1:
        count -= 1
        total += float(sys.argv[count])

    print("Total is", total)
    print("Average is", total / num_args)
