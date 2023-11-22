# 1

try:

    num1 = int(input("Enter the first number, please: "))
    num2 = int(input("Enter the second number, please: "))

    result = num1 / num2
    print(result)

except ZeroDivisionError:
    print("Error: Division by zero!")

# 2
try:

    input_str = input("Enter the number: ")

    number = float(input_str)

    print(f"Entered number: {number}")

except ValueError:

    print("Error: Non-numeric data entered!")

# 3
my_list = [1, 2, 3, 4, 5]

try:

    index_to_access = 3
    value = my_list[index_to_access]

    print(f"Value at index {index_to_access}: {value}")

except IndexError:

    print("Error: Index exceeds list size!")

# 4


def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of division: {result}")

    except ZeroDivisionError:
        print("Error: Division by zero!")


divide_numbers(10, 2)
divide_numbers(8, 0)

# from imports import num_operations
# st = 'yo'
# st2 = 'gurt'
# res = str_concatenate(st, st2)
# print(res)
# n1 = 8
# n2 = 6
# res_num = num_operations(n1, n2)
# print(res_num)
