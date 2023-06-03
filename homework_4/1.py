while True:
    print("ВАС ВІТАЄ ЗАСТОСУНОК 'КАЛЬКУЛЯТОР'\n Для виходу з нього напишіть 'quit'")
    first_number = input("Напишіть ПЕРШЕ число: ")
    if first_number == 'quit':
        break
    else:
        operation = input("Вкажіть математичну ДІЮ( + , - , / , *): ")
        if operation == 'quit':
            break
        else:
            second_number = input("Введіть ДРУГЕ число: ")
            if second_number == 'quit':
                break
            else:
                if operation == '/' and second_number == '0':
                    print("На нуль ділити не можна.")
                    break
                elif operation == '+':
                    result = float(first_number) + float(second_number)
                    print(f"{first_number} + {second_number} = {result}")
                elif operation == '-':
                    result = float(first_number) - float(second_number)
                    print(f"{first_number} - {second_number} = {result}")
                elif operation == '/':
                    result = float(first_number) / float(second_number)
                    print(f"{first_number} / {second_number} = {result}")
                elif operation == '*':
                    result = float(first_number) * float(second_number)
                    print(f"{first_number} * {second_number} = {result}")