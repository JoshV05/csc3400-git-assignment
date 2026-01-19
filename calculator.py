import math
# Conflict test
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a**b

def square_root(a):
    if a < 0:
        return "Error: Negative square root"
    return math.sqrt(a)


print("Basic Calculator")
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power Of")
print("6. Square Root Of")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print("Result:", add(num1, num2))
elif choice == "2":
    print("Result:", subtract(num1, num2))
elif choice == "3":
    print("Result:", multiply(num1, num2))
elif choice == "4":
    print("Result:", divide(num1, num2))
elif choice == "5":
    print("Result:", power(num1, num2))
elif choice == "6":
    print("Result:", square_root(num1))
else:
    print("Invalid choice")

