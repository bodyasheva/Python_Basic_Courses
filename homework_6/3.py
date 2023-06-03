own_list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1), ('red', 10)]
new_dict = {}
for i in range(len(own_list)):
    if own_list[i][0] not in new_dict:
        new_dict[own_list[i][0]] = [(own_list[i][1])]
    else:
        new_dict[own_list[i][0]].append(own_list[i][1])

print(new_dict)