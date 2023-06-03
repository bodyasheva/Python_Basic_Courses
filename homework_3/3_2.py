snake = input("Введіть строку з трьох слів відділених, один від одного, символом _ :")
snake = snake.split("_")
print(f"{snake[0].capitalize()}{snake[1].capitalize()}{snake[2].capitalize()}")