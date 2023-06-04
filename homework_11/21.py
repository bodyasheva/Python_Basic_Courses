def is_even(number):
    code = bin(number)
    return int(code[-1]) == 0

print(is_even(24945638940387**3))