create_list = list(input("Введіть набір елементів без пробілів: "))
diict = {}

for i in range(len(create_list)):
    if create_list[i] not in diict:
        diict[create_list[i]] = 1
    else:
        diict[create_list[i]] += 1

print(create_list)
print(diict)