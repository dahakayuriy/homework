# # 1
# employee_name = input("Enter your name please: ")
# employee_surename = input("Enter your surename please: ")
# firm = "@kobzar.com"
# print(
#     f"Your new mail will be as follows: {employee_name}.{employee_surename}{firm}")
# print(
#     f"Your new mail will be as follows: {employee_name[0] + employee_name[1] + employee_name[2]}{employee_surename[0]}{firm}")
# # 2
# customer_age = int(input("Enter your age please: "))

# if customer_age > 18:
#     print("You can buy alcoholic beverages")
# elif customer_age > 14 and customer_age < 18:
#     print("You can buy only energetics")
# else:
#     print("You can buy anything")

# # 3
# data = ";yu7i9om0iymn%"
# if data[0] == ';' and data[-1] == '%':
#     change = data[1:-1]
#     print(change)

# # 4
# new_data = "yu&7i9om&0iym&n"
# new_data = new_data.replace('&', '')
# print(new_data)

# # 5
# user_age = int(input("Enter your age please: "))
# user_salary = int(input("Enter your salary please: "))
# user_job = input("Do you have a job: ")

# if user_age > 16 and user_salary > 300 and user_job.lower() == 'yes':
#     print("You can take out a loan from a bank")

# else:
#     print("You cant take out a loan from a bank")

# # 6
# registration_age = int(input("Enter your age please: "))
# registration_email = input("Enter the name of your mail: ")
# registration_password = input("Enter the password of your mail: ")

# if registration_age < 18:
#     print("You are too young to register on the site")
# elif '@' not in registration_email or '.' not in registration_email:
#     print("Invalid email address")
# elif len(registration_password) < 8:
#     print("The password is too short. The password must contain at least 8 characters.")
# else:
#     print("Registration successful. Welcome to the site!")

# # 7
# count = 0
# while count < 5:
#     response = input("Would you like us to call you back? (yes/no): ")
#     if response.lower() == "yes":
#         print("Thank you! Our operator will contact you.")
#         break
#     elif count == 4:
#         print("Okay, we'll leave you alone. Happy shopping!")
#     else:
#         print("Thank you for your reply.")
#     count += 1

# # 8
# num_customers = input("Enter the number of buyers: ")

# if num_customers.isdigit():
#     num_customers = int(num_customers)

#     pens = 0
#     rulers = 0
#     for customer_number in range(1, num_customers + 1):
#         if customer_number % 3 == 0:
#             print(f"Customer {customer_number}: Gift - pen")
#         pens += 1
#         if customer_number % 5 == 0:
#             print(f"Customer {customer_number}: Gift - rulers")
#         rulers += 1
# else:
#     print("Incorrect input")

# # 9
# customer_account = 500
# purchase_amount = int(input("Please enter the purchase amount: "))
# if customer_account < purchase_amount:
#     print("You can't buy this")
# else:
#     print("Its ok! You can bye this!")

range_len = 10
range_obj = range(range_len)
i = 0
while i < range_len:
    print(range_obj[i]+1)
    i += 1
