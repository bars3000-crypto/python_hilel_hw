class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        self.coins += v


n = int(input())
m = int(input())
k = int(input())

box = MoneyBox(n)
box.add(m)
print(box.can_add(k))