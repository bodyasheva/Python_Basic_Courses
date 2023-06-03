def find_unique_value(list_numbers, unique_value=None):
    numbers_note = {}
    for i in range(len(list_numbers)):
        if list_numbers[i] not in numbers_note:
            numbers_note[list_numbers[i]] = 1
        else:
            numbers_note[list_numbers[i]] += 1
    for j in range(len(list_numbers)):
        if numbers_note[list_numbers[j]] == 1:
            unique_value = list_numbers[j]
    return unique_value

print(find_unique_value([5, 5, 5, 0.5]))
