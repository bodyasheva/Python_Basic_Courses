def is_palindrome(stroka):
    list_punctuation = [",", ".", ":", "-", "!", "?", " "]
    for i in list_punctuation:
        if i in stroka:
            stroka = stroka.replace(i, "")
    stroka = stroka.lower()
    return stroka == stroka[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))
