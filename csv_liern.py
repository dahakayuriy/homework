import csv
fruits_data = [
    ["Name", "Quantity", "Price"],
    ["Apple", 10, 2.5],
    ["Banana", 8, 1.8],
    ["Orange", 12, 3.0]
]

csv_file_path = 'fruits.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(fruits_data)

with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

new_fruit = ["Pear", 15, 2.2]

with open(csv_file_path, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(new_fruit)

total_cost = 0

with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаємо заголовок
    for row in reader:
        quantity = int(row[1])
        price = float(row[2])
        total_cost += quantity * price

print(f"The total cost of all fruits: {total_cost}")
print()

with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
