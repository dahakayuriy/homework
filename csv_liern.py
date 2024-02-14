import csv
# fruits_data = [
#     ["Name", "Quantity", "Price"],
#     ["Apple", 10, 2.5],
#     ["Banana", 8, 1.8],
#     ["Orange", 12, 3.0]
# ]

# csv_file_path = 'fruits.csv'
# with open(csv_file_path, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(fruits_data)

# with open(csv_file_path, 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# new_fruit = ["Pear", 15, 2.2]

# with open(csv_file_path, 'a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(new_fruit)

# total_cost = 0

# with open(csv_file_path, 'r') as file:
#     reader = csv.reader(file)
#     next(reader)  # Пропускаємо заголовок
#     for row in reader:
#         quantity = int(row[1])
#         price = float(row[2])
#         total_cost += quantity * price

# print(f"The total cost of all fruits: {total_cost}")
# print()

# with open(csv_file_path, 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
# print()

# with open(csv_file_path, 'r', newline='') as file:
#     reader = csv.reader(file)

#     for i in range(5):
#         row = next(reader, None)
#         if row:
#             print(row)

csv_file_path2 = 'employees.csv'
new_csv_file_path = 'selected_employees.csv'

headers = ['Name', 'City', 'Age', 'Department']


employees_data = [
    {'Name': 'John Doe', 'City': 'New York', 'Age': 30, 'Department': 'IT'},
    {'Name': 'Jane Smith', 'City': 'Los Angeles', 'Age': 25, 'Department': 'HR'},
    {'Name': 'Bob Johnson', 'City': 'Chicago', 'Age': 35, 'Department': 'Finance'},
    {'Name': 'Alice Brown', 'City': 'New York', 'Age': 28, 'Department': 'IT'},
    {'Name': 'Charlie Davis', 'City': 'Los Angeles',
        'Age': 40, 'Department': 'Marketing'}
]

with open(csv_file_path2, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(employees_data)
print(f"CSV the file was created by the path: {csv_file_path2}")

target_city = 'New York'

employees = []
with open(csv_file_path2, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        employees.append(row)
employees_in_target_city = [
    employee for employee in employees if employee['City'] == target_city]
for employee in employees_in_target_city:
    print(employee)

ages = [int(employee['Age']) for employee in employees]
average_age = sum(ages) / len(ages)
print(f"Average age of employees: {average_age}")

departments_count = {}
for employee in employees:
    department = employee['Department']
    if department in departments_count:
        departments_count[department] += 1
    else:
        departments_count[department] = 1
print("Number of employees in each department:")
for department, count in departments_count.items():
    print(f"{department}: {count} employees")

# add new employee
new_employee = {'Name': 'Eva Green', 'City': 'Paris',
                'Age': 28, 'Department': 'Marketing'}

with open(csv_file_path2, 'a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=new_employee.keys())
    writer.writerow(new_employee)

# delete employee
target_name = 'John Doe'
employees2 = []
with open(csv_file_path2, 'r') as file:
    reader = csv.DictReader(file)
    employees2 = [row for row in reader]
employees2 = [
    employee for employee in employees2 if employee['Name'] != target_name]

with open(csv_file_path2, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)

    writer.writeheader()
    writer.writerows(employees2)

# Створити та записати новий CSV файл лише з обраними полями
selected_headers = ['Name', 'Age', 'Department']
with open(new_csv_file_path, 'w', newline='') as new_file:
    writer = csv.DictWriter(new_file, fieldnames=selected_headers)
    writer.writeheader()

    with open(csv_file_path2, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            selected_data = {key: row[key] for key in selected_headers}
            writer.writerow(selected_data)

print(f"Selected CSV file was created at the path: {new_csv_file_path}")
