def roman_to_integer(roman_str):
    roman_note = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    roman_str = roman_str[::-1]
    result = 0
    new_value = 0

    for roma in range(len(roman_str)):
        value = roman_note[roman_str[roma]]
        if value < new_value:
            result -= value
        else:
            result += value
        new_value = value
    return result

print(roman_to_integer("IV"))
