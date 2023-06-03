def popular_words(stroke_words, *list_words):
    list_punctuation = [",", ".", ":", "-", "!", "?"]
    for i in list_punctuation:
        if i in stroke_words:
            stroke_words = stroke_words.replace(i, " ")
    stroke_words = stroke_words.lower().split()

    for m in range(len(list_words[0])):
        list_words[0][m] = list_words[0][m].lower()

    note_popular = {}
    for j in range(len(list_words[0])):
        note_popular[list_words[0][j]] = 0

    for k in range(len(list_words[0])):
        for n in range(len(stroke_words)):
            if list_words[0][k] == stroke_words[n]:
                note_popular[list_words[0][k]] += 1

    return note_popular


print(popular_words("When I was One, I had just begun When I was Two I was nearly new",
                    ['I', 'wAs', 'three', 'near']))
