import json


json_str = '{"id":235, "brand":"Nike", "qty":84, "status": {"ifForeSale":true}}'

sneakers = json.loads(json_str)
sneakers['a'] = 4

print(type(sneakers))
print(sneakers)

print(sneakers['brand'])

# file_path = 'txt_files/virtual_machines.json'
# with open(file_path, 'r') as file:
#     data_dict = json.load(file)

# print(data_dict)
json_from_dict = json.dumps(sneakers, indent=2)
print(json_from_dict)
print(type(json_from_dict))

#
with open('proba.json', 'w+') as file:
    file.write(
        '{"id":235, "brand":"Nike", "qty":84, "status": {"ifForeSale":true}}')

with open('proba.json', 'r') as file:
    content = file.read()
    data = json.loads(content)
print(data)
data['boo'] = 'ghost'
with open('proba.json', 'w') as file:
    json.dump(data, file, indent=2)

print(data)

print(bool)
print(dir(bool))
