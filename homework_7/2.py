def correct_sentence(striing):
    striing = striing.capitalize()
    if not striing.endswith("."):
        striing += "."
    return striing


users_str = str(input("Введіть речення: "))

print(correct_sentence(users_str))