def first_word(string) -> str:
    list_punctuation = [",", ".", ":", "-", "!", "?"]

    for i in list_punctuation:
        if i in string:
            string = string.replace(i, " ")

    result = string.split()

    for j in range(len(result) - 1):
        if result[j] == "":
            result.pop(j)
    return result[0]


print(first_word("... and so on ..."))
