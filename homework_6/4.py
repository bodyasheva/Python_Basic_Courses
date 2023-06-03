new_list = list(map(int, input("Введіть список чисел через пробіл:").split(" ")))
result = int(input("Введіть цільове значення: "))
result_list = []
for i in range(len(new_list)):
    for j in range(i + 1, len(new_list)):
        if new_list[i] + new_list[j] == result:
            result_list.append((new_list[i], new_list[j]))
            result_list.append((new_list[j], new_list[i]))

print(result_list)