def generate_cube_numbers(number):
    for i in range(2, number + 1):
        result = True
        if i ** 3 > number:
            result = False
            break
        elif result:
            yield i ** 3

print(list(generate_cube_numbers(100)))