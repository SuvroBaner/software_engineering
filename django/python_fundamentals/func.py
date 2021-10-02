def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator(operation, n1, n2):
    return operation(n1, n2)

print(calculator(add, 5, 10))
print(calculator(subtract, 5, 10))
print(calculator(multiply, 5, 10))
print(calculator(divide, 5, 10))


print(calculator(lambda a, b: a + b, 10, 20))
print(calculator(lambda a, b: a - b, 20, 10))

print("\n\n")

num_list = [0, 1, 2, 3, 4, 5]

double_list = map(lambda n: n * 2, num_list)
print(list(double_list))
print(num_list)

even_list = filter(lambda n: n % 2 == 0, num_list)
print(list(even_list))

def factorial(n):
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(4))