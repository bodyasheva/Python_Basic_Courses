import random
random_list = []

for i in range(random.randrange(3, 10)):
    random_list.append(random.randrange(0, 199))

new_list = []
new_list.append(random_list[0])
new_list.append(random_list[2])
new_list.append(random_list[-2])

print(random_list)
print(new_list)