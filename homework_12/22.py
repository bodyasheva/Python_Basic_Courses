class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name} price: {self.price}"


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        self.items_list = []
        for item, count in self.products.items():
            obj = {
                item.name: f"{count} pcs."
            }
            self.items_list.append(obj)
        return f"User: {self.user}\nItems: {self.items_list}"

    def get_total(self):
        for item, count in self.products.items():
            self.total += item.price * count
        return self.total

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
iphone = Item("iphone", 500, "gold", "XS")

buyer = User("Bodya", "Slavincskii", "0676615687")
buyer1 = User("Misha", "Litvinov", "0938475")

cart = Purchase(buyer)
cart.add_item(lemon, 9)
cart.add_item(apple, 26)
cart.add_item(iphone, 2)

cart1 = Purchase(buyer1)
cart1.add_item(iphone, 2.5)

print(cart)
print(f"Check amount = {cart.get_total()}")
print(cart1)
print(f"Check amount = {cart1.get_total()}")
