def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old."

name_user = input("Введіть ім'я: ")
age_user = int(input("Введіть вік: "))
while age_user <= 0:
    print("Вік повинен бути додатнім!")
    age_user = int(input("Введіть вік: "))

print(say_hi(name_user, age_user))
