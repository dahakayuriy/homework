from functools import wraps


# def str_decorator(func):
#     @wraps(func)
#     def wrapper():
#         return str(func())
#     return wrapper


# @str_decorator
# def say_hi():

#     return 4 + 5


# print(say_hi())
# print(type(say_hi()))


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        result2 = 2 + 2
        return result2

    return wrapper


@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")


print(say_hello("Yuriy"))
print("its ok")