number = int(input("Введіть число: "))

while number <= 0:
    number = int(input("Введіть число: "))

number_list = list(str(number))
result = 10

while result > 9:
    result = 1
    for i in range(len(number_list)):
        result *= int(number_list[i])
    number_list = list(str(result))

print(result)