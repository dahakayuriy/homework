# 1
my_favorit_colors = ['blue', 'yellow', 'black', 'red', 'green']
print(my_favorit_colors[0], my_favorit_colors[-1])

# 2
months_of_year = ("January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December")
months_of_year[0] = "March"
print(months_of_year)

# 3
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
unification = set1.union(set2)
print(unification)
crossing = set1.intersection(set2)
print(crossing)
distinction = set1.difference(set2)
print(distinction)

# 4
name_surename = ['Yuriy', 'Murachov', 'Georg', 'Woodwind']
name_surename.sort()
print(name_surename)

# 5
even_numbers = set(range(2, 21, 2))
numbers_are_divisible_by_3 = set(range(3, 21, 3))
union_set = even_numbers.union(numbers_are_divisible_by_3)
print(union_set)

# 6
international = (2, 4, 'Yo', 'Hello', True, False)
print(international)

# 7
sum_of_numbers = [2, 4, 5, 3, 2, 6, 1]
i = 0
num = 0
while i < len(sum_of_numbers):
    num += sum_of_numbers[i]
    # print(num)
    i += 1
print(num)

# sum_of_numbers = [2, 4, 5, 3, 2, 6, 1]
# sum = sum(sum_of_numbers)
# print(sum)

# 8
different = ('banana', 'thing', 'beer', 'Cthulhu', 'egg', 'architects')
print(different[4])

# 9
words = ['apple', 'racoon', 'zombee', "dark souls", "queens of the stoun age"]
for word in words:
    if len(word) > 5:
        print(word)

# 10
students = [("Anna", 95), ("Alexey", 88),
            ("Maria", 92), ("Petro", 75), ("Olga", 98)]
highest_score = -1
name_of_the_best_student = ""
for name, score in students:
    if score > highest_score:
        highest_score = score
        name_of_the_best_student = name
print(name_of_the_best_student)

# 11
orders = [(1, 25.50), (2, 38.17), (3, 46.51)]
total_amount = 0
for order in orders:
    total_amount += order[1]
print(total_amount)

# 12
site_visit = [("192.168.0.1", "08:15:30"),
              ("192.168.0.2", "08:30:45"),
              ("192.168.0.3", "10:45:20"),
              ("192.168.0.4", "08:30:45"),
              ("192.168.0.5", "10:45:20")]
hours = []
number_of_visits = []
for ip, hour in site_visit:
    new_hour = hour

    if new_hour in hours:
        i = hours.index(new_hour)
        number_of_visits[i] += 1
    else:
        hours.append(new_hour)
        number_of_visits.append(1)
most_popular_time_of_day = hours[number_of_visits.index(max(number_of_visits))]
total_number_of_visits = sum(number_of_visits)
print("The most popular time of day to visit the site:", most_popular_time_of_day)
print("Total number of visits:", total_number_of_visits)


# 13
product_and_price = [('TV', 345.70), ('laptop', 256.17),
                     ('refrigerator', 312.70)]
tax_rate = 0.2

total_cost = 0

for product in product_and_price:
    name, cost = product
    cost_with_tax = cost * (1 + tax_rate)
    total_cost += cost_with_tax
print("Total cost of goods including tax:", total_cost)

# 14
order = [
    ("Customer1", [("Product1", 5), ("Product2", 3), ("Product3", 2)]),
    ("Customer2", [("Product1", 2), ("Product3", 1), ("Product4", 4)]),
    ("Customer3", [("Product2", 7), ("Product5", 2)]),

]

threshold = 100

price_of_product = {
    "Product1": 10.0,
    "Product2": 15.0,
    "Product3": 5.0,
    "Product4": 20.0,
    "Product5": 7.0
}

for customer, goods_quantity in order:
    total_amount = 0
    for product, quantity in goods_quantity:
        cost = price_of_product[product] * quantity
        total_amount += cost
    print(f"Client {customer}: Total amount = {total_amount}")
    if total_amount > threshold:
        print(f"Customer {customer} made an order for more than {threshold}")
