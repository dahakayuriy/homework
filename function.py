# 1


def a(a, b):
    return a + b


print(a(4, 5))

# 2


def b(a):
    if a % 2 == 0:
        print(True)
    else:
        print(False)
        return a


b(3)

# 3


def c(a, b, v, g):
    return max(a, b, v, g)


print(c(4, 6, 8, 2))

# 4


def calculator_podatkiv(suma_dohodu):
    if suma_dohodu <= 0:
        return "The amount of income must be greater than 0"

    if suma_dohodu <= 10000:
        podatok = suma_dohodu * 0.1
    elif suma_dohodu <= 50000:
        podatok = 10000 * 0.1 + (suma_dohodu - 10000) * 0.15
    else:
        podatok = 10000 * 0.1 + (50000 - 10000) * \
            0.15 + (suma_dohodu - 50000) * 0.2

    return podatok


suma_dohodu = float(input("Enter the amount of income: "))
podatok = calculator_podatkiv(suma_dohodu)
print(f"Income tax amount: {podatok}")

# 5
stocks = {"Books": 1, }


def add_product(product_name, quantity):
    if product_name in stocks:
        stocks[product_name] += quantity
    else:
        stocks[product_name] = quantity


def information_about_inventory():
    print("Stocks in the warehouse:")
    for product, quantity in stocks.items():
        print(f"{product}: {quantity} units")


add_product("Books", 50)
add_product("Clothes", 100)
add_product("Electronics", 20)

information_about_inventory()


# 6
def Calculation_of_delivery_cost(weight, distance):
    tariff_kg = 8
    tariff_km = 4
    cost = weight * tariff_kg + distance * tariff_km
    return cost


print(f"Delivery cost: {Calculation_of_delivery_cost(10, 5)} uah")
# vaga = float(input("Введіть вагу товару (кг): "))
# vidstan = float(input("Введіть відстань доставки (км): "))

# vartist_dostavky = vartist_dostavky(vaga, vidstan)
# print(f"Вартість доставки: {vartist_dostavky} грн")

# 7


def project_costs(cost_of_working_hours, number_of_hours, additional_costs):
    total_cost_of_the_project = cost_of_working_hours * \
        number_of_hours * additional_costs
    return total_cost_of_the_project


print(f"Total cost of the project: {project_costs(78.15, 34.25, 94)}")

# 8


# def create_account(account_holder, initial_balance=0):
#     return {'account_holder': account_holder, 'balance': initial_balance, 'transaction_history': []}


# def check_balance(account):
#     return f"Current balance for {account['account_holder']}: {account['balance']} uah"


# 9
def add_a_task(task_list, tasks):
    task_list.append({'task': tasks, 'completed': False})


def identify_completed(task_list, index_of_task):
    if 0 <= index_of_task <= task_list:
        task_list[index_of_task]['completed'] = True
    else:
        print("Invalid task index")


def list_of_active_tasks(task_list):
    active_tasks = [tasks['task']
                    for tasks in task_list if not tasks['completed']]
    return active_tasks


# list_tasks = []

# add_a_task(list_tasks, "Write a code")
def all(*args):
    return sum(args) - 3


print(all(2, 4, 5, 4))
