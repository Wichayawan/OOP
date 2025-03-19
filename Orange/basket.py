class Basket:
    def __init__(self, location):
        self.location = location
        self.oranges = []
        
    def accept(self, orange):
        self.oranges.append(orange)
        
    def sell(self, customer):
        while len(self.oranges) > 0:
            orange = self.oranges.pop()
            customer.purchase(orange)