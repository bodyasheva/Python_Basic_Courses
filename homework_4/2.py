lst = list(input("Введіть послідовно без пробілів елементи з яких буде складено список: "))
len_list = len(lst)
if len_list % 2 == 0 and len_list != 0:
    half = int(len_list/2)
    new_list = [lst[0:half], lst[half:]]
    print(new_list)
elif len_list % 2 != 0 and len_list != 1:
    half = int((len_list + 1) / 2)
    new_list = [lst[0:half], lst[half:]]
    print(new_list)
elif len_list == 1:
    new_list = [lst, []]
    print(new_list)
else:
    new_list = [[], []]
    print(new_list)