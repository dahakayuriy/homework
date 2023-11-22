# 1
phone_directory = {}

phone_directory["Stepan"] = "123-456-789"
phone_directory["Maria"] = "987-654-321"
phone_directory["Petro"] = "555-555-555"
print(phone_directory)

name = "Maria"
if name in phone_directory:
    phone_number = phone_directory[name]
    print(f"Phone number for {name}: {phone_number}")
else:
    print(f"{name} is not found in the phone book")

new_name = "Anna"
new_phone_number = "111-222-333"
phone_directory[new_name] = new_phone_number

print("Updated phone book:")
for name, phone_number in phone_directory.items():
    print(f"{name}: {phone_number}")

# a = [121, 384, 23, 45, 456, 173, 281, 45]
# a.sort(reverse=True)
# print(a)
# b = a[:]
# print(b)
# v = a.copy()
# print(id(v), id(a))
# print(type(v))
# res = a.count(384)
# print(res)

# list = [1, 'a', 4.5, True, ['b']]
# list.pop(2)
# print(len(list))
# list.reverse()
# print(list)
# list2 = [2, '2']
# list.extend(list2)
# print(list, list2)


# 2
input_string = 'ababagalamaga'
letter_count = {}
for char in input_string:
    if char.isalpha():
        char = char.lower()
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
letter_to_count = 'a'
count = letter_count.get(letter_to_count, 0)
print(f"Number of letters '{letter_to_count}' in the line: {count}")
print(letter_count)

# 3
prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}
product_name = 'banana'
if product_name in prices:
    price = prices[product_name]
    print(f"Product price '{product_name}': {price}")
else:
    print(f"Product '{product_name}' not found in the price dictionary.")
new_product_name = 'tomato'
new_product_price = 2.5
prices[new_product_name] = new_product_price
print(prices)

# 4
names_to_ages1 = {
    "Petro": 30,
    "Maria": 25,
    "Samson": 35
}

names_to_ages2 = {
    "Anna": 28,
    "Petro": 32,
    "Lesya": 29
}
name_to_find = 'Petro'
if name_to_find in names_to_ages1:
    age1 = names_to_ages1[name_to_find]
    print(f"{name_to_find}: {age1} years in the first dictionary")
else:
    print(f"The name '{name_to_find}' was not found in the first dictionary")
if name_to_find in names_to_ages2:
    age2 = names_to_ages2[name_to_find]
    print(f"{name_to_find}: {age2} ages in the second dictionary")
else:
    print(f"The name '{name_to_find}' was not found in the second dictionary")

combined_dict = {}
for name, age in names_to_ages1.items():
    combined_dict[name] = age

for name, age in names_to_ages2.items():
    if name in combined_dict:
        pass
    else:
        combined_dict[name] = age
print("Common dictionary:")
print(combined_dict)

# 5
prices = {
    "banana": 4,
    "yabluko": 2,
    "orange": 1.5,
    "pear": 3
}

shopping_list = [
    ("banana", 3),
    ("yabluko", 5),
    ("pear", 2)
]

total_cost = 0
for item, quantity in shopping_list:
    if item in prices:
        item_price = prices[item]
        cost = item_price * quantity
        total_cost += cost
        print(
            f"Purchased {item} (price per unit: {item_price} UAH) x {quantity} pcs = {cost} UAH")
    else:
        print(f"The item '{item}' is not found in the price dictionary.")
print(f"Total cost of purchases: {total_cost} UAH")

# 6
student_scores = {
    "Dyma": [85, 90, 78, 92, 88],
    "Maria": [76, 88, 90, 82, 94],
    "Petro": [92, 80, 87, 91, 89]
}
total_average = 0
total_students = len(student_scores)
for student, scores in student_scores.items():
    average_score = sum(scores) / len(scores)
    print(f"Average score for {student}: {average_score}")
    total_average += average_score

if total_students > 0:
    total_average /= total_students
    print(f"Total average score for all students: {total_average}")
else:
    print("The dictionary with grades is empty.")

# function



