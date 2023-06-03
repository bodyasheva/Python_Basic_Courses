import random


def common_elemets(first_value, second_value):
    first_list = []
    second_list = []
    set_first = ()
    set_second = ()

    while len(first_list) < first_value:
        random_number = random.randrange(-50, 50)
        if random_number % 3 == 0:
            first_list.append(random_number)
    set_first = set(first_list)

    while len(second_list) < second_value:
        random_number = random.randrange(-50, 50)
        if random_number % 5 == 0:
            second_list.append(random_number)
    set_second = set(second_list)

    intersection_set = set_first.intersection(set_second)
    return intersection_set


first_number = int(input("Введіть довжину першого списка:"))
second_number = int(input("Введіть довжину другого списка:"))
print(common_elemets(first_number, second_number))
