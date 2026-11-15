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


num1 = 10
num2 = 0
print(divide(num1, num2))
