list_numbers = list(map(int, input("Введіть послідовність чисел через пробіл: ").split()))

for i in range(len(list_numbers)):
    if list_numbers[i] == 0:
        del(list_numbers[i])
        list_numbers.append(0)

print(list_numbers)