"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    return [i * i for i in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True


def filter_numbers(nums, filter_type):

    if filter_type == ODD:
        return list(filter(lambda x: x % 2 == 1, nums))
    elif filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, nums))
    elif filter_type == PRIME:
        return list(filter(is_prime, nums))
