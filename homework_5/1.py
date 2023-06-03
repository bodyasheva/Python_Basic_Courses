import string
letters = input("Введіть через дефіс дві букви: ").split("-")
start_letter = string.ascii_letters.index(f"{letters[0]}")
end_letter = string.ascii_letters.index(f"{letters[1]}")
print(string.ascii_letters[start_letter:end_letter + 1])