def power(number):
    return number ** 2


def some_gen(begin, n, func):
    for i in range(n):
        yield begin
        begin = func(begin)


print(list(some_gen(2, 4, power)))
