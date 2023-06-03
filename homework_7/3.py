def second_index(string, found_letter):
    answer = 0
    index_first_letter = int(string.index(found_letter))
    for i in range(index_first_letter + 1, len(string)):
        if found_letter in string[(index_first_letter + 1):len(string)]:
            answer = string[(index_first_letter + 1):len(string)].index(found_letter) + \
                     len(string[:index_first_letter + 1])
            break
        else:
            answer = None
    return answer


string_user = input("Введіть слово: ")
find_letter = input("Введіть літеру:")

print(second_index(string_user, find_letter))