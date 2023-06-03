number_line = int(input("Введіть кількість рядків: "))

i = 0
j = 1
number_space = number_line
while i < number_line:
    number_space -= 1
    trian = number_space * " " + j * "*" + number_space * " "
    print(trian)
    i += 1
    j += 2