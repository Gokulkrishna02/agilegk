import sys

# Ensure argument is passed
if len(sys.argv) < 2:
    print("Error: Please provide a number as argument")
    sys.exit(1)

try:
    num = int(sys.argv[1])

    if num < 0:
        print("Error: Factorial is not defined for negative numbers")
        sys.exit(1)

    fact = 1
    for i in range(1, num + 1):
        fact *= i

    print(f"Factorial of {num} is {fact}")

except ValueError:
    print("Error: Please enter a valid integer")
