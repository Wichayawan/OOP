class Shoes:
    def __init__(self, size):
        self.size = size
    def __str__(self):
        return f"shoes -- size: {self.size}"

class Leg:
    def __init__(self, length):
        self.leg = length
    def __str__(self):
        return f"leg -- length: {self.leg}"

class Man:
    def __init__(self, shoes):
        self.shoes = shoes
        self.leg = Leg(120)
    def __str__(self):
        return f"man -- shoes: {self.shoes},\n\t-- leg: {self.leg}"   

shoes = Shoes(9)
man = Man(shoes)
print(man.shoes)
print(man.leg)
print(man)
del man
print(shoes)
print(man.leg)