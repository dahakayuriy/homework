# 1
employee_name = 'Dmytro'
employee_surename = 'Tereshyuk'
firm = "@kobzar.com"
print(
    f"Your new mail will be as follows: {employee_name}.{employee_surename}{firm}")
print(
    f"Your new mail will be as follows: {employee_name[0] + employee_name[1] + employee_name[2]}{employee_surename[0]}{firm}")
# 2
customer_age = 19

if customer_age > 18:
    print("You can buy alcoholic beverages")
elif customer_age > 14 and customer_age < 18:
    print("You can buy only energetics")
else:
    print("You can buy anything")

# 3
data = ";yu7i9om0iymn%"
if data[0] == ';' and data[-1] == '%':
    change = data[1:-1]
    print(change)

# 4
new_data = "yu&7i9om&0iym&n"
new_data = new_data.replace('&', '')
print(new_data)

# 5
user_age = 35
user_salary = 500
user_job = True

if user_age > 16 and user_salary > 300 and user_job == True:
    print("You can take out a loan from a bank")

else:
    print("You cant take out a loan from a bank")
