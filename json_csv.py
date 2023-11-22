import json
a = "Hello, World."
b = "I'm learning Python."
c = "How are you?"
with open('example.txt', 'a') as file:
    # Adding a new line to the file

    file.write('\n' + a)
    file.write('\n' + b)
    file.write('\n' + c)

print("The new line was successfully added to the file.")

# # 2
# lines = []
# while True:
#     line = input("Введіть рядок тексту (або введіть 'stop' для завершення): ")
#     if line.lower() == 'stop':
#         break
#     lines.append(line)

# # Запис у файл
# with open('output.txt', 'w') as file:
#     for line in lines:
#         file.write(line + '\n')

# print("Рядки були успішно записані у файл output.txt.")

# 3
# Creating a JSON object
book_info = {
    "title": "The Great Gatsby",
    "author": "Francis Scott Fitzgerald",
    "year_of_publication": 1925

}

# Write to file
with open('book.json', 'w') as json_file:
    json.dump(book_info, json_file, indent=2)

print("The book information was saved to the file 'book.json'.")

# Reading information from a file
with open('book.json', 'r') as json_file:
    loaded_book_info = json.load(json_file)

# Displaying information on the screen
print("\nInformation about the book from the file 'book.json':")
print(f"Title: {loaded_book_info['title']}")
print(f"Author: {loaded_book_info['author']}")
print(f"Year of publication: {loaded_book_info['year_of_publication']}")

# Print the number of books in the list (in this case, 1)
print("\nNumber of books in the list:", len([loaded_book_info]))

# 5
json_file_path = 'txt_files/virtual_machines.json'

# with open(json_file_path, 'r') as file:
#     virtual_machines = json.load(file)
#     print(virtual_machines)
# new_vm = {'hello': 'world!'}
# virtual_machines.append(new_vm)

# with open(json_file_path, 'w') as file:
#     json.dump(virtual_machines, file, indent=2)
#     print(virtual_machines)

# 6
json_file_path = 'txt_files/virtual_machines.json'
with open(json_file_path, 'r') as file:
    data = json.load(file)


target_region = "Europe (Germany)"
vm_in_region = [vm for vm in data if vm.get("region") == target_region]
print(vm_in_region)
print()
#

vms_with_more_than_16gb_memory = [
    vm for vm in data if "memory" in vm and int(vm["memory"][:-2]) > 16]
print(vms_with_more_than_16gb_memory)
#

# new_vm = {
#     "name": "VM51",
#     "processor": "Intel Core i5",
#     "memory": "12GB",
#     "storage": "1TB",
#     "location": "Paris, France Cloud Tower",
#     "region": "Europe (France)",
#     "provider": "Provider ZZ"
# }
# print()

# data.append(new_vm)
# with open(json_file_path, 'w') as file:

#     json.dump(data, file, indent=2)


# print(data)
#

with open(json_file_path, 'r') as file:
    data = json.load(file)
vms_in_russia = [vm for vm in data if vm.get("region") == "Europe (Russia)"]
for vm in vms_in_russia:
    vm["region"] = "Europe (Germany)"
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=2)
#
