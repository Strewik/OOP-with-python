class Item:
    def total_price(self, price, quantity):
        return price * quantity


item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "Laptop"
item2.price = 500
item2.quantity = 3
print(item2.total_price(item2.price, item2.quantity))
