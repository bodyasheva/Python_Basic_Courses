info = input(
    "Ввведіть наступну інформацію в такому вигляді: "
    "Ім'я Призвіще*рік народження-місяць-день*рік смерті-місяць-день: "
            )
info = info.split("*")
start_life = info[1].split("-")
end_life = info[2].split("-")
age = int(end_life[0]) - int(start_life[0])
print(f"Name : {info[0]}\nAge : {age}")