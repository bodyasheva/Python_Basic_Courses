def prime_generator(number):
    for i in range(2, number + 1):
        result = True
        for j in range(2, i):
            if i % j == 0:
                result = False
                break
        if result:
            yield i

print(list(prime_generator(20)))