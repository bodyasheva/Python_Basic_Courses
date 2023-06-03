a = input("Введіть значення а: ")
b = input("Введіть значення b: ")
print(f"Спочатку a = {a}, b = {b}")
a, b = b, a
print(f"Тепер a = {a}, b = {b}")