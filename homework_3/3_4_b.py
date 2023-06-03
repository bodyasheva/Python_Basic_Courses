number = int(input("Введіть 3-х значне число: "))
first = number % 10
second = number % 100 // 10
third = (number - number % 100) // 100
summa = first + second + third
print(f"Сумма цифр: {summa}")