def group_by_surname(list_of_enrollees) -> str:
    group_value = [0, 0, 0, 0]
    surname = []
    first_element_surname = []

    for i in list_of_enrollees:
        name_surname = i.split()
        surname.append(name_surname[1])

    for j in surname:
        first_element_surname.append(j)

    for k in first_element_surname:
        if 'A' <= k <= 'I':
            group_value[0] += 1
        elif 'J' <= k <= 'P':
            group_value[1] += 1
        elif 'Q' <= k <= 'T':
            group_value[2] += 1
        elif 'U' <= k <= 'Z':
            group_value[3] += 1
    return group_value[0], group_value[1], group_value[2], group_value[3]


print(group_by_surname(['Will Smith', 'Jay Z', 'John Doe', 'Jane Smith',"Michael Jonns"]))
