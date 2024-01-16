import sys

try:
    x = int(input("x: "))
except ValueError:
    print("Error: Invaild Input. Enter a number for x.")
    sys.exit(1)

try:
    y = int(input("y: "))
except ValueError:
    print("Error: Invaild Input. Enter a number for y.")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1) # Exit the program with an Error Code 1 meaning an error occured

print(f"{x} / {y} = {result}")

