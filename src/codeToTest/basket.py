class Basket:

    def __init__(self, count, capacity) -> None:
        self._count = count
        self._capacity = capacity

    @property
    def count(self):
        return self._count

    def add_item(self, num_item):
        new_count = self._count + num_item
        if self._capacity < new_count:
            raise ValueError("Reached Max Capacity.Can't add new item")
        self._count = new_count

    def remove_item(self, num_item):
        new_count = self._count - num_item
        if new_count < 0:
            raise ValueError("No items to remove!")
        self._count = new_count
