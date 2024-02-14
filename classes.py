# # 1
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.is_running = False

#     def start(self):
#         if not self.is_running:
#             print(f"{self.brand} {self.model} started to move")
#             self.is_running = True
#         else:
#             print(f"{self.brand} {self.model} already on the move.")


# info_car = Car('Toyota', 'Camry', 2022)

# print(f"Brand: {info_car.brand}")
# print(f"Model: {info_car.model}")
# print(f"Year: {info_car.year}")

# info_car.start()
# info_car.start()
############################################

# 2
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")


# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def display_info(self):
#         super().display_info()
#         print(f"Student ID: {self.student_id}")

#     def study(self):
#         print(f"{self.name} studies the material")


# class Teacher(Person):
#     def __init__(self, name, age, employee_id):
#         super().__init__(name, age)
#         self.employee_id = employee_id

#     def display_info(self):
#         super().display_info()
#         print(f"Teacher identification number: {self.employee_id}")

#     def teach(self):
#         print(f"{self.name} teaches a subject")


# student1 = Student(name='Stepan', age=20, student_id="SF83627")
# student1.display_info()
# student1.study()
# print()

# teacher1 = Teacher(name='Iryna', age=35, employee_id="FS948558")
# teacher1.display_info()
# teacher1.teach()
#########################################


class Animal:
    def __init__(self):
        self.limbs = 4
        self.eyes = 2

    def display_info(self):
        print(f"Limbs: {self.limbs} Eyes: {self.eyes}")


class FlyingAnimal(Animal):
    # eyes = None

    def __init__(self):
        super().__init__()
        self.can_fly = True

    def display_info(self):
        super().display_info()
        print("This type can also fly.")

    # def display_info(self):
    #     print(f"Limbs: {self.limbs}")
    #     print("This type can also fly.")


class SixEyesAnimal(FlyingAnimal):
    def __init__(self):
        super().__init__()
        self.eyes = 6

    def display_info(self):
        super().display_info()
        print("Extra: 6 eyes.")


animal = Animal()
flying_animal = FlyingAnimal()
six_eyes_animal = SixEyesAnimal()

print("Animal:")
animal.display_info()

print("\nFlying Animal:")
flying_animal.display_info()

print("\nSix Eyes Animal:")
six_eyes_animal.display_info()


# 3
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def book_info(self):
#         print(
#             f"Title of book: {self.title} \nAuthor: {self.author} \nYear: {self.year}")


# book = Book(title='Misery', author="Stephen King", year='1987')
# book.book_info()

# 4
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.brand} {self.model} {self.year}")


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Type: Car, Doors: {self.num_doors}")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, num_wheels):
        super().__init__(brand, model, year)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print(f"Type: Motorcycle, Wheels: {self.num_wheels}")


class Truck(Vehicle):
    def __init__(self, brand, model, year, playload_capacity):
        super().__init__(brand, model, year)
        self.playload_capacity = playload_capacity

    def display_info(self):
        super().display_info()
        print(f"Type: Truck, Payload capacity {self.playload_capacity} tons")


car = Car("Toyota", "Camry", 2022, 4)
motorcycle = Motorcycle("Harley-Davidson", "Street-750", 2022, 2)
truck = Truck("Ford", "F-150", 2022, 2.5)

car.display_info()
motorcycle.display_info()
truck.display_info()

####################################################


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def area(self):
        return 3.14 * self.radius**2


# Створення об'єкта
circle = Circle(5)

# Використання властивостей
print(circle.radius)
print(circle.diameter)
print(circle.area)

###############################################


class MyClass:
    def __init__(self):
        # Приватне поле, до якого ми отримуємо доступ через геттер і сеттер
        self._my_attribute = 2

    # Геттер для отримання значення атрибута
    @property
    def my_attribute(self):
        print("Getting the value")
        return self._my_attribute

    # Сеттер для встановлення значення атрибута
    @my_attribute.setter
    def my_attribute(self, value):
        print("Setting the value")
        self._my_attribute = value


# Створення об'єкта
obj = MyClass()

# Використання геттера для отримання значення
current_value = obj.my_attribute
print(f"Current value: {current_value}")

# Використання сеттера для встановлення нового значення
obj.my_attribute = 42

# Використання геттера для отримання оновленого значення
new_value = obj.my_attribute
print(f"New value: {new_value}")

#######################################


class CelciusToFahrenheitDescriptor:
    def __get__(self, instance, owner):
        return instance.celsius * 9/5 + 32

    def __set__(self, instance, value):
        instance.celsius = value


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    temperature = CelciusToFahrenheitDescriptor()


temp_instance = Temperature(25)
print("Temperature in degrees Celsius:", temp_instance.celsius)
print("Temperature in degrees Fahrenheit:", temp_instance.temperature)
temp_instance.temperature = 30
print("New temperature in degrees Celsius:", temp_instance.celsius)
print("New temperature in degrees Fahrenheit:", temp_instance.temperature)

#############################################


class CartLimit:
    def __init__(self, limit):
        self.limit = limit

    def __get__(self, instance, owner):
        return instance.quantity

    def __set__(self, instance, value):
        if value > self.limit:
            raise ValueError(f"Exceeded the cart limit of {self.limit} items.")
        instance.quantity = value


class ShoppingCart:
    cart_limit = CartLimit(10)

    def __init__(self, initial_quantity=0):
        self.quantity = initial_quantity


cart = ShoppingCart(5)
print("Initial number of products:", cart.cart_limit)

try:
    cart.cart_limit = 15
except ValueError as e:
    print(f"Error: {e}")

cart.cart_limit = 8
print("Updated number of products:", cart.cart_limit)
