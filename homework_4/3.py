age = int(input("Введіть вік для визначення соціальної категорії: "))

if age < 0:
    print("Такого віку не існує.")
if 2 > age > 0:
    print("Класифікується як BABY")
elif 2 <= age < 4:
    print("Класифікується як KID")
elif 4 <= age < 13:
    print("Класифікується як CHILD")
elif 13 <= age < 20:
    print("Класифікується як TEENAGER")
elif 20 <= age < 65:
    print("Класифікується як GROWN-UP")
elif 65 <= age:
    print("Класифікується як SENIOR")