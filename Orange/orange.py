class Orange:
    def __init__(self, weight, orchard, date_picked):
        self.weight = weight
        self.orchard = orchard
        self.date_piked = date_picked
        
    def squeeze(self):
        juice = self.weight * 0.7
        self.weight = self.weight - juice
        return juice
    
    def pick(self, basket):
        basket.accept(self)
        
    def __str__(self):
        return f"Orange({self.weight}, {self.orchard}, {self.date_piked})"