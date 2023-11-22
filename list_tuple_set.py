# # 4 Використовуючи цикл for, вивести числа від 1 до 5.
# for number in range(1, 6):
#     print(number)

# # 5 Використовуючи цикл while, вивести парні числа від 2 до 10.
# number = 2
# while number <= 10:
#     print(number)
#     number += 2

# number = 10
# while number >= 2:
#     if number % 2 == 0:
#         print(number)
#     number -= 1

# #7
# num = 1
# while num <= 5:
#     for num in range(1, 6):
#         print(num)
#         num += 1

# 1
# clients_name = input("Enter your name please: ")
# soup = 4.54
# juice = 5.45
# beer = 2.12
# hamburger = 3.45
# order = []

# 2
# responses = []
# while True:
#     question = input("Питання (або 'кінець' для завершення опитування): ")
#     if question == 'кінець':
#         break

#     answer = input("Ваша відповідь: ")
#     responses.append((question, answer))

# print("Результати опитування:")

# 1
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# 2
sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
print(sum)

# 3
counter = 0
num = 1
while num <= 100:
    if num % 5 == 0:
        counter += 1
    num += 1
print(counter)

# 4
correct_password = 'secret'
entered_password = input("Please enter the password: ")

while entered_password != correct_password:
    print("This is wrong password!")
    entered_password = input("Please enter the password: ")
print("Password has been accepted. You are now logged in.")

# 5
list_of_numbers = [2, 4, 8, 16, 88, 104, 99, 5]
i = 0
while i < len(list_of_numbers):
    num = list_of_numbers[i]
    print(num)
    i += 1

