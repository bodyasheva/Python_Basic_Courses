list_dict = [{'item': 'banana', 'amount': 400},
             {'item': 'apple', 'amount': 300},
             {'item': 'lemon', 'amount': 342},
             {'item': 'lemon', 'amount': 750},
             {'item': 'apple', 'amount': 856},
             {'item': 'banana', 'amount': 157}]
new_dict = {}
for dictor in list_dict:
    if dictor["item"] not in new_dict:
        new_dict[dictor["item"]] = dictor["amount"]
    else:
        new_dict[dictor["item"]] += dictor["amount"]

print(new_dict)