class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def __capacity(self):
        return len(self.items)

    def add_item(self, item):
        if len(self.items) == self.capacity:
            return "not enough room in the inventory"
        else:
            self.items.append(item)

    def get_capacity(self):
        return self.__capacity()

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity - self.__capacity()}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

