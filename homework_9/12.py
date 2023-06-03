def difference(*mass_numbers):
    if mass_numbers == ():
        result = 0
    else:
        min_numbers = mass_numbers[0]
        for min_element in mass_numbers:
            if min_numbers > min_element:
                min_numbers = min_element
        max_numbers = mass_numbers[0]
        for max_element in mass_numbers:
            if max_numbers < max_element:
                max_numbers = max_element
        result = round(max_numbers - min_numbers, 1)
    return result

print(difference(10.2, -2.2, 0, 1.1, 0.5))
