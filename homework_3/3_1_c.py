a = int(input("Введіть ціле значення значення а: "))
b = int(input("Введіть ціле значення значення b: "))
print(f"Спочатку a = {a}, b = {b}")
a = a + b
b = a - b
a = a - b
print(f"Тепер a = {a}, b = {b}")