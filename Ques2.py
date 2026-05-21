# Write a function for basic math operations like add multiply substract divide and use this in your program, take 2 number input from user.
# Function Definitions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not possible"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition =", add(num1, num2))
print("Subtraction =", subtract(num1, num2))
print("Multiplication =", multiply(num1, num2))
print("Division =", divide(num1, num2))