num1 = ()
num2 = ()


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Division by zero is not allowed"
    return num1 / num2


num1 = float(input("Enter first number: "))
operation = input("Choose operation: ")
num2 = float(input("Enter second number: "))

if operation == "+":
    print(f"{num1}+{num2}={add(num1, num2)}")
elif operation == "-":
    print(f"{num1}-{num2}={subtract(num1, num2)}")
elif operation == "*":
    print(f"{num1}*{num2}={multiply(num1, num2)}")
elif operation == "/":
    print(f"{num1}/{num2}={divide(num1, num2)}")
else:
    print("Invalid operation")
