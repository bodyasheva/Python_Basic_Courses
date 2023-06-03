def add_one(list_numbers):
    list_numbers[len(list_numbers)-1] += 1
    list_numbers = list_numbers[::-1]
    for i in range(len(list_numbers)-1):
        if list_numbers[i] == 10:
            list_numbers[i] = 0
            list_numbers[i + 1] += 1
    if list_numbers[len(list_numbers) - 1] == 10:
        list_numbers[len(list_numbers) - 1] = 0
        list_numbers.append(1)
    list_numbers = list_numbers[::-1]
    return list_numbers

print(add_one([8,9,9]))
